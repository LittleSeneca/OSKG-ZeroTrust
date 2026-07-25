---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-governance
  - topic/zt-implementation
claim_id: "gc-ch1-3.6"
statement: "Three expanded principles — API integration, automation, and business value delivery — are equally necessary for enterprise-class ZT."
confidence: "high"
confidence_rationale: "HIGH for principles 4 and 5 (they're engineering requirements derived from the core principles). MEDIUM-HIGH for principle 6 — it's a project"
claim_type: "governance"
source_note: "[[Garbis and Chapman — Ch1-3 — Introduction and Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-ch1-3.6: Three expanded principles — API integration, automation, and business value delivery — are equally necessary for enterprise-class ZT.

**Source:** [[Garbis and Chapman — Ch1-3 — Introduction and Architecture]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"In addition to the core Zero Trust principles, we believe that there are three additional principles that are equally important and necessary in any enterprise-class Zero Trust environment."

## Evidence

4. **All components support APIs for event and data exchange.** "Every security and IT component that's integrated into your Zero Trust platform adds to its value, effectiveness, and reach. Conversely, every siloed (un-integrated) component adds friction, diminishes your Zero Trust system effectiveness, and can impede security."

5. **Automate actions across environments, driven by context and events.** Required for operating at even small scale. Automation ≠ automatic — manual approval steps in workflows are fine. But day-to-day policy changes must be automated.

6. **Deliver tactical and strategic value.** "Incremental deployments and tactical wins must be realized. Doing so will simplify your Zero Trust journey, and build momentum and support internally."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH for principles 4 and 5 (they're engineering requirements derived from the core principles). MEDIUM-HIGH for principle 6 — it's a project management principle rather than a technical one, but its importance is validated by the high failure rate of ZT initiatives that lack executive buy-in.

## Stakes

These principles distinguish "paper ZT" from operational ZT. Without API integration and automation, ZT policies are static — which is just traditional security with ZT branding. Without business value delivery, ZT initiatives lose funding and political support.

## Disagreement

**Who disagrees:**

Principle 6 is the most contested. Some argue that security is inherently valuable and shouldn't need to justify itself with "tactical wins." But in practice, security teams that can't show business value get defunded. The disagreement is about strategy, not truth.

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

The automation principle (5) is the most technically significant of the expanded set. It makes explicit what NIST implies — that ZT's dynamism requires programmatic policy enforcement, not periodic rule updates. The key insight "automation ≠ automatic" resolves the fear that ZT means robots taking over security decisions.
