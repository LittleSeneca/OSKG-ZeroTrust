---
tags:
  - source/standards
  - nsa
  - zt-device
  - endpoint-security
  - edr
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
confidence: high
source:
  title: "Advancing Zero Trust Maturity Throughout the Device Pillar"
  authors: "National Security Agency"
  year: 2023
  publisher: "NSA"
  document_id: "U/OO/214644-23 | PP-23-3606 | OCT 2023 Ver. 1.0"
  local_file: "sources/standards/_txt/NSA_ZT_Device_Pillar.txt"
related:
  - "[[NSA — Embracing a Zero Trust Security Model]]"
  - "[[CISA ZTMM — Device Pillar]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[Concepts Index]]"
---

# NSA — Device Pillar

The NSA's authoritative guidance on maturing the Zero Trust device pillar. Published October 2023, this Cybersecurity Information Sheet (CSI) is part of a series providing pillar-specific maturation guidance for National Security System (NSS), DoD, and Defense Industrial Base (DIB) owners and operators. It defines seven key device pillar capabilities, each with four maturity phases: Preparation → Basic → Intermediate → Advanced. 18 pages.

## Claim 1: The device pillar has seven interdependent capabilities that collectively establish device trust

**NSA's claim:** The device pillar is a foundational ZT component ensuring devices are "located, enumerated, authenticated, and assessed" before access is granted. Access decisions are based on dynamic risk calculations — a device is only authorized if it meets the environment's security conditions specified by policy.

**The seven capabilities:**

| # | Capability | Core Function |
|---|-----------|--------------|
| 1 | **Device Inventory** | Maintain real-time inventories of all devices; enroll authorized devices for deny-by-default access |
| 2 | **Device Detection & Compliance** | Detect devices connecting to the network; ensure compliance with device-specific policies |
| 3 | **Device Authorization with Real-Time Inspection** | Deny-by-default access with explicit allow based on compliance, function, and measured risk; continuous monitoring |
| 4 | **Remote Access Protection** | Authenticate and authorize remote users/devices; assume hostile remote environments |
| 5 | **Automated Vulnerability & Patch Management** | Identify hardware/firmware/software versions, correlate with known vulnerabilities, automate patching |
| 6 | **Centralized Device Management** | Manage, secure, and deploy configurations/applications via UEM/MDM from a single console |
| 7 | **Endpoint Threat Detection & Response** | Monitor, detect, and remediate malicious activity on devices using EDR/XDR, integrated with network-wide visibility |

**Evidence presented:** The document structures its entire body around these seven capabilities, each with a dedicated section containing a maturity table. NSA describes how each capability feeds into the others — e.g., inventory provides the list of known devices for compliance checking, compliance feeds risk scores for authorization, and centralized management automates the patch and configuration workflows. EDR/XDR integrates with Visibility & Analytics and Automation & Orchestration pillars.

**Confidence:** HIGH. This seven-capability model is the most granular decomposition of the device pillar in any ZT standard. NIST 800-207 treats devices more abstractly (asset management, configuration management); CISA's ZTMM v2 groups device functions into visibility/analytics, automation/orchestration, and governance functions. NSA's decomposition is more operationally specific.

**What's at stake:** If any one capability is neglected, the device pillar has a single point of failure. For example, strong EDR without a complete inventory means threats on unmanaged devices go undetected. Real-time inspection without patch management means you're inspecting known-vulnerable devices and granting access anyway. The seven capabilities must mature together.

**Who disagrees:** CISA's ZTMM v2 organizes device maturity differently — it maps device functions across five pillars (Identity, Device, Network/Environment, Application/Workload, Data) rather than treating device as a self-contained pillar. CISA's approach emphasizes cross-pillar integration earlier in the maturity curve, while NSA treats intra-pillar maturity as a prerequisite for cross-pillar integration. Both are valid; NSA's approach is more actionable for DoD program managers who need discrete capability milestones.

**My assessment:** NSA's seven-capability model is the most practical framework for device pillar implementation. It maps cleanly to procurement categories (inventory → CMDB, compliance → NAC, EDR → endpoint security), making it easier to assign ownership and budget. The CISA model is better for cross-pillar maturity assessment, but NSA's is better for planning and procurement.

---

## Claim 2: Device Inventory progresses from manual lists to real-time, deny-by-default enrollment

**NSA's claim:** "Knowing what is in an organization's environment is a foundation to establishing trust." A complete inventory of registered devices that are allowed to access enterprise resources enables a "deny all" by default environment.

**Maturity progression:**

| Phase | State |
|-------|-------|
| **Preparation** | Manual inventory; may be based on multiple partial inventories from disparate systems |
| **Basic** | Complete list in separate inventories; planning for NPE (Non-Person Entity) PKI certificates started; specific capabilities identified for new acquisitions |
| **Intermediate** | Standardized device attributes and version information; NPE certificate authentication mostly implemented with "deny all, allow by exception"; specific make/model/revisions eligible for acquisition; automation begins to unify disparate inventories |
| **Advanced** | Complete inventory updated in real time via NPE certificates; only approved devices allowed, all others denied by default; acceptance process checks all new devices; deprovisioning process sanitizes retired devices |

**Key procurement implications:** NSA specifies that inventory governance must cover the full lifecycle: procurement criteria (TPM certificates, firmware configuration, component revisions), acceptance testing (SBOM, Reference Integrity Manifest, TPM Platform Certificate for auditable supply chain chain of custody, per NIST SP 800-161), and deprovisioning (secure erase storage, factory reset firmware, erase TPM NVRAM, reset BMC, remove UEFI Secure Boot modifications).

**Evidence presented:** NSA emphasizes that devices present cybersecurity risks differently — user devices leveraging session access protocols vs. resource devices hosting applications vs. embedded service devices. The inventory solution must distinguish device types and roles.

**Confidence:** HIGH. Inventory as the foundation of device trust is universally accepted across ZT standards (NIST 800-207 Tenet 5, CISA ZTMM v2 Device pillar function 1).

**My assessment:** The advanced-level emphasis on real-time updates and full lifecycle governance (procure → accept → operate → deprovision) is NSA's most distinctive contribution here. Most organizations stop at "we have a CMDB." NSA says: real-time, NPE-certificate-backed, with supply chain integrity artifacts at acquisition and forensic sanitization at retirement. This is an exceptionally high bar.

---

## Claim 3: Authorization decisions must be continuous and risk-based, not one-time at connection

**NSA's claim:** "Making proper authorization decisions requires the most up-to-date information on which to assess the risk of granting access." Real-time inspection compares current device properties against the recorded inventory, examines patch status, and looks for unexpected credentials or applications — not just at connection time, but continuously.

**Maturity progression (Device Authorization with Real Time Inspection):**

| Phase | State |
|-------|-------|
| **Preparation** | None at this level |
| **Basic** | Devices provisioned with unique identifiers; individually authorized |
| **Intermediate** | NextGen AV, Application Control, FIM, EDR integration informs risk posture; access decisions leverage risk posture accounting for device integrity, authentication, and encryption |
| **Advanced** | Device activity data integrated into risk decisions for real-time behavioral assessment; all access requests continuously vetted prior to allowing access to any enterprise or cloud assets |

**Complementary detection & compliance maturity:**

| Phase | State |
|-------|-------|
| **Preparation** | Asset management for user device compliance with baseline configurations |
| **Basic** | Asset management for different device types; compliance violations logged for later remediation |
| **Intermediate** | Minimum compliance attributes established; compliance checked at connection time; non-compliant devices denied access |
| **Advanced** | Continuous compliance checking on all devices; automatic remediation of non-compliance; risk-based criteria for exceptions when remediation isn't feasible |

**Evidence presented:** NSA frames authorization as the integration point where inventory data, compliance status, and real-time inspection converge. This is the risk-calculation engine of the device pillar — the decision point that says "based on everything we know about this device right now, should we grant access?"

**Confidence:** HIGH. Continuous authorization is a core ZT tenet (NIST Tenet 4 — "access to resources is determined by dynamic policy"). NSA operationalizes it with specific tooling references (NextGen AV, FIM, EDR).

**What's at stake:** If authorization is only performed at session establishment, a device that becomes compromised mid-session retains access. Continuous re-authentication — triggered by new resource accesses or behavioral anomalies — is the defense against session hijacking and lateral movement.

**My assessment:** The jump from Intermediate (tool integration for risk posture) to Advanced (behavioral analysis integrated into real-time decisions) is the hardest part of the maturity curve. It requires streaming telemetry from EDR, SIEM correlation, and automated policy enforcement — all working in real time. This is where device pillar maturity starts depending heavily on the Automation & Orchestration and Visibility & Analytics pillars.

---

## Claim 4: Remote access requires heightened scrutiny — assume the remote environment is hostile

**NSA's claim:** "Organizations should assume a remote user's environment is hostile and that all traffic is being monitored and potentially modified by threat actors, so additional scrutiny of those devices and their access requests is needed."

**Maturity progression:**

| Phase | State |
|-------|-------|
| **Preparation** | None at this level |
| **Basic** | Dynamic access policies with implicit denials, explicit approvals, and centralized management for all remote devices; control device access to protected resources and report compliance |
| **Intermediate** | Centralized management systems track remote device configurations; compliance checked at access request time; all protected services require dynamic access decisions |
| **Advanced** | Automatic remediation of non-compliance when identified |

**Scope:** Remote access requirements cover basic BYOD and IoT access. BYOD domains should use enterprise IdP and only grant access to approved applications when using acceptable device attributes, ideally governed via MDM.

**Evidence presented:** NSA contrasts this with the conventional architecture flaw — "the user's credentials alone were treated as adequate to grant access to network resources." In mature ZT, devices are continually authenticated regardless of location. Remote access is not a separate network path (the old VPN model); it's the same device authentication and authorization flow with heightened scrutiny.

**Confidence:** HIGH. This aligns with ZTNA principles (replace VPN with per-application access) and CISA's guidance on remote access in the device pillar.

**My assessment:** The hostile-environment assumption is the key insight. It bridges the device pillar to the network pillar — if every remote network is assumed compromised, then the device must prove its trustworthiness without relying on network-based security controls. This is why ZTNA architectures terminate access at the application layer, not the network layer.

---

## Claim 5: Patch management must cover firmware and components below the OS layer

**NSA's claim:** "Organizations must maintain awareness of firmware patches below the software layer." Two realms of device-specific patches: (1) Fixed System firmware (CPU microcode, NIC firmware — shared by the device manufacturer) and (2) Component firmware (storage drives, graphics processors — updated by individual component vendors).

**Maturity progression:**

| Phase | State |
|-------|-------|
| **Preparation** | Vulnerabilities tracked and patches applied manually |
| **Basic** | Automated feeds for patch awareness; manual testing before deployment; all unsupported devices identified with upgrade/retirement plans |
| **Intermediate** | Automated tests for patch reliability; manual approval for automated deployment on a schedule; all unsupported devices removed from network; manual/automated firmware maintenance processes instituted |
| **Advanced** | Automated feeds trigger patch download, initial testing, rollout sequencing with log/performance analysis; unsupported devices auto-flagged for quarantine; automated asset acceptance testing knowledge used for component-specific updates |

**Evidence presented:** NSA cites a 2023 Adaptiva study: large companies manage at least 2,900 applications across all devices, but more than half are not up to date. Threat actors "constantly probe for known vulnerabilities — 'low-hanging fruit' that provide an entry route." NSA also documents persistent low-level threats: LoJax boot rootkit, MosaicRegressor firmware implant, BootHole and BlackLotus UEFI Secure Boot bypasses, Spectre/Meltdown/Downfall/Inception side-channel vulnerabilities, and SSD over-provisioning malware.

**Confidence:** HIGH. Firmware-level threats are real and documented. NSA's dual-realm distinction (fixed system vs. component firmware) is practically useful for procurement and patch management workflows.

**What's at stake:** Most organizations' patch management stops at the OS layer. The threats NSA lists — UEFI bootkits, firmware implants, side-channel attacks — all operate below the OS. If the device pillar doesn't reach firmware, it leaves a blind spot that sophisticated adversaries (nation-state, per NSA's audience) will exploit.

**My assessment:** This is where NSA's NSS/DoD focus adds the most value over general-purpose ZT guidance. CISA's ZTMM v2 mentions patch management but doesn't drill into firmware. NSA's firmware emphasis reflects their threat intelligence: nation-state actors deploy firmware implants specifically because most defenders don't look there.

---

## Claim 6: Centralized device management (UEM/MDM) is the enforcement backbone for all other capabilities

**NSA's claim:** Centralized device management "grants organizations the ability to centrally manage endpoint devices from a single location" and "provides a method for organizations to manage all devices from one central location, regardless of what platform they function in."

**Maturity progression:**

| Phase | State |
|-------|-------|
| **Preparation** | None at this level |
| **Basic** | Centralized management confirms compliance status for user devices; reports if a device meets minimum standards |
| **Intermediate** | UEM and MDM integrated with inventory for automated, dynamic inventory combined with compliance management; device integrity values collected from TPM and similar mechanisms |
| **Advanced** | All devices inventoried via automated management; vulnerabilities identified and patched/mitigated automatically; policy enforced through IT remote management of issued mobile devices; device integrity values compared against SBOM and RIM |

**Evidence presented:** NSA cites UEM (Unified Endpoint Management for traditional IT) and MDM (Mobile Device Management for mobile) as the two tooling categories. At Advanced maturity, device integrity verification includes TPM measurements compared against SBOM (Software Bill of Materials) and RIM (Reference Integrity Manifest) — linking centralized management to supply chain integrity.

**Confidence:** HIGH. Without centralized management, the other six capabilities must be implemented per-device or per-platform, which doesn't scale.

**What's at stake:** Centralized management is the enforcement point. Inventory tells you what exists; compliance checking tells you what's wrong; centralized management actually fixes it — pushes configurations, deploys patches, enforces policies, remotely wipes compromised devices. Without it, the device pillar is monitoring without remediation.

**My assessment:** The Advanced-level integration of SBOM/RIM with TPM attestation is the most ambitious requirement in the entire pillar. It means every device must not only be managed but cryptographically proven to be running only authorized firmware and software, with an auditable chain from manufacturer to operation. This is the device equivalent of Zero Trust's "verify explicitly" principle applied at the hardware root of trust.

---

## Claim 7: EDR/XDR is the bridge between device-local defense and network-wide ZT

**NSA's claim:** "Endpoint threat detection is an essential component of ZT for the device pillar since malicious activity is assumed to be happening at any time." EDR builds on prior generation Endpoint Security Systems; XDR further increases visibility by correlating artifacts from endpoints that "differ in design, location, or hardware."

**Maturity progression:**

| Phase | State |
|-------|-------|
| **Preparation** | Anti-malware solutions and endpoint auditing to support manual remediation |
| **Basic** | EDR solutions protect, monitor, and respond to malicious/anomalous activities; prepare for Comply to Connect (C2C) integration; NextGen AV covers maximum number of services/applications |
| **Intermediate** | XDR solutions protect, monitor, and respond across device types; cross-pillar integration points identified and prioritized by risk; riskiest points integrated; basic alerting from XDR to SIEM |
| **Advanced** | XDR integrated at all points with fullest coverage; exceptions tracked via risk-based methodology; extended analytics enabling ZT advanced functionalities integrated into SIEM and other solutions |

**Cross-pillar dependencies:** EDR/XDR integrates with Visibility & Analytics (SIEM correlation) and Automation & Orchestration (SOAR response). Robust EDR/XDR deployment enhances: endpoint coverage across differing hardware/software, standardization of management interfaces/logging formats/APIs, and compounding maturity effects in other pillars.

**Additional considerations NSA lists:**
- EDR benefits from Threat Intelligence and Threat Reputation provider integration
- Solution evaluation must account for other ZT pillar capability requirements
- EDR/XDR solutions have varying protection features — suitability evaluation per environment is required

**Evidence presented:** The progression from ESS → EDR → XDR mirrors the industry evolution and is the maturity backbone for endpoint security in ZT. At Intermediate, organizations begin Comply to Connect (C2C) preparation — a DoD-specific program that checks device and user posture before granting network access.

**Confidence:** HIGH. EDR/XDR as the device pillar's detection/response capability is universally recognized across ZT frameworks.

**What's at stake:** If EDR/XDR is treated as a standalone security tool rather than integrated with the broader ZT fabric, its value is limited to device-local detection. The real power comes from feeding endpoint telemetry into cross-pillar analytics (SIEM, SOAR) to detect multi-stage attacks that span devices, networks, and applications.

**My assessment:** The Advanced maturity bar — "XDR integrated at all points with fullest coverage" — is aspirational for most organizations. It requires every device type, every integration point, and every analytics pipeline to be instrumented. The pragmatic approach (reflected in Intermediate) is to prioritize by risk: integrate the riskiest points first and expand coverage iteratively.

---

## Claim 8: Cross-pillar dependencies make the device pillar a team sport

**NSA's claim:** "The pillars are not independent; many capabilities in the device pillar depend on or align with capabilities in other pillars."

**Key cross-pillar dependencies identified:**

| Device Capability | Depends On | Pillar |
|------------------|------------|--------|
| Identity and authentication | User credentials, NPE certificates | User |
| Device connection protocols | Network policies, encryption standards | Network & Environment, Data |
| Remote access | Authentication infrastructure, network segmentation | Network & Environment |
| EDR/XDR analytics | SIEM correlation, threat intelligence | Visibility & Analytics |
| Automated response | SOAR playbooks, orchestration workflows | Automation & Orchestration |
| Application-level access | Application identity, workload protection | Application & Workload |

**Evidence presented:** NSA explicitly calls out that "dynamic authentication and authorization decisions are strictly enforced before access is allowed" — this requires the device pillar to consume identity from the User pillar and network policy from the Network & Environment pillar. EDR/XDR "enable system administrators to identify, detect, and respond to threats that may be pervasive or present in the environment" — requiring the Visibility & Analytics pillar to aggregate and correlate.

**Confidence:** HIGH. Cross-pillar dependency is a defining characteristic of ZT architecture.

**What's at stake:** Organizations that mature the device pillar in isolation — without corresponding maturity in User (identity), Network (segmentation), and Visibility (SIEM) — will have device trust scores that can't be enforced because the policy enforcement points (in the network and application pillars) aren't consuming them.

**My assessment:** This is the "why you can't just buy EDR and call it Zero Trust" argument. The device pillar produces trust signals; other pillars consume them to make access decisions. Both sides must exist and be integrated.

---

## Cross-Reference: NSA Device Pillar vs. CISA ZTMM v2 Device Pillar

| Dimension | NSA (Oct 2023) | CISA ZTMM v2 (Apr 2023) |
|-----------|---------------|-------------------------|
| **Audience** | NSS, DoD, DIB — national security systems | Federal Civilian Executive Branch (FCEB) agencies |
| **Structure** | Seven capabilities with 4-phase maturity tables | Five pillars with 4 maturity levels (Traditional → Initial → Advanced → Optimal) mapped across functions |
| **Device functions in CISA** | Covered as dedicated "Device pillar" | Spread across: Identity (device identity), Device (asset/endpoint management), Network (device connectivity) |
| **Threat framing** | Adversary-focused: firmware implants, UEFI bootkits, nation-state actors | Risk-management-focused: configuration drift, unauthorized devices, compliance gaps |
| **Firmware emphasis** | Extensive — dual-realm firmware patching, TPM attestation, SBOM/RIM | Limited — mentions configuration management but not firmware-level threats |
| **Maturity terminology** | Preparation → Basic → Intermediate → Advanced | Traditional → Initial → Advanced → Optimal |
| **Key difference** | NSA requires supply chain integrity artifacts (SBOM, RIM, TPM certificates) from procurement through deprovisioning | CISA's device maturity focuses on operational visibility and automated compliance |

**Complementary use:** NSA provides the threat-informed, technically specific "how" for high-security environments. CISA provides the cross-pillar maturity framework for assessing overall organizational posture. Organizations should use NSA's capability maturity tables for device-specific planning and CISA's cross-pillar functions for overall ZT program maturity assessment.

---

## Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| Seven interdependent device capabilities | HIGH | Capability silos obscuring cross-capability dependencies |
| Inventory as deny-by-default foundation | HIGH | Most orgs never reach real-time, certificate-backed inventory |
| Continuous, risk-based authorization | HIGH | Requires streaming telemetry infrastructure most orgs lack |
| Remote access with hostile-environment assumption | HIGH | BYOD/IoT edge cases complicate uniform application |
| Firmware-level patch management | HIGH | Component vendor fragmentation makes automation difficult |
| Centralized management as enforcement backbone | HIGH | UEM/MDM tools vary dramatically in ZT feature support |
| EDR/XDR as device-network bridge | HIGH | Advanced XDR coverage is aspirational; risk-prioritized adoption is realistic |
| Cross-pillar dependencies | HIGH | Isolation is the default; cross-pillar integration is the hard work |

**Strongest section:** The seven-capability decomposition with maturity tables. No other ZT document provides this level of operational specificity for the device pillar. The firmware threat documentation (LoJax, MosaicRegressor, BlackLotus, side-channel attacks) grounds the guidance in real adversary behavior.

**Weakest section:** The Summary of Guidance (p. 16-17) is thin — seven bullet points that restate the capabilities without synthesis or prioritization. For an 18-page document with this much detail, a more substantive roadmap would have been valuable. The lack of an explicit dependency graph between the seven capabilities is also a gap — organizations need to know that inventory must mature before compliance, and compliance must mature before real-time authorization.

**Significance:** This CSI, together with the companion User Pillar CSI (March 2023) and subsequent pillar CSIs, operationalizes the NSA's 2021 Embracing a Zero Trust Security Model for specific implementation domains. It bridges the gap between the high-level ZT framework and actionable procurement/implementation guidance. For DoD program managers, these maturity tables directly inform milestone planning and budget justification.
