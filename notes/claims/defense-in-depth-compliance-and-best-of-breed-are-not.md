---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-governance
  - topic/zt-definition
  - topic/zt-network
  - topic/zt-threats
claim_id: "finney-ch1-3.5"
statement: "Defense in depth, compliance, and best-of-breed are not strategies"
confidence: "high"
confidence_rationale: "HIGH. The critique of defense in depth as non-measurable is well-established in the ZT literature (Kindervag's original Forrester research makes the"
claim_type: "definitional"
source_note: "[[Finney — Ch1-3 — The Zero Trust Story]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch1-3.5: Defense in depth, compliance, and best-of-breed are not strategies

**Source:** [[Finney — Ch1-3 — The Zero Trust Story]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"To be successful at anything, and especially in cybersecurity, you need a strategy to achieve your goals. In cybersecurity, the goal is to avoid being breached. Zero Trust is that strategy for success." He systematically disqualifies alternatives:

- **Defense in depth:** "How many layers do you need to keep the bad guys out? Eight? Ten? Twenty? This is why embracing defense in depth as your strategy really turns out to look a lot more like 'expense in depth.' There's no measure for success."
- **Compliance:** "There are some good tactics on those lists, but a lot of companies that were compliant got breached."
- **Best of breed:** "Having the best products doesn't stop organizations from getting breached. What really matters is making all those separate elements work together in one integrated system that is custom tailored to fit your unique business."
- **Attack surface reduction:** "The whole world is your attack surface! Instead, with Zero Trust, we focus only on the things that we can control... like the 'protect surface.'"

## Evidence

Each alternative is rejected with a specific criterion: a strategy must be *measurable* (you know when you've succeeded). Defense in depth has no completion criterion. Compliance has a completion criterion (you're compliant or not) but the goal is wrong (compliance ≠ security). Best of breed has no completion criterion and the wrong goal (best products ≠ breach prevention).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The critique of defense in depth as non-measurable is well-established in the ZT literature (Kindervag's original Forrester research makes the same argument). The compliance critique is widely accepted post-SolarWinds/Target/Equifax (all were compliant when breached).

## Stakes

If any of these alternatives *are* valid strategies, organizations don't need ZT. Finney needs to close off the escape hatches. His criterion (measurability + correct goal) is stringent — arguably too stringent, since many accepted business strategies (e.g., "be the innovation leader") aren't precisely measurable either.

## Disagreement

**Who disagrees:**

Compliance advocates argue that frameworks like PCI-DSS or FedRAMP are constantly evolving and that "compliance" can be a strategic goal if the framework is robust. Finney implicitly responds: compliance is a *floor*, not a *strategy*. This is consistent with NIST's treatment of compliance as a baseline.

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

This is the strongest intellectual contribution in Ch2. By defining what makes something a strategy (measurable progress toward a specific goal) and showing that common security approaches fail the test, Finney creates a gap that only ZT fills. The argument is rigorous enough for a business audience and would hold up in a boardroom. The risk is that it's too dismissive of defense in depth — many ZT implementations *are* defense in depth, just with micro-perimeters instead of a single perimeter. Finney would probably agree; his critique is of unmeasured, unbounded defense in depth, not layered controls per se.
