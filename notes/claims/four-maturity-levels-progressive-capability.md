---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-maturity
  - topic/zt-governance
  - topic/zt-identity
  - topic/zt-migration
claim_id: "cisa-ztmm-ov.7"
statement: "The four maturity levels define progressive capability from static/manual to dynamic/automated"
confidence: "high"
confidence_rationale: "HIGH. The maturity levels are internally consistent and follow a clear progression logic: manual → automated → dynamic. The descriptions are specific"
claim_type: "maturity"
source_note: "[[CISA ZTMM — Overview and Framework]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-ov.7: The four maturity levels define progressive capability from static/manual to dynamic/automated

**Source:** [[CISA ZTMM — Overview and Framework]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

The four maturity stages are Traditional, Initial, Advanced, and Optimal, each representing "greater levels of protection, detail, and complexity for adoption."

## Evidence

The document provides detailed criteria for each level:

| Level | Key Characteristics |
|-------|-------------------|
| **Traditional** | Manually configured lifecycles; static security policies; pillar-siloed enforcement; least privilege only at provisioning; manual incident response; limited log correlation |
| **Initial** | Starting automation of attribute assignment; initial cross-pillar solutions; some responsive least-privilege changes; aggregated visibility for internal systems |
| **Advanced** | Automated lifecycle controls with cross-pillar coordination; centralized visibility and identity control; policy enforcement integrated across pillars; risk/posture-based least privilege; building toward enterprise-wide awareness |
| **Optimal** | Fully automated, just-in-time lifecycles; self-reporting assets; dynamic policies from automated triggers; dynamic least privilege (just-enough); cross-pillar interoperability with continuous monitoring; centralized comprehensive situational awareness |

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The maturity levels are internally consistent and follow a clear progression logic: manual → automated → dynamic. The descriptions are specific enough to be auditable — an assessor can identify which level a function currently occupies.

## Stakes

If Optimal is unrealistic (fully automated, just-in-time everything), agencies may view the entire model as aspirational and disengage. The document mitigates this by stating that different pillars can be at different levels — an agency doesn't need Optimal Identity before starting on Devices. But the risk of Optimal as an unattainable "perfect state" is real.

## Disagreement

**Who disagrees:**

Some practitioners argue that the Traditional → Initial → Advanced → Optimal progression implies a linear path when ZTA adoption is often non-linear — an agency might achieve Advanced in Data but remain Traditional in Devices. The document explicitly permits this ("each pillar can progress at its own pace"), but the four-level progression still visually implies linearity.

**Alternative reading:**

The maturity levels could be read as a procurement roadmap rather than a technical assessment — Traditional justifies current spend, Initial justifies first investments, Advanced justifies major programs, and Optimal justifies indefinite sustainment funding. This reading is cynical but not inconsistent with how federal budget cycles work.

## Edges

**Depends on:**

**Supports:**
- [[zero-trust-never-ends-the-maturity-model-turns|The four progressive maturity levels (Traditional→Initial→Advanced→Optimal) provide the scaffolding that turns a short-t]]
- [[zt-maturity-incremental|nsa-embrace.4 claims ZT maturity is incremental, not binary. cisa-ztmm-ov.7 supports this by providing the concrete four]]
  - "[[cross-pillar-maturity-trajectory]]"

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The maturity levels are the most valuable part of the ZTMM because they're specific. "Traditional" for Authentication means "passwords or MFA with static access" — that's testable. "Advanced" means "phishing-resistant MFA with password-less FIDO2/PIV" — also testable. This specificity is what makes the ZTMM actionable where NIST 800-207 is architectural. The risk of Optimal-as-perfect is managed by the document's explicit permission for asynchronous pillar progress.
