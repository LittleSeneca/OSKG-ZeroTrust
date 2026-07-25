---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-trust
  - topic/zt-policy
claim_id: "nist207-ch3.6"
statement: "Trust algorithms vary on two axes — criteria/score-based and singular/contextual"
confidence: "medium"
confidence_rationale: "MEDIUM-HIGH — The taxonomy is analytically sound, but NIST significantly understates the operational complexity of contextual TAs. Maintaining state"
claim_type: "architectural"
source_note: "[[NIST 800-207 — Ch3 — Logical Components]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch3.6: Trust algorithms vary on two axes — criteria/score-based and singular/contextual

**Source:** [[NIST 800-207 — Ch3 — Logical Components]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

TAs differ along two dimensions: (a) Criteria-based (binary: all criteria must be met) vs. score-based (weighted confidence level compared to threshold), and (b) Singular (each request evaluated independently) vs. Contextual (subject's recent history considered). Contextual, score-based TAs provide the most dynamic and granular access control. A contextual TA can detect attacks that a singular TA misses (e.g., unusual access patterns, off-hours activity, anomalous volume).

## Evidence

**Key examples from NIST:**

- HR employee normally accesses 20–30 records/day → contextual TA alerts at 100+ in a day
- After-hours access from unrecognized location → contextual TA triggers additional authentication
- Accountant accessing financial system at midnight → contextual TA requires more stringent confidence level

**Cross-reference to CISA:**

CISA's "Optimal" maturity level describes "fully automated, context-aware access decisions with continuous risk assessment" — essentially NIST's contextual, score-based TA. The gap between CISA's Traditional and Optimal levels on this dimension is larger than for any other capability.

**Cross-reference to DoD:**

The DoD ZT RA specifies "dynamic, risk-based access decisions" (Capability 5.1) but acknowledges that "fully automated contextual decisions" are a Target-level capability, not achievable at Intermediate.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM-HIGH — The taxonomy is analytically sound, but NIST significantly understates the operational complexity of contextual TAs. Maintaining state on all subjects, training behavioral baselines, and tuning anomaly thresholds is hard. False positives from contextual TAs can cripple workflows.

## Stakes

_Not addressed separately in the source note._

## Disagreement

**Who disagrees:**

Practitioners who have attempted contextual TA deployments report that the tuning phase NIST mentions can last indefinitely, and many organizations operate effectively with criteria-based TAs augmented by periodic re-authentication rather than continuous behavioral analysis. The gap between the "ideally" contextual TA and practical implementations remains wide.

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
