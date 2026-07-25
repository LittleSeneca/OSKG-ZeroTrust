---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-architecture
  - topic/zt-data
  - topic/zt-definition
  - topic/zt-network
claim_id: "gb-ch3.4"
statement: "Agent data is sensitive and should be contained to the control plane, with controlled, format-flexible exposure to the data plane"
confidence: "medium"
confidence_rationale: 'MEDIUM-HIGH. The principle is sound but the implementation details are underdeveloped. "Injecting headers into network requests that flow through a'
claim_type: "architectural"
source_note: "[[Gilman and Barth — Ch3 — Network Agents]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch3.4: Agent data is sensitive and should be contained to the control plane, with controlled, format-flexible exposure to the data plane

**Source:** [[Gilman and Barth — Ch3 — Network Agents]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"To adequately secure the sensitive agent details, the entirety of the agent lifecycle should be contained to trusted control plane systems, which themselves are heavily secured. These systems should be logically and physically separated from the data plane systems, have clear boundaries, and change infrequently."

## Evidence

The chapter identifies two categories of sensitive agent data: (1) PII — user name, address, phone number — and (2) device details that an attacker could use for targeted attacks or physical theft patterns. The solution is a "trusted communication channel" from control plane to application, like a reverse proxy injecting agent-derived headers into requests. The proxy enforces its own authorization and exposes only a subset of agent data downstream. For pre-existing applications with their own authorization systems, the agent data format should be flexible — use whatever format the application expects.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM-HIGH. The principle is sound but the implementation details are underdeveloped. "Injecting headers into network requests that flow through a reverse proxy" is a specific implementation pattern (Google's IAP does exactly this with `X-Goog-Authenticated-User-*` headers), but the chapter doesn't discuss header spoofing risks, signed assertions, or integrity protection for the exposed agent data.

## Stakes

If the exposed agent data isn't integrity-protected, a compromised downstream application (or an attacker who can reach it directly) can fabricate agent claims and bypass authorization. The chapter mentions "trusted communication channel" but doesn't specify what makes it trusted — mutual TLS? Signed tokens? Network-level isolation?

## Disagreement

**Who disagrees:**

BeyondCorp-style implementations often use signed JWTs rather than plain headers to carry agent data to applications, specifically to prevent tampering. The chapter's description is closer to a reverse-proxy pattern that assumes network-level trust between proxy and application, which is less robust.

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

This is the chapter's weakest section. The security model of exposing agent data to the data plane deserved a deeper treatment — integrity protection, least-privilege field exposure, and the risks of header injection/interception. The principle (keep agent data in the control plane) is right, but the "how" is sketched rather than specified.
