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
claims_status: extracted
claims_extracted: 2026-07-24
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
  - topic/zt-device
  - topic/zt-identity
  - topic/zt-implementation
---

# NSA — Device Pillar

The NSA's authoritative guidance on maturing the Zero Trust device pillar. Published October 2023, this Cybersecurity Information Sheet (CSI) is part of a series providing pillar-specific maturation guidance for National Security System (NSS), DoD, and Defense Industrial Base (DIB) owners and operators. It defines seven key device pillar capabilities, each with four maturity phases: Preparation → Basic → Intermediate → Advanced. 18 pages.

**Claim 1 —** The device pillar has seven interdependent capabilities that collectively establish device trust → [[seven-device-capabilities-interdependent]]
---

**Claim 2 —** Device Inventory progresses from manual lists to real-time, deny-by-default enrollment → [[device-inventory-deny-by-default]]
---

**Claim 3 —** Authorization decisions must be continuous and risk-based, not one-time at connection → [[continuous-risk-based-device-authorization]]
---

**Claim 4 —** Remote access requires heightened scrutiny — assume the remote environment is hostile → [[remote-access-hostile-environment-assumption]]
---

**Claim 5 —** Patch management must cover firmware and components below the OS layer → [[firmware-level-patch-management]]
---

**Claim 6 —** Centralized device management (UEM/MDM) is the enforcement backbone for all other capabilities → [[centralized-device-management-enforcement-backbone]]
---

**Claim 7 —** EDR/XDR is the bridge between device-local defense and network-wide ZT → [[edr-xdr-device-network-bridge]]
---

**Claim 8 —** Cross-pillar dependencies make the device pillar a team sport → [[device-cross-pillar-dependencies]]
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
