---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-access-mgmt
  - topic/zt-security
claim_id: "gb-ch4-6.14"
statement: "Group authorization is the highest-trust mechanism for extremely sensitive operations"
confidence: "high"
confidence_rationale: "HIGH on the concept, with the DNS ceremony as the gold-standard example of defense-in-depth for root trust anchors."
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch4-6 — Authorization Devices Users]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch4-6.14: Group authorization is the highest-trust mechanism for extremely sensitive operations

**Source:** [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"Nearly every system has a small set of actions or requests that must be closely guarded... it is desirable to gain the consent of multiple individuals in order to authorize a particularly sensitive action."

## Evidence

Three mechanisms: (1) Shamir's Secret Sharing — split a secret into n parts, require k parts to reconstruct (cryptographically guaranteed); (2) Cloudflare's Red October — layered asymmetric encryption requiring n-of-m users; (3) DNS Root Zone Signing Ceremony — seven actors, HSMs, biometric scanners, air-gapped systems, quarterly ceremony achieving "one-in-a-million chance" of compromise (assuming 5% dishonesty rate). The authors use these to illustrate the spectrum from purely cryptographic (Shamir) to heavily procedural (DNS ceremony).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the concept, with the DNS ceremony as the gold-standard example of defense-in-depth for root trust anchors.

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
