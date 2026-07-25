---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-trust
  - topic/zt-architecture
  - topic/zt-definition
  - topic/zt-network
claim_id: "gc-ch1-3.13"
statement: "The implicit trust zone is the key architectural trade-off in ZT deployment."
confidence: "high"
confidence_rationale: "VERY HIGH. The implicit trust zone is the operationalization of \"zero implicit trust\" — it's where trust still exists in a ZT architecture"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Ch1-3 — Introduction and Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-ch1-3.13: The implicit trust zone is the key architectural trade-off in ZT deployment.

**Source:** [[Garbis and Chapman — Ch1-3 — Introduction and Architecture]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"By definition, any interactions between components that stay within the implicit trust zone occur outside of the control of the PEP. Naturally, you want to minimize the size of the implicit trust zone — understanding that there are trade-offs involved with each of the deployment models."

## Evidence

The implicit trust zone concept appears in every deployment model. Resource-based has the smallest zone (single resource OS). Enclave-based has a larger zone (all resources in the enclave, which "can and may communicate with one another outside the visibility and control of the PEP"). Cloud-routed inherits enclave-based zone properties. Microsegmentation has small zones but for server-to-server traffic only.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. The implicit trust zone is the operationalization of "zero implicit trust" — it's where trust still exists in a ZT architecture. Minimizing it is the architectural goal; the trade-off is deployment complexity.

## Stakes

The implicit trust zone is where attacks that bypass ZT controls will happen. If the zone is large (e.g., a full data center behind a single PEP), ZT provides minimal improvement over perimeter security. If the zone is small but deployment is impossible (legacy systems), ZT remains aspirational.

## Disagreement

**Who disagrees:**

Proponents of microsegmentation argue the implicit trust zone should be as small as a single process. Proponents of enclave-based models argue that well-understood communication patterns within an enclave make a larger zone acceptable. The debate is about acceptable risk, not architectural truth.

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

The implicit trust zone concept is the most important architectural insight for evaluating ZT deployments. It provides a single metric: "how large is your implicit trust zone, and what happens if something inside it is compromised?" This is the question that separates real ZT from ZT theater. The chapter's honest treatment of zone trade-offs — acknowledging that smaller zones come with higher deployment cost — is a model of pragmatic security architecture.
