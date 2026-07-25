---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-network
  - topic/zt-segmentation
  - topic/zt-architecture
  - topic/zt-device
claim_id: "cisa-ztmm-dnad.6"
statement: "Network Segmentation — maturity progresses from large perimeter/macro-segmentation with minimal intra-segment restrictions to fully distributed ingress/egress micro-perimeters with extensive micro-segmentation based on application profiles and dynamic JIT/JEA connectivity."
confidence: "high"
confidence_rationale: "HIGH. Direct from the source document."
claim_type: "implementation"
source_note: "[[CISA ZTMM — Device Network App Data Pillars]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-dnad.6: Network Segmentation — maturity progresses from large perimeter/macro-segmentation with minimal intra-segment restrictions to fully distributed ingress/egress micro-perimeters with extensive micro-segmentation based on application profiles and dynamic JIT/JEA connectivity.

**Source:** [[CISA ZTMM — Device Network App Data Pillars]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

Network segmentation progresses from coarse perimeter to fine-grained application-profile-based micro-perimeters. (§5.3)

## Evidence

| Stage | Description |
|-------|-------------|
| **Traditional** | Defines network architecture using large perimeter/macro-segmentation with minimal restrictions on reachability within segments. May rely on multi-service interconnections (bulk VPN tunnels). |
| **Initial** | Begins deploying network architecture with isolation of critical workloads, constraining connectivity to least function principles, and transitioning toward service-specific interconnections. |
| **Advanced** | Expands deployment of endpoint and application profile isolation mechanisms; ingress/egress micro-perimeters; service-specific interconnections. |
| **Optimal** | Fully distributed ingress/egress micro-perimeters; extensive micro-segmentation based on application profiles; dynamic just-in-time and just-enough connectivity for service-specific interconnections. |

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Direct from the source document.

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
- [[micro-segmentation-blast-radius|The CISA maturity model independently confirms that micro-segmentation with dynamic JIT connectivity is the optimal end-]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[macro-segmentation-cross-function|The CISA maturity model extends the NSA macro segmentation concept by specifying fully distributed ingress/egress micro-]]

## Assessment

_Not addressed separately in the source note._
