---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-device-pillar
  - topic/zt-device
  - topic/zt-remote-access
  - topic/zt-identity
  - topic/zt-network
claim_id: "nsa-device.4"
statement: "Remote access requires heightened scrutiny — assume the remote environment is hostile"
confidence: "high"
confidence_rationale: "HIGH. This aligns with ZTNA principles (replace VPN with per-application access) and CISA's guidance on remote access in the device pillar."
claim_type: "implementation"
source_note: "[[NSA — Device Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-device.4: Remote access requires heightened scrutiny — assume the remote environment is hostile

**Source:** [[NSA — Device Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the Device Pillar*, 2023

## The Claim

"Organizations should assume a remote user's environment is hostile and that all traffic is being monitored and potentially modified by threat actors, so additional scrutiny of those devices and their access requests is needed."

## Evidence

NSA contrasts this with the conventional architecture flaw — "the user's credentials alone were treated as adequate to grant access to network resources." In mature ZT, devices are continually authenticated regardless of location. Remote access is not a separate network path (the old VPN model); it's the same device authentication and authorization flow with heightened scrutiny.

**Maturity progression:**

| Phase | State |
|-------|-------|
| **Preparation** | None at this level |
| **Basic** | Dynamic access policies with implicit denials, explicit approvals, and centralized management for all remote devices; control device access to protected resources and report compliance |
| **Intermediate** | Centralized management systems track remote device configurations; compliance checked at access request time; all protected services require dynamic access decisions |
| **Advanced** | Automatic remediation of non-compliance when identified |

**Scope:**

Remote access requirements cover basic BYOD and IoT access. BYOD domains should use enterprise IdP and only grant access to approved applications when using acceptable device attributes, ideally governed via MDM.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This aligns with ZTNA principles (replace VPN with per-application access) and CISA's guidance on remote access in the device pillar.

## Stakes

_Not addressed separately in the source note._

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
- [[continuous-risk-based-device-authorization|Heightened scrutiny for hostile remote environments is a specific intensification of continuous risk-based authorization]]
  - "[[accessible-applications-public-networks]]"

## Assessment

The hostile-environment assumption is the key insight. It bridges the device pillar to the network pillar — if every remote network is assumed compromised, then the device must prove its trustworthiness without relying on network-based security controls. This is why ZTNA architectures terminate access at the application layer, not the network layer.
