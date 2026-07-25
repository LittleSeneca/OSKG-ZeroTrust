---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-architecture
  - topic/zt-segmentation
claim_id: "go-ch3-5.2"
statement: "Enclave design is trust classification — what criteria justify grouping and what criteria justify access between groups"
confidence: "high"
confidence_rationale: "HIGH. This is the most comprehensive enclave taxonomy in the ZT literature. Gilman & Barth's agent model is more architecturally elegant but doesn't"
claim_type: "architectural"
source_note: "[[Green-Ortiz — Ch3-5 — Trust and Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch3-5.2: Enclave design is trust classification — what criteria justify grouping and what criteria justify access between groups

**Source:** [[Green-Ortiz — Ch3-5 — Trust and Policy]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

Enclaves (also called zones or segments) are "a categorization of common functionality, common business impact, or common regulatory requirements" used to "provide common security policy to sets of assets where logical or physical grouping can be achieved." From a ZT perspective, "enclave design is foundational to determining trust (what criteria need to be met for an asset to be placed in an enclave) and trustworthiness (what criteria need to be met to allow assets to communicate with other assets)." Ch4 provides a comprehensive taxonomy: User Layer (corporate workstations, guests, BYOD, IoT, collaboration, lab/demo), Proximity Networks, PANs, Cloud, Enterprise (business services, DMZ, common services, PCI-DSS, facility, mainframe, legacy).

## Evidence

Ch4 enumerates enclave categories with detailed trust criteria for each:
- **Corporate workstations:** Two identities combined — machine identity (device profile + attributes) + user identity. Posture checks: anti-malware running, recent definitions, patching status, NAC integration. Combined identity via 802.1X EAP-TEAP or service account + user interrogation.
- **Guests:** Limited posture assessment (agent-based controls infeasible). Network-based controls and visibility critical. Regular audits, penetration testing. Segmented from internal resources.
- **BYOD:** MDM for credential + posture management. Agent-based posture. Opt-in management for limited corporate resource access.
- **IoT:** Headless, limited patching, no agent-based controls. Network segmentation + behavior analytics. Profiling for identity. Regular vulnerability scans (carefully, due to limited error handling).
- **Collaboration:** Access governance: who can connect, what features, what access needed, how content consumed, how provisioned.
- **Lab/Demo:** Centralized policy, firewall between test segments, periodic registration/authentication.
- **Cloud:** Native tools + external tools. Contextually relevant identity data. Privileged access management. Defense-in-depth even with cloud provider tools.
- **Enterprise applications:** Development → Testing → Production → Customer/Partner facing. Each segment has distinct trust criteria.
- **Mainframe:** Segmentation, PAM (keystroke logging), session behavior monitoring (UAM), automated monitoring/response.
- **Legacy systems:** Compensating controls — segmentation, IDS/IPS, firewalls.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is the most comprehensive enclave taxonomy in the ZT literature. Gilman & Barth's agent model is more architecturally elegant but doesn't address the diversity of device types and trust assessment methods needed at enterprise scale. NIST 800-207 abstracts enclave design entirely — it's an implementation detail from the standards perspective.

## Stakes

Enclave design determines the scope of policy: what gets enforced together, what's isolated, what's the blast radius of a compromise. Bad enclave design either over-segments (policy management overhead explodes) or under-segments (enforcement is too coarse to prevent lateral movement).

## Disagreement

**Who disagrees:**

The cloud-native community argues that enclave design is a legacy concept — in a fully identity-based, agent-enforced model, enclaves are unnecessary because every connection is individually authorized. Green-Ortiz's position is pragmatic: enterprises have brownfield networks and cannot deploy agents on every device (IoT, legacy, guests), so network-based enclave enforcement remains necessary.

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

Ch4 is the most practically useful chapter in Green-Ortiz for enterprise architects. The enclave-by-enclave trust criteria serve as a readiness checklist: for each enclave type, here's what trust data you need, what posture checks are feasible, and what enforcement mechanisms apply. It bridges the gap between abstract ZT principles and operational deployment.
