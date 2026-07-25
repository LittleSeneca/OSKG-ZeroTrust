---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-1800-35
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-migration
claim_id: "nist-1800-35.4"
statement: "ZTA implementation is a continuous improvement journey, not a one-time project — seven sequential steps, with discovery and identity as the non-negotiable foundations."
confidence: "high"
confidence_rationale: "HIGH on the framework's validity — the seven steps are logically sequenced and reflect real implementation experience. MEDIUM on the achievability"
claim_type: "implementation"
source_note: "[[NIST 1800-35 — Implementing ZTA]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist-1800-35.4: ZTA implementation is a continuous improvement journey, not a one-time project — seven sequential steps, with discovery and identity as the non-negotiable foundations.

**Source:** [[NIST 1800-35 — Implementing ZTA]] — NIST, *SP 1800-35 — Implementing a Zero Trust Architecture*, 2023

## The Claim

ZTA implementation is a continuous improvement journey, not a one-time project — seven sequential steps, with discovery and identity as the non-negotiable foundations.

## Evidence

_No evidence separable from the claim statement in the source note._

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the framework's validity — the seven steps are logically sequenced and reflect real implementation experience. MEDIUM on the achievability for resource-constrained organizations — the framework assumes a level of tooling, staffing, and organizational maturity that smaller organizations may lack.

## Stakes

If organizations treat ZTA as a procurement exercise (buy the products, configure them, done), they'll fail. The journey framework emphasizes that ZTA is a process transformation with technology enablement, not the reverse. Step 3 (identify existing capabilities) is politically crucial — it gives organizations permission to build on what they have rather than starting over.

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

The seven-step framework is well-structured and likely to be widely cited. The emphasis on discovery (Step 1) as the *first* step — before policy, before technology — is correct and often overlooked. Organizations that skip discovery end up protecting assets they don't know about. The framework's weakness is that it doesn't provide estimated timelines or resource requirements for each step — a small organization and a federal agency both follow the same seven steps, but the implementation looks radically different. The "incremental" emphasis throughout is the framework's most important characteristic — it directly counters the paralyzing perception that ZTA requires a big-bang deployment.
