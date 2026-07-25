---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-device
  - topic/zt-policy
  - topic/zt-identity
  - topic/zt-network
claim_id: "go-ch9-11.2"
statement: "Distributed enforcement — applying policies as close to the endpoint as possible across four layers (intra-VLAN, inter-VLAN, inter-VRF, host-level) — yields substantial firewall rule reduction and enables firewall consolidation."
confidence: "high"
confidence_rationale: "HIGH — The 50% rule reduction is a specific, quantified outcome from a documented case study. The multi-layer model is Cisco's core enforcement"
claim_type: "implementation"
source_note: "[[Green-Ortiz — Ch9-11 — Advanced and Future]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch9-11.2: Distributed enforcement — applying policies as close to the endpoint as possible across four layers (intra-VLAN, inter-VLAN, inter-VRF, host-level) — yields substantial firewall rule reduction and enables firewall consolidation.

**Source:** [[Green-Ortiz — Ch9-11 — Advanced and Future]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

The cardinal rule is: "apply policies as close to the endpoint as possible." The authors prescribe four enforcement layers: intra-VLAN (TrustSec tags on switch ports), inter-VLAN (downloadable ACLs on switches), inter-VRF (firewalls), and host-level (agents modifying local firewall).

## Evidence

SBC Corporate's implementation yielded a 50% reduction in edge firewall rules (from 350,000+) and allowed firewall consolidation, reducing both CapEx and OpEx. The authors warn that enforcement is not a finite accomplishment — policies evolve continuously as new endpoints and use cases emerge. Never fall back to firewall-only segmentation; maintain layered identity-based enforcement.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The 50% rule reduction is a specific, quantified outcome from a documented case study. The multi-layer model is Cisco's core enforcement architecture and is consistent with Green-Ortiz Ch6's layered segmentation framework.

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
