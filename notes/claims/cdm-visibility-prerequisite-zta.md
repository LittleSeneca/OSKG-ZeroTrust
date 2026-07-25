---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-governance
  - topic/zt-device
claim_id: "nist207-ch6.8"
statement: "CDM is the visibility prerequisite for ZTA — without CDM's four foundational questions answered (what is connected, who is on the network, what is happening, how is data protected), ZTA cannot evaluate device posture or make informed access decisions."
confidence: "high"
confidence_rationale: "HIGH. The CDM-to-ZTA dependency is explicit and structural — without asset inventory, the \"verify explicitly\" tenet is undermined because you're"
claim_type: "governance"
source_note: "[[NIST 800-207 — Ch6 — Federal Guidance]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch6.8: CDM is the visibility prerequisite for ZTA — without CDM's four foundational questions answered (what is connected, who is on the network, what is happening, how is data protected), ZTA cannot evaluate device posture or make informed access decisions.

**Source:** [[NIST 800-207 — Ch6 — Federal Guidance]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

The CDM program answers four foundational questions that ZTA depends on. DHS Hardware Asset Management (HWAM) enables the "first steps" toward ZTA. (§6.6)

## Evidence

| CDM Question | ZTA Dependency |
|---|---|
| **What is connected?** (devices, apps, services) | PEP needs complete asset inventory to evaluate device posture |
| **Who is on the network?** (users, NPEs) | Policy Engine needs subject identity and role attributes |
| **What is happening?** (traffic patterns, messages) | Continuous monitoring and anomaly detection feed dynamic policy |
| **How is data protected?** (at rest, in transit, in use) | Data classification informs access policy and encryption requirements |

- Key dependency chain: **CDM/HWAM → asset visibility → device posture assessment → PEP enforcement.**

**Implication for OSKG-ZeroTrust:**

CDM is the *visibility prerequisite*. Without CDM, a ZTA is blindly enforcing policy on unknown assets — undermining the entire "verify explicitly" tenet.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The CDM-to-ZTA dependency is explicit and structural — without asset inventory, the "verify explicitly" tenet is undermined because you're verifying against an incomplete picture.

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
