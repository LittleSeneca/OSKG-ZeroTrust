---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-trust
  - topic/zt-architecture
claim_id: "gb-ch2.3"
statement: "Variable trust scores replace binary policy with continuous, dynamic authorization"
confidence: "high"
confidence_rationale: "HIGH in principle, MODERATE in implementation. The conceptual model is sound and has been adopted by every major ZT product (Zscaler's risk score"
claim_type: "architectural"
source_note: "[[Gilman and Barth — Ch2 — Managing Trust]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch2.3: Variable trust scores replace binary policy with continuous, dynamic authorization

**Source:** [[Gilman and Barth — Ch2 — Managing Trust]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

The core innovation of ZT trust management is replacing binary access decisions with a variable trust score: "Instead of defining binary policy decisions assigned to specific actors in the network, a zero trust network will continuously monitor the actions of an actor on the network to update their trust score." This score is then measured against the sensitivity of the requested resource — a calendar view needs a low score, changing system settings needs a high score. The credit agency analogy crystallizes the insight: just as credit scores let lenders make risk-based decisions without personally evaluating each borrower, trust scores let the control plane make authorization decisions without enumerating every possible access scenario.

## Evidence

The credit agency analogy is the central piece of evidence. The argument is that binary policies create perverse incentives — either the policy is too rigid (creating human toil to continually adjust) or too loose (resulting in weak security). A trust score captures "a number of conditions without complicating the policy with edge cases" and allows "authorization systems to adjust to novel threats." Figure 2-3 illustrates how fewer score-based policies replace many binary policies.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH in principle, MODERATE in implementation. The conceptual model is sound and has been adopted by every major ZT product (Zscaler's risk score, Okta's risk-based authentication, Google's access tiers). But the chapter's treatment of HOW scores are computed is thin — that's deferred to the trust engine discussion and Chapter 3.

## Stakes

If trust scores are computable and reliable, ZT authorization becomes genuinely adaptive. If scores are noisy, gamed, or opaque, they create new attack surfaces and user frustration. The authors acknowledge the key concern: "Could it be possible for a persistent attacker to slowly build their credibility in a system to gain more access?" Their mitigations (requiring extended normal behavior, binding scores to device/application metadata, multi-signal authentication) are sensible but not proven.

## Disagreement

**Who disagrees:**

The NIST 800-207 model doesn't explicitly require trust scores — it requires policy decisions based on "as many sources of data as possible" (Tenet 6), which could be implemented with binary rules on top of many attributes. Some security engineers argue that trust scores create an opaque, unexplainable authorization system where users don't understand why they were denied — a legitimate usability concern the authors acknowledge but don't fully resolve.

**Alternative reading:**

Variable trust can be read as an implementation detail rather than a fundamental ZT property. You can build a ZT network with complex, multi-attribute binary policies that achieve the same effect. The trust score is an aggregation mechanism, not a requirement.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

This is the most conceptually important claim in Ch2 and the one that most distinguishes ZT from traditional network security. Traditional security asks "is this allowed?" ZT asks "how trustworthy is this right now?" The shift from static rules to continuous evaluation is what makes ZT networks genuinely more secure, not just differently architected. The credit agency analogy is brilliant pedagogy — it makes an abstract concept immediately intuitive.
