---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-identity
  - topic/zt-architecture
  - topic/zt-definition
  - topic/zt-device
claim_id: "gb-ch3.1"
statement: "The network agent is the marriage of user, device, and application — the atomic unit of authorization"
confidence: "high"
confidence_rationale: "HIGH. The agent construct is the implementation bridge between the abstract five assertions (Ch1) and concrete authorization decisions (Ch4). Every"
claim_type: "architectural"
source_note: "[[Gilman and Barth — Ch3 — Network Agents]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch3.1: The network agent is the marriage of user, device, and application — the atomic unit of authorization

**Source:** [[Gilman and Barth — Ch3 — Network Agents]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"A network agent is the term given to the combination of data known about the actors in a network request, typically containing a user, application, and device. Traditionally, these entities have been authorized separately, but zero trust networks recognize that policy is best captured as a combination of all participants in a request."

## Evidence

The chapter opens with the canonical ZT scenario: an organization that allows code commits from company-issued laptops but blocks source code access from phones. Here, "one factor has influenced the other — a user which might 'normally' have source code access won't enjoy such access from their mobile device." Without the agent construct, this cross-factor policy is awkward to express. With it, the policy is simply "authorize the agent" — the combined entity. The agent is formed on demand as the union of queried data at a point in time.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The agent construct is the implementation bridge between the abstract five assertions (Ch1) and concrete authorization decisions (Ch4). Every ZTNA product, service mesh sidecar, and BeyondCorp-style access proxy implements some version of this concept — even if they don't use the word "agent."

## Stakes

If the agent is the right atomic unit, then ZT authorization is fundamentally contextual — you can't authorize a user without knowing what device they're on, and you can't authorize a device without knowing who's using it. This invalidates any ZT implementation that does user auth and device auth as separate, sequential steps rather than as a single combined evaluation.

## Disagreement

**Who disagrees:**

Service mesh implementations (Istio, Linkerd) tend to authorize at the workload identity level without a user dimension, which is a simplified agent. Some argue that the user dimension belongs at the application layer, not the network layer. The authors' counter is that the agent includes "sparse data" by design — an autonomous system's agent might lack a user field entirely, and policy should handle that gracefully.

**Alternative reading:**

The agent could be seen as nothing more than a structured claim bundle — similar to a JWT with richer claims. The innovation isn't the data structure but the architectural insistence that authorization must consume the whole bundle at once, never piecemeal.

## Edges

**Depends on:**

**Supports:**
- [[the-three-layer-authorization-model-reveals-why-zt-is|The network agent defines the atomic unit of authorization (user+device+app) that the three-layer model enforces across]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

This is the chapter's most important contribution. NIST 800-207 talks about "all communication" being authenticated and authorized, but doesn't provide the granular entity model. Gilman & Barth give us the agent — the thing you actually write policy against. It's the difference between "we do ZT" and "we have an agent construct in our policy engine."
