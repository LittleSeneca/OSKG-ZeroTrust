#!/usr/bin/env python3
"""
Update chapter notes after Batch 4 extraction:
- Add claims_status: extracted and claims_extracted to frontmatter
- Replace claim blocks with compact summaries (Claim N — Title → [[slug]])
- Preserve interstitial content (assessment tables, cross-references, ## section headers)
"""
import os, re

BASE = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust")
CONCEPTS_DIR = os.path.join(BASE, "notes/concepts")
CLAIMS_DIR = os.path.join(BASE, "notes/claims")

TODAY = "2026-07-24"

CHAPTERS = [
    {"file": "Gilman and Barth — Ch2 — Managing Trust.md", "n": 6},
    {"file": "Gilman and Barth — Ch3 — Network Agents.md", "n": 5},
    {"file": "Gilman and Barth — Ch4-6 — Authorization Devices Users.md", "n": 14},
    {"file": "Gilman and Barth — Ch7-8 — Applications and Traffic.md", "n": 13},
    {"file": "Gilman and Barth — Ch9 — Realizing a Zero Trust Network.md", "n": 7},
    {"file": "Gilman and Barth — Ch10 — The Adversarial View.md", "n": 8},
    {"file": "Garbis and Chapman — Ch1-3 — Introduction and Architecture.md", "n": 14},
    {"file": "Garbis and Chapman — Network and Access Technologies.md", "n": 8},
    {"file": "Garbis and Chapman — Practice IAM Policy.md", "n": 13},
    {"file": "Garbis and Chapman — Cloud IaaS SaaS.md", "n": 6},
    {"file": "Garbis and Chapman — SOC Data IoT.md", "n": 5},
    {"file": "Garbis and Chapman — Scenarios and Conclusion.md", "n": 5},
    {"file": "Finney — Ch1-3 — The Zero Trust Story.md", "n": 12},
    {"file": "Finney — Ch4-7 — Building the ZT Strategy.md", "n": 11},
    {"file": "Finney — Ch8-11 — Execution and Sustainability.md", "n": 13},
    {"file": "Green-Ortiz — Intro Ch1-2 — Foundations.md", "n": 8},
    {"file": "Green-Ortiz — Ch3-5 — Trust and Policy.md", "n": 6},
    {"file": "Green-Ortiz — Ch6-8 — Implementation.md", "n": 9},
    {"file": "Green-Ortiz — Ch9-11 — Advanced and Future.md", "n": 7},
]

HEADING_RE = re.compile(r'^(#{2,3}\s*Claim\s+(\d+)(?:\s*\([^)]*\))?\s*:\s*(.+))$')
SECTION_HEADING_RE = re.compile(r'^##\s+\S')


def find_claim_blocks(text):
    """Return [{num, heading_line, end_line, title}, ...]"""
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

    for idx, claim in enumerate(claims):
        start = claim["heading_line"]
        end = len(lines)
        for j in range(start + 1, len(lines)):
            stripped = lines[j].strip()
            if stripped == '---':
                end = j
                break
            if HEADING_RE.match(stripped):
                end = j
                break
            # Stop at ## section headers (not ### sub-headers)
            if SECTION_HEADING_RE.match(stripped):
                end = j
                break
        claim["end_line"] = end

    return claims


def build_note_to_claims():
    """Build lookup: note_name -> [(num, slug, statement), ...] from claim files."""
    note_to_claims = {}
    for fname in os.listdir(CLAIMS_DIR):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(CLAIMS_DIR, fname)
        with open(fpath) as fh:
            fc = fh.read(2000)
        cid_match = re.search(r'^claim_id:\s*"([^"]+)"', fc, re.MULTILINE)
        src_match = re.search(r'^source_note:\s*"\[\[([^\]]+)\]\]"', fc, re.MULTILINE)
        stmt_match = re.search(r'^statement:\s*(.+)$', fc, re.MULTILINE)
        if cid_match and src_match:
            cid = cid_match.group(1)
            src = src_match.group(1)
            stmt = stmt_match.group(1).strip().strip('"').strip("'") if stmt_match else ""
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
    return note_to_claims


def update_chapter_note(filepath, note_to_claims):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Add claims_status to frontmatter if not present
    if "claims_status:" not in text[:2500]:
        updated_line = re.search(r'^updated:.*$', text[:2500], re.MULTILINE)
        if updated_line:
            pos = updated_line.end()
            text = text[:pos] + f"\nclaims_status: extracted\nclaims_extracted: {TODAY}" + text[pos:]
        else:
            fm_end = text.find("\n---", 5)
            if fm_end > 0:
                text = text[:fm_end] + f"\nclaims_status: extracted\nclaims_extracted: {TODAY}" + text[fm_end:]

    lines = text.split('\n')
    claims = find_claim_blocks(text)

    note_name = os.path.basename(filepath).replace('.md', '')
    my_claims = note_to_claims.get(note_name, [])
    my_claims.sort(key=lambda x: x[0])

    # Build replacement map
    replacements = {}
    for claim in claims:
        n = claim["num"]
        matching = [c for c in my_claims if c[0] == n]
        if matching:
            _, slug, stmt = matching[0]
            summary = f"**Claim {n} —** {stmt} → [[{slug}]]"
        else:
            summary = f"**Claim {n} —** {claim['title']} → (claim file not found)"

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
        new_lines[start_line:end_line] = [summary, ""]  # Add blank line after summary

    result = '\n'.join(new_lines)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(result)

    return len(claims)


def main():
    if not os.path.isdir(CLAIMS_DIR):
        print("Claims directory not found!")
        return

    note_to_claims = build_note_to_claims()
    print(f"Found {sum(len(v) for v in note_to_claims.values())} claim-file mappings for {len(note_to_claims)} notes")

    for ch in CHAPTERS:
        filepath = os.path.join(CONCEPTS_DIR, ch["file"])
        if not os.path.isfile(filepath):
            print(f"MISSING: {ch['file']}")
            continue
        n = update_chapter_note(filepath, note_to_claims)
        print(f"Updated {ch['file']}: {n} claims compressed")

    print("\n=== CHAPTER NOTE UPDATES COMPLETE ===")


if __name__ == "__main__":
    main()
