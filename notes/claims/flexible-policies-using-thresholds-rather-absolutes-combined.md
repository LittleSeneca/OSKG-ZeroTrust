---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/beyondcorp
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-definition
  - topic/zt-governance
claim_id: "beyondcorp.10"
statement: 'Flexible policies using thresholds rather than absolutes, combined with platform-normalized security evaluations, prevent draconian enforcement that causes users to seek workarounds — "100% uniform control deployment is a mythical state where unicorns frolic unconcerned about malware."'
confidence: "high"
confidence_rationale: 'HIGH — The "thresholds not absolutes" principle and "100% uniform control is mythical" are specific, documented operational philosophies. The'
claim_type: "implementation"
source_note: "[[BeyondCorp — Research Papers]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondcorp.10: Flexible policies using thresholds rather than absolutes, combined with platform-normalized security evaluations, prevent draconian enforcement that causes users to seek workarounds — "100% uniform control deployment is a mythical state where unicorns frolic unconcerned about malware."

**Source:** [[BeyondCorp — Research Papers]] — Google, *BeyondCorp Research Papers*, 2014-2020

## The Claim

Flexible policies using thresholds rather than absolutes, combined with platform-normalized security evaluations, prevent draconian enforcement that causes users to seek workarounds — "100% uniform control deployment is a mythical state where unicorns frolic unconcerned about malware."

## Evidence

Platform measurement and control parity: different platforms have fundamentally different capabilities — Chrome OS has robust software control via Secure Access; Linux has no out-of-the-box malware prevention. Google's approach: normalized security evaluations — analyze each platform against ideal control state, evaluate gaps, produce fleet health report (not a report card, a shared understanding of capabilities). For each platform evaluate: can the platform support the control? Is it on by default? Can we measure its state? Is the fleet in compliance? Where preventative controls are lacking: compensate with higher monitoring/detection signal confidence or more effective controls on a different platform. Exception management: exceptions must be measurable and time-based; classify root causes consistently; if exception perpetually renewed → control is not working → redesign; focus on new machines in compliance from first use → grandfather existing fleet → cluster failure reasons → tackle largest/riskiest clusters → repeat. Control rollout process: design/prototype → dogfood on targeted populations → monitor mode first → iterate → graduate to enforcement. Communications: map each control to threats addressed, high transparency and explicit criteria build consensus.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The "thresholds not absolutes" principle and "100% uniform control is mythical" are specific, documented operational philosophies. The platform-normalized evaluation methodology is a concrete approach to heterogeneous environments.

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
- [[pillar-ideals-vs-operational-realities|BeyondCorp's flexible threshold-based policies demonstrate a practical approach to resolving the tension between ZT pill]]
- [[beyondcorp-caused-30-fewer-support-issues-comparable|Flexible threshold-based policies prevent the draconian enforcement that drives users to seek workarounds, directly redu]]
- [[tiered-access|Threshold-based trust policies (rather than binary absolutes) make tiered access practical by allowing devices to be dow]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
