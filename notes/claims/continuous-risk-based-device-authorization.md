---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-device-pillar
  - topic/zt-device
  - topic/zt-trust
  - topic/zt-identity
  - topic/zt-access-mgmt
claim_id: "nsa-device.3"
statement: "Authorization decisions must be continuous and risk-based, not one-time at connection"
confidence: "high"
confidence_rationale: 'HIGH. Continuous authorization is a core ZT tenet (NIST Tenet 4 — "access to resources is determined by dynamic policy"). NSA operationalizes it with'
claim_type: "implementation"
source_note: "[[NSA — Device Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-device.3: Authorization decisions must be continuous and risk-based, not one-time at connection

**Source:** [[NSA — Device Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the Device Pillar*, 2023

## The Claim

"Making proper authorization decisions requires the most up-to-date information on which to assess the risk of granting access." Real-time inspection compares current device properties against the recorded inventory, examines patch status, and looks for unexpected credentials or applications — not just at connection time, but continuously.

## Evidence

NSA frames authorization as the integration point where inventory data, compliance status, and real-time inspection converge. This is the risk-calculation engine of the device pillar — the decision point that says "based on everything we know about this device right now, should we grant access?"

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

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Continuous authorization is a core ZT tenet (NIST Tenet 4 — "access to resources is determined by dynamic policy"). NSA operationalizes it with specific tooling references (NextGen AV, FIM, EDR).

## Stakes

If authorization is only performed at session establishment, a device that becomes compromised mid-session retains access. Continuous re-authentication — triggered by new resource accesses or behavioral anomalies — is the defense against session hijacking and lateral movement.

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

The jump from Intermediate (tool integration for risk posture) to Advanced (behavioral analysis integrated into real-time decisions) is the hardest part of the maturity curve. It requires streaming telemetry from EDR, SIEM correlation, and automated policy enforcement — all working in real time. This is where device pillar maturity starts depending heavily on the Automation & Orchestration and Visibility & Analytics pillars.
