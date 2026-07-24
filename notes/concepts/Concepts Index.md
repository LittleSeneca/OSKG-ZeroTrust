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
- [[Garbis and Chapman — Practice IAM Policy]] — Ch4+5+17 combined: three ZT implementation case studies (BeyondCorp, PagerDuty, SDP), IAM as ZT keystone (three-layer authorization model, authentication protocols, identity lifecycle), and the four-component policy model (Subject Criteria → Action → Target + Condition) with evaluation flows and triggers. 13 claims with cross-references to NIST 800-207, Gilman & Barth, CISA ZTMM, and NSA guidance.
- [[Garbis and Chapman — Cloud IaaS SaaS]] — Ch14–15 combined: How ZT applies to IaaS/PaaS (PEP at cloud boundary, source IP allowlisting, service mesh integration) and SaaS (public-by-design limitations, identity-centric policies, SWG/CASB/SASE landscape). Six claims with cross-references to NIST, Gilman & Barth, and DoD ZT RA.
- [[Finney — Ch1-3 — The Zero Trust Story]] — Finney's business fable: Ch1-3 establish the complete business case for ZT through a fictional ransomware attack on MarchFit. Covers the 12 claims: trust as root vulnerability, prevention economics, ZT as strategy (vs. defense-in-depth/compliance/best-of-breed), the four design principles + five-step methodology + Kipling Method, the implementation curve (learning→practice→crown jewels), physical security as ZT analogy, incident vs. problem management, and third-party responsibility gaps. Cross-referenced with NIST 800-207 Ch7 and CISA ZTMM.
- [[Finney — Ch8-11 — Execution and Sustainability]] — Combined note on Ch8–11: cloud execution (CASB/SASE/API visibility, vendor contracts, container security), sustainable culture (security awareness as ZT protect surface, "trust people not packets," the Pygmalion effect), tabletop exercise (NIST 800-84 MSEL, live-fire purple teaming, remaining trust relationships in IoT and security tools), and long-term journey (CMM-based maturity model, deception/MITRE Engage, CISO leadership). 13 claims with cross-references to NIST 800-207 Ch5/Ch7, CISA ZTMM, and Gilman & Barth Ch9-10.
- [[Gilman and Barth — Ch1 — Zero Trust Fundamentals]] — The five fundamental ZT assertions, control plane / data plane architecture, and the agent model. The most important single chapter from an implementation perspective.
- [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Combined note: authorization architecture (policy engine, trust engine, enforcement, data stores), device trust (X.509, TPM, remote attestation, trust signals), and user trust (MFA, security tokens, adaptive auth, group authorization). Three chapters as a single unit on trust computation and the entities trusted.
- [[Gilman and Barth — Ch7-8 — Applications and Traffic]] — Combined note on trusting applications and traffic: the provenance-to-packet trust chain. Ch7 covers the build pipeline (signed source → reproducible builds → immutable artifacts → instance authorization) and runtime security. Ch8 covers traffic encryption/authentication (mTLS vs IPsec), SPA, three-tier filtering (host/bookended/intermediary), and SDN routing authorization. 13 claims with cross-references to NIST 800-207, CISA ZTMM, and NSA pillars.
- [[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]] — The implementation chapter: MUST/SHOULD prioritized requirements, flow enumeration strategy, controller-less architecture (CM as stepping stone), zero trust proxies, log-then-enforce migration, and the two canonical case studies (Google BeyondCorp client-to-server + PagerDuty Cloud Agnostic Network server-to-server). Cross-referenced with NIST 800-207 Ch7.
- [[Gilman and Barth — Ch10 — The Adversarial View]] — The threat model chapter: identity theft, DDoS, endpoint enumeration, untrusted computing platform, social engineering, physical coercion, invalidation, control plane security. Views ZT through the adversary's lens. Cross-referenced with NIST 800-207 Ch5 and NSA Embracing ZT.
- [[Green-Ortiz — Ch3-5 — Trust and Policy]] — Trust assessment and policy engine: spatial trust signal model (branch/campus/core/WAN/data center/cloud), enclave design as trust classification, multi-layered trust assessment (identity + posture + behavior), data-driven policy creation (discover → log → enforce), policy governance through mergers and shadow IT, automation bridging assessment and enforcement. Cross-referenced with NIST 800-207 Ch3, Gilman & Barth Ch2, and Garbis & Chapman Ch4-5.
- [[Green-Ortiz — Intro Ch1-2 — Foundations]] — Combined note on Introduction, Ch1, and Ch2 of the most technically detailed ZT book (Cisco Press, 2024). Covers the historical origins (Morris Worm → Marsh → Jericho Forum → Kindervag → BeyondCorp), the Zero Trust Discovery Workshop methodology, organizational dynamics, and Cisco's comprehensive five-pillar capability model (Policy & Governance, Identity, Vulnerability Management, Enforcement, Analytics) with 45+ discrete sub-capabilities. 8 claims with cross-references to Gilman & Barth Ch1 and NIST 800-207 Ch3. Synthesis table maps all three frameworks.
- [[Yu — Cyber Defense Matrix]] — Sounil Yu's MECE 5×5 framework (NIST CSF functions × asset classes). Maps ZT access proxies to specific PROTECT cells (NETWORK-PROTECT, APPLICATION-PROTECT, DEVICE-PROTECT, DATA-PROTECT), establishing ZT as a PROTECT strategy rather than a complete security program. Dependency curves (TECHNOLOGY → PEOPLE across left/right of boom). 4 claims with cross-references to NIST 800-207, CISA ZTMM, and Forrester ZTX. Key insight: ZT occupies specific cells — not the whole matrix.
- [[Halley — Zero Trust in Resilient Cloud]] — Cisco Press (2025) practitioner guide operationalizing ZT across on-premises, cloud-native, hybrid, and industrial environments. Four core claims: environment-specific ZT patterns (on-prem vs cloud comparison), segmentation as ZT's primary architectural primitive (macro → micro → identity-based), cloud-native architectures as inherently ZT-aligned, and automation as ZT prerequisite at scale. Cross-reference synthesis table with NIST 800-207 and CISA ZTMM. Cisco-product-centric but architecturally transferable.

---

## Research Papers and Government Guidance

- [[Academic — ZT Research Papers]] — Combined note on three peer-reviewed academic papers: Dotse et al. (2025) large-scale empirical analysis of ZTA effectiveness (modeled 40-78% improvement across all metrics, p < 0.001, Cohen's d > 2.0), Liu et al. (2024) bibliometric analysis of 814 ZT publications and IoT threat/ZT-solution mapping, and Cao et al. (2024) systematic review of AI techniques for ZTA automation and orchestration. **Key finding: the quantitative empirical evidence base for ZT is entirely synthetic — modeled, not measured. The academic consensus supports ZT's direction but the confidence level expressed in practitioner literature exceeds the evidence.**

- [[ANSSI-BSI — LLM and Zero Trust]] — Joint BSI (Germany) / ANSSI (France) guidance on applying Zero Trust principles to LLM-based systems (August 2025). Six design principles: Authentication & Authorization, Input/Output Restrictions, Sandboxing, Monitoring/Reporting/Controlling, Threat Intelligence, and Awareness. **First binational government standard bridging ZT and AI. Key conclusion: "blind trust in LLM systems is not advisable, and the fully autonomous operation of such systems without human oversight is not recommended."**
