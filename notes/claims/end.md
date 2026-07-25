---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/beyondprod
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-identity
claim_id: "beyondprod.5"
statement: "End-User Context Tickets solve the problem of compromised services using their legitimate service identity for lateral movement — access decisions depend on both service identity AND the originating end user's identity."
confidence: "high"
confidence_rationale: "HIGH — The end-user context ticket mechanism addresses a specific, well-defined threat (compromised service lateral movement) with a specific"
claim_type: "implementation"
source_note: "[[BeyondProd — Cloud-Native Security]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondprod.5: End-User Context Tickets solve the problem of compromised services using their legitimate service identity for lateral movement — access decisions depend on both service identity AND the originating end user's identity.

**Source:** [[BeyondProd — Cloud-Native Security]] — Google, *BeyondProd: Cloud-Native Security*, 2019

## The Claim

Without end-user context tickets, a compromised service could use its own legitimate service identity to access data it shouldn't. The tickets — integrity-protected, centrally-issued, forwardable credentials — attest to the identity of the end user who originated the request, breaking this attack path.

## Evidence

The request flow demonstrates composition: User → GFE (TLS termination) → application frontend (authenticates user via EUA service, receives short-lived cryptographic end-user context ticket) → RPC over ALTS to storage backend, forwarding the ticket → backend service checks: frontend ALTS identity authorized to make requests AND present EUC ticket? Ticket valid? User in ticket authorized to access requested data? Every intermediary service does a service access check on inbound RPCs, and the ticket is forwarded on outbound RPCs. This is "Zero Trust at every hop" — no link inherits trust from a previous link.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The end-user context ticket mechanism addresses a specific, well-defined threat (compromised service lateral movement) with a specific, well-described solution. The "chain of backend calls" pattern demonstrates practical hop-by-hop ZT enforcement.

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
