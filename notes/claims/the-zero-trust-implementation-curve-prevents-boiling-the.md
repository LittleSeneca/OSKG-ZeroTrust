---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-implementation
  - topic/zt-migration
claim_id: "finney-ch1-3.7"
statement: 'The Zero Trust Implementation Curve prevents "boiling the ocean"'
confidence: "high"
confidence_rationale: 'HIGH. This is standard ZT implementation guidance (Kindervag, CISA ZTMM, NIST 800-207 Ch7). The "protect surface" concept itself is'
claim_type: "implementation"
source_note: "[[Finney — Ch1-3 — The Zero Trust Story]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch1-3.7: The Zero Trust Implementation Curve prevents "boiling the ocean"

**Source:** [[Finney — Ch1-3 — The Zero Trust Story]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"The only way to eat an elephant is one bite at a time. Everybody thinks, 'Oh, how are we ever going to implement Zero Trust?' Our environment is big so we break it down into little sections." The implementation curve prioritizes:

- **Learning protect surfaces** (non-critical, low risk if mistakes are made)
- **Practice protect surfaces** (increasing complexity)
- **Crown Jewels** (most business-critical protect surfaces)
- **Secondary** and **Tertiary** protect surfaces

## Evidence

The team starts with Rose's training SharePoint site — "It won't be a big deal if we take it down for a bit. Nobody will notice." Aaron explicitly rejects starting with DNS ("business-critical") as a first protect surface. The narrative demonstrates the learning value: by starting simple, the team discovers common patterns (stale firewall rules, missing outbound restrictions, copy-paste architectures) that will apply to more critical surfaces.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is standard ZT implementation guidance (Kindervag, CISA ZTMM, NIST 800-207 Ch7). The "protect surface" concept itself is Finney's/Kindervag's alternative to "attack surface" — you shrink scope to what you can control rather than trying to defend everything.

## Stakes

If organizations start with crown jewels, they risk catastrophic failures that kill the ZT program. If they never graduate from learning surfaces, they never protect what matters. The curve provides a path; organizational discipline is needed to follow it.

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

The implementation curve is the most operationally useful concept in Ch2. It directly addresses the "where do we start?" question that paralyzes ZT adoption. The learning → practice → crown jewels progression is intuitive and provides a natural governance framework: different change control for learning vs. crown jewel surfaces. The risk is that organizations get stuck in "learning" mode indefinitely; the book should address this later.
