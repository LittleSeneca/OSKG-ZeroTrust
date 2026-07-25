---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-threats
  - topic/zt-network
  - topic/zt-device
claim_id: "gb-ch10.5"
statement: "Social engineering and physical coercion are the threats ZT can't solve — only contain"
confidence: "high"
confidence_rationale: "HIGH on the framing — these are genuinely threats ZT doesn't eliminate. MEDIUM on the mitigations — behavioral analysis detects anomalies but doesn't"
claim_type: "threat"
source_note: "[[Gilman and Barth — Ch10 — The Adversarial View]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch10.5: Social engineering and physical coercion are the threats ZT can't solve — only contain

**Source:** [[Gilman and Barth — Ch10 — The Adversarial View]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

For social engineering: "A zero trust network can only do so much to defend against attacks enabled by an unwitting participant." For physical coercion: "Defending against these types of compromises is ill-advised. No security professional would ever tell someone in this situation to risk their physical well-being to protect the information that they have access to."

## Evidence

The social engineering discussion covers phishing and face-to-face communication (customer service attacks). Mitigations: behavioral analysis for less-sensitive resources, group authentication/authorization (Shamir's Secret Sharing) for critical assets. The physical coercion section includes the famous XKCD #538 reference ("someone with a blunt instrument can force even the most honest individuals to aid them") and recommends group authorization for high-value targets, with credential/device cycling and scanning for subtler physical attacks (USB insertion, unattended device tampering).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the framing — these are genuinely threats ZT doesn't eliminate. MEDIUM on the mitigations — behavioral analysis detects anomalies but doesn't prevent willing-but-deceived actions.

## Stakes

These two sections together acknowledge that the human element remains the irreducible vulnerability. Every technical control in ZT is mediated by humans who can be tricked, coerced, or compromised. The best defense is limiting the blast radius of any single human's compromise.

## Disagreement

**Who disagrees:**

NSA Embracing ZT's threat scenarios (compromised credentials, insider threat) directly parallel these concerns but frame them as ZT's raison d'être — the scenarios that prove ZT's value. Gilman & Barth are more cautious: ZT improves containment but doesn't prevent the initial compromise.

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

The XKCD reference is the right frame. Physical coercion is a solved problem in the only way it can be solved: accept it and limit blast radius. The social engineering discussion is thinner than it should be — Ch6 has more detail on mechanisms (Shamir's Secret Sharing) but this section serves more as a catalog entry than a deep analysis. The group authentication recommendation is repeated across both sections, which is correct — it's the only reliable mitigation for single-human compromise of critical systems.
