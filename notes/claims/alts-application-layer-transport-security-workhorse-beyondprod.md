---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/beyondprod
  - topic/zt-cloud
  - topic/zt-implementation
claim_id: "beyondprod.2"
statement: "ALTS (Application Layer Transport Security) is the workhorse of BeyondProd — binding identities to services rather than hosts is the critical design decision that enables seamless replication, load balancing, and rescheduling across machines."
confidence: "high"
confidence_rationale: "HIGH — ALTS is a well-documented, production-proven protocol at Google scale. The identity-to-service binding is a specific architectural decision"
claim_type: "implementation"
source_note: "[[BeyondProd — Cloud-Native Security]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondprod.2: ALTS (Application Layer Transport Security) is the workhorse of BeyondProd — binding identities to services rather than hosts is the critical design decision that enables seamless replication, load balancing, and rescheduling across machines.

**Source:** [[BeyondProd — Cloud-Native Security]] — Google, *BeyondProd: Cloud-Native Security*, 2019

## The Claim

Google states that ALTS provides mutual authentication and transport encryption for every service-to-service RPC call in Google's infrastructure. Identities are bound to services, not hosts — a microservice has its own ALTS identity independent of the machine it runs on.

## Evidence

Machine-level ALTS credentials are provisioned using the host integrity system and can only be decrypted if secure boot was verified. Borg Prime grants microservice-level ALTS credentials based on the microservice's identity, provisioned over the machine-level secure channel. This creates a chain: Titan chip → verified boot → host integrity → machine ALTS credentials → service ALTS credentials. The design means a compromised host cannot impersonate a service, and a rescheduled service retains its identity.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — ALTS is a well-documented, production-proven protocol at Google scale. The identity-to-service binding is a specific architectural decision with clear security rationale.

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
