#!/usr/bin/env python3
"""Phase 3 Pass 1: Topic-Cluster Candidate Generator.

Groups 406 claims into clusters of 5-25 for LLM batch edge detection.
Strategy:
  1. Group by primary topic tag
  2. Split groups >25 by claim_type
  3. Split subgroups still >25 by secondary topic tag
  4. Merge subgroups <5 with nearest sibling (same parent topic)
  5. Merge remaining <5 groups with nearest topic group
  6. Output JSON manifest: clusters, stats, candidate pair counts
"""

import os
import re
import json
from collections import defaultdict, Counter

CLAIMS_DIR = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/notes/claims")


def make_cluster_label(claims_list):
    """Generate a short human-readable label from a cluster's claims."""
    topics = Counter(c['primary_topic'] for c in claims_list)
    types = Counter(c['claim_type'] for c in claims_list)
    top_topics = [t.replace('topic/zt-', '') for t, _ in topics.most_common(2)]
    top_type = types.most_common(1)[0][0]
    return f"{'+'.join(top_topics)} ({top_type})"

# Topic adjacency map: which topics are "near" each other for merging orphans
TOPIC_ADJACENCY = {
    'topic/zt-definition': ['topic/zt-trust', 'topic/zt-tenets', 'topic/zt-architecture'],
    'topic/zt-architecture': ['topic/zt-network', 'topic/zt-definition', 'topic/zt-policy'],
    'topic/zt-network': ['topic/zt-architecture', 'topic/zt-cloud', 'topic/zt-app'],
    'topic/zt-identity': ['topic/zt-access-mgmt', 'topic/zt-authentication', 'topic/zt-governance'],
    'topic/zt-access-mgmt': ['topic/zt-identity', 'topic/zt-authentication', 'topic/zt-policy'],
    'topic/zt-authentication': ['topic/zt-identity', 'topic/zt-access-mgmt'],
    'topic/zt-implementation': ['topic/zt-migration', 'topic/zt-cloud', 'topic/zt-device'],
    'topic/zt-migration': ['topic/zt-implementation', 'topic/zt-governance'],
    'topic/zt-governance': ['topic/zt-policy', 'topic/zt-identity', 'topic/zt-migration'],
    'topic/zt-policy': ['topic/zt-governance', 'topic/zt-architecture'],
    'topic/zt-cloud': ['topic/zt-implementation', 'topic/zt-network', 'topic/zt-data'],
    'topic/zt-device': ['topic/zt-monitoring', 'topic/zt-implementation'],
    'topic/zt-monitoring': ['topic/zt-device', 'topic/zt-threats'],
    'topic/zt-threats': ['topic/zt-monitoring', 'topic/zt-network'],
    'topic/zt-app': ['topic/zt-cloud', 'topic/zt-network'],
    'topic/zt-data': ['topic/zt-encryption', 'topic/zt-cloud'],
    'topic/zt-encryption': ['topic/zt-data', 'topic/zt-network'],
    'topic/zt-trust': ['topic/zt-definition', 'topic/zt-tenets'],
    'topic/zt-tenets': ['topic/zt-definition', 'topic/zt-trust'],
    'topic/zt-maturity': ['topic/zt-governance', 'topic/zt-migration'],
    'topic/zt-supply-chain': ['topic/zt-device', 'topic/zt-governance'],
}


def parse_frontmatter(text):
    match = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if not match:
        return {}
    fm = match.group(1)
    data = {}
    current_key = None
    for line in fm.split('\n'):
        kv = re.match(r'^(\w[\w_]*):\s*(.*)', line)
        if kv:
            current_key = kv.group(1)
            val = kv.group(2).strip().strip('"').strip("'")
            data[current_key] = val
        elif current_key and line.strip().startswith('- '):
            val = line.strip()[2:].strip().strip('"').strip("'")
            existing = data.get(current_key)
            if not isinstance(existing, list):
                data[current_key] = [existing] if existing else []
            data[current_key].append(val)
    return data


def load_claims():
    claims = []
    for fname in sorted(os.listdir(CLAIMS_DIR)):
        if not fname.endswith('.md'):
            continue
        slug = fname[:-3]
        text = open(os.path.join(CLAIMS_DIR, fname)).read()
        fm = parse_frontmatter(text)

        # Skip non-claim files (indices, templates)
        if 'claim_id' not in fm:
            continue

        tags = fm.get('tags', []) if isinstance(fm.get('tags'), list) else []
        topic_tags = [t for t in tags if t.startswith('topic/')]
        primary_topic = topic_tags[0] if topic_tags else 'untagged'

        claims.append({
            'slug': slug,
            'claim_id': fm.get('claim_id', 'unknown'),
            'statement': fm.get('statement', ''),
            'primary_topic': primary_topic,
            'all_topics': topic_tags,
            'secondary_topic': topic_tags[1] if len(topic_tags) > 1 else None,
            'claim_type': fm.get('claim_type', 'unknown'),
            'confidence': fm.get('confidence', 'medium'),
            'filename': fname,
        })
    return claims


def build_clusters(claims):
    MAX_SIZE = 25
    MIN_SIZE = 5

    # Step 1: Group by primary topic
    topic_groups = defaultdict(list)
    for c in claims:
        topic_groups[c['primary_topic']].append(c)

    clusters = []  # List of {label, claims, size}
    cluster_id = 0

    # Step 2: Split large groups by claim_type, then secondary topic
    for topic, group in sorted(topic_groups.items()):
        if len(group) <= MAX_SIZE:
            # Small enough — maybe one cluster or need to merge later
            clusters.append({
                'id': f'c{cluster_id}',
                'label': make_cluster_label(group),
                'claims': group,
                'size': len(group),
                'split_method': 'none',
            })
            cluster_id += 1
        else:
            # Split by claim_type first
            ct_subs = defaultdict(list)
            for c in group:
                ct_subs[c['claim_type']].append(c)

            for ctype, ct_group in sorted(ct_subs.items()):
                if len(ct_group) <= MAX_SIZE:
                    clusters.append({
                        'id': f'c{cluster_id}',
                        'label': make_cluster_label(ct_group),
                        'claims': ct_group,
                        'size': len(ct_group),
                        'split_method': 'by claim_type',
                    })
                    cluster_id += 1
                else:
                    # Still too big — split by secondary topic
                    sec_subs = defaultdict(list)
                    for c in ct_group:
                        sec = c['secondary_topic'] or 'none'
                        sec_subs[sec].append(c)

                    for sec, sec_group in sorted(sec_subs.items()):
                        clusters.append({
                            'id': f'c{cluster_id}',
                            'label': make_cluster_label(sec_group),
                            'claims': sec_group,
                            'size': len(sec_group),
                            'split_method': 'by secondary_topic',
                        })
                        cluster_id += 1

    return clusters


def merge_small_clusters(clusters):
    """Iteratively merge clusters < MIN_SIZE with best available partner.
    Runs multiple passes until no more merges are possible or all clusters >= MIN_SIZE."""
    MIN_SIZE = 5
    MAX_COMBINED = 30

    def find_best_merge(small, candidates_list):
        """Find the best candidate to merge small into. candidates_list is list of (index_in_working, cluster).
        Returns index_in_working or None."""
        sc_primary = small['claims'][0]['primary_topic']
        best_score = -1
        best_target = None

        for j, tc in candidates_list:
            if tc is small:
                continue
            combined_size = small['size'] + tc['size']
            if combined_size > MAX_COMBINED:
                continue

            tc_primary = tc['claims'][0]['primary_topic']
            score = 0
            if tc_primary == sc_primary:
                score += 3
            elif tc_primary in TOPIC_ADJACENCY.get(sc_primary, []):
                score += 2
            tc_types = set(c['claim_type'] for c in tc['claims'])
            sc_types = set(c['claim_type'] for c in small['claims'])
            if tc_types & sc_types:
                score += 1
            if score > best_score or (score == best_score and best_target is not None and tc['size'] > working[best_target]['size']):
                best_score = score
                best_target = j

        return best_target

    working = list(clusters)
    merge_counter = 0
    prev_small_count = None

    for _pass in range(5):
        small_idxs = [i for i, cl in enumerate(working) if cl['size'] < MIN_SIZE]
        if not small_idxs:
            break

        if prev_small_count is not None and len(small_idxs) >= prev_small_count:
            break
        prev_small_count = len(small_idxs)

        # Process smallest first
        small_idxs.sort(key=lambda i: working[i]['size'])

        consumed = set()  # Indices that will be removed (merged into another)

        for si in small_idxs:
            if si in consumed:
                continue
            small = working[si]

            # Candidates: all other clusters not yet consumed
            candidates = [(j, working[j]) for j in range(len(working))
                         if j != si and j not in consumed]

            target_idx = find_best_merge(small, candidates)
            if target_idx is not None:
                target = working[target_idx]
                merge_counter += 1
                combined = {
                    'id': f'merged-{merge_counter}',
                    'label': make_cluster_label(target['claims'] + small['claims']),
                    'claims': target['claims'] + small['claims'],
                    'size': target['size'] + small['size'],
                    'split_method': 'merged',
                }
                working[target_idx] = combined
                consumed.add(si)

        # Rebuild: drop consumed indices
        working = [cl for i, cl in enumerate(working) if i not in consumed]

    return working


def compute_stats(clusters):
    total_pairs = 0
    cluster_stats = []
    for cl in clusters:
        n = cl['size']
        pairs = n * (n - 1) // 2
        total_pairs += pairs
        cluster_stats.append({
            'id': cl['id'],
            'label': cl['label'],
            'size': n,
            'candidate_pairs': pairs,
            'split_method': cl.get('split_method', 'unknown'),
            'topics': list(set(c['primary_topic'] for c in cl['claims'])),
        })
    return cluster_stats, total_pairs


def main():
    claims = load_claims()
    print(f"Loaded {len(claims)} claims")

    clusters = build_clusters(claims)
    print(f"After building: {len(clusters)} clusters")

    # Show initial size distribution
    sizes = Counter(cl['size'] for cl in clusters)
    print(f"  Size distribution: {dict(sorted(sizes.items()))}")

    merged = merge_small_clusters(clusters)
    print(f"After merging: {len(merged)} clusters")
    sizes = Counter(cl['size'] for cl in merged)
    print(f"  Size distribution: {dict(sorted(sizes.items()))}")

    stats, total_pairs = compute_stats(merged)

    print(f"\n=== CLUSTER DETAILS ===")
    for s in sorted(stats, key=lambda x: x['size'], reverse=True):
        print(f"  {s['id']:15s} | {s['size']:3d} claims | {s['candidate_pairs']:5d} pairs | {s['label']}")

    print(f"\n=== SUMMARY ===")
    print(f"Clusters: {len(merged)}")
    print(f"Candidate pairs: {total_pairs}")
    print(f"Average cluster size: {sum(s['size'] for s in stats) / len(stats):.1f}")
    print(f"Orphan claims (<5, unmerged): {sum(1 for cl in merged if cl['size'] < 5)}")

    # Write manifest
    manifest = {
        'version': '1.0',
        'total_claims': len(claims),
        'total_clusters': len(merged),
        'total_candidate_pairs': total_pairs,
        'cluster_stats': stats,
        'clusters': []
    }

    for cl in merged:
        manifest['clusters'].append({
            'id': cl['id'],
            'label': cl['label'],
            'size': cl['size'],
            'claim_slugs': [c['slug'] for c in cl['claims']],
        })

    out_path = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/scripts/phase3_clusters.json")
    with open(out_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"\nManifest written to {out_path}")


if __name__ == '__main__':
    main()
