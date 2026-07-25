---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-migration
  - topic/zt-policy
claim_id: "nist207-ch7.8"
statement: "Policy formulation for the ZTA candidate requires evaluating asset value/risk via RMF, identifying all upstream/downstream resources, and choosing between criteria-based (binary) and score-based (confidence-weighted) trust evaluation — a choice with cascading effects on tooling and operational complexity."
confidence: "high"
confidence_rationale: "HIGH. The criteria-vs-score choice is a genuine architectural decision point with documented tradeoffs."
claim_type: "migration"
source_note: "[[NIST 800-207 — Ch7 — Migration]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch7.8: Policy formulation for the ZTA candidate requires evaluating asset value/risk via RMF, identifying all upstream/downstream resources, and choosing between criteria-based (binary) and score-based (confidence-weighted) trust evaluation — a choice with cascading effects on tooling and operational complexity.

**Source:** [[NIST 800-207 — Ch7 — Migration]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

After identifying a candidate workflow, the enterprise must evaluate value/risk, identify all upstream/downstream resources, and determine access criteria. (§7.3.4)

## Evidence

1. **Evaluate the value/risk** of the asset or workflow using the NIST RMF ([[NIST SP 800-37]])
2. **Identify all upstream resources** (ID management systems, databases, micro-services), **downstream resources** (logging, security monitoring), and **entities** (subjects, service accounts)
3. **Determine the access criteria** — either criteria-based (TA using binary rules) or score-based (TA using confidence level weights) — see NIST 800-207 §3.3.1
- **Candidate selection influence:** An application used by a specific subset of subjects (e.g., purchasing) may be preferred over one vital to the entire subject base (e.g., email).
- **Tuning:** Administrators may need to adjust criteria or confidence weights during the tuning phase.

**Cross-reference:**

Gilman & Barth's [[Zero Trust Networks]] provides detailed guidance on constructing trust scores and policy logic. The [[DoD ZT Strategy]] mandates automated policy decision points with continuous runtime authorization.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The criteria-vs-score choice is a genuine architectural decision point with documented tradeoffs.

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
  - [[trust-algorithm-five-input-categories]]

**Extends:**

## Assessment

_Not addressed separately in the source note._
