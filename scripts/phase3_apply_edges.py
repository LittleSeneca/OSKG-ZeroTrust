#!/usr/bin/env python3
"""Phase 3 Pass 3: Apply detected edges to claim files.

Reads phase3_edge_inventory.json and patches each claim's ## Edges section
with wikilinks. Verifies resolution, flags contradictions, reports orphans.
"""

import json
import os
import re
from collections import Counter

INVENTORY_PATH = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/scripts/phase3_edge_inventory.json")
CLAIMS_DIR = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/notes/claims")


def patch_edge_section(filepath, edge_type, target_slug, rationale=""):
    """Add a wikilink under the specified edge type heading in a claim file.
    Handles three cases: empty section, comment-only section, section with existing edges.
    Returns 'added', 'skip', or 'no_header'."""
    with open(filepath, 'r') as f:
        content = f.read()

    header_map = {
        'depends_on': '**Depends on:**',
        'supports': '**Supports:**',
        'extends': '**Extends:**',
        'contradicts': '**Contradicts:**',
    }

    header = header_map.get(edge_type)
    if not header:
        return f'unknown_type:{edge_type}'

    # Build the wikilink line
    display = rationale[:120].strip() if rationale else target_slug
    wikilink = f'- [[{target_slug}|{display}]]\n'

    # Check if this edge already exists (any wikilink to this slug under this header)
    header_pos = content.find(header)
    if header_pos == -1:
        return 'no_header'

    # Find the next section header or end of Edges section
    next_section = content.find('\n**', header_pos + len(header))
    if next_section == -1:
        edges_end = content.find('\n## ', header_pos)
        section_body = content[header_pos:edges_end] if edges_end != -1 else content[header_pos:]
    else:
        section_body = content[header_pos:next_section]

    if f'[[{target_slug}' in section_body or f'[[{target_slug}]]' in section_body:
        return 'skip'

    # Find insertion point: after header line, optionally after HTML comment
    newline_pos = content.find('\n', header_pos)
    insert_pos = newline_pos + 1

    # Skip placeholder HTML comment if present
    peek = content[insert_pos:insert_pos + 6]
    if peek.startswith('<!--'):
        comment_end = content.find('-->\n', insert_pos)
        if comment_end != -1:
            insert_pos = comment_end + 4  # after -->\n
            # Also skip trailing blank line after comment
            if content[insert_pos:insert_pos + 1] == '\n':
                insert_pos += 1

    # Insert the wikilink
    new_content = content[:insert_pos] + wikilink + content[insert_pos:]
    with open(filepath, 'w') as f:
        f.write(new_content)
    return 'added'


def main():
    with open(INVENTORY_PATH) as f:
        inventory = json.load(f)

    edges = inventory['edges']
    print(f"Processing {len(edges)} edges...\n")

    results = Counter()
    application_log = []
    contradictions = []

    for edge in edges:
        claim_a = edge['claim_a']
        claim_b = edge['claim_b']
        edge_type = edge['edge_type']
        rationale = edge.get('rationale', '')

        file_a = os.path.join(CLAIMS_DIR, f"{claim_a}.md")
        file_b = os.path.join(CLAIMS_DIR, f"{claim_b}.md")

        # Determine which file(s) to patch based on edge direction
        # depends_on: claim_a is what claim_b depends on → claim_b gets "Depends on: [[claim_a]]"
        # supports: claim_a supports claim_b → claim_a gets "Supports: [[claim_b]]"
        # extends: claim_a extends claim_b → claim_a gets "Extends: [[claim_b]]"
        # contradicts: symmetric → both get "Contradicts: [[other]]"

        patches = []  # (file, slug, type, rationale)

        if edge_type == 'depends_on':
            # claim_b depends on claim_a
            patches.append((file_b, claim_a, 'depends_on', rationale))
        elif edge_type == 'supports':
            # claim_a supports claim_b
            patches.append((file_a, claim_b, 'supports', rationale))
        elif edge_type == 'extends':
            # claim_a extends claim_b
            patches.append((file_a, claim_b, 'extends', rationale))
        elif edge_type == 'contradicts':
            # Both get contradicts
            patches.append((file_a, claim_b, 'contradicts', rationale))
            patches.append((file_b, claim_a, 'contradicts', rationale))
            contradictions.append(edge)

        for patch_file, target_slug, et, rat in patches:
            if not os.path.isfile(patch_file):
                results[f'missing_source:{edge_type}'] += 1
                application_log.append(f"MISSING: {patch_file} (edge: {claim_a} {edge_type} {claim_b})")
                continue

            outcome = patch_edge_section(patch_file, et, target_slug, rat)
            results[outcome] += 1
            if outcome not in ('added', 'skip'):
                application_log.append(f"{outcome}: {os.path.basename(patch_file)} → {et} → {target_slug}")

    print("=== APPLICATION RESULTS ===")
    for outcome, count in results.most_common():
        print(f"  {outcome}: {count}")

    # Count modified files
    modified = results.get('added', 0) + results.get('skip', 0)
    skipped = results.get('skip', 0)
    print(f"\n  Total patches attempted: {modified}")
    print(f"  Already present (skipped): {skipped}")
    print(f"  Newly added: {results.get('added', 0)}")

    if application_log:
        print(f"\n=== {len(application_log)} ISSUES ===")
        for entry in application_log[:30]:
            print(f"  {entry}")
        if len(application_log) > 30:
            print(f"  ... and {len(application_log) - 30} more")

    # Orphan report
    print(f"\n=== ORPHAN REPORT ===")
    orphans = inventory.get('orphan_claims', [])
    print(f"Claims with zero edges: {len(orphans)}")
    if len(orphans) <= 20:
        for s in orphans:
            print(f"  - [[{s}]]")
    else:
        for s in orphans[:20]:
            print(f"  - [[{s}]]")
        print(f"  ... and {len(orphans) - 20} more")

    # Contradiction report
    print(f"\n=== CONTRADICTIONS (needs review) ===")
    print(f"Flagged: {len(contradictions)}")
    for c in contradictions:
        print(f"  - [[{c['claim_a']}]] ↔ [[{c['claim_b']}]]")
        if c.get('rationale'):
            print(f"    {c['rationale'][:150]}")

    # Save application log
    log_path = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/scripts/phase3_application_log.json")
    report = {
        'results': dict(results),
        'modified_files': results.get('added', 0) + results.get('skip', 0),
        'newly_added': results.get('added', 0),
        'issues': application_log,
        'contradictions': [{'claim_a': c['claim_a'], 'claim_b': c['claim_b'],
                            'rationale': c.get('rationale', '')} for c in contradictions],
    }
    with open(log_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\nApplication log: {log_path}")


if __name__ == '__main__':
    main()
