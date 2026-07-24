---
tags:
  - source/standards
  - nist
  - zt-architecture
  - policy-engine
  - pep
  - microsegmentation
  - sdp
  - oskg-zerotrust
  - concepts
  - reading-notes
created: 2026-07-24
confidence: high
source:
  title: "NIST SP 800-207 — Zero Trust Architecture"
  author: "Scott Rose et al., NIST"
  year: 2020
  publisher: "National Institute of Standards and Technology"
  local_file: "sources/standards/_txt/NIST_SP_800-207_Zero_Trust_Architecture.txt"
  section: "Chapter 3 — Logical Components of Zero Trust Architecture"
  lines: 706–1289
related:
  - "[[Concepts Index]]"
  - "[[NIST 800-207 — Ch1-2 — Introduction and Tenets]]"
  - "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
  - "[[CISA Zero Trust Maturity Model]]"
  - "[[DoD ZT Reference Architecture v2]]"
  - "[[Gilman & Barth — Control Plane and Data Plane]]"
---

# NIST SP 800-207 — Chapter 3: Logical Components

> **Significance:** This is the single most important architectural chapter in the Zero Trust canon. It defines the canonical ZTA component model — Policy Engine (PE), Policy Administrator (PA), Policy Enforcement Point (PEP) — that every subsequent standard, reference architecture, and vendor framework either adopts or maps to. The chapter also introduces the control plane / data plane separation, the trust algorithm concept, and the three ZTA approach variations (identity governance, micro-segmentation, SDP) and four deployment models. No other 24-page section of government prose carries more architectural weight in cybersecurity.

---

## 3.0 — Core Logical Components

### Claim 1: ZTA has three core decision-making components (PE, PA, PEP)

**NIST's claim:** A Zero Trust Architecture is built on three logical components: the Policy Engine (PE) which makes access decisions, the Policy Administrator (PA) which executes them by configuring communication paths, and the Policy Enforcement Point (PEP) which enables, monitors, and terminates connections between subjects and resources. The PE and PA together form the Policy Decision Point (PDP) from Figure 1. These components communicate on a separate control plane while application data travels on the data plane.

**Evidence presented:** Architectural model (Figure 2) with enumerated component definitions. This is an ideal logical model — not a deployment specification. NIST explicitly notes that implementations may combine PE and PA into a single service, but separates them for conceptual clarity.

**Confidence:** HIGH — This is the canonical definition. Every major ZT framework (CISA, DoD, Forrester ZTX, Gartner CARTA) references or maps to this tripartite model. The architecture has withstood five years of implementation experience without fundamental revision.

**What's at stake:** If this component model were fundamentally wrong, the entire ZT standards ecosystem — CISA Maturity Model, DoD Reference Architecture, NIST 800-207A, and every vendor ZTNA/SDP implementation — would need re-architecture. This claim is **load-bearing** for the entire domain.

**Who disagrees:** No serious disagreement exists on the conceptual components. Vendor implementations vary in where component boundaries fall (combined PE/PA services, split PEPs into client-side agent and resource-side gateway), but the logical separation is universally accepted. The closest to a counter-position is practitioners who argue the tripartite model is too abstract to guide implementation directly — but this is about utility, not correctness.

**Alternative reading:** The PE/PA/PEP model could be seen as a restatement of the IETF AAA architecture (Authentication, Authorization, Accounting) with a new control-plane framing. The PDP/PEP split dates to IETF RFC 2753 (2000) and XACML (2003). NIST's contribution is integrating these existing concepts into a coherent ZT-specific architecture and adding the trust algorithm.

**My assessment:** Holds up strongly. The logical separation is both conceptually clean and practically useful. The fact that implementations routinely collapse PE and PA into one service while preserving the PEP as distinct confirms the model's flexibility. The weakest element is that NIST doesn't provide an interface specification between components — the model defines what the components do, not how they talk to each other.

### Claim 2: Eight data sources feed the Policy Engine's access decisions

**NIST's claim:** The PE makes decisions using inputs from: (1) Continuous Diagnostics and Mitigation (CDM) systems for asset posture, (2) Industry Compliance systems for regulatory rules, (3) Threat Intelligence feeds for external attack/vulnerability data, (4) Network and System Activity Logs for real-time security feedback, (5) Data Access Policies as the baseline authorization rules, (6) Enterprise PKI for certificate generation and management, (7) ID Management systems for user identity and attributes, and (8) SIEM systems for security-centric event analysis.

**Evidence presented:** Enumerated descriptions of each data source with its role in access decisions. NIST distinguishes between local (enterprise-controlled) and external sources.

**Confidence:** HIGH — This data-source taxonomy is comprehensive and maps cleanly to real-world implementations. Every ZTA deployment needs these inputs, though the maturity and integration of each varies widely.

**Cross-reference table:**

| NIST Data Source | CISA Maturity Model Pillar | DoD ZT RA Mapping |
|---|---|---|
| CDM System | Device pillar | Device compliance / continuous monitoring |
| Industry Compliance | Governance pillar | Policy administration |
| Threat Intelligence | (Cross-cutting) | Threat intelligence integration |
| Activity Logs | Visibility & Analytics | SIEM / analytics plane |
| Data Access Policies | Data pillar | Data security policies |
| Enterprise PKI | Device + Identity pillars | PKI / certificate services |
| ID Management | Identity pillar | Identity, Credential, and Access Management (ICAM) |
| SIEM | Visibility & Analytics | Security analytics |

**Assessment:** The data-source model holds up as a reference, but in practice, integration between these sources remains a major implementation challenge. The CISA Maturity Model effectively operationalizes this by defining progressive maturity levels for each data-source domain, from "manual" to "fully automated and integrated." The gap between NIST's ideal data-source integration and real-world deployments is where most ZT implementations fail.

---

## 3.1 — Variations of Zero Trust Architecture Approaches

### Claim 3: Three ZTA approaches exist — identity governance, micro-segmentation, and SDP

**NIST's claim:** Enterprises can enact ZTA through three approaches: (1) enhanced identity governance–driven, where access policies are based on identity and attributes; (2) logical micro-segmentation, where resources are placed on unique network segments protected by gateway security components; and (3) network infrastructure and Software Defined Perimeter (SDP), using overlay networks with the PA acting as a network controller. A full ZT solution includes elements of all three. Each approach implements all ZT tenets from Section 2.1.

**Evidence presented:** Conceptual descriptions with use-case mapping. NIST explicitly states these are not mutually exclusive and that one approach may be more suitable than others depending on existing enterprise policies and workflows.

**Confidence:** MEDIUM-HIGH — The three-way classification is analytically useful but has proven somewhat fluid in practice. The industry has largely converged on SDP/ZTNA as the primary implementation pattern, with identity governance treated as a prerequisite rather than a distinct approach, and micro-segmentation as a network-layer complement.

**What's at stake:** Misclassifying approaches could lead enterprises to choose an unsuitable implementation strategy. However, NIST's framing that all three are complementary rather than competing is protective — a full ZTA deployment needs elements of each.

**Who disagrees:** Forrester's ZTX framework treats micro-segmentation as a network capability within a broader ecosystem, not a standalone ZTA approach. Gartner's CARTA emphasizes identity at the center. Vendor positioning distorts the taxonomy: SDP vendors claim primacy, identity vendors claim identity is the "new perimeter," and network vendors claim segmentation is foundational. NIST's neutrality on this question is itself significant.

**Assessment:** The taxonomy is defensible as a conceptual framework but has limited practical utility for implementation planning. The more important observation is NIST's insistence that **all three approaches implement all ZT tenets** — this forecloses the argument that any single approach alone constitutes "full ZT." The CISA Maturity Model operationalizes this by defining maturity across five pillars (Identity, Device, Network, Application/Workload, Data) rather than by approach.

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

---

## 3.2 — Deployed Variations of the Abstract Architecture

### Claim 4: Four deployment models operationalize the logical architecture

**NIST's claim:** The logical components can be deployed in four ways: (1) Device Agent/Gateway, where the PEP is split into a client-side agent and a resource-side gateway; (2) Enclave-Based, where a gateway protects a collection of resources behind a boundary; (3) Resource Portal, where a single portal serves as a gateway without requiring client-side agents; and (4) Device Application Sandboxing, where vetted applications run in isolated compartments on assets. Multiple models may coexist in one enterprise.

**Evidence presented:** Descriptions with architectural diagrams (Figures 3–6). Each model is evaluated for use cases, strengths, and limitations.

**Confidence:** HIGH — These deployment models accurately characterize the real-world implementation patterns observed in enterprise ZT deployments. They are not mutually exclusive and an enterprise may use different models for different workflows.

#### 3.2.1 Device Agent/Gateway

**Model:** Client-side agent forwards requests to PA; PA configures secure channel between agent and resource-side gateway. This is the CSA SDP client-server implementation.

**Best for:** Enterprises with robust device management programs and discrete resources that can have individual gateways. Not suitable for BYOD (agent must be installed on enterprise-owned assets).

**Confidence:** HIGH — This is the dominant ZTNA deployment pattern.

#### 3.2.2 Enclave-Based

**Model:** Gateway at the boundary of a resource enclave (e.g., data center, private cloud) protecting a collection of resources that serve a single business function. Can be hybrid with agent/gateway model.

**Best for:** Legacy applications, on-premises data centers that cannot support individual resource gateways, cloud micro-services behind a single gateway.

**Key downside:** Gateway protects a collection, not individual resources. Subjects may see resources they don't have access to. Less granular than agent/gateway.

**Confidence:** HIGH — This is a pragmatic model for legacy environments and correctly identifies the trade-offs.

#### 3.2.3 Resource Portal

**Model:** Single PEP component acting as a gateway portal — no client-side agent required. Access is via a web portal or similar interface.

**Best for:** BYOD policies, inter-organizational collaboration, environments where agent installation is infeasible.

**Key limitation:** Cannot continuously monitor devices between sessions. Limited device visibility. Portal is exposed to discovery and DoS attacks.

**Confidence:** HIGH — This model is widely used (browser-based access, Citrix-style portals) and the limitations are accurately described.

#### 3.2.4 Device Application Sandboxing

**Model:** Vetted applications run in isolated compartments (VMs, containers) on assets. The PEP refuses access requests from non-sandboxed applications.

**Advantage:** Protects individual applications from potentially compromised hosts.

**Disadvantage:** Enterprise must maintain sandboxed applications for all assets. May not have full visibility into client assets. More operational overhead than monitoring devices.

**Confidence:** MEDIUM — This model is conceptually sound but less commonly deployed as a standalone ZTA pattern. It's better understood as a defense-in-depth complement rather than a primary deployment model.

---

## 3.3 — Trust Algorithm

### Claim 5: The Trust Algorithm is the PE's decision-making process with five input categories

**NIST's claim:** The trust algorithm (TA) is "the brain" of the ZTA — the process the PE uses to grant or deny access. It takes five categories of input: (1) Access Request (resource requested, requester info, OS/patch level), (2) Subject Database (who is requesting, attributes, privileges, historical behavior), (3) Asset Database (known vs. observable asset status, OS, software integrity, location, patch level), (4) Resource Requirements (minimum requirements including authenticator assurance levels, network location constraints, data sensitivity), and (5) Threat Intelligence (external/internal feeds about active threats, malware, vulnerabilities).

**Evidence presented:** Conceptual model (Figure 7) with categorized inputs. NIST notes that input weights may be proprietary or enterprise-configured.

**Confidence:** HIGH — The input taxonomy is comprehensive. Every ZT implementation uses some version of these inputs. The distinction between Subject Database (who you are) and Asset Database (what you're on) captures the two primary dimensions of access decisions.

**Assessment:** This is one of NIST's most durable contributions — the five-category input model provides a template against which any ZT product's decision inputs can be evaluated. The CISA Maturity Model operationalizes each input category through its pillar structure. The DoD Reference Architecture adds mission-criticality and operational tempo as additional context inputs.

### Claim 6: Trust algorithms vary on two axes — criteria/score-based and singular/contextual

**NIST's claim:** TAs differ along two dimensions: (a) Criteria-based (binary: all criteria must be met) vs. score-based (weighted confidence level compared to threshold), and (b) Singular (each request evaluated independently) vs. Contextual (subject's recent history considered). Contextual, score-based TAs provide the most dynamic and granular access control. A contextual TA can detect attacks that a singular TA misses (e.g., unusual access patterns, off-hours activity, anomalous volume).

**Confidence:** MEDIUM-HIGH — The taxonomy is analytically sound, but NIST significantly understates the operational complexity of contextual TAs. Maintaining state on all subjects, training behavioral baselines, and tuning anomaly thresholds is hard. False positives from contextual TAs can cripple workflows.

**Key examples from NIST:**
- HR employee normally accesses 20–30 records/day → contextual TA alerts at 100+ in a day
- After-hours access from unrecognized location → contextual TA triggers additional authentication
- Accountant accessing financial system at midnight → contextual TA requires more stringent confidence level

**Who disagrees:** Practitioners who have attempted contextual TA deployments report that the tuning phase NIST mentions can last indefinitely, and many organizations operate effectively with criteria-based TAs augmented by periodic re-authentication rather than continuous behavioral analysis. The gap between the "ideally" contextual TA and practical implementations remains wide.

**Cross-reference to CISA:** CISA's "Optimal" maturity level describes "fully automated, context-aware access decisions with continuous risk assessment" — essentially NIST's contextual, score-based TA. The gap between CISA's Traditional and Optimal levels on this dimension is larger than for any other capability.

**Cross-reference to DoD:** The DoD ZT RA specifies "dynamic, risk-based access decisions" (Capability 5.1) but acknowledges that "fully automated contextual decisions" are a Target-level capability, not achievable at Intermediate.

---

## 3.4 — Network/Environment Components

### Claim 7: Control plane and data plane must be logically separated

**NIST's claim:** In a ZT environment, there must be separation (logical or possibly physical) between communication flows used to control/configure the network (control plane) and application/service communication flows (data plane). The control plane is used by PE, PA, and PEPs to maintain assets, make access decisions, and set up communication paths. The data plane is used for actual application communication — and this channel may not be possible before the control plane has established the path. **NIST explicitly credits Gilman & Barth for this concept** (citation: [Gilman]).

**Confidence:** HIGH — Control/data plane separation is one of the foundational architectural principles of ZT, adapted from SDN and telecommunications. Gilman & Barth's formulation in "Zero Trust Networks" (2017) predates NIST 800-207 and provides the theoretical grounding.

**Assessment:** This claim is genuinely load-bearing. Without control plane / data plane separation, ZTA collapses into a traditional perimeter model where the network carries both control and data indiscriminately. The separation enables:
- PEPs that block all data-plane traffic until the control plane authorizes it
- Resources that are invisible/unreachable without control-plane mediation
- Session-specific, dynamically configured communication paths

**Cross-reference:** Gilman & Barth's (2017) "Zero Trust Networks" book provides the most thorough treatment of control plane / data plane architecture, including practical considerations like control plane availability, latency, and the single-point-of-failure risk that the PA/PE becomes. NIST 800-207 acknowledges scalability as a requirement (Requirement 9) but doesn't explore the failure modes Gilman & Barth discuss.

### Claim 8: Ten network requirements support ZTA

**NIST's claim:** ZTA-capable networks must satisfy ten requirements: (1) basic network connectivity for enterprise assets, (2) ability to distinguish enterprise-owned/managed assets by credentials (not spoofable attributes like MAC addresses), (3) observation of all network traffic with metadata extraction for policy updates, (4) enterprise resources not reachable without accessing a PEP, (5) logically separate data and control planes, (6) enterprise assets can reach PEP components, (7) PEP is the only component accessing the PA in business flows, (8) remote assets can access enterprise resources without VPN backhaul, (9) scalable ZT infrastructure for process load changes, (10) policy-based restrictions on which PEPs certain assets can reach.

**Confidence:** HIGH — These requirements are concrete and testable. Requirement 8 (remote access without VPN backhaul) is particularly significant: it formalizes one of ZT's most important operational benefits over traditional perimeter models.

**Assessment of critical requirements:**

| # | Requirement | Operational Significance | Implementation Difficulty |
|---|---|---|---|
| 4 | Resources unreachable without PEP | Defines the architectural "cloaking" of resources | HIGH — requires rearchitecting network access |
| 5 | Separate control/data planes | Foundational to ZTA | MEDIUM — well-understood from SDN |
| 8 | Remote access without VPN backhaul | Key operational benefit of ZT | LOW-MEDIUM — SDP/ZTNA products deliver this |
| 9 | Scalable infrastructure | Prevents the PE/PA/PEP from becoming bottleneck | HIGH — often underestimated in initial deployments |
| 10 | Policy-based PEP restriction | Enables geolocation/device-type access controls | MEDIUM — depends on PE policy granularity |

**Cross-reference to CISA:** CISA's Network pillar maps Requirements 4, 5, and 8 to specific maturity progression steps. CISA's Optimal level for the Network pillar assumes all ten requirements are met.

**Cross-reference to DoD:** DoD ZT RA v2 operationalizes Requirement 8 through the "Universal Control Plane" concept, where remote users connect to enterprise resources through cloud-hosted PEPs without traversing the enterprise perimeter. DoD's Capability 2.3 (Remote Access) explicitly requires VPN replacement with ZTNA/SDP.

---

## Chapter-Level Assessment

### What Holds Up Strongest

1. **PE/PA/PEP tripartite model.** Five years of implementation have validated this as the right abstraction level — not too granular, not too coarse.
2. **Control plane / data plane separation.** The clearest architectural differentiator between ZTA and traditional perimeter models.
3. **Trust algorithm input taxonomy.** Five categories (access request, subject, asset, resource requirements, threat intelligence) provide a durable evaluation framework.
4. **Deployment model diversity.** The four models accurately reflect real-world patterns without constraining implementation.

### What Is Most Vulnerable

1. **Contextual trust algorithms.** The "ideally contextual" aspiration understates the operational burden. The tuning phase can be indefinite, and many organizations achieve adequate security with criteria-based TAs plus strong authentication.
2. **Data source integration.** NIST assumes data sources are available and integrated. The CISA Maturity Model is more honest about how far most organizations are from this ideal.
3. **Application sandboxing as a standalone model.** This is better understood as a defense-in-depth complement, not a primary ZTA deployment pattern.

### The Single Biggest Gap

**NIST 800-207 Chapter 3 defines the WHAT (components, approaches, models) but not the HOW (interfaces, protocols, APIs).** The DoD ZT Reference Architecture and CISA Maturity Model fill this gap partially, but neither provides an interface specification between PE, PA, and PEP. This is the largest unaddressed standardization gap in ZTA — and the primary reason vendor implementations are not interoperable.

### Cross-Standard Architecture Alignment

| Concept | NIST 800-207 Ch.3 | CISA Maturity Model | DoD ZT RA v2 |
|---|---|---|---|
| Decision components | PE, PA, PEP | Implicit in all pillars | Policy Decision Point, Policy Enforcement Point |
| Control/data plane | Section 3.4 | Network pillar | Universal Control Plane |
| Identity approach | Section 3.1.1 | Identity pillar (foundational) | ICAM + ABAC |
| Micro-segmentation | Section 3.1.2 | Network pillar (maturity levels) | Network Environment pillar |
| SDP/ZTNA | Section 3.1.3 | Implicit in Network pillar | Capability 2.3 (Remote Access) |
| Trust algorithm | Section 3.3 | Cross-cutting "automation and orchestration" | Dynamic risk-based access (Capability 5.1) |
| Deployment models | Section 3.2 (4 models) | Not explicitly modeled | Reference designs (7 architectures) |

### Existential Threat to the Chapter's Authority

If any other standards body were to define a fundamentally incompatible ZT component model (e.g., merging PE/PA/PEP into a single component, or splitting control plane into three separate planes), NIST 800-207 Chapter 3's canonical status would weaken. This has not happened. The chapter's authority grows with each standard that adopts its model rather than competing with it.

---

## Inline Cross-References

- **[[CISA Zero Trust Maturity Model]]** — Operationalizes the five pillars (Identity, Device, Network, Application/Workload, Data) that map to NIST's data sources and approaches. See especially the Network pillar for micro-segmentation and SDP maturity progression.
- **[[DoD ZT Reference Architecture v2]]** — Adopts the PE/PA/PEP model and provides seven reference designs. Adds mission-criticality and operational tempo as trust-algorithm inputs. Operationalizes the "VPN replacement" requirement (Requirement 8) through Capability 2.3.
- **[[Gilman & Barth — Control Plane and Data Plane]]** — The foundational text (2017, "Zero Trust Networks") that NIST explicitly cites for control plane / data plane separation. Provides practical implementation guidance that NIST 800-207 deliberately omits, including control plane availability, latency considerations, and the PA/PE as single point of failure.
- **[[NIST 800-207 — Ch1-2 — Introduction and Tenets]]** — The ZT definition and seven tenets that Chapter 3's architecture implements.
- **[[NIST 800-207 — Ch4 — Deployment Scenarios]]** — Practical use cases that exercise the architecture defined in Chapter 3.

---

*Notes prepared for the OSKG-ZeroTrust knowledge graph. This chapter will generate approximately 15–20 claim nodes during Phase 2 extraction. See [[Concepts Index]] for related concept notes and [[METHODOLOGY]] for the claim format specification.*
