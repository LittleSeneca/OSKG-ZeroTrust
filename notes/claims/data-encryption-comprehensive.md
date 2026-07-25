---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-data
  - topic/zt-encryption
claim_id: "cisa-ztmm-dnad.21"
statement: "Data Encryption — maturity progresses from encrypting minimal agency data with ad hoc key management to encrypting data in use where appropriate, enforcing least privilege for secure key management enterprise-wide, and applying encryption using up-to-date standards and cryptographic agility."
confidence: "high"
confidence_rationale: "HIGH. Direct from the source document."
claim_type: "implementation"
source_note: "[[CISA ZTMM — Device Network App Data Pillars]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-dnad.21: Data Encryption — maturity progresses from encrypting minimal agency data with ad hoc key management to encrypting data in use where appropriate, enforcing least privilege for secure key management enterprise-wide, and applying encryption using up-to-date standards and cryptographic agility.

**Source:** [[CISA ZTMM — Device Network App Data Pillars]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

Encryption must extend from minimal to comprehensive, including data in use. (§5.5)

## Evidence

| Stage | Description |
|-------|-------------|
| **Traditional** | Encrypts minimal agency data at rest and in transit; relies on manual or ad hoc processes to manage and secure encryption keys. |
| **Initial** | Encrypts all data in transit; where feasible, encrypts data at rest (mission-critical data, data stored in external environments); begins formalizing key management policies and securing encryption keys. |
| **Advanced** | Encrypts all data at rest and in transit to maximum extent possible; begins incorporating cryptographic agility; protects encryption keys (secrets not hard coded, regular rotation). |
| **Optimal** | Encrypts data in use where appropriate; enforces least privilege for secure key management enterprise-wide; applies encryption using up-to-date standards and cryptographic agility to the extent possible. |

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Direct from the source document.

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
  - "[[traffic-encryption-cryptographic-agility]]"

## Assessment

_Not addressed separately in the source note._
