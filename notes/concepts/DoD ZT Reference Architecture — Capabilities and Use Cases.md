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
claims_status: extracted
claims_extracted: 2026-07-24
  - topic/zt-architecture
  - topic/zt-governance
  - topic/zt-implementation
---

# DoD ZT Reference Architecture — Capabilities and Use Cases

> **Significance:** Chapters 3 and 4 of the DoD ZT RA v2 operationalize the Pillars from Chapter 2 into a concrete capability taxonomy and a set of 17 use cases. The capability taxonomy (CV-2) defines *what* the DoD must be able to do; the Fit-for-Purpose mapping (CV-7) defines *how* those capabilities map to pillars, decision points, and data flows. The 17 use cases (OV-1 and OV-2 diagrams) define *what problems* these capabilities solve. Together, they form the architecture's prescriptive core — moving beyond principles and into implementable functions.

---

## Chapter 3: Capabilities

**Claim 1 —** The Seven Pillars serve as the organizing taxonomy for all ZT capabilities, with seven aggregated capabilities (Continuous Authentication, Conditional Authorization, Enabling Infrastructure, Securing Application & Workload, Securing Data, Analytics, Automation & Orchestration) each nesting into sub-capabilities that extend the entire taxonomy. → [[dod-seven-aggregated-capabilities-taxonomy]]
---

**Claim 2 —** Continuous authentication and identity validation are common to all pillars — every access transaction requires it regardless of what pillar the capability falls under — and three enterprise-scale enablers (federated enterprise identity service, enterprise analytics, enterprise orchestration) are prerequisites, not optional. → [[continuous-authentication-common-all-pillars]]
---

**Claim 3 —** The Fit-for-Purpose (FFP) mapping instantiates a chain of five decision points — not NIST's single PDP — extending from Authentication through Authorization, Resource, Application, to Data, with each building on the previous and independently evaluating confidence levels. → [[ffp-five-decision-points-chain]]
---

**Claim 4 —** NPE and person identities are tracked independently, allowing separate paths for validating confidence levels — device and user confidence are independently developed and then aggregated at policy enforcement time, with access granted only if the combined confidence score exceeds a measured threshold that varies by data sensitivity. → [[npe-person-identities-independent-confidence]]
---

## Chapter 4: Use Cases

The following 17 use cases represent the DoD's catalog of ZT implementation patterns. Each is documented with both an OV-1 (high-level operational concept) and OV-2 (operational resource flow) diagram. They fall into six thematic clusters.

---

**Claim 5 —** Data-Centric Security (Use Cases 1–4) — data protection must shift from network-centric RBAC to attribute-based ABAC with four coordinating protection mechanisms (Data Tagging, DRM, DLP, DDM) operating around the Data Store, and encryption decisions made by the ZT policy engine rather than as a separate concern. → [[data-centric-security-abac-protection]]
---

**Claim 6 —** Analytics and AI (Use Cases 5–6) — ZT must unify siloed domain data through a pipeline (Sensors → SIEM → SOAR + AI → ZT Controller → ML/AI storage) to enable consistent policies, user/NPE confidence scoring, advanced threat detection, and automated threat mitigation, collecting far more data than traditional architectures to power automation. → [[analytics-ai-unified-pipeline-zt]]
---

**Claim 7 —** Orchestration and Policy Management (Use Cases 7–9) — centralized orchestration through a four-layer hierarchy (Global SDE Orchestrator → Cybersecurity Domain Orchestrator → ZT Policy Controller → PEPs) resolves siloed policy conflicts, and the dynamic adaptive policy feedback loop enables ZT policy to improve over time rather than being static, evolving from out-of-band AI (human review) to in-band AI (automated within acceptable risk bounds). → [[orchestration-policy-four-layer-hierarchy]]
---

**Claim 8 —** Network Transformation (Use Cases 10–11) — VPN removal is an architectural consequence of ZT's \"no distinction between internal and external users\" principle, with all users passing through the same PEPs and gateways; east-west segmentation requires three levels (network-level micro-segmentation, process-level host-based inspection, API-level per-call auth) to prevent lateral movement. → [[network-transformation-vpn-removal-segmentation]]
---

**Claim 9 —** Device Hygiene (Use Cases 12–13) — device hygiene must shift from checklist-based (STIG benchmarks, version numbers) to Event-Condition-Action automation where device posture is continuously checked by multiple tools, confidence scoring for devices considers behavioral patterns beyond patch status, and severity determines response speed (gradual restriction to instant termination). → [[device-hygiene-event-condition-automation]]
---

**Claim 10 —** Authentication and Authorization (Use Cases 14–17) — authentication must become dynamic and continuous, driven by UEBA-based confidence scoring that triggers real-time access changes (deny, challenge, re-authenticate, downgrade) throughout sessions; authorization is no longer binary (yes/no) but scalar — a confidence score compared against a threshold that varies by data sensitivity, with the same user potentially authorized for unclassified but denied for classified data in the same session. → [[authentication-authorization-dynamic-continuous]]
---

**Claim 11 —** The DoD's capability-driven approach distinguishes itself from other ZT frameworks — where NIST 800-207 provides the abstract logical model and CISA provides the maturity ladder, the DoD provides an exhaustive capability inventory, a concrete five-decision-point enforcement architecture, and 17 use cases that operationalize every major ZT concept with defined resource flows. → [[dod-capability-driven-approach-distinction]]
---

## Related Notes

| Note | Relationship |
|---|---|
| [[NIST 800-207 — Ch3 — Logical Components]] | The abstract component model that DoD instantiates with concrete capabilities and decision points |
| [[NIST 800-207 — Ch4 — Deployment Scenarios]] | NIST's five scenarios — complementary to DoD's 17 use cases; cross-referenced throughout this note |
| [[CISA ZTMM — Identity Pillar]] | CISA's identity maturity progression — maps to DoD's authentication and authorization use cases |
| [[CISA ZTMM — Device Network App Data Pillars]] | CISA's remaining pillar maturity models — maps to DoD's device hygiene, east-west segmentation, and data-centric use cases |
| [[NSA — Embracing a Zero Trust Security Model]] | NSA's 2021 guidance — provides some of the operational principles the DoD RA instantiates |
