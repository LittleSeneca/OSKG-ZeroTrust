---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-threats
  - topic/zt-network
claim_id: "gb-ch10.2"
statement: "DDoS is still a problem — ZT doesn't mitigate it, it reframes how you respond"
confidence: "medium"
confidence_rationale: "MEDIUM-HIGH. The policy-derived filtering approach is clever and genuinely novel — converting ZT's detailed knowledge of expected communication"
claim_type: "threat"
source_note: "[[Gilman and Barth — Ch10 — The Adversarial View]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch10.2: DDoS is still a problem — ZT doesn't mitigate it, it reframes how you respond

**Source:** [[Gilman and Barth — Ch10 — The Adversarial View]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"While the architecture strives to authenticate and authorize just about everything on the network, it does not provide good mitigation against denial-of-service (DoS) attacks on its own. Distributed DoS (DDoS) attacks that are volumetric in nature can be particularly troublesome."

## Evidence

The authors acknowledge that "darkening" internet-facing endpoints via pre-authentication protocols (deny-all rules, narrow exceptions based on signaling) helps obscure addresses but "does not fundamentally mitigate DDoS attacks." Their key innovation: **policy-derived upstream filtering** — use ZT policy information about expected traffic patterns to calculate coarse, stateless enforcement rules for upstream devices. This has two advantages: fully automated configuration, and stateless operation that "obviates the need for expensive hardware and complicated state replication schemes."

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM-HIGH. The policy-derived filtering approach is clever and genuinely novel — converting ZT's detailed knowledge of expected communication patterns into upstream scrubber rules. But it only works for large networks that control their own upstream infrastructure. Cloud-native deployments are told to "leverage an online DDoS-prevention service" — which is the same advice for non-ZT networks.

## Stakes

If the control plane itself is DDoS'd, the entire ZT network becomes unavailable — because nothing happens without the PE/PA. This is the ZT-specific DoS vulnerability that the authors don't address directly (NIST 800-207 §5.2 does).

## Disagreement

**Who disagrees:**

NIST 800-207 §5.2 identifies the PE/PA as DDoS targets specifically — a vulnerability the authors mention only implicitly through their control plane security discussion. NSA Embracing ZT subsumes availability under "assume breach" — the expectation is rapid recovery rather than prevention.

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

This is one of the chapter's weakest sections — honest but thin. The policy-derived filtering idea is interesting but underdeveloped. The real concern (control plane availability) is deferred to the control plane security section. In practice, cloud-hosted ZT implementations (Zscaler, Cloudflare One) solve this through provider-scale DDoS protection, which the authors correctly identify as the pragmatic answer for most deployments.
