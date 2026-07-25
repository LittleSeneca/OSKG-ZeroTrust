---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-access-mgmt
  - topic/zt-implementation
claim_id: "gb-ch3.3"
statement: "Revoke authorization first, credentials second"
confidence: "high"
confidence_rationale: "HIGH on the logic, MEDIUM on the evidence base (it's thin). The principle is correct but the chapter could have spent more space on the operational"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch3 — Network Agents]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch3.3: Revoke authorization first, credentials second

**Source:** [[Gilman and Barth — Ch3 — Network Agents]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"In the event that access must be revoked, updating authorization is more effective than changing authentication credentials. This is doubly so when considering that authentication results are typically cached and assigned to session identifier. The act of validating an authenticated session is really an authorization decision."

## Evidence

This claim appears as an inset box — a standalone principle, not argued at length with multiple pieces of evidence. The logic is crisp: (1) authentication results are cached, so changing a password doesn't immediately terminate existing sessions; (2) session validation is an authorization check, not an authentication check; (3) therefore, the fastest way to cut off access is to update the authorization policy, not the credential. The chapter doesn't provide empirical data (e.g., time-to-revoke measurements) but the reasoning is sound on its face.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the logic, MEDIUM on the evidence base (it's thin). The principle is correct but the chapter could have spent more space on the operational implications — how fast does an authorization change propagate? What if the authorization engine is the bottleneck?

## Stakes

If you prioritize credential rotation over authorization policy updates during incident response, you leave active sessions alive. This is a common operational mistake. The principle inverts the intuitive response (change passwords!) in favor of the more effective one (update policy!).

## Disagreement

**Who disagrees:**

No one argues against the principle itself. The real debate is implementation: in a system with 10,000 policies and rapid-change trust scores, changing authorization might be just as slow as rotating credentials. The chapter doesn't address revocation latency in detail.

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

This is a pithy, memorable principle that deserves a place in every ZT operator's mental model. It's the kind of thing you print on a poster. But it should be paired with operational detail — how fast is your authorization update propagation? What's the latency from policy change to enforcement? — that the chapter doesn't provide.
