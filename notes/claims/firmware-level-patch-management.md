---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-device-pillar
  - topic/zt-device
  - topic/zt-implementation
claim_id: "nsa-device.5"
statement: "Patch management must cover firmware and components below the OS layer"
confidence: "high"
confidence_rationale: "HIGH. Firmware-level threats are real and documented. NSA's dual-realm distinction (fixed system vs. component firmware) is practically useful for"
claim_type: "implementation"
source_note: "[[NSA — Device Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-device.5: Patch management must cover firmware and components below the OS layer

**Source:** [[NSA — Device Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the Device Pillar*, 2023

## The Claim

"Organizations must maintain awareness of firmware patches below the software layer." Two realms of device-specific patches: (1) Fixed System firmware (CPU microcode, NIC firmware — shared by the device manufacturer) and (2) Component firmware (storage drives, graphics processors — updated by individual component vendors).

## Evidence

NSA cites a 2023 Adaptiva study: large companies manage at least 2,900 applications across all devices, but more than half are not up to date. Threat actors "constantly probe for known vulnerabilities — 'low-hanging fruit' that provide an entry route." NSA also documents persistent low-level threats: LoJax boot rootkit, MosaicRegressor firmware implant, BootHole and BlackLotus UEFI Secure Boot bypasses, Spectre/Meltdown/Downfall/Inception side-channel vulnerabilities, and SSD over-provisioning malware.

**Maturity progression:**

| Phase | State |
|-------|-------|
| **Preparation** | Vulnerabilities tracked and patches applied manually |
| **Basic** | Automated feeds for patch awareness; manual testing before deployment; all unsupported devices identified with upgrade/retirement plans |
| **Intermediate** | Automated tests for patch reliability; manual approval for automated deployment on a schedule; all unsupported devices removed from network; manual/automated firmware maintenance processes instituted |
| **Advanced** | Automated feeds trigger patch download, initial testing, rollout sequencing with log/performance analysis; unsupported devices auto-flagged for quarantine; automated asset acceptance testing knowledge used for component-specific updates |

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Firmware-level threats are real and documented. NSA's dual-realm distinction (fixed system vs. component firmware) is practically useful for procurement and patch management workflows.

## Stakes

Most organizations' patch management stops at the OS layer. The threats NSA lists — UEFI bootkits, firmware implants, side-channel attacks — all operate below the OS. If the device pillar doesn't reach firmware, it leaves a blind spot that sophisticated adversaries (nation-state, per NSA's audience) will exploit.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
  - "[[asset-supply-chain-risk-management]]"

## Assessment

This is where NSA's NSS/DoD focus adds the most value over general-purpose ZT guidance. CISA's ZTMM v2 mentions patch management but doesn't drill into firmware. NSA's firmware emphasis reflects their threat intelligence: nation-state actors deploy firmware implants specifically because most defenders don't look there.
