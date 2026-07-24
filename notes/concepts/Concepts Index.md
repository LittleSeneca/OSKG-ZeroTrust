---
tags:
  - type/index
  - oskg-zerotrust
  - notes
  - concepts
created: 2026-07-24
related:
  - "[[../Notes Index]]"
---

# Concepts Index

Core Zero Trust concepts, definitions, and principles. These notes define the vocabulary of the knowledge graph.

## Core Concepts (to be developed)

- Zero Trust definition and tenets (NIST SP 800-207)
- Never trust, always verify
- Assume breach
- Least privilege access
- Microsegmentation
- Identity-centric security
- Policy engine / policy administrator / policy enforcement point
- Control plane / data plane separation
- Software-Defined Perimeter (SDP)
- Zero Trust Network Access (ZTNA)
- Zero Trust eXtended (ZTX) framework
- Continuous verification
- Dynamic policy
- Trust zones
- Implicit trust zone elimination
- Lateral movement prevention

## Concept Categories

| Category | Key Concepts |
|----------|-------------|
| **Identity** | Authentication, authorization, MFA, continuous validation, identity fabric |
| **Device** | Device trust, posture assessment, endpoint compliance, BYOD |
| **Network** | Microsegmentation, SDP, ZTNA, VPN replacement, SD-WAN integration |
| **Application** | Application-level access, API security, workload identity |
| **Data** | Data classification, encryption, DLP, data-centric security |

## Reading Notes

Chapter-by-chapter conceptual analysis of each book in the Book Guide. These notes capture definitions, principles, and conceptual frameworks from each source before they are decomposed into claims.

- [[NIST 800-207 — Ch2 — Zero Trust Basics]] — The operative definition, seven tenets, network assumptions, PDP/PEP model. The most-cited chapter in Zero Trust literature.
- [[NIST 800-207 — Ch3 — Logical Components]] — The canonical ZTA component model: PE, PA, PEP; three approach variations; four deployment models; trust algorithm; control plane / data plane separation. **Load-bearing chapter for the entire ZT standards ecosystem.**
- [[NIST 800-207 — Ch4 — Deployment Scenarios]] — Five deployment scenarios: satellite facilities, multi-cloud/cloud-to-cloud, contracted services/nonemployee access, cross-enterprise collaboration, public-facing services. Cross-referenced with DoD ZT RA, BeyondCorp, and Green-Ortiz implementation patterns.
- [[NIST 800-207 — Ch7 — Migration]] — Migration to ZTA: pure vs. hybrid brownfield, the 7-step deployment cycle (actors → assets → processes → policies → solutions → deploy/monitor → expand).
- [[CISA ZTMM — Identity Pillar]] — Maturity progression for authentication, identity stores, risk assessments, and access management; Traditional → Initial → Advanced → Optimal with NSA User Pillar cross-references.
- [[CISA ZTMM — Device Network App Data Pillars]] — Combined note covering the four remaining CISA ZTMM v2 pillars: Device, Network/Environment, Application Workload, and Data. Each pillar documented with all functions at all maturity stages plus cross-cutting capabilities. Cross-referenced to NIST 800-207 logical components, NSA Device Pillar, and NSA Network Pillar.
- [[DoD ZT Reference Architecture — Capabilities and Use Cases]] — The 7-aggregate capability taxonomy (CV-2), the 5-decision-point Fit-for-Purpose mapping (CV-7), and all 17 ZT use cases organized into six thematic clusters: data-centric security, analytics/AI, orchestration, network transformation, device hygiene, and authentication/authorization. Cross-referenced with NIST 800-207, CISA ZTMM, and NSA guidance.
- [[Garbis and Chapman — Network and Access Technologies]] — Combined note on Ch6–10+12: how existing network security technologies (firewalls, DNS, WANs, NAC, IDPS, VPNs, NGFW, PAM) fit — or don't — in a Zero Trust framework. Each technology evaluated against ZT principles with a verdict spectrum from Replace (VPNs) to Persist (WAFs). Cross-referenced with NIST 800-207, CISA ZTMM, and NSA guidance.
- [[Garbis and Chapman — Cloud IaaS SaaS]] — Ch14–15 combined: How ZT applies to IaaS/PaaS (PEP at cloud boundary, source IP allowlisting, service mesh integration) and SaaS (public-by-design limitations, identity-centric policies, SWG/CASB/SASE landscape). Six claims with cross-references to NIST, Gilman & Barth, and DoD ZT RA.
- [[Gilman and Barth — Ch1 — Zero Trust Fundamentals]] — The five fundamental ZT assertions, control plane / data plane architecture, and the agent model. The most important single chapter from an implementation perspective.
- [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Combined note: authorization architecture (policy engine, trust engine, enforcement, data stores), device trust (X.509, TPM, remote attestation, trust signals), and user trust (MFA, security tokens, adaptive auth, group authorization). Three chapters as a single unit on trust computation and the entities trusted.
- [[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]] — The implementation chapter: MUST/SHOULD prioritized requirements, flow enumeration strategy, controller-less architecture (CM as stepping stone), zero trust proxies, log-then-enforce migration, and the two canonical case studies (Google BeyondCorp client-to-server + PagerDuty Cloud Agnostic Network server-to-server). Cross-referenced with NIST 800-207 Ch7.
- [[Gilman and Barth — Ch10 — The Adversarial View]] — The threat model chapter: identity theft, DDoS, endpoint enumeration, untrusted computing platform, social engineering, physical coercion, invalidation, control plane security. Views ZT through the adversary's lens. Cross-referenced with NIST 800-207 Ch5 and NSA Embracing ZT.

---

*Concepts will be populated as source texts are read. Each concept note links to the claims that depend on it.*
