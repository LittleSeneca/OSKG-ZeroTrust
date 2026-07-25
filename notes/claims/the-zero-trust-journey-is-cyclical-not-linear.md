---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-governance
  - topic/zt-maturity
  - topic/zt-identity
  - topic/zt-architecture
claim_id: "go-ch9-11.6"
statement: "The Zero Trust journey is cyclical, not linear — five capabilities (Policy & Governance, Identity, Vulnerability Management, Enforcement, Analytics) form a continuous feedback loop with no final destination."
confidence: "high"
confidence_rationale: "HIGH — The cyclical model is a synthesis that aligns with NIST 800-207's emphasis on continuous monitoring and iterative improvement. The SBC case"
claim_type: "governance"
source_note: "[[Green-Ortiz — Ch9-11 — Advanced and Future]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch9-11.6: The Zero Trust journey is cyclical, not linear — five capabilities (Policy & Governance, Identity, Vulnerability Management, Enforcement, Analytics) form a continuous feedback loop with no final destination.

**Source:** [[Green-Ortiz — Ch9-11 — Advanced and Future]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

The book's capstone model presents five ongoing capabilities where analytics feeds identity, which feeds vulnerability management, which refines enforcement, which triggers policy updates, which loops back. "Zero Trust has no final destination — removing trust from a network is an ongoing, never-ending process."

## Evidence

The five capabilities: (1) Policy & Governance — executive buy-in codified into policy, the foundation; (2) Identity — authentication + authorization based on contextual identity, "the long pole in the tent"; (3) Vulnerability Management — behavioral baseline vs. expected behavior; (4) Enforcement — layered, distributed, applied at correct network location; (5) Analytics — feeds all other capabilities, aggregates logs/switch counters/syslog/identity accounting. The SBC case study validates this: firewall rule cleanup went from 350,000 → ~125,000 active → further reduced via identity-based policies; TrustSec tag strategy capped at 10 tags; the question isn't "When will the building be secured?" but "Which phase is the building at, and how far along?"

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The cyclical model is a synthesis that aligns with NIST 800-207's emphasis on continuous monitoring and iterative improvement. The SBC case study provides empirical grounding for the framework's practical application.

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
