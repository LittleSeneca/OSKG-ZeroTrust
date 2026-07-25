---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/ncsc
  - topic/zt-cloud
  - topic/zt-implementation
claim_id: "ncsc.3"
statement: "Google's ZT architecture maps to the PDP/PEP model with IAP as the Policy Enforcement Point, Access Context Manager as the Rules Engine, and Cloud IAM/Identity as the Policy Decision Point."
confidence: "high"
confidence_rationale: "HIGH. This architecture cleanly maps to the NIST logical component model: IAP/IAM = PEP, Access Context Manager = Policy Engine/Policy Administrator"
claim_type: "implementation"
source_note: "[[NCSC — ZT Principles on Google Cloud]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# ncsc.3: Google's ZT architecture maps to the PDP/PEP model with IAP as the Policy Enforcement Point, Access Context Manager as the Rules Engine, and Cloud IAM/Identity as the Policy Decision Point.

**Source:** [[NCSC — ZT Principles on Google Cloud]] — NCSC, *Zero Trust Principles on Google Cloud*, 2023

## The Claim

The whitepaper describes a four-step policy enforcement flow that directly implements the PDP/PEP model:

1. **PEP:** Identity-Aware Proxy (IAP), IAM, Cloud Identity, or VPC Service Controls — depending on request type
2. **Rules Engine:** Access Context Manager
3. **Enforcement:** Requests not matching policy are dropped by the Enforcement Point
4. **Continuous Evaluation:** Each request in a session is evaluated by the Rules Engine in real time; if context changes (e.g., geolocation), the request is dropped or requires re-authentication

## Evidence

Access Context Manager uses multiple signals for access decisions — user and device posture, IP address, geolocation, session age, time of day, and credential strength (e.g., hardware second factor). Access levels can be tiered (e.g., "High_Trust" vs. "Medium_Trust") and applied to different resources.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This architecture cleanly maps to the NIST logical component model: IAP/IAM = PEP, Access Context Manager = Policy Engine/Policy Administrator (combined PDP function), multiple signal sources = feed into the Policy Engine. The continuous evaluation within a session (Principle 4, point 4) is a sophisticated implementation of NIST's "access is granted on a per-session basis" tenet.

## Stakes

If the PDP/PEP model is the correct ZT architecture (as NIST asserts), Google's implementation validates that the model is commercially viable at scale. The tiered access levels ("High_Trust" / "Medium_Trust") demonstrate how ZT moves beyond binary allow/deny to risk-adaptive authorization.

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

The continuous evaluation capability — "if an element of context changes, such as geolocation, the request will be dropped or re-authenticated" — is the most architecturally significant feature described. Most ZT implementations evaluate context at session establishment but don't continuously re-evaluate within a session. This is genuine ZT maturity. The tiered access levels capability enables risk-based policies that balance security and usability.
