---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-migration
  - topic/zt-implementation
  - topic/zt-governance
claim_id: "nist207-ch7.2"
statement: "Pure greenfield ZTA is rarely viable for existing organizations, but new infrastructure projects (new applications, services, databases) create opportunities to introduce ZT concepts to some degree."
confidence: "high"
confidence_rationale: "HIGH. NIST's honesty about greenfield impracticality is notable — most ZT marketing implies greenfield is the target, but NIST says it's the"
claim_type: "migration"
source_note: "[[NIST 800-207 — Ch7 — Migration]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch7.2: Pure greenfield ZTA is rarely viable for existing organizations, but new infrastructure projects (new applications, services, databases) create opportunities to introduce ZT concepts to some degree.

**Source:** [[NIST 800-207 — Ch7 — Migration]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

In a greenfield scenario, an enterprise can design a pure ZTA from the start: identify workflows, narrow components, engineer against ZT tenets, evaluate trust before access, and establish micro-perimeters. But this is **rarely viable** for federal agencies or any organization with an existing network. (§7.1)

## Evidence

- NIST acknowledges the greenfield ideal but immediately caveats: "new responsibilities that require building new infrastructure (a new application, service, or database) create opportunities to introduce ZT concepts to some degree."
- Success depends on how dependent the new infrastructure is on existing resources (e.g., identity management systems).
- References [[NIST SP 800-160v1]] (Systems Security Engineering) as the companion framework for greenfield ZT design.

**Cross-reference:**

Finney's [[Project Zero Trust]] structures the entire book around an organizational narrative of how ZT adoption unfolds inside an enterprise — the greenfield scenario maps loosely to the "new initiative" pattern where a team gets to build fresh rather than retrofitting.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. NIST's honesty about greenfield impracticality is notable — most ZT marketing implies greenfield is the target, but NIST says it's the exception.

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
- [[hybrid-model-indefinite-reality|Since pure greenfield is rarely viable, the hybrid model is not a temporary concession but the expected and necessary mi]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
