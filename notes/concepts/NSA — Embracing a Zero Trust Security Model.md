---
tags:
  - source/standards
  - nsa
  - zt-definition
  - zt-principles
  - zt-threat-model
  - assume-breach
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
confidence: high
source:
  title: "Embracing a Zero Trust Security Model"
  authors: "National Security Agency"
  year: 2021
  publisher: "NSA"
  local_file: "sources/standards/_txt/NSA_Embracing_Zero_Trust.txt"
related:
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[CISA ZTMM — Overview and Framework]]"
  - "[[NSA ZT User Pillar]]"
  - "[[NSA ZT Device Pillar]]"
  - "[[NSA ZT Network Environment Pillar]]"
  - "[[Concepts Index]]"
claims_status: "extracted"
claims_extracted_date: 2026-07-24
claims_count: 5
claims_files:
  - "[[zt-assume-breach]]"
  - "[[zt-three-guiding-principles]]"
  - "[[zt-threat-scenarios-illustrative]]"
  - "[[zt-maturity-incremental]]"
  - "[[zt-organizational-commitment]]"
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-network
---

# NSA — Embracing a Zero Trust Security Model

The NSA's foundational Zero Trust document. Published February 2021, it predates CISA's maturity model v2 (April 2023) and the NSA pillar-specific guidance (2023-2024). It establishes the threat-centric framing that distinguishes NSA's approach from NIST's more architectural framing. 7 pages.

**Claim 1 —** Zero Trust is defined by "assume breach," not architecture → [[zt-assume-breach]]

**Claim 2 —** The three guiding principles operationalize ZT for defenders → [[zt-three-guiding-principles]]

**Claim 3 —** The threat examples demonstrate ZT's value, not ZT's completeness → [[zt-threat-scenarios-illustrative]]

**Claim 4 —** ZT maturity is incremental, not binary → [[zt-maturity-incremental]]

**Claim 5 —** Organizational commitment is the primary implementation challenge → [[zt-organizational-commitment]]

## Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| ZT defined by "assume breach" | HIGH | Overemphasis on threat vs. architecture |
| Three guiding principles | HIGH | Oversimplification of complex implementation |
| Threat scenarios as evidence | MEDIUM-HIGH | Lack of empirical validation |
| Incremental maturity | HIGH | Purist objection to "partial ZT" |
| Organizational commitment as primary challenge | MEDIUM-HIGH | Technology challenges understated |

**Strongest section:** The three guiding principles and the threat scenarios. These are the most cited and most operationally useful parts of the document.

**Weakest section:** "Potential challenges." Three paragraphs is too thin for the hardest part of ZT adoption. Compare to NIST 800-207 Ch 7 (the full 7-step migration process) or Finney's Project Zero Trust (224 pages on organizational change).

**Historical significance:** This document, published in February 2021, sits between EO 14028 (May 2021) and the federal ZT mandate. It gave NSS owners and operators a threat-centric rationale for ZT adoption before the executive order made it mandatory. It also introduced the maturity framework that CISA later refined.