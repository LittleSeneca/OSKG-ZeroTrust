#!/usr/bin/env python3
"""
Phase 2 Batch 5a: Extract 17 DoD ZT RA claims (missed Tier 1 notes).
Adapted from extract_batch3.py pattern.
"""
import os, re

BASE = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust")
CONCEPTS_DIR = os.path.join(BASE, "notes/concepts")
CLAIMS_DIR = os.path.join(BASE, "notes/claims")
TODAY = "2026-07-24"

CHAPTERS = [
    {"key": "dod-ra-ov", "file": "DoD ZT Reference Architecture — Overview and Strategy.md",
     "note": "DoD ZT Reference Architecture — Overview and Strategy", "n": 6,
     "source_tag": "source/dod-zt-ra",
     "source_line": "DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022",
     "marker_label": "DoD"},
    {"key": "dod-ra-cap", "file": "DoD ZT Reference Architecture — Capabilities and Use Cases.md",
     "note": "DoD ZT Reference Architecture — Capabilities and Use Cases", "n": 11,
     "source_tag": "source/dod-zt-ra",
     "source_line": "DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022",
     "marker_label": "DoD"},
]

META = {
    ("dod-ra-ov", 1): {"slug": "dod-zt-operational-not-architectural",
                        "topics": ["zt-definition", "zt-governance"], "type": "definitional"},
    ("dod-ra-ov", 2): {"slug": "dod-threat-model-different-from-civilian",
                        "topics": ["zt-threats", "zt-definition"], "type": "definitional"},
    ("dod-ra-ov", 3): {"slug": "zt-evolution-existing-capabilities-incremental",
                        "topics": ["zt-migration", "zt-implementation"], "type": "migration"},
    ("dod-ra-ov", 4): {"slug": "dod-five-tenets-threat-operational",
                        "topics": ["zt-tenets", "zt-threats"], "type": "definitional"},
    ("dod-ra-ov", 5): {"slug": "dod-seven-pillars-identical-cisa",
                        "topics": ["zt-architecture", "zt-governance"], "type": "architectural"},
    ("dod-ra-ov", 6): {"slug": "dod-seven-ra-principles-bridge",
                        "topics": ["zt-architecture", "zt-implementation"], "type": "architectural"},

    ("dod-ra-cap", 1): {"slug": "dod-seven-aggregated-capabilities-taxonomy",
                         "topics": ["zt-architecture", "zt-implementation"], "type": "architectural"},
    ("dod-ra-cap", 2): {"slug": "continuous-authentication-common-all-pillars",
                         "topics": ["zt-identity", "zt-authentication"], "type": "implementation"},
    ("dod-ra-cap", 3): {"slug": "ffp-five-decision-points-chain",
                         "topics": ["zt-architecture", "zt-policy"], "type": "architectural"},
    ("dod-ra-cap", 4): {"slug": "npe-person-identities-independent-confidence",
                         "topics": ["zt-identity", "zt-architecture"], "type": "architectural"},
    ("dod-ra-cap", 5): {"slug": "data-centric-security-abac-protection",
                         "topics": ["zt-data", "zt-access-mgmt"], "type": "implementation"},
    ("dod-ra-cap", 6): {"slug": "analytics-ai-unified-pipeline-zt",
                         "topics": ["zt-monitoring", "zt-implementation"], "type": "implementation"},
    ("dod-ra-cap", 7): {"slug": "orchestration-policy-four-layer-hierarchy",
                         "topics": ["zt-policy", "zt-implementation"], "type": "architectural"},
    ("dod-ra-cap", 8): {"slug": "network-transformation-vpn-removal-segmentation",
                         "topics": ["zt-network", "zt-segmentation"], "type": "implementation"},
    ("dod-ra-cap", 9): {"slug": "device-hygiene-event-condition-automation",
                         "topics": ["zt-device", "zt-implementation"], "type": "implementation"},
    ("dod-ra-cap", 10): {"slug": "authentication-authorization-dynamic-continuous",
                          "topics": ["zt-authentication", "zt-identity"], "type": "implementation"},
    ("dod-ra-cap", 11): {"slug": "dod-capability-driven-approach-distinction",
                          "topics": ["zt-governance", "zt-definition"], "type": "governance"},
}

HEADING_RE = re.compile(r'^#{2,3}\s*Claim\s+(\d+)\s*(?:\([^)]*\))?\s*:\s*(.+)$')
MARKER_RE = re.compile(r'^\*\*([^*:]+?):\*\*\s*(.*)$')
TRAILING_ANNOTATION_RE = re.compile(r'\s*(?:\(Scenario|\(Step)[^)]*\)\.?\s*$')

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


def normalize_marker(name):
    name = name.strip().lower()
    name = re.sub(r'\s*\([^)]*\)\s*$', '', name)
    name = re.sub(r'\s*[—-]\s*.*$', '', name)
    return name.strip()


def clean_title(title):
    return TRAILING_ANNOTATION_RE.sub('', title).strip()


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
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def extract_sections(block_lines):
    split_idx = None
    for i, line in enumerate(block_lines):
        if line.strip().startswith('#### '):
            split_idx = i
            break
    if split_idx is not None:
        main_lines = block_lines[:split_idx]
        extended_lines = block_lines[split_idx:]
    else:
        main_lines = block_lines
        extended_lines = []

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


RATING_RE = re.compile(r'^(VERY HIGH|HIGH|MEDIUM-HIGH|MEDIUM-LOW|MEDIUM|LOW)', re.IGNORECASE)


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
    meta = META[(chapter["key"], num)]
    sections = extract_sections(block["lines"])
    statement = block["title"]
    claim_id = "%s.%d" % (chapter["key"], num)

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
    for topic in meta["topics"]:
        tags_lines.append("  - topic/%s" % topic)

    front_matter = "\n".join([
        "---", "tags:", "\n".join(tags_lines),
        'claim_id: "%s"' % claim_id,
        "statement: %s" % yaml_quote(statement),
        'confidence: "%s"' % rating,
        "confidence_rationale: %s" % yaml_quote(rationale),
        'claim_type: "%s"' % meta["type"],
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

    return meta["slug"], front_matter + body


def main():
    os.makedirs(CLAIMS_DIR, exist_ok=True)
    total = 0
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
            slug, content = build_claim_file(chapter, num, blocks[num])
            out_path = os.path.join(CLAIMS_DIR, "%s.md" % slug)
            with open(out_path, "w", encoding="utf-8") as out:
                out.write(content)
            written += 1
        print("%s: %d/%d claims written" % (chapter["key"], written, chapter["n"]))
        total += written

    print("\n=== EXTRACTION COMPLETE ===")
    print("Total: %d DoD claims" % total)


if __name__ == "__main__":
    main()
