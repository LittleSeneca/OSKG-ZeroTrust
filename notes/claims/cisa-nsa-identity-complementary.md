---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-identity
  - topic/zt-governance
  - topic/zt-definition
  - topic/zt-implementation
claim_id: "cisa-ztmm-id.8"
statement: 'CISA and NSA identity frameworks are complementary, not redundant — CISA provides the maturity model framework (what to measure, what "good" looks like for FCEB agencies), while NSA provides the implementation roadmap (how to get there, tailored for national security systems but broadly applicable), and together they form the most complete federal guidance for identity maturity in a ZTA context.'
confidence: "medium"
confidence_rationale: "MEDIUM-HIGH. The complementary relationship is visible when the two documents are compared side-by-side, but neither document explicitly frames"
claim_type: "governance"
source_note: "[[CISA ZTMM — Identity Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-id.8: CISA and NSA identity frameworks are complementary, not redundant — CISA provides the maturity model framework (what to measure, what "good" looks like for FCEB agencies), while NSA provides the implementation roadmap (how to get there, tailored for national security systems but broadly applicable), and together they form the most complete federal guidance for identity maturity in a ZTA context.

**Source:** [[CISA ZTMM — Identity Pillar]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

This is a synthesis claim by this note's author comparing the two frameworks.

## Evidence

- CISA's four functions (Authentication, Identity Stores, Risk Assessments, Access Management) map to NSA's four ICAM sub-capabilities (Credential Management, Identity Management, Access Management, Federation) with tight alignment at each maturity level.
- NSA provides much more tactical detail: PAM tools, privileged access workstations, ABAC models, fine-grained risk-adaptive access policies.
- CISA provides the maturity *targets*; NSA provides the *how-to*.

**Key takeaways from the synthesis:**

1. **Authentication is the keystone function.** The jump from Traditional (passwords) to Advanced/Optimal (phishing-resistant MFA + continuous validation) is the largest single capability gap.

2. **Identity stores must be integrated, not just federated.** Optimal means identity data flows seamlessly between on-prem, cloud, and partner systems.

3. **Risk assessment evolves from static → dynamic → continuous.** At Optimal, it's a real-time feed into every access decision.

4. **Access management is where least privilege becomes operational.** CISA's progression (permanent → expiring → session-based → JIT/JEA) operationalizes the principle. NSA adds the tactical layer.

5. **ICAM is the substrate beneath this entire pillar.** As NIST 800-207 Chapter 6 makes explicit: *without mature ICAM, ZTA cannot function.*

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM-HIGH. The complementary relationship is visible when the two documents are compared side-by-side, but neither document explicitly frames itself as complementary to the other. This is an analytical observation.

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
