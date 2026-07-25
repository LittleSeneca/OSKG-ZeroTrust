---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-threats
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-identity
claim_id: "finney-ch8-11.10"
statement: "Red herrings and the fog of war — the tabletop must simulate confusion, not just attack"
confidence: "medium"
confidence_rationale: "MEDIUM. Confidence not explicitly stated in source."
claim_type: "implementation"
source_note: "[[Finney — Ch8-11 — Execution and Sustainability]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch8-11.10: Red herrings and the fog of war — the tabletop must simulate confusion, not just attack

**Source:** [[Finney — Ch8-11 — Execution and Sustainability]] — George Finney, *Project Zero Trust*, 2022

## The Claim

Real incidents are messy. Multiple things go wrong simultaneously, some of which are unrelated to the attack. The tabletop deliberately injected unrelated events (protest, call center spike) to test whether the team could distinguish signal from noise and avoid premature conclusions. "The best way to combat the fog of war is to communicate, ask questions, be transparent, but most of all, don't stick with your conclusions when you receive new information."

## Evidence

The protest (labor conditions, drone, media) was a red herring that consumed leadership attention and created a plausible cover story for the drone. The call center spike was a red herring that could have been a real indicator but was contextual (Tuesday before Thanksgiving). The MFA acceptance by a user's child was a false positive that initially looked like a compromise.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. Confidence not explicitly stated in source.

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
- [[deception-technologies-invert-zt-selectively-add-trust-back|deception-technologies-invert-zt-selectively-add-trust-back]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

This is sophisticated tabletop design. Most exercises focus only on the attack chain; Finney adds operational noise. The lesson is that incident response isn't just about technical forensics — it's about maintaining situational awareness while the organization is under multiple simultaneous pressures.
