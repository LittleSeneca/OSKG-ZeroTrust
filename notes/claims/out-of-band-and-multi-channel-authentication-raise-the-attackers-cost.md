---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-authentication
  - topic/zt-threats
  - topic/zt-identity
  - topic/zt-device
claim_id: "gb-ch4-6.12"
statement: "Out-of-band and multi-channel authentication raise the attacker's cost by requiring compromise of independent channels"
confidence: "high"
confidence_rationale: "HIGH. Multi-channel is foundational to modern auth (WebAuthn + platform authenticator, push-to-approve). The SMS warning was prescient — NIST"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch4-6 — Authorization Devices Users]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch4-6.12: Out-of-band and multi-channel authentication raise the attacker's cost by requiring compromise of independent channels

**Source:** [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"Leveraging multiple channels is effective not because compromising a channel is hard, but because compromising many is hard."

## Evidence

Separate communication channels (push notification to mobile device, confirmation call, email notification) verify that the requestor controls something independent of the primary authentication channel. The authors warn: "be sure to use a different channel than the one you are trying to authenticate/authorize in the first place." They explicitly reject SMS as a channel ("SMS system does not make sufficient guarantees to protect the random code in transit").

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Multi-channel is foundational to modern auth (WebAuthn + platform authenticator, push-to-approve). The SMS warning was prescient — NIST deprecated SMS-based 2FA in 2017 (SP 800-63B).

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
- [[authentication-authorization-dynamic-continuous|Multi-channel and out-of-band techniques are building blocks for continuous authentication: independent channel verifica]]
- [[mfa-is-necessary-but-insufficient-attackers-have-at|Out-of-band/multi-channel authentication directly addresses the MFA bypass strategies (SMS intercept, compromised device]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
