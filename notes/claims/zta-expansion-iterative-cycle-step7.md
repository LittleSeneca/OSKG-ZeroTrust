---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-migration
  - topic/zt-implementation
  - topic/zt-governance
claim_id: "nist207-ch7.11"
statement: "ZTA expansion follows the same iterative cycle — each new business process repeats steps 1–7 — and significant workflow changes trigger reevaluation of existing ZTA deployments, making the cycle both iterative and reactive."
confidence: "high"
confidence_rationale: "HIGH. The cyclical nature follows directly from the one-process-at-a-time migration model established in Claim 1."
claim_type: "migration"
source_note: "[[NIST 800-207 — Ch7 — Migration]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch7.11: ZTA expansion follows the same iterative cycle — each new business process repeats steps 1–7 — and significant workflow changes trigger reevaluation of existing ZTA deployments, making the cycle both iterative and reactive.

**Source:** [[NIST 800-207 — Ch7 — Migration]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

When enough confidence is gained, the enterprise enters the **steady operational phase** and begins planning the **next phase** of ZT deployment. (§7.3.7)

## Evidence

- Network and assets are still monitored, traffic is logged.
- Responses and policy modifications are done at a **lower tempo**.
- Subjects and stakeholders provide **feedback** to improve operations.
- **Change management:** If a significant change occurs to the workflow — new devices, major software updates, or shifts in organizational structure — the **entire process should be reconsidered**. However, not all steps need to be repeated from scratch.
- The deployment cycle is **both iterative and triggered**: it cycles through new business processes continuously, but is also triggered reactively by significant changes to existing ZTA-protected workflows.

**Cross-reference:**

The [[DoD ZT Strategy & Roadmap]] structures expansion as a phased progression through **target levels** (zero through advanced) across seven pillars, with explicit timelines and capability milestones. Finney's [[Project Zero Trust]] frames expansion as an organizational change management problem — each new process brought into ZTA is another team that must adapt their workflow.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The cyclical nature follows directly from the one-process-at-a-time migration model established in Claim 1.

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
  - [[zta-migration-incremental-recurring-cycle]]

## Assessment

_Not addressed separately in the source note._
