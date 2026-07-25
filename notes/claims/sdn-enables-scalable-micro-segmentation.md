---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-network-pillar
  - topic/zt-network
  - topic/zt-sdn
  - topic/zt-segmentation
claim_id: "nsa-network.5"
statement: "SDN is the enabling technology that makes micro segmentation manageable at scale"
confidence: "high"
confidence_rationale: "HIGH on the capability description. MEDIUM on the implicit assumption that SDN is the best or only path to micro segmentation at scale — host-based"
claim_type: "architectural"
source_note: "[[NSA — Network Environment Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-network.5: SDN is the enabling technology that makes micro segmentation manageable at scale

**Source:** [[NSA — Network Environment Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the Network and Environment Pillar*, 2024

## The Claim

"Though micro segmentation can be achieved with traditional system components and manual configuration, the centralized nature of SDN allows for dynamic implementation and management across the network. SDN enables the control of packet routing by a centralized control server via a distributed forwarding plane, provides additional visibility into the network, and enables unified policy enforcement."

## Evidence

Four-phase maturity progression:

| Phase | Capability |
|-------|-----------|
| **Preparation** | Map network segments within administrative purview. Identify a roadmap for SDN component integrations. |
| **Basic** | Integrate SDN components and develop a central control plane, along with management policy, network configuration rules, and task schedule (such as updates). |
| **Intermediate** | Map SDN APIs, establish roles, and configure the SDNC to make API calls using encryption and authentication. Test interconnectedness and set configurations to employ segmentation rules at the optimal level of granularity. |
| **Advanced** | Create alert systems to notify administrators of anomalous or suspicious behavior. Employ advanced analytics and controls. Test the network to determine which network paths would allow an intruder to move between segments laterally or otherwise. Restrict the paths as appropriate with strict access controls. |

**SDN Controller Risk:**

NSA explicitly warns: "the SDN Controller (SDNC) itself can become a priority target that requires proper configuration and continuous monitoring." Recommended mitigations include:
- Dedicated API administrator roles with restricted privileges (separate from SDN administrators)
- SDNC should only accept API calls from authorized API administrators
- API calls secured using encrypted protocols (TLS v1.2+, SSH v2+) and mutual authentication (client and server certificates)

This is a significant operational warning — the centralized control that makes SDN powerful also makes the SDNC a single point of compromise. If an attacker compromises the SDNC, they can reconfigure the entire segmented network.

**Cross-reference to NIST 800-207 §3.1.3 (SDP):**

NIST describes SDP as an overlay network approach where "the PA acts as a network controller that sets up and reconfigures the network based on PE decisions." This is essentially the same concept that NSA frames as SDN-enabled micro segmentation. NIST also references SDN and IBN (Intent-Based Networking) as enabling technologies. The two documents converge on the same architectural pattern: a central controller making policy decisions that are enforced at distributed points.

**Cross-reference to CISA Network Pillar:**

CISA's "dynamic just-in-time and just-enough connectivity for service-specific interconnections" at the Optimal level is the policy outcome that NSA's SDN capability enables. CISA describes the *what*; NSA describes the *how*.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the capability description. MEDIUM on the implicit assumption that SDN is the best or only path to micro segmentation at scale — host-based micro segmentation (software agents on endpoints) is an alternative that NSA does not discuss.

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
  - "[[network-segmentation-micro-perimeters]]"

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The SDN maturity model's most valuable contribution is at the Advanced level: "Test the network to determine which network paths would allow an intruder to move between segments laterally or otherwise. Restrict the paths as appropriate." This is a call for adversarial testing of segmentation boundaries — essentially, red-teaming the network segmentation. No other ZT standard makes this explicit. It's a characteristically NSA addition: test your defenses against the threat you're designing against.
