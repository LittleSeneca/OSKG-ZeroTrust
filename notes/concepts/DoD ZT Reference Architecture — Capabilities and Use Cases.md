---
tags:
  - source/standards
  - dod
  - zt-capabilities
  - zt-use-cases
  - zt-implementation
  - oskg-zerotrust
created: 2026-07-24
confidence: high
source:
  title: "DoD Zero Trust Reference Architecture v2.0"
  author: "DISA and NSA Zero Trust Engineering Team"
  year: 2022
  publisher: "Department of Defense"
  local_file: "sources/standards/_txt/DoD_ZT_Reference_Architecture_v2.txt"
  section: "Chapters 3 & 4 — Capabilities and Use Cases"
related:
  - "[[Concepts Index]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
  - "[[CISA ZTMM — Identity Pillar]]"
  - "[[CISA ZTMM — Device Network App Data Pillars]]"
  - "[[NSA — Embracing a Zero Trust Security Model]]"
---

# DoD ZT Reference Architecture — Capabilities and Use Cases

> **Significance:** Chapters 3 and 4 of the DoD ZT RA v2 operationalize the Pillars from Chapter 2 into a concrete capability taxonomy and a set of 17 use cases. The capability taxonomy (CV-2) defines *what* the DoD must be able to do; the Fit-for-Purpose mapping (CV-7) defines *how* those capabilities map to pillars, decision points, and data flows. The 17 use cases (OV-1 and OV-2 diagrams) define *what problems* these capabilities solve. Together, they form the architecture's prescriptive core — moving beyond principles and into implementable functions.

---

## Chapter 3: Capabilities

### Claim 1: The Seven Pillars serve as the organizing taxonomy for all ZT capabilities, with seven aggregated capabilities (Continuous Authentication, Conditional Authorization, Enabling Infrastructure, Securing Application & Workload, Securing Data, Analytics, Automation & Orchestration) each nesting into sub-capabilities that extend the entire taxonomy.

**Author's claim:** Each capability is "the ability to achieve a desired effect under specified (performance) standards and conditions through combinations of ways and means (activities and resources)." The entire taxonomy is subject to change as technologies evolve. (§3.1, CV-2)

**Evidence presented (aggregated capabilities):**

| Aggregate Capability | Description | Maps To |
|---|---|---|
| **Continuous Authentication** | Validating identity of entities during all access transactions, enhanced with behavioral metrics and additional identifying factors | User, Device |
| **Conditional Authorization** | Granting access contingent on continued trustworthiness — influenced by device hygiene, user/NPE behavior, and other factors | User, Device, Data |
| **Enabling Infrastructure** | Network/environment segmentation (macro and micro), Software Defined Perimeters, cloud resources | Network/Environment |
| **Securing Application & Workload** | Preventing lateral movement, validating software practices, segmenting applications, API standardization | Applications & Workload |
| **Securing Data** | Tagging, sensitive data identification, exfiltration protections, encryption at rest and in transit | Data |
| **Analytics** | Continuous entity monitoring, sensors, logging, event-driven analytics, machine learning for baselining | Visibility & Analytics |
| **Automation & Orchestration** | Automated policy deployment, ingestion of desired target state from SDE, AI/RPA augmentation (future) | Automation & Orchestration |

**Confidence:** HIGH. This is the direct capability taxonomy from the DoD RA.

**Three enabling cross-cutting domains:**
1. **Data Governance** — Processes, tools, and frameworks for managing data from creation to disposition.
2. **Risk Management (RMF)** — Interdependent with ZT: ZT provides discovery content to feed RMF; RMF's prepare/assess/monitor steps adapt to DevSecOps practices.
3. **Software-Defined Enterprise (SDE)** — As compute, network, and storage are virtualized and software-defined, data and applications can be isolated at scale.

---

### Claim 2: Continuous authentication and identity validation are common to all pillars — every access transaction requires it regardless of what pillar the capability falls under — and three enterprise-scale enablers (federated enterprise identity service, enterprise analytics, enterprise orchestration) are prerequisites, not optional.

**Author's claim:** Key dynamics within the capability taxonomy. (§3.1)

**Evidence presented:**
- Continuous authentication and identity validation are common to all pillars — every access transaction requires it.
- Capabilities point to multiple pillars — white arrows in Figure 6 show which aggregated capability acts on which pillar.
- Enterprise-scale enablers are required: a federated enterprise identity service, enterprise analytics, and enterprise orchestration are prerequisites.
- Data discovery and labeling must precede implementation — proper attributes and data labeling during the discovery process are prerequisites for a ZT architecture to function.

**Confidence:** HIGH. These are direct assertions from the capability taxonomy section.

**Cross-reference — CISA ZTMM:** CISA's maturity model organizes capabilities differently — by *maturity stage* within each pillar rather than as a taxonomy. Where DoD provides the capability inventory (what must exist), CISA provides the maturity progression (how advanced each capability should be). See [[CISA ZTMM — Identity Pillar]] and [[CISA ZTMM — Device Network App Data Pillars]].

**Cross-reference — NIST 800-207 Ch3:** NIST's logical component model (PE, PA, PEP) is the abstract architectural pattern. DoD's capability taxonomy is the concrete instantiation — it specifies *which* capabilities populate the control plane and data plane. DoD's "Analytics & Confidence Scoring" capability maps to NIST's trust algorithm; DoD's "Automation & Orchestration" maps to NIST's Policy Administrator function. See [[NIST 800-207 — Ch3 — Logical Components]].

---

### Claim 3: The Fit-for-Purpose (FFP) mapping instantiates a chain of five decision points — not NIST's single PDP — extending from Authentication through Authorization, Resource, Application, to Data, with each building on the previous and independently evaluating confidence levels.

**Author's claim:** Figure 11 (CV-7) provides an operational view of how security measures are implemented within the architecture, organized around decision points placed at key enforcement locations. (§3.2)

**Evidence presented (architecture of decision points):**

| Decision Point | What It Evaluates | Capability |
|---|---|---|
| **Authentication Decision Point** | Credential issuance, user/NPE identity, device managed/unmanaged state | Continuous Authentication, ICAM Service |
| **Authorization Decision Point** | User and device confidence levels against policy | Conditional Authorization, C2C Service |
| **Resource Authorization Decision Point** | Combined NPE + user confidence level for resource access | Securing Application Workload |
| **Application Authorization Decision Point** | Combined user + NPE for application-specific access | Securing Application Workload, Securing Supply Chain |
| **Data Authorization Decision Point** | Data tagging, classification, owner-defined policies | Securing Data, Data Discovery & Classification, Dynamic Data Masking |

**Confidence:** HIGH. The five-decision-point chain is documented in the FFP mapping.

**Cross-reference — NIST 800-207:** The DoD's multi-decision-point architecture extends NIST's single PDP/PEP model. NIST defines one Policy Decision Point; the DoD instantiates a chain of *five* decision points, each with independent confidence evaluation. This reflects the scale and classification requirements unique to defense environments.

---

### Claim 4: NPE and person identities are tracked independently, allowing separate paths for validating confidence levels — device and user confidence are independently developed and then aggregated at policy enforcement time, with access granted only if the combined confidence score exceeds a measured threshold that varies by data sensitivity.

**Author's claim:** NPE and person identities are tracked independently. Confidence levels for device and user are independently developed and then **aggregated** at policy enforcement time. (§3.2)

**Evidence presented (data flow through the enforcement chain):**
1. User/endpoint → Authentication DP → Authorization DP → Resource DP → Application DP → Data DP
2. At each enforcement point, logs are sent to the **SIEM**
3. Analytics develop a **confidence level** from SIEM data
4. **DLP** feeds the SIEM to ensure data is being used properly even after access is granted
5. If confidence drops below threshold → SOAR triggers policy changes → PEPs enforce new restrictions

**Supporting infrastructure capabilities:**

| Capability | Description |
|---|---|
| **Enterprise Identity Service (FEIS + AAP + MUR)** | Federated identity credentials across organizations; automatic account provisioning/deprovisioning; Master User Record for audit and threat detection |
| **Comply-to-Connect (C2C)** | Discovers, identifies, characterizes, and reports all connecting devices; orchestrates tools to prevent non-compliant device access |
| **Policy Engine & Automation (SOAR)** | Threat management, incident response, policy enforcement automation; works with analytics to develop confidence levels and push policy to PEPs |
| **Analytics & Confidence Scoring** | Statistical analysis of event/incident logs to produce confidence scores — the probability that a user/NPE is who they assert to be |
| **SIEM** | Aggregates and stores activity data; provides both security information management and security event management |

**Confidence:** HIGH. The independent identity tracking and confidence scoring model is foundational to the DoD RA's enforcement architecture.

---

## Chapter 4: Use Cases

The following 17 use cases represent the DoD's catalog of ZT implementation patterns. Each is documented with both an OV-1 (high-level operational concept) and OV-2 (operational resource flow) diagram. They fall into six thematic clusters.

---

### Claim 5: Data-Centric Security (Use Cases 1–4) — data protection must shift from network-centric RBAC to attribute-based ABAC with four coordinating protection mechanisms (Data Tagging, DRM, DLP, DDM) operating around the Data Store, and encryption decisions made by the ZT policy engine rather than as a separate concern.

**Author's claim:** Data is protected by network-centric policies — username/password, device-based access, encryption only at rest, and static RBAC rarely updated or validated. The ZT solution is a unified framework with data-centric policies coordinated through continuous assessment. (§4.1–4.4)

**Evidence presented:**

**Four protection mechanisms:**
| Mechanism | Function |
|---|---|
| **Data Tagging** | On creation/import, categorize data with attributes for PII/sensitivity classification; feeds DRM and DLP |
| **DRM (Data Rights Management)** | Allow/block access, editing, or copying of data based on tags and policy |
| **DLP (Data Loss Prevention)** | Block access and transmission of data; monitor for exfiltration |
| **DDM (Dynamic Data Masking)** | Mask and alter data while being accessed/transmitted — column-level security at query time |

**RBAC → ABAC evolution:** Data tagging enables Attribute-Based Access Control (ABAC), which creates dynamic policies based on attributes rather than static roles. RBAC answers "what role are you?" ABAC answers "what are the attributes of this access request?" — and can change in real time.

**Encryption integration (4.3):** Encryption and access control are not separate concerns. The decision to decrypt is itself a policy decision made by the ZT policy engine. The flow: request → PEPs → check policy → if allowed, decrypt; simultaneously, SIEM analyzes the request and can trigger SOAR to terminate sessions and re-encrypt data.

**Confidence:** HIGH. The data-centric security model is well-specified with defined mechanisms and flows.

---

### Claim 6: Analytics and AI (Use Cases 5–6) — ZT must unify siloed domain data through a pipeline (Sensors → SIEM → SOAR + AI → ZT Controller → ML/AI storage) to enable consistent policies, user/NPE confidence scoring, advanced threat detection, and automated threat mitigation, collecting far more data than traditional architectures to power automation.

**Author's claim:** Siloed domains create inconsistent policies, data, logs, and analytics. ZT makes siloed domains obsolete through unified analytics and AI. (§4.5–4.6)

**Evidence presented (data pipeline):**
```
Sensors → SIEM (initial processing, threat detection) → SOAR + AI (advanced analysis)
                                                            ↓
                                                     ZT Controller (automated mitigation)
                                                            ↓
                              ML/AI storage (confidence scoring, baselining, external intel)
```

**What this enables:**
- Systematic data collection identifying data types and finding correlations between datasets
- Accelerated automation of data preparation (gather → discover → assess → clean → structure → transform → enrich → publish)
- Consistent policies, data, logs, and analytics across the architecture
- User/NPE confidence scoring, advanced threat detection, and automated threat mitigation

**Scale difference:** A ZT model collects far more data than traditional architecture — required to power automation. This demands advanced tools beyond traditional SIEM.

**Confidence:** MEDIUM-HIGH. The pipeline is architecturally sound but the DoD's claim that it makes siloed domains "obsolete" is aspirational — most organizations have significant data integration debt.

---

### Claim 7: Orchestration and Policy Management (Use Cases 7–9) — centralized orchestration through a four-layer hierarchy (Global SDE Orchestrator → Cybersecurity Domain Orchestrator → ZT Policy Controller → PEPs) resolves siloed policy conflicts, and the dynamic adaptive policy feedback loop enables ZT policy to improve over time rather than being static, evolving from out-of-band AI (human review) to in-band AI (automated within acceptable risk bounds).

**Author's claim:** Administrators apply configuration and policy changes within their own domains with little regard to other control areas, producing non-cohesive policies. ZT requires centralized orchestration of policy creation, deployment, and continued validation. (§4.7–4.9)

**Evidence presented (orchestration hierarchy):**

| Layer | Component | Role |
|---|---|---|
| **Global** | SDE Global Orchestrator | Provides desired/target state of the environment |
| **Domain** | Cybersecurity Domain Orchestrator (CDO) | Compares desired state to security policies, resolves conflicts, pushes policy to controllers |
| **Controller** | ZT Policy Controller | Disseminates policy to enforcement points specific to each area of influence |
| **Enforcement** | Policy Enforcement Points (PEPs) | Execute policy at the point of access |

**The adaptive feedback loop (4.9 — most architecturally significant use case):**
```
Policy Created → Deployed to PEPs → Monitored → Analyzed → Changes Identified
                                                                    ↓
                        (future: AI generates policy for review/stopgap)
                                                                    ↓
           Changes Approved → Reapplied to PEPs → Cycle repeats
```

**Confidence:** HIGH for the architecture; MEDIUM for the AI evolution timeline. The feedback loop is well-defined but the AI evolution (out-of-band → in-band) is aspirational without a timeline or decision criteria.

**Cross-reference — NIST 800-207:** NIST's trust algorithm (Ch3) is the *calculation engine*. DoD's adaptive feedback loop is the *continuous improvement mechanism* that refines the trust algorithm over time. NIST defines the static comparison; DoD adds the dynamic refinement dimension.

---

### Claim 8: Network Transformation (Use Cases 10–11) — VPN removal is an architectural consequence of ZT's "no distinction between internal and external users" principle, with all users passing through the same PEPs and gateways; east-west segmentation requires three levels (network-level micro-segmentation, process-level host-based inspection, API-level per-call auth) to prevent lateral movement.

**Author's claim:** There is no distinction between "internal" and "external" users in ZT. One outcome: VPN removal. Implicit trust in communication between systems allows lateral movement; ZT requires only allowing specific communication required for applications to function. (§4.10–4.11)

**Evidence presented (VPN problems):**
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

**Confidence:** HIGH. The VPN removal argument and three-level segmentation model are well-specified.

---

### Claim 9: Device Hygiene (Use Cases 12–13) — device hygiene must shift from checklist-based (STIG benchmarks, version numbers) to Event-Condition-Action automation where device posture is continuously checked by multiple tools, confidence scoring for devices considers behavioral patterns beyond patch status, and severity determines response speed (gradual restriction to instant termination).

**Author's claim:** Device hygiene has been checklist-based — hitting STIG benchmarks, being at certain version numbers, and general event monitoring. ZT makes hygiene part of authorization to specific information, continuously checked by multiple tools. (§4.12–4.13)

**Evidence presented (Event-Condition-Action structure):**

| Component | Description |
|---|---|
| **Event** | Signal or criteria that invokes the rule (e.g., vulnerability detected, anomalous behavior) |
| **Condition** | Logical test that determines if action is needed (e.g., confidence score below threshold) |
| **Action** | Policy update — from gradual restriction to instant session termination |

**Key dynamics:**
- **Baselining:** ZT baselines not only "what a normal device looks like" but also *patterns of individual machines*. Discrepancies between current actions and historical patterns trigger different policies.
- **Event-driven triggers:** Detection of a system issue initiates unified, coordinated policy provisioned across PEPs. Severity determines response speed — gradual change or instant termination.
- **Confidence scoring for devices:** Erratic systems have their score affected by network behavior, process behavior, or other characteristics — not just patch status.
- **Real-time validation against exploits:** If remediation is possible, the system attempts it; if not, the device is removed from the environment to prevent exploitation.

**Confidence:** HIGH. The ECA model is well-defined and operationally specific.

**Cross-reference — NSA Device Pillar:** NSA's Device Pillar framework (four phases: Preparation → Basic → Intermediate → Advanced) aligns with DoD's device hygiene progression. NSA emphasizes TPM, secure boot, and device attestation; DoD adds the event-condition-action automation layer.

---

### Claim 10: Authentication and Authorization (Use Cases 14–17) — authentication must become dynamic and continuous, driven by UEBA-based confidence scoring that triggers real-time access changes (deny, challenge, re-authenticate, downgrade) throughout sessions; authorization is no longer binary (yes/no) but scalar — a confidence score compared against a threshold that varies by data sensitivity, with the same user potentially authorized for unclassified but denied for classified data in the same session.

**Author's claim:** Conventional authentication uses persona-based identities, credentials, and attributes that are not dynamic or context-aware. Traditional authorization does not consider dynamic context. ZT requires multi-attribute-based confidence levels enabling continuous authentication and conditional authorization under least-privilege. (§4.14–4.17)

**Evidence presented (continuous authentication process):**
1. User/NPE requests access → provides attribute data (CAC, certificate, biometric) to identity agent
2. Throughout the session, **behavior data** is collected at PDPs: time of day, resource/operation requested
3. Behavior data is logged to SIEM → feeds **UEBA engine** for analysis
4. UEBA develops a **confidence score** distributed to policy enforcement points
5. If confidence drops → SOAR can deny, challenge, re-authenticate, or downgrade access

**Entity authentication types:**

| Entity Type | Examples | Authentication Mechanism |
|---|---|---|
| **User Device** (with loadable services) | Laptop, mobile, desktop | User identity + device identity |
| **Resource Device** (with loadable services) | Servers, network infrastructure | NPE identity via device manager |
| **IoT/Sensor** (ID and interface only) | Sensors, embedded devices | Unique ID via embedded service |
| **User Proxy** | Application standing in for user | Proxy identity to authentication service |
| **Device Management Proxy** | Device manager representing device | Unique device ID to auth service |
| **Application Service** | Software with unique instance ID | Instance-specific authentication |

**Conditional authorization flow (OV-2 step-by-step):**

| Step | What Happens | Capabilities Involved |
|---|---|---|
| **Step 0** (continuous) | Device sends inventory, system information, scans, and status to PDP | Device Hygiene, C2C, Continuous Authentication |
| **Step 0** (continuous) | ZT Policy Controller constantly sends updated policy to PDP | Automation & Orchestration |
| **Step 1** | User sends access request from device → if device passed Step 0, hits PEP | Conditional Authorization |
| **Step 2** | User provides sign-on credentials → multi-attribute evaluation begins | Authentication, UEBA |
| **Step 3** | Multiple controllers score the request: RBAC, ABAC, C2C, NAC, hygiene diagnostics, application sensitivity, data tags | All pillars |
| **Step 4** | PDP computes final confidence score from all controller inputs | Analytics & Confidence Scoring |
| **Step 5** | If score meets organizational threshold → authorization granted | Conditional Authorization |

**Multi-attribute scoring inputs:** RBAC, ABAC, C2C, NAC, hygiene diagnostics, application sensitivity, data tags.

**Confidence:** HIGH. The authentication/authorization flows are among the most detailed in the document.

**Cross-reference — NIST 800-207:** NIST mentions continuous authentication as a desirable property. DoD makes it a first-class capability with a defined process flow, UEBA integration, and confidence scoring that triggers real-time access changes.

**Cross-reference — CISA ZTMM:** CISA's Identity and Device pillar maturity stages track the progression from static RBAC (Traditional) to fully dynamic, risk-adaptive ABAC with continuous validation (Optimal). DoD's conditional authorization describes the Optimal-level end state.

---

### Claim 11: The DoD's capability-driven approach distinguishes itself from other ZT frameworks — where NIST 800-207 provides the abstract logical model and CISA provides the maturity ladder, the DoD provides an exhaustive capability inventory, a concrete five-decision-point enforcement architecture, and 17 use cases that operationalize every major ZT concept with defined resource flows.

**Author's claim:** This is a synthesis claim by this note's author comparing the three major frameworks.

**Evidence presented (framework comparison):**
1. **An exhaustive capability inventory** — 7 aggregated capabilities with dozens of sub-capabilities, each mapped to specific pillars and decision points
2. **A concrete enforcement architecture** — not one PDP but a chain of five decision points, each with independent confidence evaluation
3. **17 use cases that operationalize every major ZT concept** — each with defined resource flows

**The confidence scoring feedback loop (through-line across all use cases):**
```
Identity + Device + Behavior → Confidence Score → Policy Decision → Enforcement → Logging → Analytics → Refined Score
```

**Confidence:** MEDIUM. The comparison is this note's analytical framing — the framework distinctions are visible in the documents but neither NIST nor CISA explicitly positions itself as complementary to the DoD RA.

**Gaps and tensions identified by this analysis:**
- The DoD taxonomy assumes significant enterprise infrastructure (FEIS, SDE, SIEM, SOAR) already in place — the "brownfield" assumption. Organizations without these face a steeper path.
- The 17 use cases are documented at OV-1/OV-2 level (operational concepts and resource flows). They stop at defining *what* must happen, not *how* to build it. Reference Designs (RDs) and Reference Implementations (RIs) are the missing next layer.
- NPE identity management is called out as critical but acknowledged as immature even in industry. The DoD flags this as an area requiring further development.
- The feedback loop's AI evolution (out-of-band → in-band) is aspirational. The architecture correctly identifies the path but does not prescribe a timeline or decision criteria for when to trust automated policy changes.

---

## Related Notes

| Note | Relationship |
|---|---|
| [[NIST 800-207 — Ch3 — Logical Components]] | The abstract component model that DoD instantiates with concrete capabilities and decision points |
| [[NIST 800-207 — Ch4 — Deployment Scenarios]] | NIST's five scenarios — complementary to DoD's 17 use cases; cross-referenced throughout this note |
| [[CISA ZTMM — Identity Pillar]] | CISA's identity maturity progression — maps to DoD's authentication and authorization use cases |
| [[CISA ZTMM — Device Network App Data Pillars]] | CISA's remaining pillar maturity models — maps to DoD's device hygiene, east-west segmentation, and data-centric use cases |
| [[NSA — Embracing a Zero Trust Security Model]] | NSA's 2021 guidance — provides some of the operational principles the DoD RA instantiates |
