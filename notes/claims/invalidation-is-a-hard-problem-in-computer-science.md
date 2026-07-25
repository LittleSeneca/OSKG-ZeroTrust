---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-access-mgmt
  - topic/zt-implementation
claim_id: "gb-ch10.6"
statement: 'Invalidation is a "hard problem in computer science" — ZT addresses it through granular authorization, not push-based revocation'
confidence: "high"
confidence_rationale: "HIGH. The pull-model limitation is real and honest. The progression from option 1 to 3 is a clear engineering tradeoff analysis."
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch10 — The Adversarial View]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch10.6: Invalidation is a "hard problem in computer science" — ZT addresses it through granular authorization, not push-based revocation

**Source:** [[Gilman and Barth — Ch10 — The Adversarial View]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"Invalidation is a hard problem in computer science. In the context of a zero trust network, invalidation applies chiefly to long-running actions that were previously authorized but are no longer."

## Evidence

Three approaches are presented in increasing sophistication: (1) more granular authorizations on short-lived actions (application-level requests instead of TCP sessions), (2) periodic session resets enforcing maximum lifetimes, (3) the best approach — enforcement components track ongoing actions and periodically reauthorize by querying the policy engine, forcibly resetting sessions if authorization is revoked. The authors note this is still a "pull" model — sessions can only be invalidated as fast as the longest polling period — but acknowledge push/event-based models "come with additional complexities and challenges which perhaps outweigh the benefits."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The pull-model limitation is real and honest. The progression from option 1 to 3 is a clear engineering tradeoff analysis.

## Stakes

If your polling period is 5 minutes and credential revocation happens at t=0, the attacker retains access until t=5. The question is whether that gap is acceptable. For most enterprises, yes. For high-security environments (defense, critical infrastructure), no — which is why push-based revocation is an active research area.

## Disagreement

**Who disagrees:**

NIST 800-207 §5.7 addresses a related concern with NPEs (non-person entities) — if autonomous agents make authorization decisions at machine speed, the invalidation gap becomes more dangerous. Gilman & Barth don't address NPEs (their 2017 framing predates widespread AI-agent deployment in security operations). Google BeyondCorp's Access Proxy model uses short-lived tokens with continuous revalidation, which is effectively approach 3 with a very short polling period.

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

This is one of the chapter's strongest sections — clearly framed, honestly bounded, with a practical solution progression. The willingness to admit that push-based models "perhaps outweigh the benefits" is characteristic of the authors' engineering pragmatism. The open question — which the authors don't address — is whether authorization granularity should be driven by risk (higher-risk resources get per-request authorization, lower-risk get per-session) or uniformly applied. The implicit answer is risk-driven, which is the right one.
