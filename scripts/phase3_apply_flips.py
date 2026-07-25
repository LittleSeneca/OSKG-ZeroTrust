#!/usr/bin/env python3
"""Apply depends_on direction flips to claim files.

Reads phase3_depends_fixes.json. For each flagged flip:
  1. Remove old depends_on wikilink from current claim_b's file
  2. Add corrected depends_on wikilink to NEW claim_b's file (old claim_a)
"""

import json, os, re

CLAIMS = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/notes/claims")
FIXES = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/scripts/phase3_depends_fixes.json")


def remove_depends_wikilink(filepath, target_slug):
    """Remove the depends_on wikilink pointing to target_slug."""
    content = open(filepath).read()
    
    dp = content.find('**Depends on:**')
    if dp == -1:
        return 'no_header'
    
    ns = content.find('\n**', dp + len('**Depends on:**'))
    if ns == -1:
        ns2 = content.find('\n## ', dp)
        section_end = ns2 if ns2 != -1 else len(content)
    else:
        section_end = ns
    
    before = content[:dp]
    section = content[dp:section_end]
    after = content[section_end:]
    
    # Remove lines containing [[target_slug
    lines = section.split('\n')
    new_lines = [l for l in lines if f'[[{target_slug}' not in l and f'[[{target_slug}]]' not in l]
    
    if len(new_lines) == len(lines):
        return 'not_found'
    
    content = before + '\n'.join(new_lines) + after
    open(filepath, 'w').write(content)
    return 'removed'


def add_depends_wikilink(filepath, target_slug, rationale=''):
    """Add a depends_on wikilink to target_slug."""
    content = open(filepath).read()
    
    dp = content.find('**Depends on:**')
    if dp == -1:
        return 'no_header'
    
    # Check if already present
    ns = content.find('\n**', dp + len('**Depends on:**'))
    if ns == -1:
        ns2 = content.find('\n## ', dp)
        section = content[dp:ns2] if ns2 != -1 else content[dp:]
    else:
        section = content[dp:ns]
    
    if f'[[{target_slug}' in section:
        return 'already_present'
    
    # Insert after header, skip comment
    nl = content.find('\n', dp)
    ip = nl + 1
    peek = content[ip:ip+6]
    if peek.startswith('<!--'):
        ce = content.find('-->\n', ip)
        if ce != -1:
            ip = ce + 4
            if content[ip:ip+1] == '\n':
                ip += 1
    
    display = rationale[:120].strip() if rationale else target_slug
    wl = f'- [[{target_slug}|{display}]]\n'
    content = content[:ip] + wl + content[ip:]
    open(filepath, 'w').write(content)
    return 'added'


def main():
    with open(FIXES) as f:
        fixes = json.load(f)
    
    results = {'removed': 0, 'added': 0, 'not_found': 0, 'already_present': 0, 'no_header': 0}
    
    for flip in fixes['flips']:
        old_a = flip['claim_a']  # This was the (wrong) dependency
        old_b = flip['claim_b']  # This was the (wrong) dependent
        rationale = flip.get('rationale', '')
        
        # After flip: old_a is the new dependent (depends on old_b)
        new_dependent = old_a  # was claim_a, now claim_b
        new_dependency = old_b  # was claim_b, now claim_a
        
        # Step 1: Remove old wikilink from old_b's file (old_b had "Depends on: [[old_a]]")
        fpath_b = os.path.join(CLAIMS, f"{old_b}.md")
        if os.path.isfile(fpath_b):
            r = remove_depends_wikilink(fpath_b, old_a)
            results[r] = results.get(r, 0) + 1
        
        # Step 2: Add new wikilink to new dependent's file (old_a now has "Depends on: [[old_b]]")
        fpath_a = os.path.join(CLAIMS, f"{old_a}.md")
        if os.path.isfile(fpath_a):
            r = add_depends_wikilink(fpath_a, old_b, rationale)
            results[r] = results.get(r, 0) + 1
    
    print("Flip results:")
    for k, v in sorted(results.items()):
        print(f"  {k}: {v}")
    
    if results.get('no_header', 0) > 0:
        print("\n  (no_header means the claim file doesn't have a Depends on: section — may need manual fix)")


if __name__ == '__main__':
    main()
