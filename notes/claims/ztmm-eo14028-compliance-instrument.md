---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-governance
  - topic/zt-definition
  - topic/zt-implementation
  - topic/zt-architecture
claim_id: "cisa-ztmm-ov.1"
statement: "The ZTMM is a compliance instrument for EO 14028, not merely a best-practice guide"
confidence: "high"
confidence_rationale: "VERY HIGH. The legal mandate is unambiguous: EO 14028 §3(b)(ii) requires agency ZTA plans. The ZTMM is CISA's answer to that requirement. OMB M-22-09"
claim_type: "governance"
source_note: "[[CISA ZTMM — Overview and Framework]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-ov.1: The ZTMM is a compliance instrument for EO 14028, not merely a best-practice guide

**Source:** [[CISA ZTMM — Overview and Framework]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

"CISA's Zero Trust Maturity Model (ZTMM) provides an approach to achieve continued modernization efforts related to zero trust... in accordance with Executive Order (EO) 14028 'Improving the Nation's Cybersecurity' § (3)(b)(ii), which requires that agencies develop a plan to implement a Zero Trust Architecture (ZTA)."

## Evidence

The ZTMM explicitly cites EO 14028 as the legal mandate. It references OMB M-22-09 (January 2022) which sets specific FY 2024 deadlines for agencies to meet cybersecurity objectives aligned with the ZTMM pillars. The document is published by CISA's Cybersecurity Division under TLP:CLEAR — it's a government operational document, not a vendor framework.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. The legal mandate is unambiguous: EO 14028 §3(b)(ii) requires agency ZTA plans. The ZTMM is CISA's answer to that requirement. OMB M-22-09 further hardens this by setting concrete deadlines.

## Stakes

If the ZTMM is merely advisory, federal agencies can ignore it. If it's a compliance instrument, every FCEB agency must assess maturity against these pillars and show progress. The FY 2024 OMB deadline makes the latter interpretation unavoidable — agencies must demonstrate advancement by the end of the fiscal year.

## Disagreement

**Who disagrees:**

No one disputes the mandate. The debate is over whether the maturity model is the BEST path to compliance. NSA's "Embracing a Zero Trust Security Model" (2021) takes a threat-model-driven approach rather than a maturity-model approach, and some agencies may argue their existing architectures already satisfy ZTA requirements under a different assessment framework.

**Alternative reading:**

The ZTMM could be read as "one of many paths" (as CISA states) — a suggested approach rather than a required one. But OMB M-22-09's specific alignment with ZTMM pillars makes this reading practically untenable for FCEB agencies.

## Edges

**Depends on:**
  - "[[ztmm-nist-800-207-definition-foundation]]"

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The ZTMM is as mandatory as any federal guidance gets without being a formal regulation. The combination of EO mandate + OMB deadlines + CISA's operational authority creates a de facto compliance requirement. The document's own hedging ("one of many paths") is standard government language that shouldn't be mistaken for optionality.
