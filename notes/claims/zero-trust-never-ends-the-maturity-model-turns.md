---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-maturity
  - topic/zt-migration
claim_id: "finney-ch8-11.11"
statement: "Zero Trust never ends — the maturity model turns a six-month project into a multi-year strategic journey"
confidence: "high"
confidence_rationale: "HIGH. The CMM-based maturity model is standard practice (CISA ZTMM uses a similar approach). The 6-9 month budget-cycle alignment is operationally"
claim_type: "maturity"
source_note: "[[Finney — Ch8-11 — Execution and Sustainability]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch8-11.11: Zero Trust never ends — the maturity model turns a six-month project into a multi-year strategic journey

**Source:** [[Finney — Ch8-11 — Execution and Sustainability]] — George Finney, *Project Zero Trust*, 2022

## The Claim

The six-month timeline was chosen because it aligns with corporate budget cycles, not because ZT can be "completed" in six months. The **Zero Trust Maturity Model** (CMM-based: Initial → Repeatable → Defined → Managed → Optimized) maps each of the five design methodology steps against five maturity levels per protect surface. Organizations should baseline, set strategic goals per protect surface, and phase improvements across budget cycles. Not every protect surface needs the same maturity level.

## Evidence

- Aaron: "I recommend to all our clients that we focus our efforts into six-to-nine-month initiatives. The biggest reason is the corporate budget cycle."
- The maturity model (Appendix B) provides a 5×5 matrix: each methodology step (define protect surface, map transaction flows, architect environment, create policy, monitor/maintain) measured at five maturity levels.
- The **transaction flow matrix** shows how protect surfaces interact — blast radius from a compromise in one protect surface affects others. This forces holistic prioritization, not isolated per-surface maturity.
- Next-phase recommendations: BAS (Breach and Attack Simulation) for continuous flow mapping, deception technologies (MITRE Engage) for active defense.

**Cross-reference — CISA ZTMM:**

CISA's maturity model operates across five pillars (Identity, Device, Network, Application, Data) with four maturity stages. Finney's model operates across the five methodology steps per protect surface. They are complementary: CISA tells you *what* to mature, Finney tells you *how* to mature each protect surface's design. Together, they provide orthogonal maturity measurement.

**Cross-reference — NIST 800-207 Ch7:**

NIST's migration chapter describes the 7-step cycle but doesn't provide a maturity measurement framework. Finney's CMM model fills this gap.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The CMM-based maturity model is standard practice (CISA ZTMM uses a similar approach). The 6-9 month budget-cycle alignment is operationally realistic and addresses the biggest reason ZT initiatives fail — loss of funding between phases.

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

The maturity model is the book's structural answer to "what comes after the initial implementation." Without it, ZT is a one-time project that decays. With it, ZT becomes an operational discipline that improves over time.
