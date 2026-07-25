---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cccs
  - topic/zt-architecture
  - topic/zt-implementation
claim_id: "cccs-arch.7"
statement: "ZT implementation faces significant organizational and technical challenges"
confidence: "high"
confidence_rationale: "HIGH. These are realistic challenges documented across implementations (see Garbis & Chapman on the difficulty of brownfield ZT)."
claim_type: "architectural"
source_note: "[[CCCS — ZT Approach to Security Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cccs-arch.7: ZT implementation faces significant organizational and technical challenges

**Source:** [[CCCS — ZT Approach to Security Architecture]] — Canadian Centre for Cyber Security, *Zero Trust Approach to Security Architecture — ITSM.10.008*, 2023

## The Claim

"Migration to a ZTA can get messy." Challenges include:
- Granular attribute definition for every user and resource requires increased technical/administrative effort
- User frustration with repeated MFA and authentication
- Cost and time for hardware tokens and device rollout
- Legacy firewall incompatibility with dynamic ZT functionality
- Scarce technical resources for implementation
- Multi-year timeline — "it can take years to move to a full ZTA"
- The transition period where some systems are ZT-compatible and others are not
- "A permanent shift in mindset must be adopted and embraced fully"

## Evidence

_No evidence separable from the claim statement in the source note._

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These are realistic challenges documented across implementations (see Garbis & Chapman on the difficulty of brownfield ZT).

## Stakes

If organizations underestimate these challenges, they risk abandoned ZT programs (the "pilot purgatory" problem). CCCS's candor about the multi-year timeline and organizational resistance is valuable for setting realistic expectations.

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

The challenge around legacy firewalls is understated — many government networks run on equipment that fundamentally cannot support dynamic, identity-aware policies. The document recommends "phased plans for introducing new equipment" but doesn't address the budget reality: replacing firewalls is a capital expense that competes with the ZT program itself. This is the hidden cost most ZT frameworks ignore.
