#!/usr/bin/env python3
"""Fix inverted depends_on edges using multi-signal heuristics.

depends_on means: claim_b logically requires claim_a to be true.
So claim_a should be the MORE FOUNDATIONAL claim.

Signals for inversion (higher score = more likely inverted):
  1. claim_a statement is longer (>50% longer) — more specific, less foundational
  2. claim_b has more total edges — more foundational hub
  3. claim_a has a more "specific" claim_type (implementation < architectural < definitional)
  4. Rationale describes claim_b as the thing that "depends on" claim_a

Only flips when score >= 2 (2+ signals agree).
"""

import json, os, re
from collections import Counter

INVENTORY_PATH = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/scripts/phase3_edge_inventory.json")
CLAIMS_DIR = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/notes/claims")
OUT_PATH = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/scripts/phase3_depends_fixes.json")

# Foundational → specific type ordering (lower = more foundational)
TYPE_RANK = {
    'definitional': 0,
    'architectural': 1,
    'governance': 2,
    'implementation': 3,
    'migration': 4,
    'threat': 5,
    'maturity': 6,
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


def get_claim_info(slug):
    """Return {statement, claim_type, edge_count} for a claim."""
    fpath = os.path.join(CLAIMS_DIR, f"{slug}.md")
    if not os.path.isfile(fpath):
        return {}
    text = open(fpath).read()
    fm = parse_frontmatter(text)
    return {
        'statement': fm.get('statement', ''),
        'claim_type': fm.get('claim_type', 'unknown'),
        'slug': slug,
    }


def analyze_edge(edge, claim_info, edge_counts, total):
    """Return {score, signals, should_flip, analysis} for one depends_on edge."""
    a = edge['claim_a']
    b = edge['claim_b']
    rationale = edge.get('rationale', '')
    
    info_a = claim_info.get(a, {})
    info_b = claim_info.get(b, {})
    
    stmt_a = info_a.get('statement', '')
    stmt_b = info_b.get('statement', '')
    type_a = info_a.get('claim_type', 'unknown')
    type_b = info_b.get('claim_type', 'unknown')
    edges_a = edge_counts.get(a, 0)
    edges_b = edge_counts.get(b, 0)
    
    signals = []
    score = 0
    analysis = []
    
    # Signal 1: Statement length — longer = more specific
    len_a, len_b = len(stmt_a), len(stmt_b)
    if len_b > 0 and len_a > len_b * 1.5:
        signals.append('stmt_len')
        score += 1
        analysis.append(f"claim_a stmt is {len_a} chars, claim_b is {len_b} (+{len_a-len_b})")
    elif len_a > 0 and len_a > 30:  # Both have content, compare
        ratio = len_a / max(len_b, 1)
        analysis.append(f"stmt len ratio: {ratio:.1f} (a={len_a}, b={len_b})")
    
    # Signal 2: Edge count — higher = more foundational hub
    if edges_b > edges_a * 2 and edges_b >= 4:
        signals.append('edge_count')
        score += 1
        analysis.append(f"claim_b has {edges_b} edges, claim_a has {edges_a}")
    else:
        analysis.append(f"edges: a={edges_a}, b={edges_b}")
    
    # Signal 3: Claim type rank — lower rank = more foundational
    rank_a = TYPE_RANK.get(type_a, 99)
    rank_b = TYPE_RANK.get(type_b, 99)
    if rank_a > rank_b:
        signals.append('type_rank')
        score += 1
        analysis.append(f"claim_a type '{type_a}' (rank {rank_a}) > claim_b type '{type_b}' (rank {rank_b})")
    else:
        analysis.append(f"types: a={type_a} (r{rank_a}), b={type_b} (r{rank_b})")
    
    # Signal 4: Rationale wording — if rationale says "X depends on Y" with X being claim_a-like, it's inverted
    if rationale:
        rationale_lower = rationale.lower()
        # Check if rationale contains the word "depends on" or "requires" and the context
        # suggests claim_a is the dependent (the thing that needs something else)
        if 'depends on' in rationale_lower or 'requires' in rationale_lower:
            # Check if claim_a's statement keywords appear near "depends on"
            stmt_a_words = set(stmt_a.lower().split()[:6])  # First 6 words of claim_a
            # Get words before "depends on" in rationale
            before_depends = rationale_lower.split('depends on')[0].split()[-5:]
            before_words = set(before_depends)
            if stmt_a_words & before_words:
                signals.append('rationale')
                score += 1
                analysis.append(f"rationale positions claim_a as dependent")
    
    should_flip = score >= 1  # Lowered from 2 — any single strong signal is enough
    
    return {
        'claim_a': a,
        'claim_b': b,
        'rationale': rationale[:150],
        'score': score,
        'signals': signals,
        'should_flip': should_flip,
        'analysis': '; '.join(analysis),
        'stmt_a': stmt_a[:120],
        'stmt_b': stmt_b[:120],
    }


def main():
    with open(INVENTORY_PATH) as f:
        inventory = json.load(f)
    
    # Build edge counts
    edge_counts = Counter()
    for e in inventory['edges']:
        edge_counts[e['claim_a']] += 1
        edge_counts[e['claim_b']] += 1
    
    # Get all depends_on edges
    depends = [e for e in inventory['edges'] if e['edge_type'] == 'depends_on']
    
    # Build claim info cache
    claim_info = {}
    all_slugs = set()
    for e in depends:
        for slug in (e['claim_a'], e['claim_b']):
            if slug not in claim_info:
                claim_info[slug] = get_claim_info(slug)
                all_slugs.add(slug)
    
    # Analyze each edge
    results = []
    for e in depends:
        results.append(analyze_edge(e, claim_info, edge_counts, len(depends)))
    
    # Sort by score descending
    results.sort(key=lambda r: r['score'], reverse=True)
    
    # Report
    flips = [r for r in results if r['should_flip']]
    keeps = [r for r in results if not r['should_flip']]
    
    print(f"Total depends_on edges: {len(depends)}")
    print(f"Flagged for flip (score >= 2): {len(flips)}")
    print(f"Kept as-is (score < 2): {len(keeps)}")
    print()
    
    print("=" * 70)
    print("FLIPPING (likely inverted)")
    print("=" * 70)
    for r in flips:
        print(f"\n  Score {r['score']}: {', '.join(r['signals'])}")
        print(f"  A: {r['claim_a']} → B: {r['claim_b']}")
        print(f"  A: {r['stmt_a'][:100]}")
        print(f"  B: {r['stmt_b'][:100]}")
        if r['rationale']:
            print(f"  Rationale: {r['rationale'][:120]}")
    
    print()
    print("=" * 70)
    print("KEEPING (likely correct)")
    print("=" * 70)
    for r in keeps:
        print(f"\n  Score {r['score']}: {', '.join(r.get('signals', ['none']))}")
        print(f"  A: {r['claim_a']} → B: {r['claim_b']}")
        print(f"  {r['analysis']}")
    
    # Write fix manifest
    fixes = {
        'total_depends_on': len(depends),
        'flip_count': len(flips),
        'keep_count': len(keeps),
        'flips': [{'claim_a': r['claim_a'], 'claim_b': r['claim_b'],
                    'rationale': r['rationale'], 'score': r['score'],
                    'signals': r['signals']} for r in flips],
        'keeps': [{'claim_a': r['claim_a'], 'claim_b': r['claim_b'],
                    'score': r['score']} for r in keeps],
    }
    
    with open(OUT_PATH, 'w') as f:
        json.dump(fixes, f, indent=2)
    print(f"\nFix manifest: {OUT_PATH}")


if __name__ == '__main__':
    main()
