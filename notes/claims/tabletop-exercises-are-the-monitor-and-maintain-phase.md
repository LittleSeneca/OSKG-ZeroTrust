---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-implementation
  - topic/zt-monitoring
claim_id: "finney-ch8-11.8"
statement: 'Tabletop exercises are the "monitor and maintain" phase operationalized — they test controls and culture simultaneously'
confidence: "high"
confidence_rationale: "HIGH. The MSEL-based approach is the industry standard (NIST 800-84, CISA templates). The specific scenario design choices — IoT as initial vector"
claim_type: "implementation"
source_note: "[[Finney — Ch8-11 — Execution and Sustainability]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch8-11.8: Tabletop exercises are the "monitor and maintain" phase operationalized — they test controls and culture simultaneously

**Source:** [[Finney — Ch8-11 — Execution and Sustainability]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"Part of the monitor and maintain phase means we need to be regularly evaluating whether our controls are good enough or whether we have any blind spots. A tabletop exercise is a great way of doing that." Tabletop exercises serve three functions: test technical controls, test incident response procedures, and build cross-departmental trust relationships that are essential during a real incident.

## Evidence

- The exercise followed NIST 800-84 methodology: defined objectives, developed MSEL, identified audience, conducted exercise, held hotwash debrief.
- Three objectives: (1) Can the team keep the organization operational? (2) Can they distinguish real issues from false positives? (3) Identify gaps in controls, procedures, resources, or training.
- The "red herrings" (protest, call center volume spike) simulated the fog of war — "Our brains will naturally start to connect the dots to draw conclusions, but often we don't have all the information."
- Key personnel removal (Noor's "family emergency") tested continuity and backup readiness.

**Cross-reference — NIST 800-207 Ch7:**

NIST's migration chapter discusses the 7-step deployment cycle (actors → assets → processes → policies → solutions → deploy/monitor → expand) but doesn't specify how to test the deployed controls. Finney's tabletop chapter fills this operational gap.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The MSEL-based approach is the industry standard (NIST 800-84, CISA templates). The specific scenario design choices — IoT as initial vector, tool compromise for lateral movement, physical exfiltration — are well-calibrated to test ZT-specific controls.

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
