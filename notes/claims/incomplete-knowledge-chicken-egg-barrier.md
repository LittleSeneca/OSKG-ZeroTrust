---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-migration
claim_id: "nist207-ch7.12"
statement: "The single biggest barrier to ZTA migration is incomplete knowledge of the enterprise — the three foundational inventories (actors, assets, processes) create a chicken-and-egg problem where you need complete inventories to migrate but need to migrate to justify building complete inventories."
confidence: "medium"
confidence_rationale: "MEDIUM-HIGH. The inventory dependency is structural, but whether it's the *single biggest* barrier is debatable — organizational resistance, budget"
claim_type: "migration"
source_note: "[[NIST 800-207 — Ch7 — Migration]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch7.12: The single biggest barrier to ZTA migration is incomplete knowledge of the enterprise — the three foundational inventories (actors, assets, processes) create a chicken-and-egg problem where you need complete inventories to migrate but need to migrate to justify building complete inventories.

**Source:** [[NIST 800-207 — Ch7 — Migration]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

The foundational inventory problem is the single biggest barrier to ZTA migration. (§7, architecture implications)

## Evidence

- Three parallel surveys form the prerequisite: actor inventory, asset inventory, process/data flow inventory.
- Without these, the Policy Engine cannot make accurate access decisions, and shadow IT deployments may break silently when ZTA policies are applied.
- The PE's ability to evaluate access requests depends directly on the quality of the three inventories. Incomplete inventories → denied access requests → business process failure.
- This creates a chicken-and-egg problem: you need complete inventories to migrate, but you need to migrate to justify building complete inventories.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM-HIGH. The inventory dependency is structural, but whether it's the *single biggest* barrier is debatable — organizational resistance, budget, and vendor lock-in are also significant.

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

_Not addressed separately in the source note._
