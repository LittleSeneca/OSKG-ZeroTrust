---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-identity
  - topic/zt-risk
  - topic/zt-governance
  - topic/zt-device
claim_id: "cisa-ztmm-id.5"
statement: "Risk assessment evolves from a static, periodic checkbox activity to a real-time, continuous feed into every access decision — a structural shift that CISA treats as a first-class function with its own maturity track, whereas NSA treats it as a property of the access management system."
confidence: "medium"
confidence_rationale: "MEDIUM-HIGH. The progression is well-defined but the operational requirements for real-time continuous risk assessment are significant and"
claim_type: "implementation"
source_note: "[[CISA ZTMM — Identity Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-id.5: Risk assessment evolves from a static, periodic checkbox activity to a real-time, continuous feed into every access decision — a structural shift that CISA treats as a first-class function with its own maturity track, whereas NSA treats it as a property of the access management system.

**Source:** [[CISA ZTMM — Identity Pillar]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

Risk assessment maturity moves from *manual, static* to *real-time, continuous, dynamic*. (§5.1 — Risk Assessments)

## Evidence

| Stage | Capability |
|-------|-----------|
| **Traditional** | Limited determinations for identity risk. |
| **Initial** | Manual methods and static rules for risk determination; supports basic visibility. |
| **Advanced** | Some automated analysis; dynamic rules inform access decisions and response activities. |
| **Optimal** | Real-time identity risk determination based on continuous analysis and dynamic rules; delivers ongoing protection. |

**NSA cross-reference:**

This is a notable structural difference: CISA treats risk as a first-class function with its own maturity track; NSA treats it as a property of the access management system. Both agree on the destination: real-time, continuous, behavior-informed risk assessment.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM-HIGH. The progression is well-defined but the operational requirements for real-time continuous risk assessment are significant and under-described.

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
- [[continuous-authentication-common-all-pillars|Continuous risk assessment feeds real-time identity risk data into the continuous authentication pipeline across all pil]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[access-mgmt-abac-least-privilege|Contrasts CISA's treatment of risk as a first-class function with NSA's treatment of risk as a property of access manage]]
- [[trust-assessment-is-multi-layered-identity-posture-and-behavior|Adds the structural shift from static periodic assessment to real-time continuous feed, distinguishing CISA's approach f]]
  - "[[continuous-risk-based-device-authorization]]"

## Assessment

_Not addressed separately in the source note._
