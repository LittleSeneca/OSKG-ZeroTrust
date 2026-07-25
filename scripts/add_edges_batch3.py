#!/usr/bin/env python3
"""Add intra-batch edges between Batch 3 claims. Uses targeted patch operations."""
import os, re

CLAIMS_DIR = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/notes/claims")

def add_edge(filepath, edge_type, target_slug):
    """Add a wikilink to the specified edge section of a claim file."""
    with open(filepath, "r") as f:
        content = f.read()

    edge_header_map = {
        "depends_on": "**Depends on:**",
        "supports": "**Supports:**",
        "contradicts": "**Contradicts:**",
        "challenged_by": "**Challenged by:**",
        "operationalizes": "**Operationalizes:**",
        "extends": "**Extends:**",
    }

    header = edge_header_map[edge_type]
    wikilink = f'  - "[[{target_slug}]]"'

    # Check if already present
    if wikilink in content:
        return "skip"

    # Find the header and add the wikilink after it.
    # Pattern: header followed by optional whitespace then blank line
    pattern = re.escape(header) + r'[ \t]*\n\s*\n'
    replacement = header + "\n" + wikilink + "\n\n"

    if not re.search(pattern, content):
        return "no_header"

    content = re.sub(pattern, replacement, content, count=1)
    with open(filepath, "w") as f:
        f.write(content)
    return "added"


def slug_path(slug):
    return os.path.join(CLAIMS_DIR, f"{slug}.md")


# === EDGE DEFINITIONS ===
# (source_slug, edge_type, target_slug) — "source EXTENDS/SUPPORTS/DEPENDS_ON target"

EDGES = [
    # NSA User ↔ CISA Identity complementarity
    ("nsa-cisa-identity-frameworks-complementary", "supports", "cisa-nsa-identity-complementary"),

    # CISA Overview → Identity foundational
    ("identity-foundational-zta-pillar", "extends", "ztmm-nist-800-207-definition-foundation"),
    ("ztmm-eo14028-compliance-instrument", "depends_on", "ztmm-nist-800-207-definition-foundation"),

    # NSA User claims operationalize CISA Identity maturity targets
    ("credential-mgmt-phishing-resistance", "operationalizes", "authentication-keystone-identity-function"),
    ("access-mgmt-abac-least-privilege", "operationalizes", "access-management-permanent-to-jit-jea"),
    ("identity-mgmt-attribute-authority", "operationalizes", "identity-stores-integrated-not-just-federated"),

    # NSA Device ↔ CISA Device claims
    ("device-policy-enforcement-compliance-monitoring", "extends", "continuous-risk-based-device-authorization"),
    ("device-inventory-deny-by-default", "extends", "asset-supply-chain-risk-management"),
    ("centralized-device-management-enforcement-backbone", "supports", "device-policy-enforcement-compliance-monitoring"),
    ("device-cross-pillar-dependencies", "extends", "cross-pillar-maturity-trajectory"),

    # NSA Network ↔ CISA Network claims
    ("macro-segmentation-cross-function", "extends", "network-segmentation-micro-perimeters"),
    ("micro-segmentation-blast-radius", "extends", "network-segmentation-micro-perimeters"),
    ("sdn-enables-scalable-micro-segmentation", "supports", "network-segmentation-micro-perimeters"),
    ("data-flow-mapping-foundational-capability", "depends_on", "network-segmentation-micro-perimeters"),

    # CISA Overview structural claims → pillar maturity
    ("four-maturity-levels-progressive-capability", "supports", "cross-pillar-maturity-trajectory"),
    ("five-pillar-comprehensive-decomposition", "depends_on", "ztmm-nist-800-207-definition-foundation"),
    ("cross-cutting-capabilities-prevent-silos", "supports", "cross-cutting-capabilities-convergence"),
    ("ztmm-operationalizes-nist-seven-tenets", "supports", "ztmm-nist-800-207-definition-foundation"),

    # CISA Identity cross-cutting → cross-pillar capability claims
    ("identity-cross-cutting-capabilities", "extends", "cross-cutting-capabilities-convergence"),
    ("cisa-four-maturity-stages", "supports", "cross-pillar-maturity-trajectory"),

    # Device pillar cross-cutting → convergence
    ("device-cross-cutting-capabilities-summary", "extends", "cross-cutting-capabilities-convergence"),
    ("network-cross-cutting-capabilities-summary", "extends", "cross-cutting-capabilities-convergence"),
    ("application-cross-cutting-capabilities-summary", "extends", "cross-cutting-capabilities-convergence"),
    ("data-cross-cutting-capabilities-summary", "extends", "cross-cutting-capabilities-convergence"),

    # Lateral movement framing
    ("lateral-movement-prevention-raison-detre", "supports", "nation-state-incidents-perimeter-obsolete"),
    ("sequential-network-maturity-journey", "extends", "cross-pillar-maturity-trajectory"),

    # Device threat protection → EDR bridge
    ("device-threat-protection-centralized", "supports", "edr-xdr-device-network-bridge"),

    # Firmware / supply chain
    ("firmware-level-patch-management", "extends", "asset-supply-chain-risk-management"),

    # Data encryption
    ("data-encryption-comprehensive", "extends", "traffic-encryption-cryptographic-agility"),

    # Tensions claim
    ("pillar-ideals-vs-operational-realities", "extends", "legacy-implicit-trust-primary-obstacle"),

    # Remote access
    ("remote-access-hostile-environment-assumption", "extends", "accessible-applications-public-networks"),

    # Federation hard problem
    ("identity-federation-hard-problem", "extends", "identity-stores-integrated-not-just-federated"),

    # Risk assessment
    ("risk-assessment-static-to-continuous", "extends", "continuous-risk-based-device-authorization"),
]

results = {"added": 0, "skip": 0, "no_header": 0, "error": 0}

for src_slug, edge_type, tgt_slug in EDGES:
    src_path = slug_path(src_slug)
    if not os.path.isfile(src_path):
        print(f"MISSING SOURCE: {src_slug}")
        results["error"] += 1
        continue
    outcome = add_edge(src_path, edge_type, tgt_slug)
    results[outcome] = results.get(outcome, 0) + 1
    if outcome not in ("skip", "added"):
        print(f"ISSUE: {src_slug} -> {edge_type} -> {tgt_slug}: {outcome}")

print(f"\n=== EDGES COMPLETE ===")
print(f"Added: {results.get('added', 0)}")
print(f"Skipped (already present): {results.get('skip', 0)}")
print(f"No header found: {results.get('no_header', 0)}")
print(f"Errors: {results.get('error', 0)}")
