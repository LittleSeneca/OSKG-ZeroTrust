---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-policy
  - topic/zt-architecture
  - topic/zt-implementation
  - topic/zt-governance
claim_id: "go-ch6-8.9"
statement: "The policy decision matrix — mapping source entities to destination entities with per-cell permit/deny, port/protocol, and directionality — is the output artifact of ZT planning, and multiple matrices will be needed across intra-data center, inter-site, and per-business-unit contexts."
confidence: "high"
confidence_rationale: "HIGH — The policy decision matrix is a concrete, implementable planning artifact. The monitor-mode-first mandate is consistent across all ZT sources"
claim_type: "architectural"
source_note: "[[Green-Ortiz — Ch6-8 — Implementation]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch6-8.9: The policy decision matrix — mapping source entities to destination entities with per-cell permit/deny, port/protocol, and directionality — is the output artifact of ZT planning, and multiple matrices will be needed across intra-data center, inter-site, and per-business-unit contexts.

**Source:** [[Green-Ortiz — Ch6-8 — Implementation]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

The segmentation planning process produces a matrix where each cell defines simple permit/deny, port/protocol policy, and directionality. The authors note multiple matrices will be needed — intra-data center, inter-site, and potentially per-business-unit.

## Evidence

Four business drivers define the segmentation charter: (1) Risk Assessments and Compliance — CMMC, PCI, ISO requirements mapped directly to the five ZT pillars, with specific CMMC assessment criteria quoted for each; (2) Threat Mapping — probability × impact of threats on critical systems; (3) Data Protection — confidentiality, integrity, availability as the trifecta; (4) Reducing Attack Surfaces — self-justifying even without regulatory mandate. Implementation guidance: "Monitor mode first — the organization should implement a discovery or monitor mode for as long as possible, and in parallel to other enforcement tasks being executed." Authorization of entities is "the most important outcome of the Zero Trust journey."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The policy decision matrix is a concrete, implementable planning artifact. The monitor-mode-first mandate is consistent across all ZT sources. The claim that authorization is the most important outcome provides clear prioritization.

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
