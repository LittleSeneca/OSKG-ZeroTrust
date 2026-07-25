---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-device-pillar
  - topic/zt-device
  - topic/zt-architecture
claim_id: "nsa-device.1"
statement: "The device pillar has seven interdependent capabilities that collectively establish device trust"
confidence: "high"
confidence_rationale: "HIGH. This seven-capability model is the most granular decomposition of the device pillar in any ZT standard. NIST 800-207 treats devices more"
claim_type: "architectural"
source_note: "[[NSA — Device Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-device.1: The device pillar has seven interdependent capabilities that collectively establish device trust

**Source:** [[NSA — Device Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the Device Pillar*, 2023

## The Claim

The device pillar is a foundational ZT component ensuring devices are "located, enumerated, authenticated, and assessed" before access is granted. Access decisions are based on dynamic risk calculations — a device is only authorized if it meets the environment's security conditions specified by policy.

## Evidence

The document structures its entire body around these seven capabilities, each with a dedicated section containing a maturity table. NSA describes how each capability feeds into the others — e.g., inventory provides the list of known devices for compliance checking, compliance feeds risk scores for authorization, and centralized management automates the patch and configuration workflows. EDR/XDR integrates with Visibility & Analytics and Automation & Orchestration pillars.

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

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This seven-capability model is the most granular decomposition of the device pillar in any ZT standard. NIST 800-207 treats devices more abstractly (asset management, configuration management); CISA's ZTMM v2 groups device functions into visibility/analytics, automation/orchestration, and governance functions. NSA's decomposition is more operationally specific.

## Stakes

If any one capability is neglected, the device pillar has a single point of failure. For example, strong EDR without a complete inventory means threats on unmanaged devices go undetected. Real-time inspection without patch management means you're inspecting known-vulnerable devices and granting access anyway. The seven capabilities must mature together.

## Disagreement

**Who disagrees:**

CISA's ZTMM v2 organizes device maturity differently — it maps device functions across five pillars (Identity, Device, Network/Environment, Application/Workload, Data) rather than treating device as a self-contained pillar. CISA's approach emphasizes cross-pillar integration earlier in the maturity curve, while NSA treats intra-pillar maturity as a prerequisite for cross-pillar integration. Both are valid; NSA's approach is more actionable for DoD program managers who need discrete capability milestones.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

NSA's seven-capability model is the most practical framework for device pillar implementation. It maps cleanly to procurement categories (inventory → CMDB, compliance → NAC, EDR → endpoint security), making it easier to assign ownership and budget. The CISA model is better for cross-pillar maturity assessment, but NSA's is better for planning and procurement.
