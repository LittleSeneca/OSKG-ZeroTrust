---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-identity
  - topic/zt-device
  - topic/zt-governance
  - topic/zt-access-mgmt
claim_id: "gb-ch4-6.9"
statement: "User identity and device identity are separate trust domains — conflating them is dangerous"
confidence: "high"
confidence_rationale: 'VERY HIGH. This is a foundational ZT principle echoed by every framework. NIST 800-207: "Access to individual enterprise resources is granted on a'
claim_type: "definitional"
source_note: "[[Gilman and Barth — Ch4-6 — Authorization Devices Users]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch4-6.9: User identity and device identity are separate trust domains — conflating them is dangerous

**Source:** [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"Zero trust networks identify and trust users separately from devices. Sometimes identifying a user will use the same technology that is used to identify devices, but we must be clear that these are two separate credentials."

## Evidence

The authors open Ch6 with the problem: "How do we know that the intended user is actually at the keyboard? Perhaps they left their device unlocked and unattended?" They also note: user credentials copied across multiple devices increase exposure; kiosk scenarios make device-user binding impossible. The solution is layered authentication — device first, user second, each with independent trust scores that combine at authorization time.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This is a foundational ZT principle echoed by every framework. NIST 800-207: "Access to individual enterprise resources is granted on a per-session basis. Trust in the requester is evaluated before access is granted." The per-session evaluation inherently combines device + user trust.

## Stakes

Conflating the two collapses the layered defense. A stolen device with a certificate becomes full user impersonation. A compromised user session on a compromised device has no redundant signal.

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
