---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-migration
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-governance
claim_id: "nist207-ch7.4"
statement: "Before the 7-step cycle can begin, the enterprise must establish a foundational inventory of all actors, assets, and business processes — without this, the Policy Engine will deny requests due to insufficient information and shadow IT deployments may break silently."
confidence: "high"
confidence_rationale: "HIGH. The inventory-is-prerequisite claim is structural — it follows directly from the Policy Engine's need for input data to make access decisions."
claim_type: "migration"
source_note: "[[NIST 800-207 — Ch7 — Migration]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch7.4: Before the 7-step cycle can begin, the enterprise must establish a foundational inventory of all actors, assets, and business processes — without this, the Policy Engine will deny requests due to insufficient information and shadow IT deployments may break silently.

**Source:** [[NIST 800-207 — Ch7 — Migration]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

"An enterprise cannot determine what new processes or systems need to be in place if there is no knowledge of the current state of operations." (§7.3 prerequisites)

## Evidence

- Three parallel surveys form the prerequisite: actor inventory, asset inventory, process/data flow inventory.
- Without this baseline, the Policy Engine will deny requests due to insufficient information — especially problematic for unknown "shadow IT" deployments.
- The surveys map to the [[NIST SP 800-37]] Risk Management Framework (RMF) — ZTA adoption is fundamentally a risk reduction exercise.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The inventory-is-prerequisite claim is structural — it follows directly from the Policy Engine's need for input data to make access decisions.

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
- [[incomplete-knowledge-chicken-egg-barrier|The foundational inventory prerequisite is presented as the solution to the chicken-and-egg barrier — you must build inv]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
