---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-architecture
  - topic/zt-authentication
  - topic/zt-network
  - topic/zt-policy
claim_id: "gb-ch4-6.13"
statement: "SSO should not remove the control plane from ongoing authorization"
confidence: "medium"
confidence_rationale: "MEDIUM. Confidence not explicitly stated in source."
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch4-6 — Authorization Devices Users]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch4-6.13: SSO should not remove the control plane from ongoing authorization

**Source:** [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"When designing authentication systems in a zero trust network, aim for as much control plane responsibility as possible, and validate authorization with the control plane as often as is reasonably possible."

## Evidence

SSO provides: single authentication point, centralized credential storage, reduced credential surface area. But the common pattern of "validate token at session start, then let the application manage its own session" is "generally undesirable" because "trust variance and invalidation is a key aspect of a zero trust network." The control plane should revalidate on every request or as frequently as latency allows.

**Cross-reference — NIST 800-207 Ch7 (Migration):**

This maps to the "per-session" access model. NIST's guidance on proxy/gateway migration models depends on this continuous revalidation property.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. Confidence not explicitly stated in source.

## Stakes

_Not addressed separately in the source note._

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
- [[the-control-plane-is-the-trust-grantor-temporary|The recommendation that SSO not bypass ongoing authorization logically requires the control plane to be the authoritativ]]

**Supports:**
- [[control-plane-compromise-is-the-worst-case-scenario-and|The danger of SSO bypassing the control plane is underscored by the fact that control plane compromise is the worst-case]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
