---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-device
  - topic/zt-implementation
claim_id: "dod-ra-cap.9"
statement: "Device Hygiene (Use Cases 12–13) — device hygiene must shift from checklist-based (STIG benchmarks, version numbers) to Event-Condition-Action automation where device posture is continuously checked by multiple tools, confidence scoring for devices considers behavioral patterns beyond patch status, and severity determines response speed (gradual restriction to instant termination)."
confidence: "high"
confidence_rationale: "HIGH. The ECA model is well-defined and operationally specific."
claim_type: "implementation"
source_note: "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-cap.9: Device Hygiene (Use Cases 12–13) — device hygiene must shift from checklist-based (STIG benchmarks, version numbers) to Event-Condition-Action automation where device posture is continuously checked by multiple tools, confidence scoring for devices considers behavioral patterns beyond patch status, and severity determines response speed (gradual restriction to instant termination).

**Source:** [[DoD ZT Reference Architecture — Capabilities and Use Cases]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

Device hygiene has been checklist-based — hitting STIG benchmarks, being at certain version numbers, and general event monitoring. ZT makes hygiene part of authorization to specific information, continuously checked by multiple tools. (§4.12–4.13)

## Evidence

| Component | Description |
|---|---|
| **Event** | Signal or criteria that invokes the rule (e.g., vulnerability detected, anomalous behavior) |
| **Condition** | Logical test that determines if action is needed (e.g., confidence score below threshold) |
| **Action** | Policy update — from gradual restriction to instant session termination |

**Key dynamics:**

- **Baselining:** ZT baselines not only "what a normal device looks like" but also *patterns of individual machines*. Discrepancies between current actions and historical patterns trigger different policies.
- **Event-driven triggers:** Detection of a system issue initiates unified, coordinated policy provisioned across PEPs. Severity determines response speed — gradual change or instant termination.
- **Confidence scoring for devices:** Erratic systems have their score affected by network behavior, process behavior, or other characteristics — not just patch status.
- **Real-time validation against exploits:** If remediation is possible, the system attempts it; if not, the device is removed from the environment to prevent exploitation.

**Cross-reference — NSA Device Pillar:**

NSA's Device Pillar framework (four phases: Preparation → Basic → Intermediate → Advanced) aligns with DoD's device hygiene progression. NSA emphasizes TPM, secure boot, and device attestation; DoD adds the event-condition-action automation layer.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The ECA model is well-defined and operationally specific.

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

## Assessment

_Not addressed separately in the source note._
