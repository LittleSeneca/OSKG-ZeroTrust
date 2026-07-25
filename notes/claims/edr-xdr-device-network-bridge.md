---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-device-pillar
  - topic/zt-device
  - topic/zt-network
  - topic/zt-monitoring
claim_id: "nsa-device.7"
statement: "EDR/XDR is the bridge between device-local defense and network-wide ZT"
confidence: "high"
confidence_rationale: "HIGH. EDR/XDR as the device pillar's detection/response capability is universally recognized across ZT frameworks."
claim_type: "architectural"
source_note: "[[NSA — Device Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-device.7: EDR/XDR is the bridge between device-local defense and network-wide ZT

**Source:** [[NSA — Device Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the Device Pillar*, 2023

## The Claim

"Endpoint threat detection is an essential component of ZT for the device pillar since malicious activity is assumed to be happening at any time." EDR builds on prior generation Endpoint Security Systems; XDR further increases visibility by correlating artifacts from endpoints that "differ in design, location, or hardware."

## Evidence

The progression from ESS → EDR → XDR mirrors the industry evolution and is the maturity backbone for endpoint security in ZT. At Intermediate, organizations begin Comply to Connect (C2C) preparation — a DoD-specific program that checks device and user posture before granting network access.

**Maturity progression:**

| Phase | State |
|-------|-------|
| **Preparation** | Anti-malware solutions and endpoint auditing to support manual remediation |
| **Basic** | EDR solutions protect, monitor, and respond to malicious/anomalous activities; prepare for Comply to Connect (C2C) integration; NextGen AV covers maximum number of services/applications |
| **Intermediate** | XDR solutions protect, monitor, and respond across device types; cross-pillar integration points identified and prioritized by risk; riskiest points integrated; basic alerting from XDR to SIEM |
| **Advanced** | XDR integrated at all points with fullest coverage; exceptions tracked via risk-based methodology; extended analytics enabling ZT advanced functionalities integrated into SIEM and other solutions |

**Cross-pillar dependencies:**

EDR/XDR integrates with Visibility & Analytics (SIEM correlation) and Automation & Orchestration (SOAR response). Robust EDR/XDR deployment enhances: endpoint coverage across differing hardware/software, standardization of management interfaces/logging formats/APIs, and compounding maturity effects in other pillars.

**Additional considerations NSA lists:**

- EDR benefits from Threat Intelligence and Threat Reputation provider integration
- Solution evaluation must account for other ZT pillar capability requirements
- EDR/XDR solutions have varying protection features — suitability evaluation per environment is required

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. EDR/XDR as the device pillar's detection/response capability is universally recognized across ZT frameworks.

## Stakes

If EDR/XDR is treated as a standalone security tool rather than integrated with the broader ZT fabric, its value is limited to device-local detection. The real power comes from feeding endpoint telemetry into cross-pillar analytics (SIEM, SOAR) to detect multi-stage attacks that span devices, networks, and applications.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[device-threat-protection-centralized|The EDR→XDR progression is the specific technical mechanism that enables centralized, unified threat protection across a]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The Advanced maturity bar — "XDR integrated at all points with fullest coverage" — is aspirational for most organizations. It requires every device type, every integration point, and every analytics pipeline to be instrumented. The pragmatic approach (reflected in Intermediate) is to prioritize by risk: integrate the riskiest points first and expand coverage iteratively.
