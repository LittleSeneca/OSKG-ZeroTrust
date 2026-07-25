---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-supply-chain
  - topic/zt-threats
claim_id: "finney-ch1-3.12"
statement: "Third-party integrators and multi-vendor responsibility gaps create systemic vulnerability"
confidence: "high"
confidence_rationale: "HIGH. This is a well-known problem in OT/IoT security and applies broadly: building management systems, HVAC, elevators, fire suppression — all are"
claim_type: "threat"
source_note: "[[Finney — Ch1-3 — The Zero Trust Story]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch1-3.12: Third-party integrators and multi-vendor responsibility gaps create systemic vulnerability

**Source:** [[Finney — Ch1-3 — The Zero Trust Story]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"Often, these controls are installed by third-party integrators as a part of a new building construction or when a company moves into a commercial real estate space. Many times, a different third-party security guard company will be in charge of using that system day to day. When so many different groups are involved with a system, it's often difficult to secure because no one group is responsible for the security of that system."

## Evidence

The physical security system has: a card reader company that uses shared encryption keys, an installer who configured remote access "to get everything working," a guard company that shares logins because "that's way too complicated for the crew," and an internal IT team that didn't know the system existed ("These computers probably aren't on the domain. They're supplied by the security installer"). No single party owns security end-to-end.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is a well-known problem in OT/IoT security and applies broadly: building management systems, HVAC, elevators, fire suppression — all are installed by third parties with security as an afterthought. The SolarWinds and Target breaches both involved third-party access as the initial vector.

## Stakes

If ZT doesn't address third-party and supply chain trust, it has a critical blind spot. Finney implies the solution is organizational (contracts, oversight, accountability) rather than technical — which is correct but underspecified.

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

This claim is strategically important because it connects ZT to supply chain security — an area that NIST 800-207 explicitly addresses through its "all data sources and computing services are considered resources" tenet. Finney shows how the problem manifests in the *physical* realm (card reader installers, guard companies, camera vendors) where it's more visible to business leaders. The unstated message: if your physical security has these trust gaps, your cybersecurity almost certainly does too, and for the same organizational reasons.
