---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-identity
  - topic/zt-governance
  - topic/zt-architecture
  - topic/zt-definition
  - topic/zt-federation
claim_id: "nist207-ch6.5"
statement: 'ICAM (FICAM) is the identity substrate on which ZTA rests — an agency cannot "bolt on" ZTA without first achieving mature identity governance, including identity proofing, authentication, and federation per SP 800-63-3.'
confidence: "high"
confidence_rationale: "VERY HIGH. This dependency is explicit and broadly agreed across all ZT frameworks — CISA, NSA, and DoD all make the same point."
claim_type: "governance"
source_note: "[[NIST 800-207 — Ch6 — Federal Guidance]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch6.5: ICAM (FICAM) is the identity substrate on which ZTA rests — an agency cannot "bolt on" ZTA without first achieving mature identity governance, including identity proofing, authentication, and federation per SP 800-63-3.

**Source:** [[NIST 800-207 — Ch6 — Federal Guidance]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

The Policy Engine cannot authorize access without sufficient subject/resource identity information. OMB M-19-17 mandates every federal agency establish an ICAM office to govern identity issuance and management. (§6.3)

## Evidence

- NIST SP 800-63-3 (Digital Identity Guidelines) provides the technical standards for identity proofing, authentication, and federation that ZTA policy engines consume.
- Key dependency chain: **ICAM maturity → usable subject attributes → functional Policy Engine → ZTA enforcement.**

**Implication for OSKG-ZeroTrust:**

ICAM is the identity substrate on which ZTA rests. This places identity at the center of the ZT architecture — consistent with the "identity-centric security" concept.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This dependency is explicit and broadly agreed across all ZT frameworks — CISA, NSA, and DoD all make the same point.

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
