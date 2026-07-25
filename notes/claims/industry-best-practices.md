---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nstac
  - topic/zt-identity
  - topic/zt-governance
  - topic/zt-device
  - topic/zt-architecture
claim_id: "nstac.2"
statement: "Industry best practices — the Five-Step Process and the Kipling Method — should be the basis for federal ZT accountability metrics, not just technical checkbox completion."
confidence: "high"
confidence_rationale: "HIGH on the validity of the Five-Step Process as an industry standard. MEDIUM on whether federal agencies can meaningfully produce the quantifiable"
claim_type: "governance"
source_note: "[[NSTAC — ZT and Trusted Identity Management]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nstac.2: Industry best practices — the Five-Step Process and the Kipling Method — should be the basis for federal ZT accountability metrics, not just technical checkbox completion.

**Source:** [[NSTAC — ZT and Trusted Identity Management]] — NSTAC, *Zero Trust and Trusted Identity Management*, 2022

## The Claim

"Rather than propose technical success metrics, NSTAC strongly encourages federal agencies to reference the industry best-practice models in Section 2. These process-oriented principles, if firmly rooted in federal organizations after 2½ years, will be the best predictor of long-term success and sustained commitment to zero trust."

## Evidence

The report maps the Five-Step Process (Define Protect Surface → Map Transaction Flows → Build ZT Architecture → Create ZT Policy → Monitor and Maintain) to quantifiable progress metrics with reporting requirements at the agency CISO level or above:

| Step | Quantifiable Metric |
|------|-------------------|
| 1. Define Protect Surface | Organizational inventory of total DAAS elements on the ZT roadmap |
| 2. Map Transaction Flows | Percentage of instrumented and validated traffic flows |
| 3. Build ZT Architecture | Percentage of DAAS elements protected by an enforcement point |
| 4. Create ZT Policy | Percentage of DAAS elements protected by a defined ZT policy |
| 5. Monitor and Maintain | Month-over-month true/false positive percentages for security incidents |

An additional sixth tenet — "Commit to Transparency and Continuous Improvement" — requires each agency to publish at least one ZT use case annually documenting implementation lessons learned.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the validity of the Five-Step Process as an industry standard. MEDIUM on whether federal agencies can meaningfully produce the quantifiable metrics without significant investment in asset discovery and instrumentation first.

## Stakes

Process-based metrics prevent ZT from being reduced to a technology procurement checklist. But they require agencies to have basic visibility of their assets — something the report itself acknowledges many agencies lack: "some federal agencies... lack basic visibility of the data, assets, applications, and services in their organization, and as a result, are not yet ready to begin their zero trust journey."

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

The Five-Step Process metrics are the right kind of metrics — they measure progress on the journey, not arrival at a destination. The inclusion of "month-over-month true/false positive percentages" as a feedback loop metric is sophisticated: it measures whether ZT policies are actually improving security outcomes, not just whether they exist. The transparency tenet (annual use case publication) is a clever institutionalization mechanism — it creates peer pressure and shared learning across agencies.
