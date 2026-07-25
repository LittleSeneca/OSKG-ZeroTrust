---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-trust
  - topic/zt-architecture
claim_id: "gb-ch4-6.2"
statement: "The trust engine is the novel contribution of ZT — using risk scoring to catch unknown attacks"
confidence: "medium"
confidence_rationale: 'MODERATE on the ML component (the authors themselves say "the zero trust model is still very new" and "known implementations still vary wildly")'
claim_type: "architectural"
source_note: "[[Gilman and Barth — Ch4-6 — Authorization Devices Users]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch4-6.2: The trust engine is the novel contribution of ZT — using risk scoring to catch unknown attacks

**Source:** [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"The trust engine is leveraged by the policy engine for risk analysis purposes. It leverages multiple data sources in order to compute a risk score, similar to a credit score. This score can be used to protect against unknown unknowns, and helps keep policy strong and robust without complicating it with edge cases and signatures."

## Evidence

The trust engine pulls from inventory systems (device, user) and historical data stores. The authors describe two approaches: (a) ad hoc static rules (e.g., "a device missing latest patches has its score reduced"), sufficient for early adoption; (b) machine learning on training data derived from activity labeled as trusted/untrusted. They argue mature systems use both — ML for predictive scoring, static rules for customization.

## Confidence

**Rating:** MEDIUM
**Rationale:** MODERATE on the ML component (the authors themselves say "the zero trust model is still very new" and "known implementations still vary wildly"). HIGH on the architectural claim that trust scoring should be separable from policy definition.

## Stakes

If trust scoring is wrong or gamed, the whole authorization system collapses to whatever static policy remains. Conversely, over-reliance on scoring without specific policy rules creates a "scoring monoculture" that clever attackers can optimize against.

## Disagreement

**Who disagrees:**

NIST 800-207 doesn't mandate trust scoring — it says the PE collects data and evaluates trust but doesn't prescribe a scoring function. NSA emphasizes deterministic compliance checks (patch level, config status) rather than probabilistic scoring. CISA's maturity model adds risk scoring only at Optimal maturity, not earlier.

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

The trust engine is the ZT component with the largest gap between aspiration and implementation. In 2017, Gilman & Barth envisioned ML-driven risk scoring. In practice, most ZT deployments in 2024 still rely primarily on static rules, with scoring limited to simple aggregations (device age, last seen, patch status). The "credit score" analogy is powerful but the data quality problem is harder than the authors anticipated.
