---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-network
  - topic/zt-architecture
  - topic/zt-implementation
  - topic/zt-definition
claim_id: "nist207-ch3.7"
statement: "Control plane and data plane must be logically separated"
confidence: "high"
confidence_rationale: "HIGH — Control/data plane separation is one of the foundational architectural principles of ZT, adapted from SDN and telecommunications. Gilman &"
claim_type: "architectural"
source_note: "[[NIST 800-207 — Ch3 — Logical Components]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch3.7: Control plane and data plane must be logically separated

**Source:** [[NIST 800-207 — Ch3 — Logical Components]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

In a ZT environment, there must be separation (logical or possibly physical) between communication flows used to control/configure the network (control plane) and application/service communication flows (data plane). The control plane is used by PE, PA, and PEPs to maintain assets, make access decisions, and set up communication paths. The data plane is used for actual application communication — and this channel may not be possible before the control plane has established the path. **NIST explicitly credits Gilman & Barth for this concept** (citation: [Gilman]).

## Evidence

**Cross-reference:**

Gilman & Barth's (2017) "Zero Trust Networks" book provides the most thorough treatment of control plane / data plane architecture, including practical considerations like control plane availability, latency, and the single-point-of-failure risk that the PA/PE becomes. NIST 800-207 acknowledges scalability as a requirement (Requirement 9) but doesn't explore the failure modes Gilman & Barth discuss.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — Control/data plane separation is one of the foundational architectural principles of ZT, adapted from SDN and telecommunications. Gilman & Barth's formulation in "Zero Trust Networks" (2017) predates NIST 800-207 and provides the theoretical grounding.

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

This claim is genuinely load-bearing. Without control plane / data plane separation, ZTA collapses into a traditional perimeter model where the network carries both control and data indiscriminately. The separation enables:
- PEPs that block all data-plane traffic until the control plane authorizes it
- Resources that are invisible/unreachable without control-plane mediation
- Session-specific, dynamically configured communication paths
