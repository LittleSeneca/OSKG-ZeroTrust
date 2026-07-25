---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-migration
  - topic/zt-implementation
  - topic/zt-cloud
  - topic/zt-architecture
claim_id: "nist207-ch7.13"
statement: "The indefinite hybrid period imposes dual-mode requirements on common infrastructure — ID management, device management, and logging must serve both ZTA and perimeter-based workflows simultaneously, and ZTA solutions must interface with existing enterprise components without requiring ZTA-only infrastructure."
confidence: "high"
confidence_rationale: "HIGH. The dual-mode requirement is a direct consequence of the hybrid model NIST establishes."
claim_type: "migration"
source_note: "[[NIST 800-207 — Ch7 — Migration]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch7.13: The indefinite hybrid period imposes dual-mode requirements on common infrastructure — ID management, device management, and logging must serve both ZTA and perimeter-based workflows simultaneously, and ZTA solutions must interface with existing enterprise components without requiring ZTA-only infrastructure.

**Source:** [[NIST 800-207 — Ch7 — Migration]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

NIST is explicit that pure ZTA is aspirational. The indefinite hybrid period means common infrastructure must operate in dual mode. (§7.2, architecture implications)

## Evidence

- ID management, device management, and logging must be dual-mode (ZTA + perimeter).
- ZTA solutions should interface with existing enterprise components.
- Common infrastructure must not be ZTA-only during transition.
- Migration proceeds at the granularity of individual business processes.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The dual-mode requirement is a direct consequence of the hybrid model NIST establishes.

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
- [[hybrid-model-indefinite-reality|Dual-mode infrastructure (ID mgmt, device mgmt, logging) is the concrete set of requirements that the indefinite hybrid]]

## Assessment

_Not addressed separately in the source note._
