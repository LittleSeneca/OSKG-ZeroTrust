---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-threats
  - topic/zt-monitoring
  - topic/zt-network
  - topic/zt-device
claim_id: "finney-ch8-11.12"
statement: "Deception technologies invert ZT — selectively add trust back to detect and disrupt attackers"
confidence: "medium"
confidence_rationale: "MODERATE. The NSA study is compelling anecdotal evidence, but the broader empirical case for deception effectiveness is still developing. The MITRE"
claim_type: "threat"
source_note: "[[Finney — Ch8-11 — Execution and Sustainability]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch8-11.12: Deception technologies invert ZT — selectively add trust back to detect and disrupt attackers

**Source:** [[Finney — Ch8-11 — Execution and Sustainability]] — George Finney, *Project Zero Trust*, 2022

## The Claim

Aaron introduces deception as a natural extension of ZT: "With Zero Trust, we've focused on removing all the trusts we can. But with deception, we can selectively add trusts back into the network using lures, beacons, breadcrumbs, and decoys." The **MITRE Engage** framework provides a structured approach to active defense: expose breadcrumbs → lure attackers → disrupt their visibility → induce them to reveal toolkits → feed threat intel back into protect surface controls.

## Evidence

- NSA study: Penetration testers told deception was in use began doubting their own tools and questioned whether vulnerable targets were decoys. This effect persisted even when deception was NOT actually deployed.
- Analogy: "Like when people put a home alarm monitoring company sign on their house but don't actually have an alarm."
- The psychology: "Deception brings the fight to the mind of the adversary" — disrupts the attacker's trust in their own telemetry and tools.

**Cross-reference — Gilman & Barth Ch10:**

Where Gilman & Barth analyze threats through the adversary's lens (what can they do?), Finney extends the adversarial view into the defender's active response (what can we do *to* them?). This is a natural progression from passive ZT to active defense.

## Confidence

**Rating:** MEDIUM
**Rationale:** MODERATE. The NSA study is compelling anecdotal evidence, but the broader empirical case for deception effectiveness is still developing. The MITRE Engage framework is well-structured but less battle-tested than ATT&CK.

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

Deception is the operationalization of the "assume breach" mindset. If you assume an attacker is already inside, you need more than preventive controls — you need detection mechanisms that work even when the attacker believes they're undetected. Deception turns the attacker's own assumptions (trust in their tools, trust in what they see) against them. This is the logical endpoint of the ZT philosophy applied to the offense/defense relationship.
