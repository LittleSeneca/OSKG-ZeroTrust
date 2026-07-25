#!/usr/bin/env python3
"""Update DoD + Tier 3/4 chapter notes with claims_status and compact summaries."""
import os, re

BASE = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust")
CONCEPTS_DIR = os.path.join(BASE, "notes/concepts")
CLAIMS_DIR = os.path.join(BASE, "notes/claims")
TODAY = "2026-07-24"

CHAPTERS = [
    "DoD ZT Reference Architecture — Overview and Strategy.md",
    "DoD ZT Reference Architecture — Capabilities and Use Cases.md",
    "NIST 800-207A — Cloud-Native Access Control.md",
    "NIST 1800-35 — Implementing ZTA.md",
    "CCCS — Zero Trust Security Model.md",
    "CCCS — ZT Approach to Security Architecture.md",
    "BSI — Zero Trust Position Paper.md",
    "DoD — ZT Strategy and Roadmap.md",
    "NSTAC — ZT and Trusted Identity Management.md",
    "BeyondCorp — Research Papers.md",
    "BeyondProd — Cloud-Native Security.md",
    "Yu — Cyber Defense Matrix.md",
    "Halley — Zero Trust in Resilient Cloud.md",
    "Academic — ZT Research Papers.md",
    "ANSSI-BSI — LLM and Zero Trust.md",
    "NCSC — ZT Principles on Google Cloud.md",
]

HEADING_RE = re.compile(r'^(#{2,3}\s*Claim\s+(\d+)\s*(?:\([^)]*\))?\s*:\s*(.+))$')

# Build lookup: note_name -> [(num, slug, statement), ...]
note_to_claims = {}
for fname in os.listdir(CLAIMS_DIR):
    if not fname.endswith(".md") or fname == "Claims Index.md":
        continue
    fpath = os.path.join(CLAIMS_DIR, fname)
    with open(fpath) as fh:
        fc = fh.read(1500)
    cid_match = re.search(r'claim_id:\s*"([^"]+)"', fc)
    src_match = re.search(r'source_note:\s*"\[\[([^\]]+)\]\]"', fc)
    stmt_match = re.search(r'statement:\s*(.+)$', fc, re.MULTILINE)
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


def update_chapter_note(filepath):
    note_name = os.path.basename(filepath).replace('.md', '')
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Add claims_status to frontmatter
    if "claims_status:" not in text[:2000]:
        updated_line = re.search(r'^updated:.*$', text[:2000], re.MULTILINE)
        if updated_line:
            pos = updated_line.end()
            text = text[:pos] + f"\nclaims_status: extracted\nclaims_extracted: {TODAY}" + text[pos:]
        else:
            fm_end = text.find("\n---", 5)
            if fm_end > 0:
                text = text[:fm_end] + f"\nclaims_status: extracted\nclaims_extracted: {TODAY}" + text[fm_end:]

    lines = text.split('\n')

    # Find claim blocks
    claim_positions = []
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line.strip())
        if m:
            num = int(m.group(2))
            end = len(lines)
            for j in range(i + 1, len(lines)):
                stripped = lines[j].strip()
                if stripped == '---':
                    end = j
                    break
                if HEADING_RE.match(stripped):
                    end = j
                    break
                if re.match(r'^##\s+\S', stripped) and not re.match(r'^###\s+', stripped):
                    end = j
                    break
            claim_positions.append({"num": num, "start": i, "end": end})

    # Build summary replacements
    my_claims = note_to_claims.get(note_name, [])
    my_claims.sort(key=lambda x: x[0])

    replacements = {}
    for cp in claim_positions:
        n = cp["num"]
        matching = [c for c in my_claims if c[0] == n]
        if matching:
            _, slug, stmt = matching[0]
            summary = f"**Claim {n} —** {stmt} → [[{slug}]]"
        else:
            summary = f"**Claim {n} —** _claim file not found_"
        replacements[cp["start"]] = {"end": cp["end"], "summary": summary}

    # Apply replacements (reverse order)
    new_lines = list(lines)
    for start_line in sorted(replacements.keys(), reverse=True):
        r = replacements[start_line]
        new_lines[start_line:r["end"]] = [r["summary"]]

    result = '\n'.join(new_lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(result)

    return len(claim_positions)


def main():
    for cf in CHAPTERS:
        filepath = os.path.join(CONCEPTS_DIR, cf)
        if not os.path.isfile(filepath):
            print(f"MISSING: {cf}")
            continue
        n = update_chapter_note(filepath)
        print(f"Updated {cf}: {n} claims compacted")

    print("\n=== ALL CHAPTER NOTES UPDATED ===")


if __name__ == "__main__":
    main()
