---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
claim_id: "nist207-ch4.3"
statement: "Multi-cloud environments require the SDP server-to-server model — a PEP at each cloud-hosted service, no enterprise network hairpinning, and the enterprise perimeter is irrelevant to the security model."
confidence: "high"
confidence_rationale: "VERY HIGH. This scenario is the theoretical death blow to perimeter-centric architectures."
claim_type: "implementation"
source_note: "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch4.3: Multi-cloud environments require the SDP server-to-server model — a PEP at each cloud-hosted service, no enterprise network hairpinning, and the enterprise perimeter is irrelevant to the security model.

**Source:** [[NIST 800-207 — Ch4 — Deployment Scenarios]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

An enterprise uses two or more cloud providers to host applications and data. Sometimes the application and its data source reside in different clouds. For performance, the application in Cloud A should connect directly to the data source in Cloud B — not tunnel through the enterprise network. This is a **server-to-server** deployment.

## Evidence

**How ZTA applies:**

- **PEP at each application/data access point** — each cloud-hosted service gets its own PEP. The PE and PA can be services in either cloud, or even a third cloud provider. This is the Software-Defined Perimeter (SDP) model applied to cloud workloads.
- **No enterprise network hairpinning** — traffic flows directly between cloud providers. The enterprise perimeter is irrelevant to the security model.
- **CSA SDP specification** — NIST explicitly references the Cloud Security Alliance's SDP spec as the canonical implementation pattern for this scenario. "This use case is the server-server implementation of the CSA's software defined perimeter (SDP) specification [CSA-SDP]."

**Key challenge NIST identifies:**

"Different cloud providers have unique ways of implementing similar functionality. Enterprise architects will need to be aware of how to implement their enterprise ZTA with each cloud provider they utilize." This is a vendor lock-in / multi-cloud complexity warning.

**Cross-references:**

| Source | How It Relates |
|--------|---------------|
| **BeyondCorp → BeyondProd** (Google) | BeyondProd extends the BeyondCorp model to service-to-service communication in cloud-native environments. It's the architectural bridge between ZTNA (user-to-app) and service mesh security (app-to-app). Google's approach: mutual TLS between services, workload identity rather than network identity, and continuous trust evaluation at the service boundary. |
| **DoD ZT Reference Architecture v2** | The DoD RA addresses cloud deployment through the Network/Environment Pillar — microsegmentation, SDP, and cloud access points aligned to DoD Cloud Computing SRG. The DoD's "Target-Level ZT" includes cloud-native workload identity. |
| **Green-Ortiz (Cisco Press)** | Ch 4 covers "cloud enclave design" — applying ZT policy at cloud ingress/egress points. Green-Ortiz's five ZT capabilities (Policy & Governance, Identity, Vulnerability Management, Enforcement, Analytics) apply identically across on-prem and cloud environments, which maps directly to NIST's point that "there should be no difference between enterprise-owned and -operated network infrastructure and infrastructure owned and operated by any other service provider." |

**Operational implication:**

The multi-cloud scenario is the strongest argument against perimeter-based security. When applications and data live in clouds the enterprise doesn't own, the enterprise perimeter is not just irrelevant — it's an architectural obstacle. ZT enforces access at the workload level, not the network level.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This scenario is the theoretical death blow to perimeter-centric architectures.

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
- [[multi|The SDP server-to-server model provides the architectural foundation for the multi-cluster, multi-cloud deployment patte]]
- [[cloud|The SDP server-to-server model validates the service mesh approach by placing a PEP at each cloud-hosted service, consis]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**
  - [[nist-control-data-plane-separation]]

**Extends:**

## Assessment

_Not addressed separately in the source note._
