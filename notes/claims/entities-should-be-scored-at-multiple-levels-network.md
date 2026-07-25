---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-trust
  - topic/zt-identity
  - topic/zt-device
claim_id: "gb-ch4-6.4"
statement: "Entities should be scored at multiple levels — network agent, device, and user"
confidence: "high"
confidence_rationale: 'HIGH on the architectural claim, MODERATE on implementation practicality. The authors acknowledge: "Presenting so many scores for consideration when'
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch4-6 — Authorization Devices Users]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch4-6.4: Entities should be scored at multiple levels — network agent, device, and user

**Source:** [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"Taken as a whole, it seems like the right solution is to score both the network agent itself and the underlying entities that make up the agent."

## Evidence

Three scenarios: (1) brute-force attack on user credentials → score the attacker's network agent, not the user account (avoids denial-of-service via lockout); (2) compromised device → all network agents on that device should be penalized; (3) malicious human user moving across kiosk devices → the user's score should follow them. Each scenario demonstrates that scoring only the agent is insufficient.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the architectural claim, MODERATE on implementation practicality. The authors acknowledge: "Presenting so many scores for consideration when writing policy, however, can make the task of crafting policy more difficult and error prone."

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

The multi-entity scoring framework anticipates the layered trust model that later became standard. Modern ZT implementations tend to score the session (agent + device + user composite) rather than exposing individual entity scores to policy writers, which addresses the "error prone" concern.
