---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-embracing-zt
  - topic/zt-tenets
  - topic/zt-implementation
  - topic/zt-network
  - topic/zt-governance
claim_id: "nsa-embrace.2"
statement: "The three guiding principles operationalize ZT for defenders"
confidence: "high"
confidence_rationale: "HIGH. These three principles have become the industry-standard shorthand for ZT, appearing in vendor marketing and government RFPs alike."
claim_type: "architectural"
source_note: "[[NSA — Embracing a Zero Trust Security Model]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---

# nsa-embrace.2: The three guiding principles operationalize ZT for defenders

**Source:** [[NSA — Embracing a Zero Trust Security Model]] — National Security Agency, *Embracing a Zero Trust Security Model*, 2021

## The Claim

Three principles: (1) Never trust, always verify — treat every user, device, application, and data flow as untrusted; (2) Assume breach — operate as if an adversary already has presence; (3) Verify explicitly — use multiple attributes to derive confidence levels for access decisions.

## Evidence

These principles echo Kindervag's original formulation but with NSA's operational emphasis. "Assume breach" is the NSA addition — it doesn't appear in NIST's seven tenets. "Verify explicitly" maps to NIST's Tenets 4 and 6 (dynamic policy, strict enforcement).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These three principles have become the industry-standard shorthand for ZT, appearing in vendor marketing and government RFPs alike.

## Stakes

The principles are simple enough to brief to leadership but operational enough to guide architects. This balance is what made the document influential beyond the DoD.

## Disagreement

**Who disagrees:**

Google BeyondCorp would add "remove the privileged network" as a fourth principle. NIST's positive-tenet approach avoids the negative "never trust" framing. Both are stylistic differences, not substantive disagreements.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
<!-- Claims this one requires to be true -->

**Supports:**
- [[zt-positive-tenets]]

**Contradicts:**
<!-- Claims that cannot be true if this one is -->

**Challenged by:**
<!-- Evidence or arguments that weaken this claim -->

**Operationalizes:**
<!-- Standards/implementations that put this claim into practice -->

**Extends:**
- [[zt-five-fundamental-assertions]]

## Assessment

"Never trust, always verify" is the best three-word summary of Zero Trust ever written. "Assume breach" is the operational imperative. "Verify explicitly" is the implementation requirement. Together they form a complete operational philosophy.

## Zero Trust Taxonomy

### Topic tags
`topic/zt-tenets` `topic/zt-implementation`

### Evidence tags
`evidence/primary-standard`
