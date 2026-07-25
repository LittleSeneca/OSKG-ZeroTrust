#!/usr/bin/env python3
"""
Update chapter notes after Batch 3 extraction:
- Add claims_status: extracted to frontmatter
- Replace claim blocks with compact summaries
- Preserve interstitial content (assessment tables, cross-references)
"""
import os, re

BASE = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust")
CONCEPTS_DIR = os.path.join(BASE, "notes/concepts")

TODAY = "2026-07-24"

CHAPTERS = [
    {"file": "NSA — User Pillar.md", "n": 6},
    {"file": "NSA — Device Pillar.md", "n": 8},
    {"file": "NSA — Network Environment Pillar.md", "n": 6},
    {"file": "CISA ZTMM — Overview and Framework.md", "n": 9},
    {"file": "CISA ZTMM — Identity Pillar.md", "n": 8},
    {"file": "CISA ZTMM — Device Network App Data Pillars.md", "n": 25},
]

HEADING_RE = re.compile(r'^(#{2,3}\s*Claim\s+(\d+)\s*(?:\([^)]*\))?\s*:\s*(.+))$')
ANY_HEADING_RE = re.compile(r'^(#{1,4}\s+)')

def find_claim_blocks(text):
    """Return [{num, start_line, end_line, heading_line, title}, ...]"""
    lines = text.split('\n')
    claims = []
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line.strip())
        if m:
            claims.append({
                "num": int(m.group(2)),
                "title": m.group(3).strip(),
                "heading_line": i,
                "heading_text": m.group(1),
            })

    # Find end for each claim
    for idx, claim in enumerate(claims):
        start = claim["heading_line"]
        # Search forward for --- or next claim heading
        end = len(lines)
        for j in range(start + 1, len(lines)):
            stripped = lines[j].strip()
            if stripped == '---':
                end = j
                break
            if HEADING_RE.match(stripped):
                end = j
                break
            # Also break at ## section headers (but not ### sub-headers within a claim)
            if re.match(r'^##\s+\S', stripped) and not re.match(r'^###\s+', stripped):
                end = j
                break
        claim["end_line"] = end

    return claims


def update_chapter_note(filepath, num_claims):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Add claims_status to frontmatter if not present
    if "claims_status:" not in text[:2000]:
        # Insert after 'updated:' line or before first '---'
        updated_line = re.search(r'^updated:.*$', text[:2000], re.MULTILINE)
        if updated_line:
            pos = updated_line.end()
            text = text[:pos] + f"\nclaims_status: extracted\nclaims_extracted: {TODAY}" + text[pos:]
        else:
            # Insert before closing ---
            fm_end = text.find("\n---", 5)
            if fm_end > 0:
                text = text[:fm_end] + f"\nclaims_status: extracted\nclaims_extracted: {TODAY}" + text[fm_end:]

    lines = text.split('\n')
    claims = find_claim_blocks(text)

    # 2. Build compact summaries
    # Read slugs from claim files to get the correct [[wikilinks]]
    claims_dir = os.path.join(BASE, "notes/claims")
    slug_map = {}

    for claim in claims:
        n = claim["num"]
        # Try to find the claim file by scanning for the claim_id in frontmatter
        for fname in os.listdir(claims_dir):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(claims_dir, fname)
            with open(fpath) as fh:
                fc = fh.read(500)
            # Look for claim_id in frontmatter - we need to match the right one
            # We can't easily map claim_num to slug without the META dict
            # So let's build a map from the claim file itself
        break  # We'll handle this differently

    # Actually let's build summary lines from the heading titles and slugs we know
    # using the META dict from extract_batch3.py would be circular
    # Instead, let's search claim files for their source_note and claim_id

    # Build a lookup: source_note -> [(num, slug, statement), ...]
    note_to_claims = {}
    for fname in os.listdir(claims_dir):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(claims_dir, fname)
        with open(fpath) as fh:
            fc = fh.read(1500)
        # Extract claim_id and source_note from frontmatter
        cid_match = re.search(r'^claim_id:\s*"([^"]+)"', fc, re.MULTILINE)
        src_match = re.search(r'^source_note:\s*"\[\[([^\]]+)\]\]"', fc, re.MULTILINE)
        stmt_match = re.search(r'^statement:\s*(.+)$', fc, re.MULTILINE)
        if cid_match and src_match:
            cid = cid_match.group(1)  # e.g., "nsa-user.1"
            src = src_match.group(1)  # e.g., "NSA — User Pillar"
            stmt = stmt_match.group(1).strip().strip('"').strip("'") if stmt_match else ""
            # Parse num from cid
            parts = cid.rsplit('.', 1)
            if len(parts) == 2:
                try:
                    num = int(parts[1])
                    slug = fname.replace('.md', '')
                    if src not in note_to_claims:
                        note_to_claims[src] = []
                    note_to_claims[src].append((num, slug, stmt))
                except ValueError:
                    pass

    # 3. Replace claim blocks with compact summaries (work backwards to preserve line indices)
    note_name = os.path.basename(filepath).replace('.md', '')
    my_claims = note_to_claims.get(note_name, [])
    my_claims.sort(key=lambda x: x[0])

    # Build replacement map: heading_line -> summary line(s)
    replacements = {}
    for claim in claims:
        n = claim["num"]
        matching = [c for c in my_claims if c[0] == n]
        if matching:
            _, slug, stmt = matching[0]
            summary = f"**Claim {n} —** {stmt} → [[{slug}]]"
        else:
            summary = f"**Claim {n} —** {claim['title']} → (claim file not found)"

        # Replace from heading_line to end_line with just the summary
        replacements[claim["heading_line"]] = {
            "end_line": claim["end_line"],
            "summary": summary,
        }

    # Apply replacements (work backwards)
    new_lines = list(lines)
    for start_line in sorted(replacements.keys(), reverse=True):
        r = replacements[start_line]
        end_line = r["end_line"]
        summary = r["summary"]
        # Delete lines from start_line to end_line-1, insert summary at start_line
        new_lines[start_line:end_line] = [summary]

    result = '\n'.join(new_lines)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(result)

    return len(claims)


def main():
    claims_dir = os.path.join(BASE, "notes/claims")
    if not os.path.isdir(claims_dir):
        print("Claims directory not found!")
        return

    for ch in CHAPTERS:
        filepath = os.path.join(CONCEPTS_DIR, ch["file"])
        if not os.path.isfile(filepath):
            print(f"MISSING: {ch['file']}")
            continue
        n = update_chapter_note(filepath, ch["n"])
        print(f"Updated {ch['file']}: {n} claims compressed")

    print("\n=== CHAPTER NOTE UPDATES COMPLETE ===")


if __name__ == "__main__":
    main()
