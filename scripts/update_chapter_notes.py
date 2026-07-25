#!/usr/bin/env python3
"""Update the 6 NIST 800-207 chapter notes after claim extraction (Phase 2 Batch 2).

For each chapter note:
  1. Insert claims_status/claims_extracted_date/claims_count/claims_files into frontmatter.
  2. Replace each `### Claim N: Title` block with a compact one-line summary linking
     to the extracted claim note, while preserving all interstitial structure
     (section headings, `---` separators, tables, assessment sections, etc.).
"""

import re
from pathlib import Path

NOTES_DIR = Path.home() / "Projects/Personal/OSKG-ZeroTrust/notes/concepts"

CLAIMS_EXTRACTED_DATE = "2026-07-24"

CHAPTERS = {
    "Ch1": {
        "filename": "NIST 800-207 — Ch1 — Introduction.md",
        "slugs": [
            "perimeter-security-obsolete",
            "zt-no-implicit-trust-continuous-eval",
            "zta-prevent-breach-limit-lateral-movement",
            "zt-not-a-product-hybrid-journey",
            "zt-predates-term-disa-jericho",
            "kindervag-coined-zero-trust",
            "federal-programs-building-toward-zt",
            "nist-document-structure-framework",
        ],
    },
    "Ch3": {
        "filename": "NIST 800-207 — Ch3 — Logical Components.md",
        "slugs": [
            "zta-three-core-components-pe-pa-pep",
            "eight-data-sources-feed-policy-engine",
            "three-zta-approaches-identity-microseg-sdp",
            "four-deployment-models-zta",
            "trust-algorithm-five-input-categories",
            "trust-algorithm-two-axes-criteria-contextual",
            "nist-control-data-plane-separation",
            "ten-network-requirements-zta",
        ],
    },
    "Ch4": {
        "filename": "NIST 800-207 — Ch4 — Deployment Scenarios.md",
        "slugs": [
            "five-deployment-scenarios-combine",
            "satellite-facilities-cloud-hosted-pe-pa",
            "multi-cloud-sdp-server-to-server",
            "contracted-services-sdp-dark-network",
            "cross-enterprise-federated-identity-peps",
            "public-facing-services-zta-boundary",
        ],
    },
    "Ch5": {
        "filename": "NIST 800-207 — Ch5 — Threats.md",
        "slugs": [
            "pe-pa-compromise-highest-impact-threat",
            "dos-against-pa-pep-unique-pathology",
            "stolen-credentials-zta-constrains-blast-radius",
            "encrypted-traffic-visibility-gap",
            "monitoring-data-reconnaissance-target",
            "proprietary-lock-in-amplified-zta",
            "npe-authentication-unresolved-risk",
            "three-threat-frameworks-progression",
        ],
    },
    "Ch6": {
        "filename": "NIST 800-207 — Ch6 — Federal Guidance.md",
        "slugs": [
            "zta-complementary-not-replacement",
            "zta-prerequisites-icam-cdm",
            "rmf-zta-changes-authorization-boundaries",
            "privacy-framework-inspect-everything-tension",
            "ficam-identity-substrate-zta",
            "tic-3-converging-with-zta",
            "einstein-ncps-evolve-perimeter-model",
            "cdm-visibility-prerequisite-zta",
            "cloud-smart-drives-zta-prioritization",
            "federal-program-interactions-synthesis",
        ],
    },
    "Ch7": {
        "filename": "NIST 800-207 — Ch7 — Migration.md",
        "slugs": [
            "zta-migration-incremental-recurring-cycle",
            "greenfield-zta-rarely-viable",
            "hybrid-model-indefinite-reality",
            "foundational-inventory-before-migration",
            "identify-all-subjects-step1-migration",
            "identify-catalog-assets-step2-migration",
            "business-process-selection-step3-migration",
            "policy-formulation-step4-migration",
            "candidate-solution-selection-step5-migration",
            "reporting-only-mode-step6-migration",
            "zta-expansion-iterative-cycle-step7",
            "incomplete-knowledge-chicken-egg-barrier",
            "dual-mode-infrastructure-indefinite-hybrid",
        ],
    },
}

CLAIM_HEADING_RE = re.compile(r"^### Claim (\d+)\s*(?:\([^)]*\))?\s*:\s*(.*)$")


def update_frontmatter(lines, claims_count, slugs):
    """Insert claims_status fields before the closing '---' of the YAML frontmatter."""
    if lines[0].strip() != "---":
        raise ValueError("File does not start with YAML frontmatter delimiter '---'")

    close_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            close_idx = i
            break
    if close_idx is None:
        raise ValueError("Could not find closing '---' for frontmatter")

    new_fields = [
        "claims_status: extracted",
        f"claims_extracted_date: {CLAIMS_EXTRACTED_DATE}",
        f"claims_count: {claims_count}",
        "claims_files:",
    ]
    new_fields += [f'  - "[[{slug}]]"' for slug in slugs]

    return lines[:close_idx] + new_fields + lines[close_idx:]


def replace_claim_blocks(lines, slugs):
    """Replace each `### Claim N: Title` block with a compact summary line.

    Block end boundary: next `### ` heading, a `---` line on its own, a `## `
    heading (non-claim), or EOF. The boundary line itself is preserved.
    """
    output = []
    found_claims = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        m = CLAIM_HEADING_RE.match(line)
        if m:
            claim_num = int(m.group(1))
            title = m.group(2).strip()
            if claim_num < 1 or claim_num > len(slugs):
                raise ValueError(f"Claim {claim_num} has no matching slug (only {len(slugs)} slugs defined)")
            slug = slugs[claim_num - 1]

            j = i + 1
            while j < n:
                candidate = lines[j]
                if candidate.strip() == "---":
                    break
                if candidate.startswith("### "):
                    break
                if candidate.startswith("## "):
                    break
                j += 1

            output.append(f"**Claim {claim_num} —** {title} → [[{slug}]]")
            output.append("")  # avoid the summary being read as a Setext heading if a `---` follows
            found_claims.append(claim_num)
            i = j
        else:
            output.append(line)
            i += 1
    return output, found_claims


def process_chapter(chapter_key, data):
    path = NOTES_DIR / data["filename"]
    slugs = data["slugs"]
    text = path.read_text(encoding="utf-8")
    trailing_newline = text.endswith("\n")
    lines = text.split("\n")
    if trailing_newline:
        lines = lines[:-1]  # drop the artifact empty string from trailing split

    new_lines, found_claims = replace_claim_blocks(lines, slugs)
    new_lines = update_frontmatter(new_lines, len(slugs), slugs)

    expected = list(range(1, len(slugs) + 1))
    if sorted(found_claims) != expected:
        raise ValueError(
            f"{chapter_key}: expected claims {expected}, found {sorted(found_claims)}"
        )

    new_text = "\n".join(new_lines) + ("\n" if trailing_newline else "")
    path.write_text(new_text, encoding="utf-8")
    return len(found_claims)


def main():
    print("=== CHAPTER NOTES UPDATED ===")
    for chapter_key in ["Ch1", "Ch3", "Ch4", "Ch5", "Ch6", "Ch7"]:
        data = CHAPTERS[chapter_key]
        count = process_chapter(chapter_key, data)
        print(f"{chapter_key}: claims_status added, {count} claims linked")
    print("=== END ===")


if __name__ == "__main__":
    main()
