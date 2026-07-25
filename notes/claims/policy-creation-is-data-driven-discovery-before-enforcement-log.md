---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-policy
  - topic/zt-monitoring
  - topic/zt-architecture
  - topic/zt-network
claim_id: "go-ch3-5.4"
statement: "Policy creation is data-driven — discovery before enforcement, log before block"
confidence: "high"
confidence_rationale: "HIGH. The discover-then-enforce pattern is validated by every major ZT migration case study (Gilman & Barth's log-then-enforce, Google BeyondCorp's"
claim_type: "implementation"
source_note: "[[Green-Ortiz — Ch3-5 — Trust and Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch3-5.4: Policy creation is data-driven — discovery before enforcement, log before block

**Source:** [[Green-Ortiz — Ch3-5 — Trust and Policy]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

Policy should be built from observed traffic patterns, not from documentation or human assumptions. Ch5's recommended logic proceeds from identity attribution (NAC on flow logs) → DNS resolution → IPAM lookup → endpoint database → classification into enclaves. The entire process is designed to produce policy from empirical communication patterns. Ch3 reinforces this: "continual analysis will contribute to an ever-evolving policy being applied." Ch5 warns against enforcement without discovery: even "full participation from all relevant stakeholders" may miss use cases "not well understood or known by their owners."

## Evidence

- Ch3 branch analysis: "combined with a traffic collection or analysis mechanism, such as NetFlow or traffic taps, both mechanisms are used to determine the impact of policy on a set number of devices."
- Ch3 campus analysis: "traffic monitoring and identity enforcement, for example, can be done on singular switches that still have a larger variety of connected endpoints" — breaking the campus into small analysis areas for iterative learning.
- Ch5 explicit procedure: NAC → DNS → IPAM → endpoint database → classification.
- Ch5 testing: model and test policy, monitor for an "extended period to collect more data and ensure users are not negatively impacted in completing their business functions."
- Ch5 monitoring: explicit warning against the common workaround — "the complete removal or bypass of enforcement from the port or session through which the entity connects" — because it "precludes the ability to actively troubleshoot."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The discover-then-enforce pattern is validated by every major ZT migration case study (Gilman & Barth's log-then-enforce, Google BeyondCorp's observe phase). Green-Ortiz operationalizes it with specific data sources and a sequenced procedure.

## Stakes

The discover-then-enforce model is what makes ZT migration safe. Without it, policy is written from assumptions and breaks production workloads. The operational discipline to avoid bypassing enforcement during troubleshooting is a cultural challenge that Green-Ortiz correctly identifies as critical.

## Disagreement

**Who disagrees:**

The disagreement isn't about the principle but about the feasibility. Organizations with thousands of applications and millions of flows may find exhaustive discovery impractical. Green-Ortiz's answer is automation (orchestration solutions) and gradual rollout (one segment at a time), but the scalability of this approach at very large enterprises is not proven in the book.

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

The "log before block" pattern is the single most important operational insight in ZT migration literature, and Green-Ortiz provides the most detailed data pipeline for implementing it. The emphasis on building an endpoint database — a living inventory with identity, location, owner, and communication patterns — is practical and hard-won advice. In real deployments, the absence of such an inventory is the first and hardest obstacle.
