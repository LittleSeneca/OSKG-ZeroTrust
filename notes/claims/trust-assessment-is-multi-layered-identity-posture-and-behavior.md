---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-identity
  - topic/zt-device
claim_id: "go-ch3-5.3"
statement: "Trust assessment is multi-layered — identity, posture, and behavior combine to produce an enforcement decision"
confidence: "medium"
confidence_rationale: "MEDIUM. The pipeline is conceptually sound and aligns with the NIST PDP model, but Green-Ortiz doesn't provide a computational model for combining"
claim_type: "implementation"
source_note: "[[Green-Ortiz — Ch3-5 — Trust and Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch3-5.3: Trust assessment is multi-layered — identity, posture, and behavior combine to produce an enforcement decision

**Source:** [[Green-Ortiz — Ch3-5 — Trust and Policy]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

Trust in Green-Ortiz is not a single score (as in Gilman & Barth) but a multi-dimensional assessment drawing from the five ZT pillars: Identity (who/what is this?), Vulnerability Management (is it secure right now?), Policy & Governance (what are the rules?), Enforcement (what can I control?), and Analytics (what does behavior look like?). The combination determines access. Ch5 makes this explicit: "the conditions for allowing data access should incorporate both the current aspects of an identity, including the user or asset based on the data collected by the various discovery mechanisms used."

## Evidence

Ch5's segmentation policy development procedure reveals the trust data pipeline:
1. **NAC consumes identity data** from flow logs to attribute communications to specific identities.
2. **DNS lookup** resolves external entities to names, adding context.
3. **IPAM/asset management** fills gaps for devices without dynamic identity (static addresses, legacy devices).
4. **Database of known endpoints** is built from all sources, with continual updates.
5. **Continual trust updates** from NAC, posture, XDR, and behavioral systems feed the enforcement policy.
6. **Integrations pass conclusions between systems** — when "an anomaly is detected, the integrations are leveraged to allow that conclusion to pass from one system to the other so that policy can be applied to provide an alert, perform mitigation and enforcement on a particular user or asset."
7. **Enforcement adjusts dynamically** — from "requiring another factor of authentication" to "complete network isolation."

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. The pipeline is conceptually sound and aligns with the NIST PDP model, but Green-Ortiz doesn't provide a computational model for combining these signals — it's a framework for what data to feed into policy, not how to compute a trust decision from it. Gilman & Barth's variable trust score model is more computationally explicit but less operationally comprehensive.

## Stakes

If trust assessment is only as good as its weakest data source, organizations need to understand which signals are load-bearing and which are supplementary. Green-Ortiz doesn't provide that prioritization — all five pillars are treated as equally important, which may not be practically achievable.

## Disagreement

**Who disagrees:**

Gilman & Barth propose a unified trust score computed by a trust engine — a quantitative model. Green-Ortiz proposes a multi-dimensional assessment consumed by policy rules — a qualitative model. Both can produce equivalent enforcement outcomes, but the operational trade-offs differ: a single trust score is simpler to implement but harder to debug; multi-dimensional rules are more transparent but harder to manage at scale.

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

Green-Ortiz's approach is the pragmatic enterprise answer to "how do you compute trust?" The answer is: you don't compute a single number. You collect identity, posture, and behavior data; you define policy rules that combine them; and you let the enforcement system apply those rules. It's less elegant than a unified trust engine but more aligned with how enterprises actually operate — with multiple security tools, each providing partial signals, integrated through a policy orchestration layer.
