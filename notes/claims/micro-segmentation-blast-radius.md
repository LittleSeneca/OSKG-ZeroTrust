---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-network-pillar
  - topic/zt-network
  - topic/zt-segmentation
  - topic/zt-implementation
  - topic/zt-architecture
claim_id: "nsa-network.4"
statement: "Micro segmentation limits blast radius within segments — it's the granular layer"
confidence: "high"
confidence_rationale: "HIGH. Micro segmentation is the capability most directly associated with Zero Trust networking, and NSA's maturity model captures the progression"
claim_type: "implementation"
source_note: "[[NSA — Network Environment Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-network.4: Micro segmentation limits blast radius within segments — it's the granular layer

**Source:** [[NSA — Network Environment Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the Network and Environment Pillar*, 2024

## The Claim

Micro segmentation "provides security at a granular level by breaking down a portion of the network into smaller components to limit how data flows laterally through strict access policies." It can be thought of as "the network separation within a sub-organization; employees in the same department should not have access to each other's resources unless explicitly required." This "provides for additional security enforcement closer to applications and resources, augmenting policies already established at the network perimeter."

## Evidence

Four-phase maturity progression:

| Phase | Capability |
|-------|-----------|
| **Preparation** | Define different security levels on the network based on identity and application access. |
| **Basic** | Begin transitioning toward service-specific interconnections and isolation of critical data flows. |
| **Intermediate** | Deploy endpoint and application isolation mechanisms to more of the network architecture with ingress/egress controls between micro segments. Controls tested and refined as needed. |
| **Advanced** | Extensive micro segmentation based on application profiles and data flows, with continuous authentication of connectivity for service-specific interconnections. Central management platforms refined to provide automated and optimal visibility and security monitoring, including alerting on anomalous behavior. |

**Key nuance:**

NSA distinguishes between endpoint/application isolation (Intermediate) and continuous authentication of connectivity (Advanced). The difference is temporal: Intermediate micro segmentation sets up static isolation boundaries; Advanced dynamically re-authenticates connectivity, meaning that even within a micro segment, a session that changes risk profile can be terminated. This maps directly to NIST 800-207's "contextual trust algorithm" concept (§3.3).

**Cross-reference to CISA Network Pillar:**

CISA's segmentation function describes: "Fully distributed ingress/egress micro-perimeters; extensive micro-segmentation based on application profiles; dynamic just-in-time and just-enough connectivity for service-specific interconnections" at the Optimal level. This maps directly to NSA's Advanced level. NSA's Intermediate level maps to CISA's Advanced level ("expands deployment of endpoint and application profile isolation mechanisms; ingress/egress micro-perimeters"). The two models are substantially aligned.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Micro segmentation is the capability most directly associated with Zero Trust networking, and NSA's maturity model captures the progression from "we define different security levels" (Preparation) to "continuous authentication of connectivity" (Advanced).

## Stakes

Micro segmentation is operationally expensive without automation. The NSA addresses this by tying micro segmentation maturity to SDN maturity — the Advanced level for micro segmentation presumes SDN-based central management. Organizations that attempt micro segmentation with traditional tools (manual firewall rules per workload) discover that the combinatorial explosion of rules is unmanageable. The document's structure — SDN as Capability #4, directly following micro segmentation — is not coincidental.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[lateral-movement-prevention-raison-detre|Micro segmentation limits the blast radius when lateral movement occurs, directly serving the pillar's raison d'être.]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[macro-segmentation-cross-function|Micro segmentation extends macro segmentation by adding granular, service-specific isolation within business function se]]
  - "[[network-segmentation-micro-perimeters]]"

## Assessment

The most operationally significant line is at the Intermediate level: "controls are tested and refined as needed." This acknowledges that micro segmentation is iterative — you will break things, you will need to tune. No other ZT standard is this honest about the operational reality of micro segmentation deployment.
