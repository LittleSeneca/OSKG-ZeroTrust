---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-network-pillar
  - topic/zt-network
  - topic/zt-maturity
  - topic/zt-implementation
  - topic/zt-segmentation
claim_id: "nsa-network.6"
statement: "The four capabilities form an integrated, sequential maturity journey"
confidence: "high"
confidence_rationale: "HIGH on the logical dependencies. MEDIUM on whether the sequence must be strictly sequential in practice — organizations with existing macro"
claim_type: "maturity"
source_note: "[[NSA — Network Environment Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-network.6: The four capabilities form an integrated, sequential maturity journey

**Source:** [[NSA — Network Environment Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the Network and Environment Pillar*, 2024

## The Claim

To mature network and environment capabilities, an organization should: (1) map data flows based on usage patterns and operational business requirements; (2) properly segment the network at both macro and micro levels; (3) use SDN for centralized control and automated tasking where available and practical; (4) automate security policies to gain operational efficiency and agility; (5) use risk-based methodologies to define access rules that ensure malicious or unauthorized traffic is dropped prior to reaching network resources at the perimeter, macro, and micro boundaries.

## Evidence

The sequential structure of the document (data flow mapping → macro → micro → SDN) itself argues for sequential dependency. You cannot segment without understanding flows. You cannot micro-segment effectively without macro segmentation as a foundation. You cannot manage micro segmentation at scale without SDN or equivalent automation.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the logical dependencies. MEDIUM on whether the sequence must be strictly sequential in practice — organizations with existing macro segmentation can begin micro segmentation pilots before completing comprehensive data flow mapping, and SDN adoption can begin in parallel with segmentation efforts.

## Stakes

The implied message is that skipping steps creates fragility. An organization that deploys SDN-enabled micro segmentation without data flow mapping will build segmentation rules based on assumptions rather than reality — and will discover broken workflows and shadow IT paths the hard way.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
- [[micro-segmentation-blast-radius|Micro segmentation is the third phase in the integrated maturity progression.]]
- [[macro-segmentation-cross-function|The sequential maturity framework requires macro segmentation as the second phase after data flow mapping.]]
- [[data-flow-mapping-foundational-capability|The maturity journey explicitly builds on data flow mapping as its foundation: 'you cannot segment without understanding]]

**Supports:**
- [[zt-control-data-plane-split|Maturity journey culminates in SDN, which embodies the control/data plane split as the architectural end-state]]
- [[micro-segmentation-blast-radius|Maturity model positions micro segmentation as the phase following macro]]
- [[macro-segmentation-cross-function|Maturity model positions macro segmentation as a foundational sequential phase]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
  - "[[cross-pillar-maturity-trajectory]]"

## Assessment

The five summary recommendations at the end of the document form a complete implementation checklist. Combined with the maturity tables, they provide more actionable guidance than CISA's Network pillar (which describes maturity *levels* but not the *sequence* of capability development). NSA's contribution relative to CISA is making the implementation pathway explicit.
