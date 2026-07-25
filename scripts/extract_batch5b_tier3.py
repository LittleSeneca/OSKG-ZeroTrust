#!/usr/bin/env python3
"""
Phase 2 Batch 5b: Extract Tier 3 claims (14 notes, ~91 claims).
Auto-generates slugs from claim titles to avoid manual META dict.
"""
import os, re
from collections import OrderedDict

BASE = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust")
CONCEPTS_DIR = os.path.join(BASE, "notes/concepts")
CLAIMS_DIR = os.path.join(BASE, "notes/claims")
TODAY = "2026-07-24"

CHAPTERS = [
    {"key": "nist-207a", "file": "NIST 800-207A — Cloud-Native Access Control.md",
     "note": "NIST 800-207A — Cloud-Native Access Control", "n": 7,
     "source_tag": "source/nist-sp-800-207a",
     "source_line": "NIST, *SP 800-207A — Cloud-Native Access Control*, 2023",
     "topics": ["zt-cloud", "zt-implementation"], "claim_type": "implementation"},
    {"key": "nist-1800-35", "file": "NIST 1800-35 — Implementing ZTA.md",
     "note": "NIST 1800-35 — Implementing ZTA", "n": 6,
     "source_tag": "source/nist-sp-1800-35",
     "source_line": "NIST, *SP 1800-35 — Implementing a Zero Trust Architecture*, 2023",
     "topics": ["zt-implementation"], "claim_type": "implementation"},
    {"key": "cccs-model", "file": "CCCS — Zero Trust Security Model.md",
     "note": "CCCS — Zero Trust Security Model", "n": 5,
     "source_tag": "source/cccs",
     "source_line": "Canadian Centre for Cyber Security, *Zero Trust Security Model — ITSAP.10.008*, 2023",
     "topics": ["zt-definition"], "claim_type": "definitional"},
    {"key": "cccs-arch", "file": "CCCS — ZT Approach to Security Architecture.md",
     "note": "CCCS — ZT Approach to Security Architecture", "n": 7,
     "source_tag": "source/cccs",
     "source_line": "Canadian Centre for Cyber Security, *Zero Trust Approach to Security Architecture — ITSM.10.008*, 2023",
     "topics": ["zt-architecture", "zt-implementation"], "claim_type": "architectural"},
    {"key": "bsi-zt", "file": "BSI — Zero Trust Position Paper.md",
     "note": "BSI — Zero Trust Position Paper", "n": 9,
     "source_tag": "source/bsi",
     "source_line": "BSI, *Zero Trust Position Paper*, 2023",
     "topics": ["zt-definition", "zt-governance"], "claim_type": "definitional"},
    {"key": "dod-strategy", "file": "DoD — ZT Strategy and Roadmap.md",
     "note": "DoD — ZT Strategy and Roadmap", "n": 5,
     "source_tag": "source/dod-zt-strategy",
     "source_line": "Department of Defense, *Zero Trust Strategy and Roadmap*, 2022",
     "topics": ["zt-governance", "zt-migration"], "claim_type": "governance"},
    {"key": "nstac", "file": "NSTAC — ZT and Trusted Identity Management.md",
     "note": "NSTAC — ZT and Trusted Identity Management", "n": 7,
     "source_tag": "source/nstac",
     "source_line": "NSTAC, *Zero Trust and Trusted Identity Management*, 2022",
     "topics": ["zt-identity", "zt-governance"], "claim_type": "governance"},
    {"key": "beyondcorp", "file": "BeyondCorp — Research Papers.md",
     "note": "BeyondCorp — Research Papers", "n": 11,
     "source_tag": "source/beyondcorp",
     "source_line": "Google, *BeyondCorp Research Papers*, 2014-2020",
     "topics": ["zt-implementation", "zt-architecture"], "claim_type": "implementation"},
    {"key": "beyondprod", "file": "BeyondProd — Cloud-Native Security.md",
     "note": "BeyondProd — Cloud-Native Security", "n": 6,
     "source_tag": "source/beyondprod",
     "source_line": "Google, *BeyondProd: Cloud-Native Security*, 2019",
     "topics": ["zt-cloud", "zt-implementation"], "claim_type": "implementation"},
    {"key": "yu-cdm", "file": "Yu — Cyber Defense Matrix.md",
     "note": "Yu — Cyber Defense Matrix", "n": 4,
     "source_tag": "source/yu-cdm",
     "source_line": "Sounil Yu, *Cyber Defense Matrix*, 2022",
     "topics": ["zt-architecture", "zt-definition"], "claim_type": "architectural"},
    {"key": "halley", "file": "Halley — Zero Trust in Resilient Cloud.md",
     "note": "Halley — Zero Trust in Resilient Cloud", "n": 4,
     "source_tag": "source/halley-resilient-cloud",
     "source_line": "Andrew Halley et al., *Zero Trust in Resilient Cloud*, 2023",
     "topics": ["zt-cloud", "zt-implementation"], "claim_type": "implementation"},
    {"key": "academic", "file": "Academic — ZT Research Papers.md",
     "note": "Academic — ZT Research Papers", "n": 6,
     "source_tag": "source/academic-zt",
     "source_line": "Various, *Academic ZT Research Papers*, 2018-2024",
     "topics": ["zt-definition"], "claim_type": "definitional"},
    {"key": "anssi-bsi", "file": "ANSSI-BSI — LLM and Zero Trust.md",
     "note": "ANSSI-BSI — LLM and Zero Trust", "n": 7,
     "source_tag": "source/anssi-bsi",
     "source_line": "ANSSI/BSI, *LLM and Zero Trust*, 2024",
     "topics": ["zt-definition", "zt-implementation"], "claim_type": "definitional"},
    {"key": "ncsc", "file": "NCSC — ZT Principles on Google Cloud.md",
     "note": "NCSC — ZT Principles on Google Cloud", "n": 7,
     "source_tag": "source/ncsc",
     "source_line": "NCSC, *Zero Trust Principles on Google Cloud*, 2023",
     "topics": ["zt-cloud", "zt-implementation"], "claim_type": "implementation"},
]

HEADING_RE = re.compile(r'^#{2,3}\s*Claim\s+(\d+)\s*(?:\([^)]*\))?\s*:\s*(.+)$')
MARKER_RE = re.compile(r'^\*\*([^*:]+?):\*\*\s*(.*)$')

CLAIM_MARKERS = {"author's claim", "nist's claim", "nist's description",
                 "nsa's claim", "cisa's claim", "authors' claim",
                 "finney's claim", "green-ortiz's claim",
                 "dod's claim", "cccs's claim", "bsi's claim",
                 "nstac's claim", "yu's claim", "halley's claim",
                 "google's claim"}
EVIDENCE_MARKERS = {"evidence presented"}
CONFIDENCE_MARKERS = {"confidence"}
STAKES_MARKERS = {"what's at stake"}
DISAGREE_WHO_MARKERS = {"who disagrees"}
DISAGREE_ALT_MARKERS = {"alternative reading"}
ASSESSMENT_MARKERS = {"my assessment", "assessment"}

STOP_WORDS = {"a", "an", "the", "is", "are", "was", "were", "be", "been",
              "of", "in", "on", "at", "to", "for", "with", "by", "from",
              "and", "or", "not", "but", "as", "it", "its", "that", "this",
              "these", "those", "has", "have", "can", "will", "may", "would",
              "should", "must", "each", "all", "both", "between", "through",
              "over", "under", "into", "more", "less", "than", "which"}


def title_to_slug(title, max_words=7):
    """Convert a claim title to a hyphenated slug."""
    # Strip trailing parentheticals and annotations
    title = re.sub(r'\s*[—–-]\s*.*$', '', title)
    title = re.sub(r'\s*\([^)]*\)\s*$', '', title)
    # Lowercase and tokenize
    words = re.findall(r'[a-z0-9]+', title.lower())
    # Remove stop words and short tokens, keep max_words
    filtered = [w for w in words if w not in STOP_WORDS and len(w) > 1]
    if len(filtered) > max_words:
        filtered = filtered[:max_words]
    if not filtered:
        filtered = words[:max_words]
    slug = '-'.join(filtered)
    # Truncate to reasonable length
    if len(slug) > 80:
        slug = slug[:80].rstrip('-')
    # Remove duplicate hyphens
    slug = re.sub(r'-{2,}', '-', slug)
    return slug.strip('-')


def normalize_marker(name):
    name = name.strip().lower()
    name = re.sub(r'\s*\([^)]*\)\s*$', '', name)
    name = re.sub(r'\s*[—-]\s*.*$', '', name)
    return name.strip()


def clean_title(title):
    return re.sub(r'\s*(?:\(Scenario|\(Step)[^)]*\)\.?\s*$', '', title).strip()


def split_claim_blocks(text):
    lines = text.split('\n')
    headings = []
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line.strip())
        if m:
            headings.append((i, int(m.group(1)), m.group(2)))
    blocks = {}
    for idx, (line_i, num, raw_title) in enumerate(headings):
        end = len(lines)
        for j in range(line_i + 1, len(lines)):
            stripped = lines[j].strip()
            if stripped == '---':
                end = j
                break
            if HEADING_RE.match(stripped):
                end = j
                break
        blocks[num] = {"title": clean_title(raw_title), "lines": lines[line_i + 1:end]}
    return blocks


def scan_markers(block_lines):
    segments = []
    current_marker = None
    current_lines = []
    for line in block_lines:
        m = MARKER_RE.match(line.strip())
        if m:
            if current_marker is not None:
                segments.append((current_marker, current_lines))
            current_marker = m.group(1)
            current_lines = [m.group(2)] if m.group(2) else []
        else:
            if current_marker is not None:
                current_lines.append(line)
    if current_marker is not None:
        segments.append((current_marker, current_lines))
    return segments


def join_content(lines):
    text = '\n'.join(lines).strip()
    return re.sub(r'\n{3,}', '\n\n', text)


def extract_sections(block_lines):
    split_idx = None
    for i, line in enumerate(block_lines):
        if line.strip().startswith('#### '):
            split_idx = i
            break
    if split_idx is not None:
        main_lines, extended_lines = block_lines[:split_idx], block_lines[split_idx:]
    else:
        main_lines, extended_lines = block_lines, []

    buckets = {"claim": [], "evidence": [], "confidence": [],
               "stakes": [], "disagree_who": [], "disagree_alt": [], "assessment": []}
    evidence_extra = []

    for raw_marker, content_lines in scan_markers(main_lines):
        norm = normalize_marker(raw_marker)
        if norm in CLAIM_MARKERS:
            buckets["claim"].append(join_content(content_lines))
        elif norm in EVIDENCE_MARKERS:
            buckets["evidence"].append(join_content(content_lines))
        elif norm in CONFIDENCE_MARKERS:
            buckets["confidence"].append(join_content(content_lines))
        elif norm in STAKES_MARKERS:
            buckets["stakes"].append(join_content(content_lines))
        elif norm in DISAGREE_WHO_MARKERS:
            buckets["disagree_who"].append(join_content(content_lines))
        elif norm in DISAGREE_ALT_MARKERS:
            buckets["disagree_alt"].append(join_content(content_lines))
        elif norm in ASSESSMENT_MARKERS:
            buckets["assessment"].append(join_content(content_lines))
        else:
            content = join_content(content_lines)
            if content:
                evidence_extra.append("**%s:**\n\n%s" % (raw_marker.strip(), content))
            else:
                evidence_extra.append("**%s:**" % raw_marker.strip())

    extended_text = join_content(extended_lines)
    if extended_text:
        evidence_extra.append(extended_text)

    return {"claim": "\n\n".join(buckets["claim"]).strip(),
            "evidence": "\n\n".join(buckets["evidence"] + evidence_extra).strip(),
            "confidence": "\n\n".join(buckets["confidence"]).strip(),
            "stakes": "\n\n".join(buckets["stakes"]).strip(),
            "disagree_who": "\n\n".join(buckets["disagree_who"]).strip(),
            "disagree_alt": "\n\n".join(buckets["disagree_alt"]).strip(),
            "assessment": "\n\n".join(buckets["assessment"]).strip()}


RATING_RE = re.compile(r'^(VERY HIGH|HIGH|MEDIUM-HIGH|MEDIUM|MEDIUM-LOW|LOW)', re.IGNORECASE)


def parse_confidence(confidence_text):
    m = RATING_RE.match(confidence_text.strip())
    if not m:
        return "medium", confidence_text.strip()
    raw = m.group(1).upper()
    if raw in ("VERY HIGH", "HIGH"):
        return "high", confidence_text.strip()
    elif raw == "LOW":
        return "low", confidence_text.strip()
    return "medium", confidence_text.strip()


def truncate_rationale(text, limit=150):
    text = ' '.join(text.split())
    if len(text) <= limit:
        return text
    truncated = text[:limit]
    if ' ' in truncated:
        truncated = truncated.rsplit(' ', 1)[0]
    return truncated.rstrip('.,;:—- ')


def yaml_quote(s):
    s = s.replace('\n', ' ').strip()
    has_dq = '"' in s
    has_sq = "'" in s
    if has_dq and has_sq:
        return '"%s"' % s.replace('\\', '\\\\').replace('"', '\\"')
    if has_dq:
        return "'%s'" % s.replace("'", "''")
    return '"%s"' % s.replace('\\', '\\\\')


FALLBACK_STAKES = "_Not addressed separately in the source note._"
FALLBACK_DISAGREE = "_None identified._"
FALLBACK_ASSESSMENT = "_Not addressed separately in the source note._"
FALLBACK_EVIDENCE = "_No evidence separable from the claim statement in the source note._"


def build_claim_file(chapter, num, block):
    statement = block["title"]
    slug = title_to_slug(statement)
    claim_id = "%s.%d" % (chapter["key"], num)
    sections = extract_sections(block["lines"])

    confidence_raw = sections["confidence"] or "MEDIUM."
    rating, rationale_full = parse_confidence(confidence_raw)
    rationale = truncate_rationale(rationale_full)

    claim_text = sections["claim"] or statement
    evidence_text = sections["evidence"] or FALLBACK_EVIDENCE
    stakes_text = sections["stakes"] or FALLBACK_STAKES
    disagree_who = sections["disagree_who"] or FALLBACK_DISAGREE
    disagree_alt = sections["disagree_alt"] or FALLBACK_DISAGREE
    assessment_text = sections["assessment"] or FALLBACK_ASSESSMENT

    tags_lines = ["  - type/claim", "  - oskg-zerotrust",
                  "  - evidence/primary-standard",
                  "  - %s" % chapter["source_tag"]]
    for topic in chapter["topics"]:
        tags_lines.append("  - topic/%s" % topic)

    front_matter = "\n".join([
        "---", "tags:", "\n".join(tags_lines),
        'claim_id: "%s"' % claim_id,
        "statement: %s" % yaml_quote(statement),
        'confidence: "%s"' % rating,
        "confidence_rationale: %s" % yaml_quote(rationale),
        'claim_type: "%s"' % chapter["claim_type"],
        "source_note: %s" % yaml_quote("[[%s]]" % chapter["note"]),
        "created: %s" % TODAY, "updated: %s" % TODAY, "status: active",
        "---"])

    body = "\n".join([
        "", "# %s: %s" % (claim_id, statement), "",
        "**Source:** [[%s]] — %s" % (chapter["note"], chapter["source_line"]),
        "", "## The Claim", "", claim_text, "",
        "## Evidence", "", evidence_text, "",
        "## Confidence", "",
        "**Rating:** %s" % rating.upper(),
        "**Rationale:** %s" % rationale_full, "",
        "## Stakes", "", stakes_text, "",
        "## Disagreement", "",
        "**Who disagrees:**", "", disagree_who, "",
        "**Alternative reading:**", "", disagree_alt, "",
        "## Edges", "",
        "**Depends on:**", "", "**Supports:**", "",
        "**Contradicts:**", "", "**Challenged by:**", "",
        "**Operationalizes:**", "", "**Extends:**", "",
        "## Assessment", "", assessment_text, ""])

    return slug, claim_id, front_matter + body


def main():
    os.makedirs(CLAIMS_DIR, exist_ok=True)
    total = 0
    all_slugs = {}

    for chapter in CHAPTERS:
        path = os.path.join(CONCEPTS_DIR, chapter["file"])
        with open(path, encoding="utf-8") as f:
            text = f.read()
        blocks = split_claim_blocks(text)
        written = 0
        for num in range(1, chapter["n"] + 1):
            if num not in blocks:
                print("MISSING claim %d in %s" % (num, chapter["file"]))
                continue
            slug, cid, content = build_claim_file(chapter, num, blocks[num])
            # Detect duplicate slugs
            if slug in all_slugs:
                slug = "%s-%d" % (slug, num)
            all_slugs[slug] = cid
            out_path = os.path.join(CLAIMS_DIR, "%s.md" % slug)
            with open(out_path, "w", encoding="utf-8") as out:
                out.write(content)
            written += 1
        print("%s: %d/%d claims written" % (chapter["key"], written, chapter["n"]))
        total += written

    print("\n=== EXTRACTION COMPLETE ===")
    print("Total: %d Tier 3/4 claims written to notes/claims/" % total)


if __name__ == "__main__":
    main()
