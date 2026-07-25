#!/usr/bin/env python3
"""
Phase 2 Batch 2 extraction: parse ### Claim N headings out of 6 NIST 800-207
chapter notes and generate one claim file per claim under notes/claims/.
"""

import os
import re

BASE = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust")
CONCEPTS_DIR = os.path.join(BASE, "notes/concepts")
CLAIMS_DIR = os.path.join(BASE, "notes/claims")

TODAY = "2026-07-24"

CHAPTERS = [
    {"key": "ch1", "file": "NIST 800-207 — Ch1 — Introduction.md",
     "note": "NIST 800-207 — Ch1 — Introduction", "n": 8},
    {"key": "ch3", "file": "NIST 800-207 — Ch3 — Logical Components.md",
     "note": "NIST 800-207 — Ch3 — Logical Components", "n": 8},
    {"key": "ch4", "file": "NIST 800-207 — Ch4 — Deployment Scenarios.md",
     "note": "NIST 800-207 — Ch4 — Deployment Scenarios", "n": 6},
    {"key": "ch5", "file": "NIST 800-207 — Ch5 — Threats.md",
     "note": "NIST 800-207 — Ch5 — Threats", "n": 8},
    {"key": "ch6", "file": "NIST 800-207 — Ch6 — Federal Guidance.md",
     "note": "NIST 800-207 — Ch6 — Federal Guidance", "n": 10},
    {"key": "ch7", "file": "NIST 800-207 — Ch7 — Migration.md",
     "note": "NIST 800-207 — Ch7 — Migration", "n": 13},
]

# Per-claim curated metadata: slug, topic tags (1-3), claim_type
META = {
    ("ch1", 1): {"slug": "perimeter-security-obsolete",
                 "topics": ["zt-network", "zt-definition"], "type": "definitional"},
    ("ch1", 2): {"slug": "zt-no-implicit-trust-continuous-eval",
                 "topics": ["zt-definition", "zt-trust"], "type": "definitional"},
    ("ch1", 3): {"slug": "zta-prevent-breach-limit-lateral-movement",
                 "topics": ["zt-definition", "zt-architecture"], "type": "definitional"},
    ("ch1", 4): {"slug": "zt-not-a-product-hybrid-journey",
                 "topics": ["zt-definition", "zt-migration"], "type": "definitional"},
    ("ch1", 5): {"slug": "zt-predates-term-disa-jericho",
                 "topics": ["zt-definition"], "type": "definitional"},
    ("ch1", 6): {"slug": "kindervag-coined-zero-trust",
                 "topics": ["zt-definition"], "type": "definitional"},
    ("ch1", 7): {"slug": "federal-programs-building-toward-zt",
                 "topics": ["zt-governance", "zt-migration"], "type": "governance"},
    ("ch1", 8): {"slug": "nist-document-structure-framework",
                 "topics": ["zt-definition"], "type": "definitional"},

    ("ch3", 1): {"slug": "zta-three-core-components-pe-pa-pep",
                 "topics": ["zt-architecture"], "type": "architectural"},
    ("ch3", 2): {"slug": "eight-data-sources-feed-policy-engine",
                 "topics": ["zt-architecture", "zt-policy"], "type": "architectural"},
    ("ch3", 3): {"slug": "three-zta-approaches-identity-microseg-sdp",
                 "topics": ["zt-architecture", "zt-identity", "zt-microsegmentation"], "type": "architectural"},
    ("ch3", 4): {"slug": "four-deployment-models-zta",
                 "topics": ["zt-architecture", "zt-implementation"], "type": "architectural"},
    ("ch3", 5): {"slug": "trust-algorithm-five-input-categories",
                 "topics": ["zt-trust", "zt-policy"], "type": "architectural"},
    ("ch3", 6): {"slug": "trust-algorithm-two-axes-criteria-contextual",
                 "topics": ["zt-trust", "zt-policy"], "type": "architectural"},
    ("ch3", 7): {"slug": "nist-control-data-plane-separation",
                 "topics": ["zt-network", "zt-architecture"], "type": "architectural"},
    ("ch3", 8): {"slug": "ten-network-requirements-zta",
                 "topics": ["zt-network", "zt-implementation"], "type": "architectural"},

    ("ch4", 1): {"slug": "five-deployment-scenarios-combine",
                 "topics": ["zt-architecture", "zt-implementation"], "type": "architectural"},
    ("ch4", 2): {"slug": "satellite-facilities-cloud-hosted-pe-pa",
                 "topics": ["zt-network", "zt-implementation", "zt-cloud"], "type": "implementation"},
    ("ch4", 3): {"slug": "multi-cloud-sdp-server-to-server",
                 "topics": ["zt-cloud", "zt-implementation"], "type": "implementation"},
    ("ch4", 4): {"slug": "contracted-services-sdp-dark-network",
                 "topics": ["zt-implementation", "zt-network"], "type": "implementation"},
    ("ch4", 5): {"slug": "cross-enterprise-federated-identity-peps",
                 "topics": ["zt-identity", "zt-implementation"], "type": "implementation"},
    ("ch4", 6): {"slug": "public-facing-services-zta-boundary",
                 "topics": ["zt-implementation", "zt-architecture"], "type": "implementation"},

    ("ch5", 1): {"slug": "pe-pa-compromise-highest-impact-threat",
                 "topics": ["zt-threats", "zt-architecture"], "type": "threat"},
    ("ch5", 2): {"slug": "dos-against-pa-pep-unique-pathology",
                 "topics": ["zt-threats", "zt-network"], "type": "threat"},
    ("ch5", 3): {"slug": "stolen-credentials-zta-constrains-blast-radius",
                 "topics": ["zt-threats", "zt-identity"], "type": "threat"},
    ("ch5", 4): {"slug": "encrypted-traffic-visibility-gap",
                 "topics": ["zt-threats", "zt-monitoring"], "type": "threat"},
    ("ch5", 5): {"slug": "monitoring-data-reconnaissance-target",
                 "topics": ["zt-threats", "zt-monitoring"], "type": "threat"},
    ("ch5", 6): {"slug": "proprietary-lock-in-amplified-zta",
                 "topics": ["zt-threats", "zt-implementation"], "type": "threat"},
    ("ch5", 7): {"slug": "npe-authentication-unresolved-risk",
                 "topics": ["zt-threats", "zt-authentication"], "type": "threat"},
    ("ch5", 8): {"slug": "three-threat-frameworks-progression",
                 "topics": ["zt-threats"], "type": "threat"},

    ("ch6", 1): {"slug": "zta-complementary-not-replacement",
                 "topics": ["zt-governance"], "type": "governance"},
    ("ch6", 2): {"slug": "zta-prerequisites-icam-cdm",
                 "topics": ["zt-governance", "zt-identity"], "type": "governance"},
    ("ch6", 3): {"slug": "rmf-zta-changes-authorization-boundaries",
                 "topics": ["zt-governance"], "type": "governance"},
    ("ch6", 4): {"slug": "privacy-framework-inspect-everything-tension",
                 "topics": ["zt-governance", "zt-monitoring"], "type": "governance"},
    ("ch6", 5): {"slug": "ficam-identity-substrate-zta",
                 "topics": ["zt-identity", "zt-governance"], "type": "governance"},
    ("ch6", 6): {"slug": "tic-3-converging-with-zta",
                 "topics": ["zt-governance", "zt-network"], "type": "governance"},
    ("ch6", 7): {"slug": "einstein-ncps-evolve-perimeter-model",
                 "topics": ["zt-governance", "zt-monitoring"], "type": "governance"},
    ("ch6", 8): {"slug": "cdm-visibility-prerequisite-zta",
                 "topics": ["zt-governance", "zt-device"], "type": "governance"},
    ("ch6", 9): {"slug": "cloud-smart-drives-zta-prioritization",
                 "topics": ["zt-governance", "zt-cloud"], "type": "governance"},
    ("ch6", 10): {"slug": "federal-program-interactions-synthesis",
                  "topics": ["zt-governance"], "type": "governance"},

    ("ch7", 1): {"slug": "zta-migration-incremental-recurring-cycle",
                 "topics": ["zt-migration"], "type": "migration"},
    ("ch7", 2): {"slug": "greenfield-zta-rarely-viable",
                 "topics": ["zt-migration"], "type": "migration"},
    ("ch7", 3): {"slug": "hybrid-model-indefinite-reality",
                 "topics": ["zt-migration"], "type": "migration"},
    ("ch7", 4): {"slug": "foundational-inventory-before-migration",
                 "topics": ["zt-migration", "zt-implementation"], "type": "migration"},
    ("ch7", 5): {"slug": "identify-all-subjects-step1-migration",
                 "topics": ["zt-migration", "zt-identity"], "type": "migration"},
    ("ch7", 6): {"slug": "identify-catalog-assets-step2-migration",
                 "topics": ["zt-migration", "zt-device"], "type": "migration"},
    ("ch7", 7): {"slug": "business-process-selection-step3-migration",
                 "topics": ["zt-migration"], "type": "migration"},
    ("ch7", 8): {"slug": "policy-formulation-step4-migration",
                 "topics": ["zt-migration", "zt-policy"], "type": "migration"},
    ("ch7", 9): {"slug": "candidate-solution-selection-step5-migration",
                 "topics": ["zt-migration"], "type": "migration"},
    ("ch7", 10): {"slug": "reporting-only-mode-step6-migration",
                  "topics": ["zt-migration", "zt-monitoring"], "type": "migration"},
    ("ch7", 11): {"slug": "zta-expansion-iterative-cycle-step7",
                  "topics": ["zt-migration"], "type": "migration"},
    ("ch7", 12): {"slug": "incomplete-knowledge-chicken-egg-barrier",
                  "topics": ["zt-migration"], "type": "migration"},
    ("ch7", 13): {"slug": "dual-mode-infrastructure-indefinite-hybrid",
                  "topics": ["zt-migration", "zt-implementation"], "type": "migration"},
}

HEADING_RE = re.compile(r'^#{2,3}\s*Claim\s+(\d+)\s*(?:\([^)]*\))?\s*:\s*(.+)$')
MARKER_RE = re.compile(r'^\*\*([^*:]+?):\*\*\s*(.*)$')
TRAILING_ANNOTATION_RE = re.compile(r'\s*\((?:Scenario|Step)[^)]*\)\.?\s*$')

CLAIM_MARKERS = {"author's claim", "nist's claim", "nist's description"}
EVIDENCE_MARKERS = {"evidence presented"}
CONFIDENCE_MARKERS = {"confidence"}
STAKES_MARKERS = {"what's at stake"}
DISAGREE_WHO_MARKERS = {"who disagrees"}
DISAGREE_ALT_MARKERS = {"alternative reading"}
ASSESSMENT_MARKERS = {"my assessment", "assessment"}


def normalize_marker(name):
    name = name.strip().lower()
    name = re.sub(r'\s*\([^)]*\)\s*$', '', name)   # trailing "(...)"
    name = re.sub(r'\s*[—-]\s*.*$', '', name)      # trailing "— Synthesis table"
    return name.strip()


def clean_title(title):
    title = TRAILING_ANNOTATION_RE.sub('', title).strip()
    return title


def split_claim_blocks(text):
    """Return {claim_num: {"title": str, "lines": [str, ...]}} for a chapter."""
    lines = text.split('\n')
    headings = []
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line.strip())
        if m:
            headings.append((i, int(m.group(1)), m.group(2)))

    blocks = {}
    for i, (line_i, num, raw_title) in enumerate(headings):
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
    """Split a list of lines into (marker_name, content_lines) segments, plus any
    leading unmarked content (ignored) before the first marker."""
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
    # Split off any #### subsections into an "extended" tail appended to evidence.
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

    buckets = {
        "claim": [], "evidence": [], "confidence": [],
        "stakes": [], "disagree_who": [], "disagree_alt": [], "assessment": [],
    }
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
            # Unmapped marker (e.g. "Key insight", "Status", "How ZTA applies") —
            # preserve it as supplementary evidence rather than dropping it.
            # Label and content always go on separate lines so block content
            # (tables, bullet lists) that started on its own line in the
            # source doesn't get glued onto the label line.
            content = join_content(content_lines)
            if content:
                evidence_extra.append("**%s:**\n\n%s" % (raw_marker.strip(), content))
            else:
                evidence_extra.append("**%s:**" % raw_marker.strip())

    extended_text = join_content(extended_lines)
    if extended_text:
        evidence_extra.append(extended_text)

    evidence_parts = buckets["evidence"] + evidence_extra
    return {
        "claim": "\n\n".join(buckets["claim"]).strip(),
        "evidence": "\n\n".join(evidence_parts).strip(),
        "confidence": "\n\n".join(buckets["confidence"]).strip(),
        "stakes": "\n\n".join(buckets["stakes"]).strip(),
        "disagree_who": "\n\n".join(buckets["disagree_who"]).strip(),
        "disagree_alt": "\n\n".join(buckets["disagree_alt"]).strip(),
        "assessment": "\n\n".join(buckets["assessment"]).strip(),
    }


RATING_RE = re.compile(r'^(VERY HIGH|HIGH|MEDIUM-HIGH|MEDIUM-LOW|MEDIUM|LOW)', re.IGNORECASE)


def parse_confidence(confidence_text):
    m = RATING_RE.match(confidence_text.strip())
    if not m:
        return "medium", confidence_text.strip()
    raw = m.group(1).upper()
    if raw in ("VERY HIGH", "HIGH"):
        rating = "high"
    elif raw == "LOW":
        rating = "low"
    else:
        rating = "medium"
    return rating, confidence_text.strip()


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
        escaped = s.replace('\\', '\\\\').replace('"', '\\"')
        return '"%s"' % escaped
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
    claim_id = "nist207-%s.%d" % (chapter["key"], num)

    confidence_raw = sections["confidence"] or "MEDIUM. Confidence not explicitly stated in source."
    rating, rationale_full = parse_confidence(confidence_raw)
    rationale = truncate_rationale(rationale_full)

    claim_text = sections["claim"] or statement
    evidence_text = sections["evidence"] or FALLBACK_EVIDENCE
    stakes_text = sections["stakes"] or FALLBACK_STAKES
    disagree_who = sections["disagree_who"] or FALLBACK_DISAGREE
    disagree_alt = sections["disagree_alt"] or FALLBACK_DISAGREE
    assessment_text = sections["assessment"] or FALLBACK_ASSESSMENT

    tags_lines = [
        "  - type/claim",
        "  - oskg-zerotrust",
        "  - evidence/primary-standard",
        "  - source/nist-sp-800-207",
    ]
    for topic in meta["topics"]:
        tags_lines.append("  - topic/%s" % topic)

    front_matter = "\n".join([
        "---",
        "tags:",
        "\n".join(tags_lines),
        'claim_id: "%s"' % claim_id,
        "statement: %s" % yaml_quote(statement),
        'confidence: "%s"' % rating,
        "confidence_rationale: %s" % yaml_quote(rationale),
        'claim_type: "%s"' % meta["type"],
        "source_note: %s" % yaml_quote("[[%s]]" % chapter["note"]),
        "created: %s" % TODAY,
        "updated: %s" % TODAY,
        "status: active",
        "---",
    ])

    body = "\n".join([
        "",
        "# %s: %s" % (claim_id, statement),
        "",
        "**Source:** [[%s]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020" % chapter["note"],
        "",
        "## The Claim",
        "",
        claim_text,
        "",
        "## Evidence",
        "",
        evidence_text,
        "",
        "## Confidence",
        "",
        "**Rating:** %s" % rating.upper(),
        "**Rationale:** %s" % rationale_full,
        "",
        "## Stakes",
        "",
        stakes_text,
        "",
        "## Disagreement",
        "",
        "**Who disagrees:**",
        "",
        disagree_who,
        "",
        "**Alternative reading:**",
        "",
        disagree_alt,
        "",
        "## Edges",
        "",
        "**Depends on:**",
        "",
        "**Supports:**",
        "",
        "**Contradicts:**",
        "",
        "**Challenged by:**",
        "",
        "**Operationalizes:**",
        "",
        "**Extends:**",
        "",
        "## Assessment",
        "",
        assessment_text,
        "",
    ])

    return meta["slug"], front_matter + body


def main():
    os.makedirs(CLAIMS_DIR, exist_ok=True)
    total = 0
    summary = []

    for chapter in CHAPTERS:
        path = os.path.join(CONCEPTS_DIR, chapter["file"])
        with open(path, "r", encoding="utf-8") as f:
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

        print("%s: %d/%d claims written" % (chapter["key"].capitalize(), written, chapter["n"]))
        summary.append((chapter["key"], written))
        total += written

    print("\n=== EXTRACTION COMPLETE ===")
    for key, count in summary:
        print("%s: %d claims" % (key.capitalize(), count))
    print("Total: %d claims written to notes/claims/" % total)
    print("=== END ===")


if __name__ == "__main__":
    main()
