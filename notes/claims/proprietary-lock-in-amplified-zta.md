---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-threats
  - topic/zt-implementation
claim_id: "nist207-ch5.6"
statement: "Proprietary data formats and vendor-specific solutions create lock-in that is amplified under ZTA — interoperability gaps can lock an enterprise into a subset of providers, and migration costs are extreme if a provider has a security issue because ZTA is heavily dependent on dynamic information access."
confidence: "medium"
confidence_rationale: "MEDIUM. The lock-in risk is real but NIST provides no data on actual migration costs or failure rates. The claim is more warning than evidence."
claim_type: "threat"
source_note: "[[NIST 800-207 — Ch5 — Threats]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch5.6: Proprietary data formats and vendor-specific solutions create lock-in that is amplified under ZTA — interoperability gaps can lock an enterprise into a subset of providers, and migration costs are extreme if a provider has a security issue because ZTA is heavily dependent on dynamic information access.

**Source:** [[NIST 800-207 — Ch5 — Threats]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

ZTA depends on diverse data sources (subject info, asset state, threat intelligence) that often lack common open standards for interaction and exchange. This creates vendor lock-in. (§5.6)

## Evidence

- Interoperability issues can lock an enterprise into a subset of providers
- If a provider has a security issue or disruption, migration costs may be extreme (replacing multiple assets, translating proprietary policy formats)
- Not unique to ZTA, but **amplified** because ZTA is "heavily dependent on the dynamic access of information" — disruption affects core business functions

- Evaluate service providers holistically: vendor security controls, enterprise switching costs, supply chain risk management — not just performance and stability

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. The lock-in risk is real but NIST provides no data on actual migration costs or failure rates. The claim is more warning than evidence.

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
  - [[zta-complementary-not-replacement]]

## Assessment

_Not addressed separately in the source note._
