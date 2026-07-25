---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-trust
  - topic/zt-authentication
  - topic/zt-identity
  - topic/zt-architecture
claim_id: "gb-ch4-6.10"
statement: "Trust score should drive authentication requirements, not static sensitivity labels"
confidence: "high"
confidence_rationale: "HIGH. This is the architecture behind adaptive authentication / step-up auth. It's now mainstream (Azure AD Conditional Access, Okta Adaptive MFA)"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch4-6 — Authorization Devices Users]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch4-6.10: Trust score should drive authentication requirements, not static sensitivity labels

**Source:** [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"Rather than selecting particular actions which require additional authentication, one should assign a required score and allow the trust score itself to drive the authentication flow and requirements."

## Evidence

The traditional approach — designate sensitive actions and authenticate heavily for those — is "likened to perimeter security, in which sensitive actions must pass a particular test, after which no further protections are present." Instead: if the user's trust score is already high (recent strong auth, normal patterns), don't re-prompt. If it's low (unusual location, new device), prompt for additional factor. The system "chooses a combination of methods in order to meet the goal, possibly reducing the invasiveness by having context about the level of sensitivity."

**Cross-reference — NIST 800-207 Ch3:**

NIST's PE evaluates trust on a per-session basis using "as many sources as possible." The dynamic trust score driving authentication is the logical extension of NIST's continuous evaluation principle.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is the architecture behind adaptive authentication / step-up auth. It's now mainstream (Azure AD Conditional Access, Okta Adaptive MFA). In 2017 it was forward-looking.

## Stakes

Static auth requirements create a false sense of security (one-time gate, then trust everything) and degrade UX (users prompted for 2FA on low-risk actions). Trust-driven auth is the ZT authentication principle.

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
