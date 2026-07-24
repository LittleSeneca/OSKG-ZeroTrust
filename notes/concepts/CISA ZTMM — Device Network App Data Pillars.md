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
---

# CISA ZTMM — Device, Network, App, and Data Pillars

Combined note covering CISA's Zero Trust Maturity Model v2 (April 2023) for the four remaining pillars beyond Identity: **Device**, **Network/Environment**, **Application Workload**, and **Data**. Each pillar is documented with its functions and maturity-stage descriptions across Traditional → Initial → Advanced → Optimal levels, plus the three cross-cutting capabilities (Visibility & Analytics, Automation & Orchestration, Governance) applied within each pillar.

The Identity pillar is documented separately in [[CISA ZTMM — Identity Pillar]].

---

## 1. Device Pillar (§5.2)

> A device refers to any asset (including its hardware, software, firmware, etc.) that can connect to a network, including servers, desktop and laptop machines, printers, mobile phones, IoT devices, networking equipment, and more.

**Related NIST 800-207 mapping:** The Device pillar maps to NIST 800-207's asset management and posture assessment components. See [[NIST 800-207 — Ch3 — Logical Components]] for the Policy Enforcement Point (PEP) role that devices play in access decisions.

**Related NSA guidance:** See [[NSA ZT Device Pillar]] for the threat-informed device security perspective — NSA emphasizes device attestation, firmware integrity, and supply chain provenance more heavily than CISA's maturity model.

### Claim 1: Device Policy Enforcement & Compliance Monitoring — maturity progresses from limited visibility and manual enforcement to continuous verification of compliance throughout device/virtual asset lifetimes, with automated methods for managing software, vulnerabilities, and patches integrated across all environments.

**Author's claim:** Agencies should secure all agency devices, manage risks of authorized non-agency devices (BYOD), and prevent unauthorized devices from accessing resources. (§5.2)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Limited, if any, visibility into device behavior; few methods of enforcing policies or managing software, configurations, or vulnerabilities. |
| **Initial** | Agency receives self-reported device characteristics (keys, tokens, users on the device) but has limited enforcement mechanisms. Preliminary process to approve software and push updates/configuration changes. |
| **Advanced** | Verified insights on device compliance upon initial access; enforces compliance for most devices and virtual assets. Automated methods to manage devices/virtual assets, approve software, identify vulnerabilities, and install patches. |
| **Optimal** | Continuous verification of compliance throughout device/virtual asset lifetime. Integrates device, software, configuration, and vulnerability management across all agency environments including virtual assets. |

**Confidence:** HIGH. Direct from the source document.

### Claim 2: Asset & Supply Chain Risk Management — maturity progresses from ad hoc, enterprise-blind tracking to comprehensive near-real-time visibility of all assets across vendors and service providers, with automated supply chain risk management and operations that tolerate supply chain failures.

**Author's claim:** Device management includes maintaining a dynamic inventory of all assets — hardware, software, firmware, configurations, and known vulnerabilities. (§5.2)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Does not track physical or virtual assets in an enterprise-wide, cross-vendor manner. Manages supply chain acquisition in ad hoc fashion with limited view of enterprise risks. |
| **Initial** | Tracks all physical and some virtual assets. Manages supply chain risks by establishing policies and control baselines according to federal recommendations (e.g., NIST SCRM framework). |
| **Advanced** | Develops comprehensive enterprise view of physical and virtual assets via automated processes functioning across multiple vendors — verifying acquisitions, tracking development cycles, providing third-party assessments. |
| **Optimal** | Comprehensive, at- or near-real-time view of all assets across vendors and service providers. Automates supply chain risk management where applicable; builds operations that tolerate supply chain failures; incorporates best practices. |

**Confidence:** HIGH. Direct from the source document.

### Claim 3: Device Resource Access — maturity progresses from requiring no device visibility for access decisions to considering real-time risk analytics within devices and virtual assets, integrating device posture with identity and environmental context.

**Author's claim:** Resource access decisions must incorporate device context. (§5.2)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Does not require visibility into devices or virtual assets used to access resources. |
| **Initial** | Requires some devices or virtual assets to report characteristics, then uses this information to approve resource access. |
| **Advanced** | Initial resource access considers verified device or virtual asset insights. |
| **Optimal** | Resource access considers real-time risk analytics within devices and virtual assets. |

**Confidence:** HIGH. Direct from the source document.

### Claim 4: Device Threat Protection — maturity progresses from manual deployment to some devices to centralized, unified threat protection with advanced capabilities for all devices and virtual assets, integrated with policy enforcement and compliance monitoring.

**Author's claim:** Threat protection capabilities must scale across all devices. (§5.2)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Manually deploys threat protection capabilities to some devices. |
| **Initial** | Some automated processes for deploying/updating threat protection to devices and virtual assets, with limited policy enforcement and compliance monitoring integration. |
| **Advanced** | Consolidates threat protection to centralized solutions for devices and virtual assets; integrates most capabilities with policy enforcement and compliance monitoring. |
| **Optimal** | Centralized threat protection solution(s) with advanced capabilities for all devices and virtual assets; unified approach for threat protection, policy enforcement, and compliance monitoring. |

**Confidence:** HIGH. Direct from the source document.

### Claim 5: Device Cross-Cutting Capabilities (Visibility & Analytics, Automation & Orchestration, Governance) — progress from manual, physically-labeled inventory to automated status collection of all network-connected devices correlated with identities, endpoint monitoring, and anomaly detection; from manual provisioning to fully automated lifecycle management; from ad hoc policies to automated enterprise-wide device lifecycle governance.

**Author's claim:** The three cross-cutting capabilities apply within the Device pillar. (§5.2)

**Evidence presented:**

**Visibility & Analytics:** Traditional → physically labeled inventory, limited software monitoring, regular review with manual analysis. Optimal → automated status collection of all network-connected devices and virtual assets, correlated with identities, endpoint monitoring, and anomaly detection to inform resource access.

**Automation & Orchestration:** Traditional → manual provisioning, configuration, and/or registration. Optimal → fully automated processes for provisioning, registering, monitoring, isolating, remediating, and deprovisioning devices and virtual assets.

**Governance:** Traditional → some policies for lifecycle of traditional/peripheral computing devices; relies on manual processes. Optimal → automated policies for lifecycle of all network-connected devices and virtual assets across the enterprise.

**Confidence:** HIGH. Direct from the source document.

---

## 2. Network/Environment Pillar (§5.3)

> A network refers to an open communications medium including agency internal networks, wireless networks, the Internet, cellular channels, and application-level channels used to transport messages.

ZTAs enable a shift away from perimeter-focused approaches. Agencies manage internal and external traffic flows, isolate hosts, enforce encryption, segment activity, and enhance enterprise-wide network visibility. Security controls are implemented closer to applications, data, and other resources — augmenting traditional network-based protections.

**Related NIST 800-207 mapping:** Maps to the control plane/data plane separation in NIST 800-207. The PEP and PA/PE operate on the network layer to enforce per-session access. See [[NIST 800-207 — Ch3 — Logical Components]].

**Related NSA guidance:** See [[NSA ZT Network Pillar]] for NSA's network segmentation, encryption, and traffic inspection requirements — NSA emphasizes cryptographic isolation and traffic filtering at a more granular level than CISA.

### Claim 6: Network Segmentation — maturity progresses from large perimeter/macro-segmentation with minimal intra-segment restrictions to fully distributed ingress/egress micro-perimeters with extensive micro-segmentation based on application profiles and dynamic JIT/JEA connectivity.

**Author's claim:** Network segmentation progresses from coarse perimeter to fine-grained application-profile-based micro-perimeters. (§5.3)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Defines network architecture using large perimeter/macro-segmentation with minimal restrictions on reachability within segments. May rely on multi-service interconnections (bulk VPN tunnels). |
| **Initial** | Begins deploying network architecture with isolation of critical workloads, constraining connectivity to least function principles, and transitioning toward service-specific interconnections. |
| **Advanced** | Expands deployment of endpoint and application profile isolation mechanisms; ingress/egress micro-perimeters; service-specific interconnections. |
| **Optimal** | Fully distributed ingress/egress micro-perimeters; extensive micro-segmentation based on application profiles; dynamic just-in-time and just-enough connectivity for service-specific interconnections. |

**Confidence:** HIGH. Direct from the source document.

### Claim 7: Network Traffic Management — maturity progresses from manually implemented static network rules with limited monitoring to dynamic rules and configurations that continuously evolve to meet application profile needs, reprioritizing applications based on mission criticality and risk.

**Author's claim:** Traffic management must become dynamic and risk-aware. (§5.3)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Manually implements static network rules and configurations at service provisioning; limited monitoring; manual audits of profile changes for mission-critical applications. |
| **Initial** | Establishes application profiles with distinct traffic management features; begins mapping all applications to profiles; expands static rules to all applications with periodic manual audits. |
| **Advanced** | Dynamic network rules and configurations for resource optimization, periodically adapted based on automated risk-aware and risk-responsive application profile assessments and monitoring. |
| **Optimal** | Dynamic network rules and configurations that continuously evolve to meet application profile needs and reprioritize applications based on mission criticality, risk, etc. |

**Confidence:** HIGH. Direct from the source document.

### Claim 8: Traffic Encryption — maturity progresses from encrypting minimal traffic with manual key management to encrypting all appropriate traffic, enforcing least privilege for secure key management enterprise-wide, and incorporating cryptographic agility as widely as possible.

**Author's claim:** Encryption must scale from minimal to comprehensive with cryptographic agility. (§5.3)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Encrypts minimal traffic; relies on manual or ad hoc processes to manage and secure encryption keys. |
| **Initial** | Begins encrypting all traffic to internal applications; prefers encryption for external application traffic; formalizes key management policies; secures server/service encryption keys. |
| **Advanced** | Ensures encryption for all applicable internal and external traffic protocols; manages issuance and rotation of keys and certificates; begins incorporating cryptographic agility best practices. |
| **Optimal** | Continues encrypting traffic as appropriate; enforces least privilege for secure key management enterprise-wide; incorporates cryptographic agility as widely as possible. |

**Confidence:** HIGH. Direct from the source document.

### Claim 9: Network Resilience — maturity progresses from case-by-case network configuration matching individual application availability demands with limited resilience for non-mission-critical workloads to holistic delivery and awareness adapting to changes in availability demands for all workloads with proportionate resilience.

**Author's claim:** Network resilience must scale from case-by-case to holistic. (§5.3)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Configures network capabilities case-by-case to match individual application availability demands; limited resilience mechanisms for non-mission-critical workloads. |
| **Initial** | Begins configuring network capabilities to manage availability demands for additional applications; expands resilience mechanisms for non-mission-critical workloads. |
| **Advanced** | Network capabilities dynamically manage availability demands and resilience mechanisms for the majority of applications. |
| **Optimal** | Holistic delivery and awareness in adapting to changes in availability demands for all workloads; proportionate resilience. |

**Confidence:** HIGH. Direct from the source document.

### Claim 10: Network Cross-Cutting Capabilities — progress from boundary-focused manual monitoring to enterprise-wide situational awareness with advanced automated telemetry correlation; from manual configuration management to infrastructure-as-code with automated change management; from static perimeter-focused policies to enterprise-wide policies enabling tailored local controls with dynamic updates.

**Author's claim:** Cross-cutting capabilities within the Network pillar. (§5.3)

**Evidence presented:**

**Visibility & Analytics:** Traditional → limited boundary-focused network monitoring. Optimal → visibility into communication across all agency networks and environments; enterprise-wide situational awareness; advanced monitoring automating telemetry correlation across all detection sources.

**Automation & Orchestration:** Traditional → manual processes for configuration and resource lifecycle. Optimal → networks defined using infrastructure-as-code managed by automated change management; automated initiation and expiration aligned with changing needs.

**Governance:** Traditional → static network policies with perimeter-protection focus. Optimal → enterprise-wide network policies enabling tailored, local controls; dynamic updates; secure external connections based on application and user workflows.

**Confidence:** HIGH. Direct from the source document.

---

## 3. Application Workload Pillar (§5.4)

> Applications and workloads include agency systems, computer programs, and services that execute on-premises, on mobile devices, and in cloud environments.

Agencies should manage and secure deployed applications and ensure secure application delivery. Granular access controls and integrated threat protections offer enhanced situational awareness. OMB M-22-09 directs agencies to make applications available over public networks to authorized users. Best practices for DevSecOps, CI/CD, and immutable workloads should be adopted.

**Related NIST 800-207 mapping:** Maps to the Policy Decision Point (PDP) and PEP functions in NIST 800-207 — applications are the resources being accessed, and the access decision considers application-specific context. See [[NIST 800-207 — Ch3 — Logical Components]].

### Claim 11: Application Access — maturity progresses from authorization based primarily on local authorization and static attributes to continuous authorization incorporating real-time risk analytics and factors such as behavior or usage patterns.

**Author's claim:** Access authorization must evolve from static to continuous, context-aware. (§5.4)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Authorizes access primarily based on local authorization and static attributes. |
| **Initial** | Begins implementing access authorization incorporating contextual information (identity, device compliance, and/or other attributes) per request with expiration. |
| **Advanced** | Automates application access decisions with expanded contextual information and enforced expiration conditions adhering to least privilege principles. |
| **Optimal** | Continuously authorizes application access, incorporating real-time risk analytics and factors such as behavior or usage patterns. |

**Confidence:** HIGH. Direct from the source document.

### Claim 12: Application Threat Protections — maturity progresses from minimal integration with application workflows and general-purpose protections to advanced threat protections integrated into all application workflows with real-time visibility and content-aware protections against sophisticated attacks tailored to applications.

**Author's claim:** Threat protections must integrate deeply into application workflows. (§5.4)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Threat protections have minimal integration with application workflows; applies general-purpose protections for known threats. |
| **Initial** | Integrates threat protections into mission-critical application workflows; applies protections against known threats and some application-specific threats. |
| **Advanced** | Integrates threat protections into all application workflows; protects against some application-specific and targeted threats. |
| **Optimal** | Advanced threat protections integrated into all application workflows; real-time visibility and content-aware protections against sophisticated attacks tailored to applications. |

**Confidence:** HIGH. Direct from the source document.

### Claim 13: Accessible Applications — maturity progresses from making mission-critical applications available only over private networks and VPNs to making all applicable applications available over open public networks to authorized users and devices.

**Author's claim:** Applications should become accessible over public networks rather than requiring VPNs. (§5.4)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Makes some mission-critical applications available only over private networks and protected public network connections (e.g., VPN) with monitoring. |
| **Initial** | Makes some applicable mission-critical applications available over open public networks to authorized users via brokered connections. |
| **Advanced** | Makes most applicable mission-critical applications available over open public network connections to authorized users. |
| **Optimal** | Makes all applicable applications available over open public networks to authorized users and devices, where appropriate. |

**Confidence:** HIGH. This directly aligns with OMB M-22-09's directive.

### Claim 14: Secure Application Development & Deployment — maturity progresses from ad hoc development/testing/production environments with non-robust code deployment to immutable workloads where changes only occur through redeployment, with automated processes replacing administrator access to deployment environments.

**Author's claim:** DevSecOps maturity is integral to the Application pillar. (§5.4)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Ad hoc development, testing, and production environments with non-robust code deployment mechanisms. |
| **Initial** | Provides infrastructure for development, testing, and production environments (including automation); formal code deployment through CI/CD pipelines; requisite access controls supporting least privilege. |
| **Advanced** | Distinct, coordinated teams for development, security, and operations; removes developer access to production environment for code deployment. |
| **Optimal** | Leverages immutable workloads where feasible; only allows changes through redeployment; removes administrator access to deployment environments in favor of automated processes for code deployment. |

**Confidence:** HIGH. Direct from the source document.

### Claim 15: Application Security Testing — maturity progresses from primarily manual pre-deployment testing to integrated security testing throughout the SDLC with routine automated testing of deployed applications.

**Author's claim:** Security testing must be integrated throughout the SDLC. (§5.4)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Performs application security testing prior to deployment, primarily via manual testing methods. |
| **Initial** | Begins using static and dynamic testing methods; includes manual expert analysis prior to application deployment. |
| **Advanced** | Integrates application security testing into development and deployment process; includes periodic dynamic testing methods. |
| **Optimal** | Integrates application security testing throughout the software development lifecycle across the enterprise; routine automated testing of deployed applications. |

**Confidence:** HIGH. Direct from the source document.

### Claim 16: Application Cross-Cutting Capabilities — progress from some performance/security monitoring of mission-critical apps with limited aggregation to continuous dynamic monitoring across all applications; from manual static application hosting to automated configurations continuously optimizing for security and performance; from manual enforcement policies to fully automated policies with dynamic updates through CI/CD.

**Author's claim:** Cross-cutting capabilities within the Application pillar. (§5.4)

**Evidence presented:**

**Visibility & Analytics:** Traditional → some performance and security monitoring of mission-critical applications. Optimal → continuous and dynamic monitoring across all applications to maintain enterprise-wide comprehensive visibility.

**Automation & Orchestration:** Traditional → manually establishes static application hosting location and access at provisioning. Optimal → automates application configurations to continuously optimize for security and performance.

**Governance:** Traditional → relies primarily on manual enforcement policies. Optimal → fully automates policies governing applications development and deployment; dynamic updates through the CI/CD pipeline.

**Confidence:** HIGH. Direct from the source document.

---

## 4. Data Pillar (§5.5)

> Data includes all structured and unstructured files and fragments that reside or have resided in federal systems, devices, networks, applications, databases, infrastructure, and backups (including on-premises and virtual environments) as well as associated metadata.

Agency data should be protected on devices, in applications, and on networks in accordance with federal requirements. Agencies should inventory, categorize, and label data; protect data at rest and in transit; deploy mechanisms to detect and stop data exfiltration. Data governance policies must ensure all data lifecycle security aspects are enforced across the enterprise.

**Related NIST 800-207 mapping:** Data is the ultimate resource being protected in the ZTA model. The Policy Engine evaluates access to data based on identity, device posture, and environmental context. NIST 800-207 tenet #1 states: "All data sources and computing services are considered resources."

### Claim 17: Data Inventory Management — maturity progresses from manual identification and inventory of some agency data to continuous inventory of all applicable agency data with robust data loss prevention strategies that dynamically block suspected data exfiltration.

**Author's claim:** Data inventory is foundational — you can't protect what you don't know exists. (§5.5)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Manually identifies and inventories some agency data (e.g., mission-critical data). |
| **Initial** | Begins automating data inventory processes for on-premises and cloud environments, covering most agency data; begins incorporating protections against data loss. |
| **Advanced** | Automates data inventory and tracking enterprise-wide, covering all applicable agency data; data loss prevention strategies based on static attributes and/or labels. |
| **Optimal** | Continuously inventories all applicable agency data; robust data loss prevention strategies that dynamically block suspected data exfiltration. |

**Confidence:** HIGH. Direct from the source document.

### Claim 18: Data Categorization — maturity progresses from limited and ad hoc categorization to automated data categorization and labeling enterprise-wide with robust techniques, granular structured formats, and mechanisms to address all data types.

**Author's claim:** Data categorization must scale from ad hoc to automated, enterprise-wide. (§5.5)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Limited and ad hoc data categorization capabilities. |
| **Initial** | Begins implementing a data categorization strategy with defined labels and manual enforcement mechanisms. |
| **Advanced** | Automates some data categorization and labeling in a consistent, tiered, targeted manner with simple structured formats and regular review. |
| **Optimal** | Automates data categorization and labeling enterprise-wide with robust techniques; granular, structured formats; mechanisms to address all data types. |

**Confidence:** HIGH. Direct from the source document.

### Claim 19: Data Availability — maturity progresses from primarily on-premises data stores with some off-site backups to dynamic methods optimizing data availability, including historical data, according to user and entity need.

**Author's claim:** Data availability must move from static on-premises to dynamic, need-based. (§5.5)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Primarily makes data available from on-premises data stores with some off-site backups. |
| **Initial** | Makes some data available from redundant, highly available data stores (e.g., cloud); maintains off-site backups for on-premises data. |
| **Advanced** | Primarily makes data available from redundant, highly available data stores; ensures access to historical data. |
| **Optimal** | Uses dynamic methods to optimize data availability, including historical data, according to user and entity need. |

**Confidence:** HIGH. Direct from the source document.

### Claim 20: Data Access — maturity progresses from static access controls governing user/entity access to automated dynamic just-in-time and just-enough data access controls enterprise-wide with continuous review of permissions, considering identity, device risk, application, and data category.

**Author's claim:** Data access controls must become dynamic, context-aware, and JIT/JEA. (§5.5)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Governs user and entity access (read, write, copy, grant others access) through static access controls. |
| **Initial** | Begins deploying automated data access controls incorporating elements of least privilege across the enterprise. |
| **Advanced** | Automates data access controls considering identity, device risk, application, data category, etc.; time-limited where applicable. |
| **Optimal** | Automates dynamic just-in-time and just-enough data access controls enterprise-wide with continuous review of permissions. |

**Confidence:** HIGH. Direct from the source document.

### Claim 21: Data Encryption — maturity progresses from encrypting minimal agency data with ad hoc key management to encrypting data in use where appropriate, enforcing least privilege for secure key management enterprise-wide, and applying encryption using up-to-date standards and cryptographic agility.

**Author's claim:** Encryption must extend from minimal to comprehensive, including data in use. (§5.5)

**Evidence presented:**

| Stage | Description |
|-------|-------------|
| **Traditional** | Encrypts minimal agency data at rest and in transit; relies on manual or ad hoc processes to manage and secure encryption keys. |
| **Initial** | Encrypts all data in transit; where feasible, encrypts data at rest (mission-critical data, data stored in external environments); begins formalizing key management policies and securing encryption keys. |
| **Advanced** | Encrypts all data at rest and in transit to maximum extent possible; begins incorporating cryptographic agility; protects encryption keys (secrets not hard coded, regular rotation). |
| **Optimal** | Encrypts data in use where appropriate; enforces least privilege for secure key management enterprise-wide; applies encryption using up-to-date standards and cryptographic agility to the extent possible. |

**Confidence:** HIGH. Direct from the source document.

### Claim 22: Data Cross-Cutting Capabilities — progress from limited visibility with manual analysis to visibility across the full data lifecycle with robust predictive analytics; from manual ad hoc data lifecycle processes to maximum automation of data lifecycles and security policies; from ad hoc governance with manual implementation to unified data lifecycle policies dynamically enforced across the enterprise.

**Author's claim:** Cross-cutting capabilities within the Data pillar. (§5.5)

**Evidence presented:**

**Visibility & Analytics:** Traditional → limited visibility into data including location, access, and usage; analysis primarily manual. Optimal → visibility across full data lifecycle; robust analytics including predictive analytics; comprehensive views of agency data and continuous security posture assessment.

**Automation & Orchestration:** Traditional → implements data lifecycle and security policies through manual, potentially ad hoc, processes. Optimal → automates, to the maximum extent possible, data lifecycles and security policies for all agency data across the enterprise.

**Governance:** Traditional → ad hoc data governance policies with manual implementation. Optimal → data lifecycle policies are unified to the maximum extent possible and dynamically enforced across the enterprise.

**Confidence:** HIGH. Direct from the source document.

---

## 5. Cross-Pillar Observations

### Claim 23: All four pillars share the same maturity trajectory — Traditional (manual, static, siloed) → Initial (automation begins) → Advanced (enterprise-wide, dynamic) → Optimal (fully automated, continuous, just-in-time, real-time risk analytics) — characterized by the same underlying shift from manual/static to automated/continuous across all functions.

**Author's claim:** This is a synthesis observation by this note's author.

**Evidence presented (common progression across pillars):**

1. **Traditional:** Manual processes, static configurations, siloed visibility, ad hoc governance, limited automation.
2. **Initial:** Automation begins (scripts, tools), basic integration across pillars, formalized policies, some contextual information in access decisions.
3. **Advanced:** Enterprise-wide automated processes, cross-pillar coordination, centralized visibility, dynamic policy adaptation, cryptographic agility begins.
4. **Optimal:** Fully automated, continuous, just-in-time, enterprise-wide; real-time risk analytics; immutable workloads; cryptographic agility; dynamic enforcement.

**Confidence:** HIGH. The pattern is directly observable across all pillar function tables in the source document.

### Claim 24: CISA's three cross-cutting capabilities — Visibility & Analytics, Automation & Orchestration, and Governance — become increasingly integrated across pillars as maturity increases, with the Optimal stage characterized by centralized dynamic monitoring, infrastructure-as-code, and fully automated enterprise-wide policies with continuous enforcement.

**Author's claim:** The cross-cutting capabilities operate within each pillar and converge at higher maturity levels. (§5.1–5.5)

**Evidence presented (cross-pillar capability summary):**

| Capability | Traditional | Optimal |
|------------|-------------|---------|
| Visibility & Analytics | Manual log collection, limited analysis | Comprehensive visibility via centralized dynamic monitoring, advanced analysis, predictive analytics |
| Automation & Orchestration | Static, manual processes | Dynamic response to enterprise-wide changing requirements; infrastructure-as-code |
| Governance | Ad hoc policies, manual enforcement | Fully automated enterprise-wide policies with continuous enforcement, dynamic updates |

**Confidence:** HIGH. Direct from the source document.

### Claim 25: Key tensions exist between pillar ideals and operational realities — Device pillar vs. BYOD constraints, network vs. application-level controls (defense-in-depth tradeoff), encryption vs. visibility (monitoring tradeoff), and immutable workloads vs. legacy systems (modernization gap) — and CISA acknowledges these tensions without fully resolving them.

**Author's claim:** This is a synthesis observation by this note's author identifying tensions across pillars.

**Evidence presented (key tensions):**

- **Device vs. BYOD:** CISA acknowledges that BYOD policies reduce visibility and control options, creating a tension between the Device pillar's ideal state and practical workforce realities.
- **Network vs. Application-level controls:** Optimal ZTA pushes security controls *closer to applications and data*, reducing reliance on network-layer protections — but network segmentation remains critical for defense-in-depth.
- **Encryption vs. Visibility:** Encrypting all traffic (Network pillar Optimal) can conflict with traffic inspection needs for threat detection. Agencies must balance cryptographic protections with monitoring requirements.
- **Immutable workloads vs. legacy systems:** The Application pillar's Optimal state (immutable workloads, automated CI/CD) assumes modern cloud-native architectures, which many federal legacy systems cannot support.

**Confidence:** MEDIUM. These tensions are visible in the source document but are this note's analytical framing — CISA acknowledges the tensions implicitly through stage descriptions rather than naming them explicitly.

---

## 6. Cross-References

| Reference | Relationship |
|-----------|-------------|
| [[NIST 800-207 — Ch3 — Logical Components]] | Canonical ZTA component model (PE, PA, PEP) that these pillars operationalize |
| [[NSA ZT Device Pillar]] | Threat-informed device security guidance — stronger emphasis on attestation, firmware integrity, supply chain |
| [[NSA ZT Network Pillar]] | Threat-informed network security guidance — stronger emphasis on cryptographic isolation, traffic filtering |
| [[CISA ZTMM — Identity Pillar]] | The fifth pillar, documented separately; identity is the foundation for access decisions across all four pillars here |
| [[CISA Zero Trust Maturity Model — Full]] | Full-standards treatment of the complete ZTMM document |
