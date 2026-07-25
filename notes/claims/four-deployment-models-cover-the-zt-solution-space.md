---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-architecture
  - topic/zt-implementation
claim_id: "gc-ch1-3.12"
statement: "Four deployment models cover the ZT solution space, and each has distinct trade-offs that must be evaluated against enterprise requirements."
confidence: "high"
confidence_rationale: "HIGH. The four models accurately represent the commercial ZT landscape. Every major ZT vendor's architecture maps to one or more of these models. The"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Ch1-3 — Introduction and Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-ch1-3.12: Four deployment models cover the ZT solution space, and each has distinct trade-offs that must be evaluated against enterprise requirements.

**Source:** [[Garbis and Chapman — Ch1-3 — Introduction and Architecture]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"These deployment models will serve as a useful framework with which you can evaluate potential vendors, and examine their pros and cons."

| Model | Mechanism | Implicit Trust Zone | Best For | Key Limitation |
|-------|-----------|---------------------|----------|----------------|
| **Resource-Based** | PEP on every resource (user agent + resource gateway) | Very small (single resource) | High-security, greenfield | 1:1 PEP-to-resource ratio; legacy OS issues; tunnels blind inline security |
| **Enclave-Based** | PEP in front of resource enclave (one-to-many) | Larger (all resources in enclave) | Ephemeral workloads, IaaS, DevOps | Larger trust zone; PEPs become new ingress points |
| **Cloud-Routed** | Traffic transits vendor cloud; on-prem connectors make outbound only | Depends on enclave behind connectors | Remote users, simpler deployment | Latency; limited protocols; hairpinning for on-prem users; shadow IT risk |
| **Microsegmentation** | Resource-based variant with resources as subjects (NPEs); bidirectional control | Small (single resource) | Server-to-server, east-west traffic | Same cons as resource-based; weaker identity for NPEs; poor for user-to-service |

## Evidence

Each model is analyzed with explicit pros/cons, architectural diagrams, and operational considerations. The analysis draws on both NIST's models (resource-based and enclave-based) and adds two models (cloud-routed and microsegmentation) for completeness.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The four models accurately represent the commercial ZT landscape. Every major ZT vendor's architecture maps to one or more of these models. The pros/cons analysis is balanced and honest — the authors don't advocate for any single model.

## Stakes

Choosing the wrong deployment model for your environment leads to failed ZT initiatives. An organization with legacy mainframes can't do resource-based deployment. An organization with latency-sensitive applications can't do cloud-routed. The framework prevents these mistakes.

## Disagreement

**Who disagrees:**

Some vendors offer hybrid models that combine elements of multiple approaches. The authors acknowledge this: "They're also not necessarily mutually exclusive — some systems may well combine elements of several of these models." The models are analytical tools, not rigid categories.

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

The deployment model framework is the chapter's most reusable output. It gives architects a structured way to evaluate vendors: "Which deployment model(s) do you support? What are the trade-offs for each in my environment?" The enclave-based model's discussion of ephemeral workloads and API-driven policy application is particularly forward-looking and relevant for cloud-native environments.
