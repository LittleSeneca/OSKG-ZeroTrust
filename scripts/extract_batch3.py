#!/usr/bin/env python3
"""
Phase 2 Batch 3 extraction: parse ## Claim N and ### Claim N headings out of
6 NSA + CISA chapter notes and generate one claim file per claim under
notes/claims/.
"""

import os
import re

BASE = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust")
CONCEPTS_DIR = os.path.join(BASE, "notes/concepts")
CLAIMS_DIR = os.path.join(BASE, "notes/claims")

TODAY = "2026-07-24"

CHAPTERS = [
    {"key": "nsa-user", "file": "NSA — User Pillar.md",
     "note": "NSA — User Pillar", "n": 6,
     "source_tag": "source/nsa-zt-user-pillar",
     "source_line": "National Security Agency, *Advancing Zero Trust Maturity Throughout the User Pillar*, 2023"},
    {"key": "nsa-device", "file": "NSA — Device Pillar.md",
     "note": "NSA — Device Pillar", "n": 8,
     "source_tag": "source/nsa-zt-device-pillar",
     "source_line": "National Security Agency, *Advancing Zero Trust Maturity Throughout the Device Pillar*, 2023"},
    {"key": "nsa-network", "file": "NSA — Network Environment Pillar.md",
     "note": "NSA — Network Environment Pillar", "n": 6,
     "source_tag": "source/nsa-zt-network-pillar",
     "source_line": "National Security Agency, *Advancing Zero Trust Maturity Throughout the Network and Environment Pillar*, 2024"},
    {"key": "cisa-ztmm-ov", "file": "CISA ZTMM — Overview and Framework.md",
     "note": "CISA ZTMM — Overview and Framework", "n": 9,
     "source_tag": "source/cisa-ztmm",
     "source_line": "CISA, *Zero Trust Maturity Model v2.0*, 2023"},
    {"key": "cisa-ztmm-id", "file": "CISA ZTMM — Identity Pillar.md",
     "note": "CISA ZTMM — Identity Pillar", "n": 8,
     "source_tag": "source/cisa-ztmm",
     "source_line": "CISA, *Zero Trust Maturity Model v2.0*, 2023"},
    {"key": "cisa-ztmm-dnad", "file": "CISA ZTMM — Device Network App Data Pillars.md",
     "note": "CISA ZTMM — Device Network App Data Pillars", "n": 25,
     "source_tag": "source/cisa-ztmm",
     "source_line": "CISA, *Zero Trust Maturity Model v2.0*, 2023"},
]

# Per-claim curated metadata: slug, topic tags (1-3), claim_type
META = {
    # === NSA User Pillar (6 claims) ===
    ("nsa-user", 1): {"slug": "icam-non-negotiable-substrate",
                       "topics": ["zt-identity", "zt-definition"], "type": "definitional"},
    ("nsa-user", 2): {"slug": "identity-mgmt-attribute-authority",
                       "topics": ["zt-identity", "zt-implementation"], "type": "implementation"},
    ("nsa-user", 3): {"slug": "credential-mgmt-phishing-resistance",
                       "topics": ["zt-identity", "zt-authentication"], "type": "implementation"},
    ("nsa-user", 4): {"slug": "access-mgmt-abac-least-privilege",
                       "topics": ["zt-identity", "zt-access-mgmt", "zt-implementation"], "type": "implementation"},
    ("nsa-user", 5): {"slug": "identity-federation-hard-problem",
                       "topics": ["zt-identity", "zt-federation"], "type": "implementation"},
    ("nsa-user", 6): {"slug": "nsa-cisa-identity-frameworks-complementary",
                       "topics": ["zt-identity", "zt-governance"], "type": "governance"},

    # === NSA Device Pillar (8 claims) ===
    ("nsa-device", 1): {"slug": "seven-device-capabilities-interdependent",
                         "topics": ["zt-device", "zt-architecture"], "type": "architectural"},
    ("nsa-device", 2): {"slug": "device-inventory-deny-by-default",
                         "topics": ["zt-device", "zt-inventory"], "type": "implementation"},
    ("nsa-device", 3): {"slug": "continuous-risk-based-device-authorization",
                         "topics": ["zt-device", "zt-trust"], "type": "implementation"},
    ("nsa-device", 4): {"slug": "remote-access-hostile-environment-assumption",
                         "topics": ["zt-device", "zt-remote-access"], "type": "implementation"},
    ("nsa-device", 5): {"slug": "firmware-level-patch-management",
                         "topics": ["zt-device", "zt-firmware", "zt-implementation"], "type": "implementation"},
    ("nsa-device", 6): {"slug": "centralized-device-management-enforcement-backbone",
                         "topics": ["zt-device", "zt-implementation"], "type": "implementation"},
    ("nsa-device", 7): {"slug": "edr-xdr-device-network-bridge",
                         "topics": ["zt-device", "zt-network", "zt-monitoring"], "type": "architectural"},
    ("nsa-device", 8): {"slug": "device-cross-pillar-dependencies",
                         "topics": ["zt-device", "zt-architecture"], "type": "architectural"},

    # === NSA Network Environment Pillar (6 claims) ===
    ("nsa-network", 1): {"slug": "lateral-movement-prevention-raison-detre",
                          "topics": ["zt-network", "zt-definition", "zt-threats"], "type": "definitional"},
    ("nsa-network", 2): {"slug": "data-flow-mapping-foundational-capability",
                          "topics": ["zt-network", "zt-implementation"], "type": "implementation"},
    ("nsa-network", 3): {"slug": "macro-segmentation-cross-function",
                          "topics": ["zt-network", "zt-segmentation"], "type": "implementation"},
    ("nsa-network", 4): {"slug": "micro-segmentation-blast-radius",
                          "topics": ["zt-network", "zt-segmentation"], "type": "implementation"},
    ("nsa-network", 5): {"slug": "sdn-enables-scalable-micro-segmentation",
                          "topics": ["zt-network", "zt-sdn", "zt-segmentation"], "type": "architectural"},
    ("nsa-network", 6): {"slug": "sequential-network-maturity-journey",
                          "topics": ["zt-network", "zt-maturity"], "type": "maturity"},

    # === CISA ZTMM Overview (9 claims) ===
    ("cisa-ztmm-ov", 1): {"slug": "ztmm-eo14028-compliance-instrument",
                            "topics": ["zt-governance", "zt-definition"], "type": "governance"},
    ("cisa-ztmm-ov", 2): {"slug": "nation-state-incidents-perimeter-obsolete",
                            "topics": ["zt-definition", "zt-threats"], "type": "definitional"},
    ("cisa-ztmm-ov", 3): {"slug": "ztmm-nist-800-207-definition-foundation",
                            "topics": ["zt-definition", "zt-governance"], "type": "definitional"},
    ("cisa-ztmm-ov", 4): {"slug": "location-centric-to-identity-data-centric-shift",
                            "topics": ["zt-definition", "zt-identity", "zt-architecture"], "type": "definitional"},
    ("cisa-ztmm-ov", 5): {"slug": "legacy-implicit-trust-primary-obstacle",
                            "topics": ["zt-migration", "zt-implementation"], "type": "implementation"},
    ("cisa-ztmm-ov", 6): {"slug": "five-pillar-comprehensive-decomposition",
                            "topics": ["zt-architecture", "zt-governance"], "type": "architectural"},
    ("cisa-ztmm-ov", 7): {"slug": "four-maturity-levels-progressive-capability",
                            "topics": ["zt-maturity", "zt-governance"], "type": "maturity"},
    ("cisa-ztmm-ov", 8): {"slug": "cross-cutting-capabilities-prevent-silos",
                            "topics": ["zt-architecture", "zt-governance"], "type": "architectural"},
    ("cisa-ztmm-ov", 9): {"slug": "ztmm-operationalizes-nist-seven-tenets",
                            "topics": ["zt-governance", "zt-definition"], "type": "governance"},

    # === CISA ZTMM Identity Pillar (8 claims) ===
    ("cisa-ztmm-id", 1): {"slug": "identity-foundational-zta-pillar",
                            "topics": ["zt-identity", "zt-definition"], "type": "definitional"},
    ("cisa-ztmm-id", 2): {"slug": "cisa-four-maturity-stages",
                            "topics": ["zt-identity", "zt-maturity"], "type": "maturity"},
    ("cisa-ztmm-id", 3): {"slug": "authentication-keystone-identity-function",
                            "topics": ["zt-identity", "zt-authentication"], "type": "implementation"},
    ("cisa-ztmm-id", 4): {"slug": "identity-stores-integrated-not-just-federated",
                            "topics": ["zt-identity", "zt-implementation"], "type": "implementation"},
    ("cisa-ztmm-id", 5): {"slug": "risk-assessment-static-to-continuous",
                            "topics": ["zt-identity", "zt-risk"], "type": "implementation"},
    ("cisa-ztmm-id", 6): {"slug": "access-management-permanent-to-jit-jea",
                            "topics": ["zt-identity", "zt-access-mgmt"], "type": "implementation"},
    ("cisa-ztmm-id", 7): {"slug": "identity-cross-cutting-capabilities",
                            "topics": ["zt-identity", "zt-governance"], "type": "architectural"},
    ("cisa-ztmm-id", 8): {"slug": "cisa-nsa-identity-complementary",
                            "topics": ["zt-identity", "zt-governance"], "type": "governance"},

    # === CISA ZTMM Device/Network/App/Data (25 claims) ===
    ("cisa-ztmm-dnad", 1): {"slug": "device-policy-enforcement-compliance-monitoring",
                               "topics": ["zt-device", "zt-implementation"], "type": "implementation"},
    ("cisa-ztmm-dnad", 2): {"slug": "asset-supply-chain-risk-management",
                               "topics": ["zt-device", "zt-supply-chain"], "type": "implementation"},
    ("cisa-ztmm-dnad", 3): {"slug": "device-resource-access-context",
                               "topics": ["zt-device", "zt-access-mgmt"], "type": "implementation"},
    ("cisa-ztmm-dnad", 4): {"slug": "device-threat-protection-centralized",
                               "topics": ["zt-device", "zt-threats"], "type": "implementation"},
    ("cisa-ztmm-dnad", 5): {"slug": "device-cross-cutting-capabilities-summary",
                               "topics": ["zt-device", "zt-governance"], "type": "governance"},
    ("cisa-ztmm-dnad", 6): {"slug": "network-segmentation-micro-perimeters",
                               "topics": ["zt-network", "zt-segmentation"], "type": "implementation"},
    ("cisa-ztmm-dnad", 7): {"slug": "network-traffic-management-dynamic",
                               "topics": ["zt-network", "zt-implementation"], "type": "implementation"},
    ("cisa-ztmm-dnad", 8): {"slug": "traffic-encryption-cryptographic-agility",
                               "topics": ["zt-network", "zt-encryption"], "type": "implementation"},
    ("cisa-ztmm-dnad", 9): {"slug": "network-resilience-holistic",
                               "topics": ["zt-network", "zt-implementation"], "type": "implementation"},
    ("cisa-ztmm-dnad", 10): {"slug": "network-cross-cutting-capabilities-summary",
                                "topics": ["zt-network", "zt-governance"], "type": "governance"},
    ("cisa-ztmm-dnad", 11): {"slug": "application-access-continuous-authorization",
                                "topics": ["zt-app", "zt-access-mgmt"], "type": "implementation"},
    ("cisa-ztmm-dnad", 12): {"slug": "application-threat-protections-integrated",
                                "topics": ["zt-app", "zt-threats"], "type": "implementation"},
    ("cisa-ztmm-dnad", 13): {"slug": "accessible-applications-public-networks",
                                "topics": ["zt-app", "zt-network"], "type": "implementation"},
    ("cisa-ztmm-dnad", 14): {"slug": "secure-app-dev-immutable-workloads",
                                "topics": ["zt-app", "zt-implementation"], "type": "implementation"},
    ("cisa-ztmm-dnad", 15): {"slug": "application-security-testing-sdlc",
                                "topics": ["zt-app", "zt-implementation"], "type": "implementation"},
    ("cisa-ztmm-dnad", 16): {"slug": "application-cross-cutting-capabilities-summary",
                                "topics": ["zt-app", "zt-governance"], "type": "governance"},
    ("cisa-ztmm-dnad", 17): {"slug": "data-inventory-management-continuous",
                                "topics": ["zt-data", "zt-inventory"], "type": "implementation"},
    ("cisa-ztmm-dnad", 18): {"slug": "data-categorization-automated-labeling",
                                "topics": ["zt-data", "zt-implementation"], "type": "implementation"},
    ("cisa-ztmm-dnad", 19): {"slug": "data-availability-dynamic-optimization",
                                "topics": ["zt-data", "zt-implementation"], "type": "implementation"},
    ("cisa-ztmm-dnad", 20): {"slug": "data-access-jit-jea-controls",
                                "topics": ["zt-data", "zt-access-mgmt"], "type": "implementation"},
    ("cisa-ztmm-dnad", 21): {"slug": "data-encryption-comprehensive",
                                "topics": ["zt-data", "zt-encryption"], "type": "implementation"},
    ("cisa-ztmm-dnad", 22): {"slug": "data-cross-cutting-capabilities-summary",
                                "topics": ["zt-data", "zt-governance"], "type": "governance"},
    ("cisa-ztmm-dnad", 23): {"slug": "cross-pillar-maturity-trajectory",
                                "topics": ["zt-maturity", "zt-architecture"], "type": "maturity"},
    ("cisa-ztmm-dnad", 24): {"slug": "cross-cutting-capabilities-convergence",
                                "topics": ["zt-architecture", "zt-governance"], "type": "architectural"},
    ("cisa-ztmm-dnad", 25): {"slug": "pillar-ideals-vs-operational-realities",
                                "topics": ["zt-implementation", "zt-governance"], "type": "implementation"},
}

HEADING_RE = re.compile(r'^#{2,3}\s*Claim\s+(\d+)\s*(?:\([^)]*\))?\s*:\s*(.+)$')
MARKER_RE = re.compile(r'^\*\*([^*:]+?):\*\*\s*(.*)$')
TRAILING_ANNOTATION_RE = re.compile(r'\s*(?:\(Scenario|\(Step)[^)]*\)\.?\s*$')

CLAIM_MARKERS = {"author's claim", "nist's claim", "nist's description",
                 "nsa's claim", "cisa's claim"}
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
    claim_id = "%s.%d" % (chapter["key"], num)

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
        "  - %s" % chapter["source_tag"],
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
        "**Source:** [[%s]] — %s" % (chapter["note"], chapter["source_line"]),
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

        print("%s: %d/%d claims written" % (chapter["key"], written, chapter["n"]))
        summary.append((chapter["key"], written))
        total += written

    print("\n=== EXTRACTION COMPLETE ===")
    for key, count in summary:
        print("%s: %d claims" % (key, count))
    print("Total: %d claims written to notes/claims/" % total)
    print("=== END ===")


if __name__ == "__main__":
    main()
