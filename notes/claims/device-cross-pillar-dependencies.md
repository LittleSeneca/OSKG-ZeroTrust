---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-device-pillar
  - topic/zt-device
  - topic/zt-architecture
claim_id: "nsa-device.8"
statement: "Cross-pillar dependencies make the device pillar a team sport"
confidence: "high"
confidence_rationale: "HIGH. Cross-pillar dependency is a defining characteristic of ZT architecture."
claim_type: "architectural"
source_note: "[[NSA — Device Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-device.8: Cross-pillar dependencies make the device pillar a team sport

**Source:** [[NSA — Device Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the Device Pillar*, 2023

## The Claim

"The pillars are not independent; many capabilities in the device pillar depend on or align with capabilities in other pillars."

## Evidence

NSA explicitly calls out that "dynamic authentication and authorization decisions are strictly enforced before access is allowed" — this requires the device pillar to consume identity from the User pillar and network policy from the Network & Environment pillar. EDR/XDR "enable system administrators to identify, detect, and respond to threats that may be pervasive or present in the environment" — requiring the Visibility & Analytics pillar to aggregate and correlate.

**Key cross-pillar dependencies identified:**

| Device Capability | Depends On | Pillar |
|------------------|------------|--------|
| Identity and authentication | User credentials, NPE certificates | User |
| Device connection protocols | Network policies, encryption standards | Network & Environment, Data |
| Remote access | Authentication infrastructure, network segmentation | Network & Environment |
| EDR/XDR analytics | SIEM correlation, threat intelligence | Visibility & Analytics |
| Automated response | SOAR playbooks, orchestration workflows | Automation & Orchestration |
| Application-level access | Application identity, workload protection | Application & Workload |

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Cross-pillar dependency is a defining characteristic of ZT architecture.

## Stakes

Organizations that mature the device pillar in isolation — without corresponding maturity in User (identity), Network (segmentation), and Visibility (SIEM) — will have device trust scores that can't be enforced because the policy enforcement points (in the network and application pillars) aren't consuming them.

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
  - "[[cross-pillar-maturity-trajectory]]"

## Assessment

This is the "why you can't just buy EDR and call it Zero Trust" argument. The device pillar produces trust signals; other pillars consume them to make access decisions. Both sides must exist and be integrated.
