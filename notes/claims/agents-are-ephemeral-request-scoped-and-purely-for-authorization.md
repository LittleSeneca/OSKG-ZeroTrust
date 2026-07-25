---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-authentication
  - topic/zt-access-mgmt
  - topic/zt-network
  - topic/zt-identity
claim_id: "gb-ch3.2"
statement: "Agents are ephemeral, request-scoped, and purely for authorization — authentication is a separate precursor"
confidence: "high"
confidence_rationale: "HIGH. This separation is operationally critical and widely adopted. It means you can authenticate once (a session token) but re-authorize every"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch3 — Network Agents]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch3.2: Agents are ephemeral, request-scoped, and purely for authorization — authentication is a separate precursor

**Source:** [[Gilman and Barth — Ch3 — Network Agents]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"It's best to think of a network agent as an ephemeral entity that is formed on demand to evaluate a policy." And: "Agents serve solely as authorization components and do not play any part in authentication. In fact, authentication is a precursor to agent formation and is generally performed separately for user and device."

## Evidence

The chapter draws a sharp line: authentication produces canonical identifiers (X.509 cert for device, MFA outcome for user), which are then used as lookup keys to populate agent fields (device type, user role, trust score). Authentication is session-oriented and cacheable; authorization is request-oriented and should not be cached because agent details "can change rapidly based on a number of factors." Caching an agent or authorization result is "ill advised."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This separation is operationally critical and widely adopted. It means you can authenticate once (a session token) but re-authorize every request (re-forming the agent with fresh trust scores and device state). This is exactly how Google's Access Proxy works — the session cookie authenticates, but every request hits the authorization engine.

## Stakes

If you conflate authentication and authorization — or cache authorization results — you lose the ability to revoke access mid-session based on changing conditions. This is the mechanism that makes "continuous verification" (NIST tenet 5) technically feasible.

## Disagreement

**Who disagrees:**

Some implementations (OAuth2/RPT-based, early ZTNA products) do cache authorization decisions for performance, accepting the security tradeoff. The authors argue agent generation should be "as lightweight as possible" so that performance pressure doesn't drive you to cache. The chapter previews that Ch4 will address performance considerations more directly.

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

This claim is underappreciated. Everyone talks about "never trust, always verify," but the implementation insight — authentication is session-scoped, authorization is request-scoped, don't mix them — is what makes the slogan executable. The agent construct decouples these concerns cleanly.
