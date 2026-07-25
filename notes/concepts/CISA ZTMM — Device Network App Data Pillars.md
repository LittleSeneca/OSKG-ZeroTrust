---
tags:
  - source/standards
  - cisa
  - zt-device
  - zt-network
  - zt-app
  - zt-data
  - zt-maturity
  - oskg-zerotrust
created: 2026-07-24
confidence: very-high
note_type: combined
justification: "Four pillars are individually documented in the CISA model but share the same maturity structure; combining reduces redundancy while preserving per-pillar detail."
source:
  title: "CISA Zero Trust Maturity Model v2.0"
  authors: "Cybersecurity and Infrastructure Security Agency"
  year: 2023
  version: "2.0"
  publisher: "CISA"
  local_file: "sources/standards/_txt/CISA_Zero_Trust_Maturity_Model_v2.txt"
related:
  - "[[Concepts Index]]"
  - "[[CISA Zero Trust Maturity Model — Full]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[NSA ZT Device Pillar]]"
  - "[[NSA ZT Network Pillar]]"
claims_status: extracted
claims_extracted: 2026-07-24
  - topic/zt-network
  - topic/zt-governance
  - topic/zt-device
---

# CISA ZTMM — Device, Network, App, and Data Pillars

Combined note covering CISA's Zero Trust Maturity Model v2 (April 2023) for the four remaining pillars beyond Identity: **Device**, **Network/Environment**, **Application Workload**, and **Data**. Each pillar is documented with its functions and maturity-stage descriptions across Traditional → Initial → Advanced → Optimal levels, plus the three cross-cutting capabilities (Visibility & Analytics, Automation & Orchestration, Governance) applied within each pillar.

The Identity pillar is documented separately in [[CISA ZTMM — Identity Pillar]].

---

## 1. Device Pillar (§5.2)

> A device refers to any asset (including its hardware, software, firmware, etc.) that can connect to a network, including servers, desktop and laptop machines, printers, mobile phones, IoT devices, networking equipment, and more.

**Related NIST 800-207 mapping:** The Device pillar maps to NIST 800-207's asset management and posture assessment components. See [[NIST 800-207 — Ch3 — Logical Components]] for the Policy Enforcement Point (PEP) role that devices play in access decisions.

**Related NSA guidance:** See [[NSA ZT Device Pillar]] for the threat-informed device security perspective — NSA emphasizes device attestation, firmware integrity, and supply chain provenance more heavily than CISA's maturity model.

**Claim 1 —** Device Policy Enforcement & Compliance Monitoring — maturity progresses from limited visibility and manual enforcement to continuous verification of compliance throughout device/virtual asset lifetimes, with automated methods for managing software, vulnerabilities, and patches integrated across all environments. → [[device-policy-enforcement-compliance-monitoring]]
**Claim 2 —** Asset & Supply Chain Risk Management — maturity progresses from ad hoc, enterprise-blind tracking to comprehensive near-real-time visibility of all assets across vendors and service providers, with automated supply chain risk management and operations that tolerate supply chain failures. → [[asset-supply-chain-risk-management]]
**Claim 3 —** Device Resource Access — maturity progresses from requiring no device visibility for access decisions to considering real-time risk analytics within devices and virtual assets, integrating device posture with identity and environmental context. → [[device-resource-access-context]]
**Claim 4 —** Device Threat Protection — maturity progresses from manual deployment to some devices to centralized, unified threat protection with advanced capabilities for all devices and virtual assets, integrated with policy enforcement and compliance monitoring. → [[device-threat-protection-centralized]]
**Claim 5 —** Device Cross-Cutting Capabilities (Visibility & Analytics, Automation & Orchestration, Governance) — progress from manual, physically-labeled inventory to automated status collection of all network-connected devices correlated with identities, endpoint monitoring, and anomaly detection; from manual provisioning to fully automated lifecycle management; from ad hoc policies to automated enterprise-wide device lifecycle governance. → [[device-cross-cutting-capabilities-summary]]
---

## 2. Network/Environment Pillar (§5.3)

> A network refers to an open communications medium including agency internal networks, wireless networks, the Internet, cellular channels, and application-level channels used to transport messages.

ZTAs enable a shift away from perimeter-focused approaches. Agencies manage internal and external traffic flows, isolate hosts, enforce encryption, segment activity, and enhance enterprise-wide network visibility. Security controls are implemented closer to applications, data, and other resources — augmenting traditional network-based protections.

**Related NIST 800-207 mapping:** Maps to the control plane/data plane separation in NIST 800-207. The PEP and PA/PE operate on the network layer to enforce per-session access. See [[NIST 800-207 — Ch3 — Logical Components]].

**Related NSA guidance:** See [[NSA ZT Network Pillar]] for NSA's network segmentation, encryption, and traffic inspection requirements — NSA emphasizes cryptographic isolation and traffic filtering at a more granular level than CISA.

**Claim 6 —** Network Segmentation — maturity progresses from large perimeter/macro-segmentation with minimal intra-segment restrictions to fully distributed ingress/egress micro-perimeters with extensive micro-segmentation based on application profiles and dynamic JIT/JEA connectivity. → [[network-segmentation-micro-perimeters]]
**Claim 7 —** Network Traffic Management — maturity progresses from manually implemented static network rules with limited monitoring to dynamic rules and configurations that continuously evolve to meet application profile needs, reprioritizing applications based on mission criticality and risk. → [[network-traffic-management-dynamic]]
**Claim 8 —** Traffic Encryption — maturity progresses from encrypting minimal traffic with manual key management to encrypting all appropriate traffic, enforcing least privilege for secure key management enterprise-wide, and incorporating cryptographic agility as widely as possible. → [[traffic-encryption-cryptographic-agility]]
**Claim 9 —** Network Resilience — maturity progresses from case-by-case network configuration matching individual application availability demands with limited resilience for non-mission-critical workloads to holistic delivery and awareness adapting to changes in availability demands for all workloads with proportionate resilience. → [[network-resilience-holistic]]
**Claim 10 —** Network Cross-Cutting Capabilities — progress from boundary-focused manual monitoring to enterprise-wide situational awareness with advanced automated telemetry correlation; from manual configuration management to infrastructure-as-code with automated change management; from static perimeter-focused policies to enterprise-wide policies enabling tailored local controls with dynamic updates. → [[network-cross-cutting-capabilities-summary]]
---

## 3. Application Workload Pillar (§5.4)

> Applications and workloads include agency systems, computer programs, and services that execute on-premises, on mobile devices, and in cloud environments.

Agencies should manage and secure deployed applications and ensure secure application delivery. Granular access controls and integrated threat protections offer enhanced situational awareness. OMB M-22-09 directs agencies to make applications available over public networks to authorized users. Best practices for DevSecOps, CI/CD, and immutable workloads should be adopted.

**Related NIST 800-207 mapping:** Maps to the Policy Decision Point (PDP) and PEP functions in NIST 800-207 — applications are the resources being accessed, and the access decision considers application-specific context. See [[NIST 800-207 — Ch3 — Logical Components]].

**Claim 11 —** Application Access — maturity progresses from authorization based primarily on local authorization and static attributes to continuous authorization incorporating real-time risk analytics and factors such as behavior or usage patterns. → [[application-access-continuous-authorization]]
**Claim 12 —** Application Threat Protections — maturity progresses from minimal integration with application workflows and general-purpose protections to advanced threat protections integrated into all application workflows with real-time visibility and content-aware protections against sophisticated attacks tailored to applications. → [[application-threat-protections-integrated]]
**Claim 13 —** Accessible Applications — maturity progresses from making mission-critical applications available only over private networks and VPNs to making all applicable applications available over open public networks to authorized users and devices. → [[accessible-applications-public-networks]]
**Claim 14 —** Secure Application Development & Deployment — maturity progresses from ad hoc development/testing/production environments with non-robust code deployment to immutable workloads where changes only occur through redeployment, with automated processes replacing administrator access to deployment environments. → [[secure-app-dev-immutable-workloads]]
**Claim 15 —** Application Security Testing — maturity progresses from primarily manual pre-deployment testing to integrated security testing throughout the SDLC with routine automated testing of deployed applications. → [[application-security-testing-sdlc]]
**Claim 16 —** Application Cross-Cutting Capabilities — progress from some performance/security monitoring of mission-critical apps with limited aggregation to continuous dynamic monitoring across all applications; from manual static application hosting to automated configurations continuously optimizing for security and performance; from manual enforcement policies to fully automated policies with dynamic updates through CI/CD. → [[application-cross-cutting-capabilities-summary]]
---

## 4. Data Pillar (§5.5)

> Data includes all structured and unstructured files and fragments that reside or have resided in federal systems, devices, networks, applications, databases, infrastructure, and backups (including on-premises and virtual environments) as well as associated metadata.

Agency data should be protected on devices, in applications, and on networks in accordance with federal requirements. Agencies should inventory, categorize, and label data; protect data at rest and in transit; deploy mechanisms to detect and stop data exfiltration. Data governance policies must ensure all data lifecycle security aspects are enforced across the enterprise.

**Related NIST 800-207 mapping:** Data is the ultimate resource being protected in the ZTA model. The Policy Engine evaluates access to data based on identity, device posture, and environmental context. NIST 800-207 tenet #1 states: "All data sources and computing services are considered resources."

**Claim 17 —** Data Inventory Management — maturity progresses from manual identification and inventory of some agency data to continuous inventory of all applicable agency data with robust data loss prevention strategies that dynamically block suspected data exfiltration. → [[data-inventory-management-continuous]]
**Claim 18 —** Data Categorization — maturity progresses from limited and ad hoc categorization to automated data categorization and labeling enterprise-wide with robust techniques, granular structured formats, and mechanisms to address all data types. → [[data-categorization-automated-labeling]]
**Claim 19 —** Data Availability — maturity progresses from primarily on-premises data stores with some off-site backups to dynamic methods optimizing data availability, including historical data, according to user and entity need. → [[data-availability-dynamic-optimization]]
**Claim 20 —** Data Access — maturity progresses from static access controls governing user/entity access to automated dynamic just-in-time and just-enough data access controls enterprise-wide with continuous review of permissions, considering identity, device risk, application, and data category. → [[data-access-jit-jea-controls]]
**Claim 21 —** Data Encryption — maturity progresses from encrypting minimal agency data with ad hoc key management to encrypting data in use where appropriate, enforcing least privilege for secure key management enterprise-wide, and applying encryption using up-to-date standards and cryptographic agility. → [[data-encryption-comprehensive]]
**Claim 22 —** Data Cross-Cutting Capabilities — progress from limited visibility with manual analysis to visibility across the full data lifecycle with robust predictive analytics; from manual ad hoc data lifecycle processes to maximum automation of data lifecycles and security policies; from ad hoc governance with manual implementation to unified data lifecycle policies dynamically enforced across the enterprise. → [[data-cross-cutting-capabilities-summary]]
---

## 5. Cross-Pillar Observations

**Claim 23 —** All four pillars share the same maturity trajectory — Traditional (manual, static, siloed) → Initial (automation begins) → Advanced (enterprise-wide, dynamic) → Optimal (fully automated, continuous, just-in-time, real-time risk analytics) — characterized by the same underlying shift from manual/static to automated/continuous across all functions. → [[cross-pillar-maturity-trajectory]]
**Claim 24 —** CISA's three cross-cutting capabilities — Visibility & Analytics, Automation & Orchestration, and Governance — become increasingly integrated across pillars as maturity increases, with the Optimal stage characterized by centralized dynamic monitoring, infrastructure-as-code, and fully automated enterprise-wide policies with continuous enforcement. → [[cross-cutting-capabilities-convergence]]
**Claim 25 —** Key tensions exist between pillar ideals and operational realities — Device pillar vs. BYOD constraints, network vs. application-level controls (defense-in-depth tradeoff), encryption vs. visibility (monitoring tradeoff), and immutable workloads vs. legacy systems (modernization gap) — and CISA acknowledges these tensions without fully resolving them. → [[pillar-ideals-vs-operational-realities]]
---

## 6. Cross-References

| Reference | Relationship |
|-----------|-------------|
| [[NIST 800-207 — Ch3 — Logical Components]] | Canonical ZTA component model (PE, PA, PEP) that these pillars operationalize |
| [[NSA ZT Device Pillar]] | Threat-informed device security guidance — stronger emphasis on attestation, firmware integrity, supply chain |
| [[NSA ZT Network Pillar]] | Threat-informed network security guidance — stronger emphasis on cryptographic isolation, traffic filtering |
| [[CISA ZTMM — Identity Pillar]] | The fifth pillar, documented separately; identity is the foundation for access decisions across all four pillars here |
| [[CISA Zero Trust Maturity Model — Full]] | Full-standards treatment of the complete ZTMM document |
