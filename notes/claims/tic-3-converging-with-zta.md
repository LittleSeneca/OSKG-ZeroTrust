---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-governance
  - topic/zt-network
claim_id: "nist207-ch6.6"
statement: "TIC 3.0 is converging with ZTA — TIC evolved from perimeter-based (1.0/2.0) to distributed enforcement (3.0) with PEP Security Capabilities applied at multiple enforcement points, making TIC 3.0 the network-security dimension of ZTA in federal environments."
confidence: "high"
confidence_rationale: "HIGH. TIC 3.0's distributed PEP model is documented and aligns structurally with ZTA. The convergence is recognized by both NIST and CISA."
claim_type: "governance"
source_note: "[[NIST 800-207 — Ch6 — Federal Guidance]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch6.6: TIC 3.0 is converging with ZTA — TIC evolved from perimeter-based (1.0/2.0) to distributed enforcement (3.0) with PEP Security Capabilities applied at multiple enforcement points, making TIC 3.0 the network-security dimension of ZTA in federal environments.

**Source:** [[NIST 800-207 — Ch6 — Federal Guidance]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

TIC 3.0 recognizes that trust varies by computing context and introduces PEP Security Capabilities applied at distributed enforcement points rather than a single perimeter chokepoint. (§6.4)

## Evidence

- **TIC 1.0/2.0:** Perimeter-based; assumed internal network is "trusted." Contradicted ZTA's core premise.
- **TIC 3.0:** Introduces Universal Security Capabilities (enterprise-level) and PEP Security Capabilities (applied at multiple distributed PEPs).
- TIC 3.0 security capabilities directly support ZTA: encrypted traffic, strong authentication, microsegmentation, network/system inventory.
- The chapter predicts a future "ZTA TIC use case" will formalize network protections at ZTA enforcement points.

**Implication for OSKG-ZeroTrust:**

TIC 3.0 is the *network-security dimension* of ZTA in federal environments. Agencies don't choose between TIC and ZTA — they deploy TIC capabilities at ZTA PEPs.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. TIC 3.0's distributed PEP model is documented and aligns structurally with ZTA. The convergence is recognized by both NIST and CISA.

## Stakes

_Not addressed separately in the source note._

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
