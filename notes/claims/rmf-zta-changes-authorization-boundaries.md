---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-governance
claim_id: "nist207-ch6.3"
statement: "RMF — ZTA changes authorization boundaries but not the RMF process itself; risk acceptance decisions become per-resource and per-session, encoded algorithmically in the Policy Engine rather than assessed per-network-zone."
confidence: "high"
confidence_rationale: "HIGH. This is a direct mapping exercise — NIST is describing how RMF applies to its own ZTA model."
claim_type: "governance"
source_note: "[[NIST 800-207 — Ch6 — Federal Guidance]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch6.3: RMF — ZTA changes authorization boundaries but not the RMF process itself; risk acceptance decisions become per-resource and per-session, encoded algorithmically in the Policy Engine rather than assessed per-network-zone.

**Source:** [[NIST 800-207 — Ch6 — Federal Guidance]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

ZTA introduces new architectural components (Policy Engine, Policy Administrator, PEPs) that expand the system boundary, but RMF's core workflow (categorize → select → implement → assess → authorize → monitor) remains unchanged. (§6.1)

## Evidence

- New PEP deployments require updated Security Assessment Reports (SARs) and Plans of Action and Milestones (POA&Ms).
- ZTA planning must integrate with the agency's existing RMF authorization lifecycle.
- The key difference: risk acceptance decisions are now *per-resource* and *per-session*, not per-network-zone.

**Implication for OSKG-ZeroTrust:**

ZTA doesn't eliminate risk management — it *automates* risk decisions at finer granularity. This is an architectural claim about the relationship between policy automation and formal risk acceptance.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is a direct mapping exercise — NIST is describing how RMF applies to its own ZTA model.

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
