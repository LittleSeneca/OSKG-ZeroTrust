---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-network
  - topic/zt-segmentation
  - topic/zt-architecture
  - topic/zt-definition
claim_id: "dod-ra-cap.8"
statement: "Network Transformation (Use Cases 10–11) — VPN removal is an architectural consequence of ZT's \"no distinction between internal and external users\" principle, with all users passing through the same PEPs and gateways; east-west segmentation requires three levels (network-level micro-segmentation, process-level host-based inspection, API-level per-call auth) to prevent lateral movement."
confidence: "high"
confidence_rationale: "HIGH. The VPN removal argument and three-level segmentation model are well-specified."
claim_type: "implementation"
source_note: "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-cap.8: Network Transformation (Use Cases 10–11) — VPN removal is an architectural consequence of ZT's "no distinction between internal and external users" principle, with all users passing through the same PEPs and gateways; east-west segmentation requires three levels (network-level micro-segmentation, process-level host-based inspection, API-level per-call auth) to prevent lateral movement.

**Source:** [[DoD ZT Reference Architecture — Capabilities and Use Cases]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

There is no distinction between "internal" and "external" users in ZT. One outcome: VPN removal. Implicit trust in communication between systems allows lateral movement; ZT requires only allowing specific communication required for applications to function. (§4.10–4.11)

## Evidence

- Off-site users placed on "internal" network with on-site users after authentication
- External resource access hairpins through enterprise perimeter → bandwidth and latency issues
- VPNs create a path through the network perimeter — once authenticated, the user has broad network access
- Cannot intelligently confirm identities or provide adaptive policy enforcement

**ZT solution:**

- All users and NPEs pass through the **same PEPs and gateways** (no separate VPN path)
- Comply-to-Connect applies universally
- Resources reside in datacenters and cloud services accessible via Internet
- Continuous MFA and least-privilege on every access request
- **No hair-pinning latency** for external users

**Three levels of east-west segmentation:**

| Level | What It Controls | Mechanism |
|---|---|---|
| **Network-level** | Host-to-host communication | Micro-segmentation: allow only required ports/protocols between defined workloads |
| **Process-level** | Process-to-process communication | Host-based agents inspecting traffic at the application layer |
| **API-level** | API-to-API communication | API micro-segmentation — authentication/authorization on each API call |

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The VPN removal argument and three-level segmentation model are well-specified.

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
