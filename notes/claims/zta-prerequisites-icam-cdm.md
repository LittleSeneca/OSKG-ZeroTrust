---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-governance
  - topic/zt-identity
claim_id: "nist207-ch6.2"
statement: "ZTA exposes two hard prerequisites in existing programs — mature ICAM (identity) and CDM (asset inventory) — without which ZTA cannot function, because the Policy Engine cannot authorize access without sufficient subject/resource identity information and complete asset visibility."
confidence: "high"
confidence_rationale: "HIGH. The dependency is explicit in §6.3 and §6.6. NIST states both programs are foundational to ZTA operation."
claim_type: "governance"
source_note: "[[NIST 800-207 — Ch6 — Federal Guidance]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch6.2: ZTA exposes two hard prerequisites in existing programs — mature ICAM (identity) and CDM (asset inventory) — without which ZTA cannot function, because the Policy Engine cannot authorize access without sufficient subject/resource identity information and complete asset visibility.

**Source:** [[NIST 800-207 — Ch6 — Federal Guidance]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

ICAM and CDM are *prerequisites* for ZTA, not parallel efforts. Weak identity provisioning = non-functional ZTA. Incomplete asset inventory = blindly enforcing policy on unknown assets.

## Evidence

The chapter identifies two dependency chains:
- **ICAM maturity → usable subject attributes → functional Policy Engine → ZTA enforcement** (§6.3)
- **CDM/HWAM → asset visibility → device posture assessment → PEP enforcement** (§6.6)

This is not stated as a single claim by NIST but emerges across two sections — it's this note's analytical synthesis.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The dependency is explicit in §6.3 and §6.6. NIST states both programs are foundational to ZTA operation.

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
  - [[ficam-identity-substrate-zta]]
  - [[cdm-visibility-prerequisite-zta]]

## Assessment

_Not addressed separately in the source note._
