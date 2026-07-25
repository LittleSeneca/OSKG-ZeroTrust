---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-tenets
  - topic/zt-governance
  - topic/zt-implementation
  - topic/zt-architecture
claim_id: "nist207-ch2.3"
statement: "The seven tenets are aspirational, not mandatory"
confidence: "high"
confidence_rationale: "HIGH. The hedging reflects political reality — federal agencies can't rip out their networks overnight. The DoD ZT Strategy (2022) also uses "target" "
claim_type: "governance"
source_note: "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---

# nist207-ch2.3: The seven tenets are aspirational, not mandatory

**Source:** [[NIST 800-207 — Ch2 — Zero Trust Basics]] — Scott Rose, Oliver Borchert, Stu Mitchell, Sean Connelly, *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

These tenets are the ideal goal, though it must be acknowledged that not all tenets may be fully implemented in their purest form for a given strategy.

## Evidence

The authors explicitly hedge before listing the tenets. This is unusual for a NIST standard — most SP 800-series documents state requirements, not aspirations. The hedging signals that ZTA is a journey (a word used repeatedly in Ch 7) rather than a destination.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The hedging reflects political reality — federal agencies can't rip out their networks overnight. The DoD ZT Strategy (2022) also uses "target" 

## Stakes

If the tenets are requirements, every federal system must comply by EO 14028 deadlines, which is practically impossible. If aspirational, they provide direction without creating an unfunded mandate. The CISA maturity model resolves this tension by defining maturity levels that normalize partial implementation.

## Disagreement

**Who disagrees:**

NSA's guidance treats the tenets as operational requirements for National Security Systems — not aspirational. The difference reflects the threat model: NSS can't afford "aspirational" security.

**Alternative reading:**

The hedging could be read as NIST acknowledging that ZTA is theoretically sound but practically incomplete — the technology and standards don't exist yet to fully implement all tenets (see Appendix B on gaps).

## Edges

**Depends on:**
<!-- Claims this one requires to be true -->

**Supports:**
- [[zt-maturity-incremental]]

**Contradicts:**
<!-- Claims that cannot be true if this one is -->

**Challenged by:**
<!-- Evidence or arguments that weaken this claim -->

**Operationalizes:**
<!-- Standards/implementations that put this claim into practice -->

**Extends:**
<!-- Claims this one builds upon or elaborates -->

## Assessment

The honesty of the hedging is what makes NIST 800-207 credible. Compare to vendor white papers that claim their product "achieves Zero Trust." NIST admits the limitations. That admission is itself evidence of rigor.

## Zero Trust Taxonomy

### Topic tags
`topic/zt-tenets` `topic/zt-governance`

### Evidence tags
`evidence/primary-standard`
