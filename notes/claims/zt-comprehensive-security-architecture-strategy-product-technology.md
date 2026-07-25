---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cccs
  - topic/zt-architecture
  - topic/zt-implementation
  - topic/zt-definition
  - topic/zt-migration
claim_id: "cccs-arch.1"
statement: "ZT is a comprehensive security architecture strategy, not a product or technology"
confidence: "high"
confidence_rationale: "HIGH. This is the consensus position across all major ZT frameworks. CCCS's contribution is making it explicit and actionable for a government"
claim_type: "architectural"
source_note: "[[CCCS — ZT Approach to Security Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cccs-arch.1: ZT is a comprehensive security architecture strategy, not a product or technology

**Source:** [[CCCS — ZT Approach to Security Architecture]] — Canadian Centre for Cyber Security, *Zero Trust Approach to Security Architecture — ITSM.10.008*, 2023

## The Claim

"A ZTA is an enterprise approach to a system design whose security perspective is based on ZT principles. Its core principle is that inherent trust is never granted by default to any subject." The document repeatedly emphasizes that "ZT is more than just a technical solution, it requires a fundamental shift in how security is managed" and warns: "Some vendors will claim that their products are the answer to adopting a full ZT security model. Be wary of these vendors. The reality is that there's not a single ZT vendor or solution that can offer all the answers."

## Evidence

The document defines ZT through NIST's operative definition verbatim, frames it as an *enterprise cybersecurity plan* (not a product suite), and structures its entire guidance around organizational change (mindset shift, executive commitment, phased implementation) rather than technology procurement. The 13 best practices include only 4 that are directly technology-oriented (MFA, encryption, SDP, segmentation); the other 9 are organizational, procedural, and strategic.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is the consensus position across all major ZT frameworks. CCCS's contribution is making it explicit and actionable for a government audience that will face vendor pressure to "buy ZT in a box."

## Stakes

If ZT were reducible to products, procurement-driven organizations could solve it with purchasing — the most dangerous misunderstanding in this domain.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[zt-implementation-faces-significant-organizational-technical-challenges|Because ZT is a comprehensive strategy rather than a product, implementation inevitably faces organizational challenges]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

CCCS correctly positions this as the first and most important message for its audience. Government procurement cycles are designed around buying products; ZT requires buying *integration, process change, and ongoing operations*. The vendor warning is sharper here than in NIST or CISA documents — likely reflecting the Canadian government's experience with vendor-driven security transformations.
