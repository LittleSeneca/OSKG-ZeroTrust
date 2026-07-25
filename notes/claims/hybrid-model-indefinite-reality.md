---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-migration
  - topic/zt-governance
  - topic/zt-maturity
claim_id: "nist207-ch7.3"
statement: "The hybrid model — ZTA workflows coexisting with non-ZTA workflows — is the expected indefinite reality, requiring common infrastructure (ID management, device management, logging) to operate in dual mode and migration to proceed one business process at a time."
confidence: "high"
confidence_rationale: "VERY HIGH. The hybrid reality is a core NIST assertion and consistent with every major ZT implementation account."
claim_type: "migration"
source_note: "[[NIST 800-207 — Ch7 — Migration]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch7.3: The hybrid model — ZTA workflows coexisting with non-ZTA workflows — is the expected indefinite reality, requiring common infrastructure (ID management, device management, logging) to operate in dual mode and migration to proceed one business process at a time.

**Source:** [[NIST 800-207 — Ch7 — Migration]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

"It is unlikely that any significant enterprise can migrate to zero trust in a single technology refresh cycle." The hybrid model is the expected reality for the indefinite future. (§7.2)

## Evidence

- Migration proceeds **one business process at a time**
- Common elements (identity management, device management, event logging) must be **flexible enough to operate in both ZTA and perimeter-based modes**
- Enterprise architects should **restrict ZTA candidate solutions to those that can interface with existing components**
- Migrating an existing workflow to ZTA likely requires at least a **partial redesign**
- The Policy Engine must handle both ZTA and legacy access patterns simultaneously

**Cross-reference:**

Gilman & Barth's [[Zero Trust Networks]] devotes substantial attention to the migration problem — their proxy-based architecture is explicitly designed to be introduced incrementally at the network boundary, making it one of the more migration-friendly ZTA deployment models. Green-Ortiz et al.'s [[Zero Trust Architecture]] treats migration as a formal lifecycle phase with maturity progression. The [[DoD ZT Strategy & Roadmap]] operationalizes this hybrid concept with target-level milestones for federal systems.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. The hybrid reality is a core NIST assertion and consistent with every major ZT implementation account.

## Stakes

_Not addressed separately in the source note._

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
- [[dual-mode-infrastructure-indefinite-hybrid|Dual-mode requirements only exist because the hybrid model is indefinite — without indefinite coexistence, infrastructur]]

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[zta-migration-incremental-recurring-cycle|The hybrid model is the reason the cycle is indefinite — you never finish because ZT and perimeter workflows coexist per]]

## Assessment

_Not addressed separately in the source note._
