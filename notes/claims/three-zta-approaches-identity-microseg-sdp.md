---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-architecture
  - topic/zt-identity
  - topic/zt-segmentation
claim_id: "nist207-ch3.3"
statement: "Three ZTA approaches exist — identity governance, micro-segmentation, and SDP"
confidence: "medium"
confidence_rationale: "MEDIUM-HIGH — The three-way classification is analytically useful but has proven somewhat fluid in practice. The industry has largely converged on"
claim_type: "architectural"
source_note: "[[NIST 800-207 — Ch3 — Logical Components]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch3.3: Three ZTA approaches exist — identity governance, micro-segmentation, and SDP

**Source:** [[NIST 800-207 — Ch3 — Logical Components]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

Enterprises can enact ZTA through three approaches: (1) enhanced identity governance–driven, where access policies are based on identity and attributes; (2) logical micro-segmentation, where resources are placed on unique network segments protected by gateway security components; and (3) network infrastructure and Software Defined Perimeter (SDP), using overlay networks with the PA acting as a network controller. A full ZT solution includes elements of all three. Each approach implements all ZT tenets from Section 2.1.

## Evidence

Conceptual descriptions with use-case mapping. NIST explicitly states these are not mutually exclusive and that one approach may be more suitable than others depending on existing enterprise policies and workflows.

#### 3.1.1 Enhanced Identity Governance

**NIST's claim:** Identity-driven ZTA uses actor identity as the primary policy input. Resource access policies are based on identity and assigned attributes, with device status and environmental factors serving as secondary modifiers. This approach often uses an open network model and works well with cloud-based SaaS applications and the resource portal deployment model.

**Key advantage:** Works without enterprise-controlled network infrastructure — suitable for cloud/SaaS environments.

**Key risk:** Basic network connectivity is granted to all assets, meaning malicious actors can still perform reconnaissance and launch DoS attacks from within the network.

**Confidence:** HIGH — Identity governance is universally acknowledged as foundational to ZT. The risk about open network reconnaissance is well-observed in practice.

**Cross-reference to DoD ZT RA:** The DoD Reference Architecture operationalizes this through ICAM (Identity, Credential, and Access Management) as a foundational capability, with attribute-based access control (ABAC) as the policy model.

#### 3.1.2 Micro-Segmentation

**NIST's claim:** Micro-segmentation places individual resources or resource groups on unique network segments protected by gateway devices (intelligent switches, NGFWs, or special-purpose gateways) acting as PEPs. Host-based micro-segmentation using software agents is an alternative implementation. The gateway dynamically grants access per request. This approach requires an identity governance program but relies on gateway components as the primary PEP.

**Key requirement:** PEP components must be managed and must react/reconfigure in response to threats or workflow changes. Stateless firewalls are a "very poor choice" due to administration cost and slow adaptation.

**Confidence:** HIGH — Micro-segmentation is a mature network security concept that predates ZT but is correctly positioned as a ZTA-enabling approach.

**Cross-reference to CISA Maturity Model:** CISA's Network pillar directly addresses micro-segmentation maturity, from "large macro-segments" at Traditional level to "fully distributed micro-perimeters" at Optimal level.

#### 3.1.3 SDP (Software Defined Perimeter)

**NIST's claim:** SDP approaches use overlay networks (typically Layer 7, but possibly lower) with the PA acting as a network controller that sets up and reconfigures the network based on PE decisions. Clients request access via PEPs managed by the PA. The most common deployment model is agent/gateway (Section 3.2.1), where the agent and resource gateway establish a secure channel. References SDN and IBN concepts.

**Confidence:** HIGH — SDP has become the dominant ZTA implementation pattern, particularly through ZTNA products. The Cloud Security Alliance (CSA) SDP specification, which NIST cites, has been widely adopted.

**Assessment:** NIST's description of SDP is notably vendor-neutral. It correctly identifies SDP as an implementation approach rather than a distinct security model — the underlying PE/PA/PEP architecture remains the same. The DoD Reference Architecture maps SDP to the "Network Environment" pillar and specifies that ZTNA/SDP should replace traditional VPN for remote access (DoD ZT Capability 2.3).

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM-HIGH — The three-way classification is analytically useful but has proven somewhat fluid in practice. The industry has largely converged on SDP/ZTNA as the primary implementation pattern, with identity governance treated as a prerequisite rather than a distinct approach, and micro-segmentation as a network-layer complement.

## Stakes

Misclassifying approaches could lead enterprises to choose an unsuitable implementation strategy. However, NIST's framing that all three are complementary rather than competing is protective — a full ZTA deployment needs elements of each.

## Disagreement

**Who disagrees:**

Forrester's ZTX framework treats micro-segmentation as a network capability within a broader ecosystem, not a standalone ZTA approach. Gartner's CARTA emphasizes identity at the center. Vendor positioning distorts the taxonomy: SDP vendors claim primacy, identity vendors claim identity is the "new perimeter," and network vendors claim segmentation is foundational. NIST's neutrality on this question is itself significant.

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

The taxonomy is defensible as a conceptual framework but has limited practical utility for implementation planning. The more important observation is NIST's insistence that **all three approaches implement all ZT tenets** — this forecloses the argument that any single approach alone constitutes "full ZT." The CISA Maturity Model operationalizes this by defining maturity across five pillars (Identity, Device, Network, Application/Workload, Data) rather than by approach.
