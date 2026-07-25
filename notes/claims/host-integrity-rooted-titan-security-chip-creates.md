---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/beyondprod
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-device
claim_id: "beyondprod.4"
statement: "Host Integrity, rooted in the Titan security chip, creates a hardware-anchored chain of trust from firmware to user mode — ALTS machine credentials are only decryptable by hosts that pass verified boot."
confidence: "high"
confidence_rationale: "HIGH — Hardware-rooted trust is a well-established security pattern. The Titan chip integration with ALTS credential provisioning is a specific"
claim_type: "implementation"
source_note: "[[BeyondProd — Cloud-Native Security]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondprod.4: Host Integrity, rooted in the Titan security chip, creates a hardware-anchored chain of trust from firmware to user mode — ALTS machine credentials are only decryptable by hosts that pass verified boot.

**Source:** [[BeyondProd — Cloud-Native Security]] — Google, *BeyondProd: Cloud-Native Security*, 2019

## The Claim

Google's Host Integrity system verifies the integrity of host system software through a secure boot process backed by a hardware root of trust (Titan security chip where supported). The verification chain covers BIOS, BMC, bootloader, OS kernel, and where supported, user-mode code and peripheral firmware.

## Evidence

Host Integrity ensures each host runs the intended version of these components — not just that signatures are valid. The critical integration is with ALTS: machine credentials are only decryptable by hosts that pass host integrity's verified boot. This creates a hardware-rooted chain of trust: Titan chip → verified boot chain → machine ALTS credentials → service ALTS credentials. Without passing host integrity, a machine cannot obtain credentials to participate in the BeyondProd trust fabric.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — Hardware-rooted trust is a well-established security pattern. The Titan chip integration with ALTS credential provisioning is a specific architectural coupling documented in Google's paper.

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
