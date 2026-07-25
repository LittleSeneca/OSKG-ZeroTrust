---
tags:
  - source/standards
  - cisa
  - zt-maturity
  - zt-pillars
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
claims_status: extracted
claims_extracted: 2026-07-24
confidence: very-high
source:
  title: "CISA Zero Trust Maturity Model"
  authors: "CISA"
  year: 2023
  version: "2.0"
  publisher: "Cybersecurity and Infrastructure Security Agency"
  local_file: "sources/standards/_txt/CISA_Zero_Trust_Maturity_Model_v2.txt"
related:
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[Concepts Index]]"
note_type: combined
combined_sections: "§§1-5"
justification: "§§1-5 (Introduction through ZTMM overview) form a single architectural overview: §1 sets the policy mandate, §2 frames the operational urgency, §3 anchors the NIST definition, §4 acknowledges adoption challenges, and §5 lays out the model's structure (pillars, maturity levels, cross-cutting capabilities). Together they constitute the framework layer that the pillar-specific tables (5.1-5.5) operationalize. The framework content across these sections is ~350 lines — too thin for 5 standalone notes but collectively the foundation for understanding the entire maturity model."
  - topic/zt-architecture
  - topic/zt-governance
  - topic/zt-identity
---

# CISA ZTMM — Overview and Framework

The Cybersecurity and Infrastructure Security Agency's Zero Trust Maturity Model (ZTMM) v2.0 (April 2023) is the U.S. federal government's roadmap for transitioning agency cybersecurity from perimeter-based, implicit-trust architectures to Zero Trust Architectures (ZTA). It operationalizes NIST SP 800-207's seven tenets into five measurable pillars with four progressive maturity levels, providing federal agencies (and by extension, all organizations) with a practical, incremental path to zero trust adoption in compliance with Executive Order 14028 and OMB Memorandum M-22-09.

## §1: Introduction — Policy Mandate and Purpose

**Claim 1 —** The ZTMM is a compliance instrument for EO 14028, not merely a best-practice guide → [[ztmm-eo14028-compliance-instrument]]
---

## §2: Current Environment — Operational Urgency

**Claim 2 —** Recent nation-state cyber incidents made legacy perimeter-based security indefensible → [[nation-state-incidents-perimeter-obsolete]]
---

## §3: What Is Zero Trust? — The NIST Anchor

**Claim 3 —** The ZTMM is built on NIST SP 800-207's operative definition — zero trust minimizes uncertainty, not risk → [[ztmm-nist-800-207-definition-foundation]]
---

**Claim 4 —** Zero trust represents a fundamental shift from location-centric to identity/data-centric security → [[location-centric-to-identity-data-centric-shift]]
---

## §4: Challenges — Why This Is Hard

**Claim 5 —** Legacy implicit-trust systems are the primary obstacle to ZTA adoption → [[legacy-implicit-trust-primary-obstacle]]
---

## §5: The ZTMM Framework — Pillars, Levels, and Cross-Cutting Capabilities

**Claim 6 —** The five-pillar structure provides a comprehensive, independently-assessable decomposition of ZTA → [[five-pillar-comprehensive-decomposition]]
---

**Claim 7 —** The four maturity levels define progressive capability from static/manual to dynamic/automated → [[four-maturity-levels-progressive-capability]]
---

**Claim 8 —** The three cross-cutting capabilities unify the pillars and prevent siloed maturity → [[cross-cutting-capabilities-prevent-silos]]
---

**Claim 9 —** The ZTMM operationalizes all seven NIST 800-207 tenets into measurable capabilities → [[ztmm-operationalizes-nist-seven-tenets]]
---

## Framework Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| 1: ZTMM is a compliance instrument for EO 14028 | VERY HIGH | A court ruling that EO 14028's ZTA requirement is not enforceable |
| 2: Recent incidents made perimeter-based security indefensible | VERY HIGH | A major ZTA breach that shows ZTA is equally vulnerable |
| 3: ZTMM inherits NIST 800-207's definition without modification | VERY HIGH | NIST revising the operative definition; current definition is from 2020 |
| 4: ZTA requires a fundamental shift from location-centric to identity/data-centric | HIGH | Evidence that most agencies achieve adequate security without full cultural transformation |
| 5: Legacy implicit-trust systems are the primary obstacle | HIGH | Successful ZTA implementations that bypass rather than migrate legacy systems |
| 6: Five-pillar structure provides comprehensive, independently-assessable decomposition | HIGH | Evidence that pillar-level optimization produces worse outcomes than holistic ZTA |
| 7: Four maturity levels define progressive capability from static/manual to dynamic/automated | HIGH | Optimal proving unattainable → model loses credibility as assessment tool |
| 8: Cross-cutting capabilities unify pillars and prevent siloed maturity | HIGH | Agencies treating cross-cutting capabilities as optional → pillar silos persist |
| 9: ZTMM operationalizes all seven NIST tenets into measurable capabilities | HIGH | Missing explicit tenet-to-function mapping → audit gaps |

**Strongest section:** §5 (The ZTMM Framework) — the four maturity levels are the ZTMM's unique contribution. They're specific, testable, and provide a concrete bridge between NIST's aspirational tenets and agency procurement. No other federal guidance provides this level of operational specificity.

**Weakest section:** §4 (Challenges) — the challenges section is brief and generic. It identifies real problems (legacy systems, siloed teams, varied starting points) but doesn't provide specific mitigation strategies. The framework itself addresses these challenges implicitly (maturity levels accommodate varied starting points; cross-cutting capabilities address silos), but the Challenges section doesn't make these connections explicit.

**Key structural observation:** The ZTMM is an assessment framework, not an architecture specification. It tells you WHAT capabilities to measure, not HOW to build them. This is both its strength (technology-agnostic, durable) and its limitation (agencies still need reference architectures to guide implementation). The implicit assumption is that agencies will use NIST 800-207's component model (PE, PA, PEP) for architecture and the ZTMM for maturity assessment — but the document doesn't make this division of labor explicit, which creates a risk that agencies use the ZTMM as both, leading to pillar-optimized architectures without a coherent component model.

**Unanswered question:** What happens when an agency reaches Optimal across all pillars? The document doesn't define a post-Optimal state or a maintenance mode. The federal ZTA journey is framed as having an endpoint (Optimal), but practical ZTA is continuous — new threats, new technologies, and new attack surfaces mean the "Optimal" target moves. Future versions of the ZTMM should either define Optimal as an evolving target or add a fifth level for continuous adaptation.
