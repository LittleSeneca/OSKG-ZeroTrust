---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-migration
  - topic/zt-implementation
claim_id: "go-ch9-11.3"
statement: "Brownfield environments require 3–4× the timeline of greenfield deployments because every newly profiled device forces recursive re-analysis of previously identified devices."
confidence: "high"
confidence_rationale: "HIGH — The 3–4× multiplier is a specific empirical finding from documented Cisco services engagements. This claim is directly actionable for project"
claim_type: "migration"
source_note: "[[Green-Ortiz — Ch9-11 — Advanced and Future]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch9-11.3: Brownfield environments require 3–4× the timeline of greenfield deployments because every newly profiled device forces recursive re-analysis of previously identified devices.

**Source:** [[Green-Ortiz — Ch9-11 — Advanced and Future]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

The authors contrast greenfield (new building, no existing endpoints, systematic and deterministic, 1× baseline) with brownfield (existing network, all devices expected to keep working, requires recursive analysis as each unique device is identified, 3–4× baseline).

## Evidence

SBC Emerging Tech (brownfield): 3 months of recursive identification where every newly profiled device required re-running the analysis against all observed devices. SBC Financial's site selection matrix prioritized both business criticality and variety of endpoints — heterogeneous sites yield more profiling lessons that transfer. The authors recommend starting where both conditions exist: large device variety AND on-site presence ("sneaker net") for physical identity validation.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The 3–4× multiplier is a specific empirical finding from documented Cisco services engagements. This claim is directly actionable for project planning.

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
