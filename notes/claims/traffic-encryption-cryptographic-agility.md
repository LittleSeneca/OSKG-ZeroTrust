---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-network
  - topic/zt-encryption
  - topic/zt-device
  - topic/zt-access-mgmt
claim_id: "cisa-ztmm-dnad.8"
statement: "Traffic Encryption — maturity progresses from encrypting minimal traffic with manual key management to encrypting all appropriate traffic, enforcing least privilege for secure key management enterprise-wide, and incorporating cryptographic agility as widely as possible."
confidence: "high"
confidence_rationale: "HIGH. Direct from the source document."
claim_type: "implementation"
source_note: "[[CISA ZTMM — Device Network App Data Pillars]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-dnad.8: Traffic Encryption — maturity progresses from encrypting minimal traffic with manual key management to encrypting all appropriate traffic, enforcing least privilege for secure key management enterprise-wide, and incorporating cryptographic agility as widely as possible.

**Source:** [[CISA ZTMM — Device Network App Data Pillars]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

Encryption must scale from minimal to comprehensive with cryptographic agility. (§5.3)

## Evidence

| Stage | Description |
|-------|-------------|
| **Traditional** | Encrypts minimal traffic; relies on manual or ad hoc processes to manage and secure encryption keys. |
| **Initial** | Begins encrypting all traffic to internal applications; prefers encryption for external application traffic; formalizes key management policies; secures server/service encryption keys. |
| **Advanced** | Ensures encryption for all applicable internal and external traffic protocols; manages issuance and rotation of keys and certificates; begins incorporating cryptographic agility best practices. |
| **Optimal** | Continues encrypting traffic as appropriate; enforces least privilege for secure key management enterprise-wide; incorporates cryptographic agility as widely as possible. |

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
- [[idps-capabilities-remain-essential-but-the-how-changes|Widespread traffic encryption creates the challenge that forces IDPS to adapt — network-based IDPS is challenged by encr]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
