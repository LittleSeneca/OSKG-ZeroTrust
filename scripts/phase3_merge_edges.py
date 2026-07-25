#!/usr/bin/env python3
"""Normalize and merge Phase 3 Pass 2 edge detection results.

Subagents used inconsistent field names. This script:
1. Reads all edge JSON files from phase3_edges/
2. Normalizes to a single format: {claim_a, claim_b, edge_type, rationale}
3. Deduplicates (same pair + same edge_type = duplicate)
4. Flags contradictions for human review
5. Outputs a merged inventory: phase3_edge_inventory.json
"""

import json
import os
from collections import Counter

EDGES_DIR = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/scripts/phase3_edges")
OUT_PATH = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/scripts/phase3_edge_inventory.json")
CLAIMS_DIR = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/notes/claims")


def normalize_edge(edge):
    """Normalize one edge dict to standard format. Returns dict or None if unparseable."""
    # Try standard format: claim_a, claim_b, edge_type
    if 'claim_a' in edge and 'claim_b' in edge:
        return {
            'claim_a': edge['claim_a'],
            'claim_b': edge['claim_b'],
            'edge_type': edge.get('edge_type', edge.get('type', 'unknown')),
            'rationale': edge.get('rationale', ''),
        }

    # Try source/target format
    if 'source' in edge and 'target' in edge:
        return {
            'claim_a': edge['source'],
            'claim_b': edge['target'],
            'edge_type': edge.get('relation', edge.get('relationship', edge.get('type', 'unknown'))),
            'rationale': edge.get('rationale', ''),
        }

    return None


def normalize_type(et):
    """Canonicalize edge type strings."""
    et = et.lower().strip()
    mapping = {
        'supports': 'supports',
        'support': 'supports',
        'extends': 'extends',
        'extend': 'extends',
        'depends_on': 'depends_on',
        'depends on': 'depends_on',
        'depends': 'depends_on',
        'contradicts': 'contradicts',
        'contradict': 'contradicts',
        'challenges': 'contradicts',
        'contradicted_by': 'contradicts',
    }
    return mapping.get(et, et)


def load_slug_map(claims_dir):
    """Build claim_id → slug lookup from all claim files."""
    import re
    slug_map = {}
    for fname in os.listdir(claims_dir):
        if not fname.endswith('.md'):
            continue
        slug = fname[:-3]
        text = open(os.path.join(claims_dir, fname)).read()
        match = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
        if not match:
            continue
        fm = match.group(1)
        for line in fm.split('\n'):
            kv = re.match(r'^claim_id:\s*"?(.*?)"?\s*$', line)
            if kv:
                cid = kv.group(1).strip().strip('"')
                slug_map[cid] = slug
                break
    return slug_map


def resolve_slug(ref, slug_map, slug_lookup):
    """Resolve a claim reference to a slug. Tries: exact slug match, claim_id→slug map, claim_id as prefix."""
    if ref in slug_lookup:
        return ref
    if ref in slug_map:
        return slug_map[ref]
    # Try prefix match (e.g. 'gb-ch4-6' matching 'gb-ch4-6.14')
    for cid, slug in slug_map.items():
        if cid.startswith(ref) or ref.startswith(cid):
            return slug
    return ref  # Give up, keep original

def main():
    # Build slug lookup
    slug_map = load_slug_map(CLAIMS_DIR)
    all_slugs_on_disk = set()
    for fname in os.listdir(CLAIMS_DIR):
        if fname.endswith('.md'):
            all_slugs_on_disk.add(fname[:-3])

    all_edges = []
    files_read = 0
    errors = []

    for fname in sorted(os.listdir(EDGES_DIR)):
        if not fname.endswith('.json'):
            continue
        fpath = os.path.join(EDGES_DIR, fname)
        try:
            data = json.load(open(fpath))
        except json.JSONDecodeError as e:
            errors.append(f"{fname}: JSON decode error: {e}")
            continue

        if not isinstance(data, list):
            # Check for wrapped format: {"edges": [...]}
            if isinstance(data, dict) and 'edges' in data:
                data = data['edges']
            else:
                errors.append(f"{fname}: not a list (got {type(data).__name__})")
                continue

        files_read += 1
        for edge in data:
            norm = normalize_edge(edge)
            if norm is None:
                errors.append(f"{fname}: unparseable edge: {json.dumps(edge)[:100]}")
                continue
            norm['edge_type'] = normalize_type(norm['edge_type'])
            norm['source_file'] = fname
            all_edges.append(norm)

    print(f"Read {files_read} files, {len(all_edges)} raw edges")

    # Deduplicate: same (claim_a, claim_b, edge_type) is a duplicate
    seen = set()
    unique = []
    dupes = 0
    for e in all_edges:
        key = (e['claim_a'], e['claim_b'], e['edge_type'])
        # Also check reversed pair for symmetric types (supports, contradicts)
        rev_key = (e['claim_b'], e['claim_a'], e['edge_type'])
        if key in seen or rev_key in seen:
            dupes += 1
            continue
        seen.add(key)
        unique.append(e)

    print(f"After dedup: {len(unique)} unique edges ({dupes} duplicates removed)")

    # Resolve claim_id references to slugs
    unresolved = 0
    for e in unique:
        old_a, old_b = e['claim_a'], e['claim_b']
        e['claim_a'] = resolve_slug(e['claim_a'], slug_map, all_slugs_on_disk)
        e['claim_b'] = resolve_slug(e['claim_b'], slug_map, all_slugs_on_disk)
        if e['claim_a'] == old_a and old_a not in all_slugs_on_disk:
            unresolved += 1
        if e['claim_b'] == old_b and old_b not in all_slugs_on_disk:
            unresolved += 1
    if unresolved:
        print(f"  ({unresolved} edge endpoints still unresolved — may be claim_id references)")

    # Stats
    type_counts = Counter(e['edge_type'] for e in unique)
    print(f"\nEdge type breakdown:")
    for t, c in type_counts.most_common():
        print(f"  {t}: {c}")

    # Flag contradictions for review
    contradicts = [e for e in unique if e['edge_type'] == 'contradicts']
    print(f"\nContradicts edges (needs human review): {len(contradicts)}")
    for e in contradicts:
        print(f"  {e['claim_a']} ↔ {e['claim_b']}: {e['rationale'][:120]}")

    # Claims with most edges
    source_counts = Counter()
    for e in unique:
        source_counts[e['claim_a']] += 1
        source_counts[e['claim_b']] += 1

    print(f"\nTop 15 densest claims:")
    for slug, count in source_counts.most_common(15):
        print(f"  {slug}: {count} edges")

    # Claims with zero edges (orphans in edges/)
    all_slugs_in_edges = set()
    for e in unique:
        all_slugs_in_edges.add(e['claim_a'])
        all_slugs_in_edges.add(e['claim_b'])

    # Also check the manifest for which claims should exist
    manifest_path = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/scripts/phase3_clusters.json")
    with open(manifest_path) as f:
        manifest = json.load(f)

    all_claim_slugs = set()
    for cluster in manifest['clusters']:
        all_claim_slugs.update(cluster['claim_slugs'])

    orphans = all_claim_slugs - all_slugs_in_edges
    print(f"\nOrphan claims (no edges at all): {len(orphans)}")
    if orphans:
        for s in sorted(orphans)[:20]:
            print(f"  {s}")

    # Write inventory
    inventory = {
        'version': '1.0',
        'total_raw_edges': len(all_edges),
        'total_unique_edges': len(unique),
        'duplicates_removed': dupes,
        'contradicts_count': len(contradicts),
        'orphan_claims_count': len(orphans),
        'orphan_claims': sorted(orphans),
        'edge_type_breakdown': dict(type_counts),
        'top_dense_claims': source_counts.most_common(20),
        'edges': unique,
    }

    with open(OUT_PATH, 'w') as f:
        json.dump(inventory, f, indent=2)
    print(f"\nInventory written to {OUT_PATH}")


if __name__ == '__main__':
    main()
