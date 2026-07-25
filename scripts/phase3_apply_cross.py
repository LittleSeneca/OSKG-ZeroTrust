#!/usr/bin/env python3
"""Apply Pass 2.5 cross-cluster edges, filtering out false contradictions and fixing directions."""
import json, os, re

CLAIMS = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/notes/claims")
CROSS_DIR = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/scripts/phase3_edges_cross")

def load_slug_map():
    """Build claim_id → slug lookup."""
    slug_map = {}
    for fname in os.listdir(CLAIMS):
        if not fname.endswith('.md'): continue
        slug = fname[:-3]
        text = open(os.path.join(CLAIMS, fname)).read()
        m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
        if not m: continue
        for line in m.group(1).split('\n'):
            kv = re.match(r'^claim_id:\s*"?(.*?)"?\s*$', line)
            if kv:
                slug_map[kv.group(1).strip().strip('"')] = slug
                break
    return slug_map

def resolve(ref, slug_map, all_slugs):
    if ref in all_slugs: return ref
    if ref in slug_map: return slug_map[ref]
    for cid, s in slug_map.items():
        if cid.startswith(ref) or ref.startswith(cid):
            return s
    return ref

# Known false contradictions from Pass 2.5 audit
FALSE_CONTRADICTS = {
    ("zt-positive-tenets", "zt-defined-cisa-five"),
    ("zt-positive-tenets", "zt-assume-breach"),
    ("nist-document-structure-framework", "zt-assume-breach"),
}

# Known inverted depends_on (claim_a should be claim_b and vice versa)
INVERTED_DEPS = {
    ("there-are-three-distinct-types-of-peps-and", "the-control-plane-is-the-trust-grantor-temporary"),
}

def apply_edge(claim_a, claim_b, edge_type, rationale):
    """Apply a single edge. Returns 'added', 'skip', or error."""
    header_map = {
        'depends_on': '**Depends on:**',
        'supports': '**Supports:**',
        'extends': '**Extends:**',
        'contradicts': '**Contradicts:**',
    }
    
    patches = []
    if edge_type == 'depends_on':
        patches.append((claim_b, claim_a, edge_type, rationale))
    elif edge_type == 'supports':
        patches.append((claim_a, claim_b, edge_type, rationale))
    elif edge_type == 'extends':
        patches.append((claim_a, claim_b, edge_type, rationale))
    elif edge_type == 'contradicts':
        patches.append((claim_a, claim_b, edge_type, rationale))
        patches.append((claim_b, claim_a, edge_type, rationale))
    
    results = []
    for slug, target, et, rat in patches:
        fpath = os.path.join(CLAIMS, f"{slug}.md")
        if not os.path.isfile(fpath):
            results.append(f"missing:{slug}")
            continue
        
        content = open(fpath).read()
        header = header_map.get(et)
        if not header:
            results.append(f"bad_type:{et}")
            continue
        
        # Check if already present
        hp = content.find(header)
        if hp == -1:
            results.append(f"no_header:{slug}:{et}")
            continue
        
        ns = content.find('\n**', hp + len(header))
        if ns == -1:
            ns2 = content.find('\n## ', hp)
            section = content[hp:ns2] if ns2 != -1 else content[hp:]
        else:
            section = content[hp:ns]
        
        if f'[[{target}' in section:
            results.append(f"skip:{slug}->{target}")
            continue
        
        # Insert wikilink
        nl = content.find('\n', hp)
        ip = nl + 1
        peek = content[ip:ip+6]
        if peek.startswith('<!--'):
            ce = content.find('-->\n', ip)
            if ce != -1:
                ip = ce + 4
                if content[ip:ip+1] == '\n':
                    ip += 1
        
        display = rat[:120].strip() if rat else target
        wl = f'- [[{target}|{display}]]\n'
        content = content[:ip] + wl + content[ip:]
        open(fpath, 'w').write(content)
        results.append(f"added:{slug}->{target}")
    
    return '; '.join(results)


def main():
    slug_map = load_slug_map()
    all_slugs = set()
    for fname in os.listdir(CLAIMS):
        if fname.endswith('.md'):
            all_slugs.add(fname[:-3])
    
    total_added = 0
    total_skipped = 0
    total_filtered = 0
    errors = []
    
    for fname in sorted(os.listdir(CROSS_DIR)):
        if not fname.endswith('.json'):
            continue
        
        data = json.load(open(os.path.join(CROSS_DIR, fname)))
        edges = data if isinstance(data, list) else data.get('edges', [])
        
        for e in edges:
            a = e.get('claim_a') or e.get('source') or ''
            b = e.get('claim_b') or e.get('target') or ''
            t = e.get('edge_type') or e.get('type') or e.get('relation') or e.get('relationship') or '?'
            r = e.get('rationale', '')
            
            # Resolve claim_ids to slugs
            a = resolve(a, slug_map, all_slugs)
            b = resolve(b, slug_map, all_slugs)
            
            # Filter false contradictions
            if t == 'contradicts':
                pair = tuple(sorted([a, b]))
                if pair in FALSE_CONTRADICTS or (b, a) in FALSE_CONTRADICTS:
                    total_filtered += 1
                    continue
            
            # Fix inverted depends_on
            if t == 'depends_on':
                if (a, b) in INVERTED_DEPS:
                    a, b = b, a  # Swap
            
            result = apply_edge(a, b, t, r)
            if 'added' in result:
                total_added += 1
            elif 'skip' in result:
                total_skipped += 1
            else:
                errors.append(f"{fname}: {result}")
    
    print(f"Added: {total_added}")
    print(f"Skipped (already present): {total_skipped}")
    print(f"Filtered (false contradictions): {total_filtered}")
    if errors:
        print(f"Errors: {len(errors)}")
        for e in errors[:10]:
            print(f"  {e}")


if __name__ == '__main__':
    main()
