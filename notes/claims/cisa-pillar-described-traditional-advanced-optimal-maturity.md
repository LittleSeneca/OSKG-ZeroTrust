---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cccs
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-threats
claim_id: "cccs-model.2"
statement: "Each CISA pillar is described at the Traditional/Advanced/Optimal maturity gradient"
confidence: "high"
confidence_rationale: "HIGH. This is a faithful summary of CISA's ZTMM v1 (June 2021 draft). Note that CISA published v2 in 2023 with refined pillars and additional"
claim_type: "definitional"
source_note: "[[CCCS — Zero Trust Security Model]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cccs-model.2: Each CISA pillar is described at the Traditional/Advanced/Optimal maturity gradient

**Source:** [[CCCS — Zero Trust Security Model]] — Canadian Centre for Cyber Security, *Zero Trust Security Model — ITSAP.10.008*, 2023

## The Claim

The document describes each pillar with specific practices at each maturity level (the table in the original is reproduced and annotated below):

| Pillar | Traditional | Advanced | Optimal |
|--------|-------------|----------|---------|
| **Identity** | Password or MFA; limited risk assessment | MFA; identity federation with cloud/on-prem; compliance enforcement | Continuous validation; real-time ML analysis |
| **Device** | Limited visibility into compliance; simple inventory | Compliance enforcement employed; data access depends on device posture | Constant device security monitor/validation; data access depends on real-time risk analytics |
| **Network/Environment** | Large macro-segmentation; minimal traffic encryption | Defined by ingress/egress micro-perimeters; basic analytics | Fully distributed ingress/egress micro-perimeters; ML-based threat protection; all traffic encrypted |
| **Application Workload** | Access based on local authorization; minimal integration with workflow | Access based on centralized authentication; basic integration into application workflow | Access authorized continuously; strong integration into application workflow |
| **Data** | Not well inventoried; static control; unencrypted | Least privilege controls; data stored in cloud/remote encrypted at rest | Dynamic support; all data encrypted |

## Evidence

_No evidence separable from the claim statement in the source note._

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is a faithful summary of CISA's ZTMM v1 (June 2021 draft). Note that CISA published v2 in 2023 with refined pillars and additional maturity stages — this document reflects v1, which is consistent with its November 2022 publication date.

## Stakes

The v1→v2 evolution of CISA ZTMM means this summary may be slightly outdated. The v2 model restructured pillars (splitting "Network/Environment" into "Network" and "Environment" as separate considerations, for example).

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

The maturity gradient is presented without the governance framing that CISA intended — Traditional/Advanced/Optimal are not just technical states but organizational maturity states requiring different governance structures. This flattening is appropriate for a 2-page document but loses the critical insight that ZT maturity is primarily an organizational journey, not a technology procurement journey.
