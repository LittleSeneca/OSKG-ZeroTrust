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

Agencies should secure all agency devices, manage risks of authorized non-agency devices (BYOD), and prevent unauthorized devices from accessing resources. Device management includes maintaining a dynamic inventory of all assets — hardware, software, firmware, configurations, and known vulnerabilities.

**Related NIST 800-207 mapping:** The Device pillar maps to NIST 800-207's asset management and posture assessment components. See [[NIST 800-207 — Ch3 — Logical Components]] for the Policy Enforcement Point (PEP) role that devices play in access decisions.

**Related NSA guidance:** See [[NSA ZT Device Pillar]] for the threat-informed device security perspective — NSA emphasizes device attestation, firmware integrity, and supply chain provenance more heavily than CISA's maturity model.

### 1.1 Policy Enforcement & Compliance Monitoring

| Stage | Description |
|-------|-------------|
| **Traditional** | Limited, if any, visibility into device behavior; few methods of enforcing policies or managing software, configurations, or vulnerabilities. |
| **Initial** | Agency receives self-reported device characteristics (keys, tokens, users on the device) but has limited enforcement mechanisms. Preliminary process to approve software and push updates/configuration changes. |
| **Advanced** | Verified insights on device compliance upon initial access; enforces compliance for most devices and virtual assets. Automated methods to manage devices/virtual assets, approve software, identify vulnerabilities, and install patches. |
| **Optimal** | Continuous verification of compliance throughout device/virtual asset lifetime. Integrates device, software, configuration, and vulnerability management across all agency environments including virtual assets. |

### 1.2 Asset & Supply Chain Risk Management

| Stage | Description |
|-------|-------------|
| **Traditional** | Does not track physical or virtual assets in an enterprise-wide, cross-vendor manner. Manages supply chain acquisition in ad hoc fashion with limited view of enterprise risks. |
| **Initial** | Tracks all physical and some virtual assets. Manages supply chain risks by establishing policies and control baselines according to federal recommendations (e.g., NIST SCRM framework). |
| **Advanced** | Develops comprehensive enterprise view of physical and virtual assets via automated processes functioning across multiple vendors — verifying acquisitions, tracking development cycles, providing third-party assessments. |
| **Optimal** | Comprehensive, at- or near-real-time view of all assets across vendors and service providers. Automates supply chain risk management where applicable; builds operations that tolerate supply chain failures; incorporates best practices. |

### 1.3 Resource Access

| Stage | Description |
|-------|-------------|
| **Traditional** | Does not require visibility into devices or virtual assets used to access resources. |
| **Initial** | Requires some devices or virtual assets to report characteristics, then uses this information to approve resource access. |
| **Advanced** | Initial resource access considers verified device or virtual asset insights. |
| **Optimal** | Resource access considers real-time risk analytics within devices and virtual assets. |

### 1.4 Device Threat Protection

| Stage | Description |
|-------|-------------|
| **Traditional** | Manually deploys threat protection capabilities to some devices. |
| **Initial** | Some automated processes for deploying/updating threat protection to devices and virtual assets, with limited policy enforcement and compliance monitoring integration. |
| **Advanced** | Consolidates threat protection to centralized solutions for devices and virtual assets; integrates most capabilities with policy enforcement and compliance monitoring. |
| **Optimal** | Centralized threat protection solution(s) with advanced capabilities for all devices and virtual assets; unified approach for threat protection, policy enforcement, and compliance monitoring. |

### 1.5 Cross-Cutting Capabilities (Device)

**Visibility & Analytics:**
| Stage | Description |
|-------|-------------|
| Traditional | Physically labeled inventory, limited software monitoring, regular review with manual analysis. |
| Initial | Digital identifiers alongside manual inventory; endpoint monitoring when available. Some devices/virtual assets under automated analysis for anomaly detection based on risk. |
| Advanced | Automated inventory collection (endpoint monitoring on all standard user devices — desktops, laptops, phones, tablets — and virtual assets) and anomaly detection to detect unauthorized devices. |
| Optimal | Automated status collection of all network-connected devices and virtual assets, correlated with identities, endpoint monitoring, and anomaly detection to inform resource access. Tracks provisioning/deprovisioning patterns for anomalies. |

**Automation & Orchestration:**
| Stage | Description |
|-------|-------------|
| Traditional | Manual provisioning, configuration, and/or registration of devices within the enterprise. |
| Initial | Begins using tools and scripts to automate provisioning, configuration, registration, and deprovisioning for devices and virtual assets. |
| Advanced | Implemented monitoring and enforcement mechanisms to identify and manually disconnect/isolate non-compliant devices and virtual assets. |
| Optimal | Fully automated processes for provisioning, registering, monitoring, isolating, remediating, and deprovisioning devices and virtual assets. |

**Governance:**
| Stage | Description |
|-------|-------------|
| Traditional | Some policies for lifecycle of traditional/peripheral computing devices; relies on manual processes to maintain (update, patch, sanitize). |
| Initial | Policies for procurement of new devices, lifecycle of non-traditional computing devices and virtual assets, and regular monitoring/scanning. |
| Advanced | Enterprise-wide policies for device/virtual asset lifecycle including enumeration and accountability, with some automated enforcement. |
| Optimal | Automated policies for lifecycle of all network-connected devices and virtual assets across the enterprise. |

---

## 2. Network/Environment Pillar (§5.3)

> A network refers to an open communications medium including agency internal networks, wireless networks, the Internet, cellular channels, and application-level channels used to transport messages.

ZTAs enable a shift away from perimeter-focused approaches. Agencies manage internal and external traffic flows, isolate hosts, enforce encryption, segment activity, and enhance enterprise-wide network visibility. Security controls are implemented closer to applications, data, and other resources — augmenting traditional network-based protections.

**Related NIST 800-207 mapping:** Maps to the control plane/data plane separation in NIST 800-207. The PEP and PA/PE operate on the network layer to enforce per-session access. See [[NIST 800-207 — Ch3 — Logical Components]].

**Related NSA guidance:** See [[NSA ZT Network Pillar]] for NSA's network segmentation, encryption, and traffic inspection requirements — NSA emphasizes cryptographic isolation and traffic filtering at a more granular level than CISA.

### 2.1 Network Segmentation

| Stage | Description |
|-------|-------------|
| **Traditional** | Defines network architecture using large perimeter/macro-segmentation with minimal restrictions on reachability within segments. May rely on multi-service interconnections (bulk VPN tunnels). |
| **Initial** | Begins deploying network architecture with isolation of critical workloads, constraining connectivity to least function principles, and transitioning toward service-specific interconnections. |
| **Advanced** | Expands deployment of endpoint and application profile isolation mechanisms; ingress/egress micro-perimeters; service-specific interconnections. |
| **Optimal** | Fully distributed ingress/egress micro-perimeters; extensive micro-segmentation based on application profiles; dynamic just-in-time and just-enough connectivity for service-specific interconnections. |

### 2.2 Network Traffic Management

| Stage | Description |
|-------|-------------|
| **Traditional** | Manually implements static network rules and configurations at service provisioning; limited monitoring (e.g., performance monitoring or anomaly detection); manual audits of profile changes for mission-critical applications. |
| **Initial** | Establishes application profiles with distinct traffic management features; begins mapping all applications to profiles; expands static rules to all applications with periodic manual audits of profile assessments. |
| **Advanced** | Dynamic network rules and configurations for resource optimization, periodically adapted based on automated risk-aware and risk-responsive application profile assessments and monitoring. |
| **Optimal** | Dynamic network rules and configurations that continuously evolve to meet application profile needs and reprioritize applications based on mission criticality, risk, etc. |

### 2.3 Traffic Encryption

| Stage | Description |
|-------|-------------|
| **Traditional** | Encrypts minimal traffic; relies on manual or ad hoc processes to manage and secure encryption keys. |
| **Initial** | Begins encrypting all traffic to internal applications; prefers encryption for external application traffic; formalizes key management policies; secures server/service encryption keys. |
| **Advanced** | Ensures encryption for all applicable internal and external traffic protocols; manages issuance and rotation of keys and certificates; begins incorporating cryptographic agility best practices. |
| **Optimal** | Continues encrypting traffic as appropriate; enforces least privilege for secure key management enterprise-wide; incorporates cryptographic agility as widely as possible. |

### 2.4 Network Resilience

| Stage | Description |
|-------|-------------|
| **Traditional** | Configures network capabilities case-by-case to match individual application availability demands; limited resilience mechanisms for non-mission-critical workloads. |
| **Initial** | Begins configuring network capabilities to manage availability demands for additional applications; expands resilience mechanisms for non-mission-critical workloads. |
| **Advanced** | Network capabilities dynamically manage availability demands and resilience mechanisms for the majority of applications. |
| **Optimal** | Holistic delivery and awareness in adapting to changes in availability demands for all workloads; proportionate resilience. |

### 2.5 Cross-Cutting Capabilities (Network)

**Visibility & Analytics:**
| Stage | Description |
|-------|-------------|
| Traditional | Limited boundary-focused network monitoring; minimal analysis to start developing centralized situational awareness. |
| Initial | Network monitoring based on known indicators of compromise (including network enumeration); develops situational awareness in each environment; begins correlating telemetry across traffic types and environments for analysis and threat hunting. |
| Advanced | Anomaly-based network detection; situational awareness across all environments; correlates telemetry from multiple sources; incorporates automated processes for robust threat hunting. |
| Optimal | Visibility into communication across all agency networks and environments; enterprise-wide situational awareness; advanced monitoring automating telemetry correlation across all detection sources. |

**Automation & Orchestration:**
| Stage | Description |
|-------|-------------|
| Traditional | Manual processes to manage configuration and resource lifecycle; periodic integration of policy requirements and situational awareness. |
| Initial | Begins using automated methods for configuration and resource lifecycle management for some networks/environments; ensures all resources have defined lifetimes based on policies and telemetry. |
| Advanced | Automated change management (e.g., CI/CD) for configuration and resource lifecycle of all networks/environments; responds to and enforces policies and protections against perceived risks. |
| Optimal | Networks and environments defined using infrastructure-as-code managed by automated change management; automated initiation and expiration aligned with changing needs. |

**Governance:**
| Stage | Description |
|-------|-------------|
| Traditional | Static network policies (access, protocols, segmentation, alerts, remediation) with perimeter-protection focus. |
| Initial | Defines and begins implementing policies tailored to individual network segments and resources; inherits corporate-wide rules as appropriate. |
| Advanced | Incorporates automation in implementing tailored policies; facilitates transition from perimeter-focused protections. |
| Optimal | Enterprise-wide network policies enabling tailored, local controls; dynamic updates; secure external connections based on application and user workflows. |

---

## 3. Application Workload Pillar (§5.4)

> Applications and workloads include agency systems, computer programs, and services that execute on-premises, on mobile devices, and in cloud environments.

Agencies should manage and secure deployed applications and ensure secure application delivery. Granular access controls and integrated threat protections offer enhanced situational awareness. OMB M-22-09 directs agencies to make applications available over public networks to authorized users. Best practices for DevSecOps, CI/CD, and immutable workloads should be adopted.

**Related NIST 800-207 mapping:** Maps to the Policy Decision Point (PDP) and PEP functions in NIST 800-207 — applications are the resources being accessed, and the access decision considers application-specific context. See [[NIST 800-207 — Ch3 — Logical Components]].

### 3.1 Application Access

| Stage | Description |
|-------|-------------|
| **Traditional** | Authorizes access primarily based on local authorization and static attributes. |
| **Initial** | Begins implementing access authorization incorporating contextual information (identity, device compliance, and/or other attributes) per request with expiration. |
| **Advanced** | Automates application access decisions with expanded contextual information and enforced expiration conditions adhering to least privilege principles. |
| **Optimal** | Continuously authorizes application access, incorporating real-time risk analytics and factors such as behavior or usage patterns. |

### 3.2 Application Threat Protections

| Stage | Description |
|-------|-------------|
| **Traditional** | Threat protections have minimal integration with application workflows; applies general-purpose protections for known threats. |
| **Initial** | Integrates threat protections into mission-critical application workflows; applies protections against known threats and some application-specific threats. |
| **Advanced** | Integrates threat protections into all application workflows; protects against some application-specific and targeted threats. |
| **Optimal** | Advanced threat protections integrated into all application workflows; real-time visibility and content-aware protections against sophisticated attacks tailored to applications. |

### 3.3 Accessible Applications

| Stage | Description |
|-------|-------------|
| **Traditional** | Makes some mission-critical applications available only over private networks and protected public network connections (e.g., VPN) with monitoring. |
| **Initial** | Makes some applicable mission-critical applications available over open public networks to authorized users via brokered connections. |
| **Advanced** | Makes most applicable mission-critical applications available over open public network connections to authorized users. |
| **Optimal** | Makes all applicable applications available over open public networks to authorized users and devices, where appropriate. |

### 3.4 Secure Application Development & Deployment Workflow

| Stage | Description |
|-------|-------------|
| **Traditional** | Ad hoc development, testing, and production environments with non-robust code deployment mechanisms. |
| **Initial** | Provides infrastructure for development, testing, and production environments (including automation); formal code deployment through CI/CD pipelines; requisite access controls supporting least privilege. |
| **Advanced** | Distinct, coordinated teams for development, security, and operations; removes developer access to production environment for code deployment. |
| **Optimal** | Leverages immutable workloads where feasible; only allows changes through redeployment; removes administrator access to deployment environments in favor of automated processes for code deployment. |

### 3.5 Application Security Testing

| Stage | Description |
|-------|-------------|
| **Traditional** | Performs application security testing prior to deployment, primarily via manual testing methods. |
| **Initial** | Begins using static and dynamic testing methods; includes manual expert analysis prior to application deployment. |
| **Advanced** | Integrates application security testing into development and deployment process; includes periodic dynamic testing methods. |
| **Optimal** | Integrates application security testing throughout the software development lifecycle across the enterprise; routine automated testing of deployed applications. |

### 3.6 Cross-Cutting Capabilities (Application)

**Visibility & Analytics:**
| Stage | Description |
|-------|-------------|
| Traditional | Some performance and security monitoring of mission-critical applications with limited aggregation and analytics. |
| Initial | Begins automating application profile (state, health, performance) and security monitoring for improved log collection, aggregation, and analytics. |
| Advanced | Automates profile and security monitoring for most applications with heuristics to identify application-specific and enterprise-wide trends; refines processes to address gaps in visibility. |
| Optimal | Continuous and dynamic monitoring across all applications to maintain enterprise-wide comprehensive visibility. |

**Automation & Orchestration:**
| Stage | Description |
|-------|-------------|
| Traditional | Manually establishes static application hosting location and access at provisioning with limited maintenance and review. |
| Initial | Periodically modifies application configurations (location and access) to meet relevant security and performance goals. |
| Advanced | Automates application configurations to respond to operational and environmental changes. |
| Optimal | Automates application configurations to continuously optimize for security and performance. |

**Governance:**
| Stage | Description |
|-------|-------------|
| Traditional | Relies primarily on manual enforcement policies for application access, development, deployment, software asset management, security testing and evaluation (ST&E), patching, and tracking software dependencies. |
| Initial | Begins automating policy enforcement for development (including access to dev infrastructure), deployment, software asset management, ST&E, patching, and tracking dependencies (e.g., SBOM). |
| Advanced | Tiered, tailored policies enterprise-wide for applications and all aspects of development/deployment lifecycles; leverages automation where possible. |
| Optimal | Fully automates policies governing applications development and deployment; dynamic updates through the CI/CD pipeline. |

---

## 4. Data Pillar (§5.5)

> Data includes all structured and unstructured files and fragments that reside or have resided in federal systems, devices, networks, applications, databases, infrastructure, and backups (including on-premises and virtual environments) as well as associated metadata.

Agency data should be protected on devices, in applications, and on networks in accordance with federal requirements. Agencies should inventory, categorize, and label data; protect data at rest and in transit; deploy mechanisms to detect and stop data exfiltration. Data governance policies must ensure all data lifecycle security aspects are enforced across the enterprise.

**Related NIST 800-207 mapping:** Data is the ultimate resource being protected in the ZTA model. The Policy Engine evaluates access to data based on identity, device posture, and environmental context. NIST 800-207 tenet #1 states: "All data sources and computing services are considered resources." See [[NIST 800-207 — Ch3 — Logical Components]].

### 4.1 Data Inventory Management

| Stage | Description |
|-------|-------------|
| **Traditional** | Manually identifies and inventories some agency data (e.g., mission-critical data). |
| **Initial** | Begins automating data inventory processes for on-premises and cloud environments, covering most agency data; begins incorporating protections against data loss. |
| **Advanced** | Automates data inventory and tracking enterprise-wide, covering all applicable agency data; data loss prevention strategies based on static attributes and/or labels. |
| **Optimal** | Continuously inventories all applicable agency data; robust data loss prevention strategies that dynamically block suspected data exfiltration. |

### 4.2 Data Categorization

| Stage | Description |
|-------|-------------|
| **Traditional** | Limited and ad hoc data categorization capabilities. |
| **Initial** | Begins implementing a data categorization strategy with defined labels and manual enforcement mechanisms. |
| **Advanced** | Automates some data categorization and labeling in a consistent, tiered, targeted manner with simple structured formats and regular review. |
| **Optimal** | Automates data categorization and labeling enterprise-wide with robust techniques; granular, structured formats; mechanisms to address all data types. |

### 4.3 Data Availability

| Stage | Description |
|-------|-------------|
| **Traditional** | Primarily makes data available from on-premises data stores with some off-site backups. |
| **Initial** | Makes some data available from redundant, highly available data stores (e.g., cloud); maintains off-site backups for on-premises data. |
| **Advanced** | Primarily makes data available from redundant, highly available data stores; ensures access to historical data. |
| **Optimal** | Uses dynamic methods to optimize data availability, including historical data, according to user and entity need. |

### 4.4 Data Access

| Stage | Description |
|-------|-------------|
| **Traditional** | Governs user and entity access (read, write, copy, grant others access) through static access controls. |
| **Initial** | Begins deploying automated data access controls incorporating elements of least privilege across the enterprise. |
| **Advanced** | Automates data access controls considering identity, device risk, application, data category, etc.; time-limited where applicable. |
| **Optimal** | Automates dynamic just-in-time and just-enough data access controls enterprise-wide with continuous review of permissions. |

### 4.5 Data Encryption

| Stage | Description |
|-------|-------------|
| **Traditional** | Encrypts minimal agency data at rest and in transit; relies on manual or ad hoc processes to manage and secure encryption keys. |
| **Initial** | Encrypts all data in transit; where feasible, encrypts data at rest (mission-critical data, data stored in external environments); begins formalizing key management policies and securing encryption keys. |
| **Advanced** | Encrypts all data at rest and in transit to maximum extent possible; begins incorporating cryptographic agility; protects encryption keys (secrets not hard coded, regular rotation). |
| **Optimal** | Encrypts data in use where appropriate; enforces least privilege for secure key management enterprise-wide; applies encryption using up-to-date standards and cryptographic agility to the extent possible. |

### 4.6 Cross-Cutting Capabilities (Data)

**Visibility & Analytics:**
| Stage | Description |
|-------|-------------|
| Traditional | Limited visibility into data including location, access, and usage; analysis primarily manual. |
| Initial | Visibility based on data inventory management, categorization, encryption, and access attempts; some automated analysis and correlation. |
| Advanced | Maintains data visibility in a comprehensive, enterprise-wide manner; automated analysis and correlation; begins employing predictive analytics. |
| Optimal | Visibility across full data lifecycle; robust analytics including predictive analytics; comprehensive views of agency data and continuous security posture assessment. |

**Automation & Orchestration:**
| Stage | Description |
|-------|-------------|
| Traditional | Implements data lifecycle and security policies (access, usage, storage, encryption, configurations, protections, backups, categorization, sanitization) through manual, potentially ad hoc, processes. |
| Initial | Uses some automated processes to implement data lifecycle and security policies. |
| Advanced | Implements data lifecycle and security policies primarily through automated methods for most agency data in a consistent, tiered, targeted manner across the enterprise. |
| Optimal | Automates, to the maximum extent possible, data lifecycles and security policies for all agency data across the enterprise. |

**Governance:**
| Stage | Description |
|-------|-------------|
| Traditional | Ad hoc data governance policies (protection, categorization, access, inventorying, storage, recovery, removal) with manual implementation. |
| Initial | Defines high-level data governance policies; relies primarily on manual, segmented implementation. |
| Advanced | Begins integration of data lifecycle policy enforcement across the enterprise, enabling more unified definitions for data governance policies. |
| Optimal | Data lifecycle policies are unified to the maximum extent possible and dynamically enforced across the enterprise. |

---

## 5. Cross-Pillar Observations

### 5.1 Common Maturity Patterns

All four pillars share the same maturity trajectory — **Traditional → Initial → Advanced → Optimal** — characterized by:

1. **Traditional:** Manual processes, static configurations, siloed visibility, ad hoc governance, limited automation.
2. **Initial:** Automation begins (scripts, tools), basic integration across pillars, formalized policies, some contextual information in access decisions.
3. **Advanced:** Enterprise-wide automated processes, cross-pillar coordination, centralized visibility, dynamic policy adaptation, cryptographic agility begins.
4. **Optimal:** Fully automated, continuous, just-in-time, enterprise-wide; real-time risk analytics; immutable workloads; cryptographic agility; dynamic enforcement.

### 5.2 Cross-Cutting Capabilities Across Pillars

CISA's three cross-cutting capabilities — **Visibility & Analytics**, **Automation & Orchestration**, and **Governance** — operate within each pillar. As agencies mature, these capabilities become increasingly integrated across pillars:

| Capability | Traditional | Optimal |
|------------|-------------|---------|
| Visibility & Analytics | Manual log collection, limited analysis | Comprehensive visibility via centralized dynamic monitoring, advanced analysis, predictive analytics |
| Automation & Orchestration | Static, manual processes | Dynamic response to enterprise-wide changing requirements; infrastructure-as-code |
| Governance | Ad hoc policies, manual enforcement | Fully automated enterprise-wide policies with continuous enforcement, dynamic updates |

### 5.3 Key Tensions

- **Device vs. BYOD:** CISA acknowledges that BYOD policies reduce visibility and control options, creating a tension between the Device pillar's ideal state and practical workforce realities.
- **Network vs. Application-level controls:** Optimal ZTA pushes security controls *closer to applications and data*, reducing reliance on network-layer protections — but network segmentation remains critical for defense-in-depth.
- **Encryption vs. Visibility:** Encrypting all traffic (Network pillar Optimal) can conflict with traffic inspection needs for threat detection. Agencies must balance cryptographic protections with monitoring requirements.
- **Immutable workloads vs. legacy systems:** The Application pillar's Optimal state (immutable workloads, automated CI/CD) assumes modern cloud-native architectures, which many federal legacy systems cannot support.

---

## 6. Cross-References

| Reference | Relationship |
|-----------|-------------|
| [[NIST 800-207 — Ch3 — Logical Components]] | Canonical ZTA component model (PE, PA, PEP) that these pillars operationalize |
| [[NSA ZT Device Pillar]] | Threat-informed device security guidance — stronger emphasis on attestation, firmware integrity, supply chain |
| [[NSA ZT Network Pillar]] | Threat-informed network security guidance — stronger emphasis on cryptographic isolation, traffic filtering |
| [[CISA ZTMM — Identity Pillar]] | The fifth pillar, documented separately; identity is the foundation for access decisions across all four pillars here |
| [[CISA Zero Trust Maturity Model — Full]] | Full-standards treatment of the complete ZTMM document |
