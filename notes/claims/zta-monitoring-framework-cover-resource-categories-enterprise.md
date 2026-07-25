---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207a
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-identity
claim_id: "nist-207a.7"
statement: "A ZTA monitoring framework must cover all resource categories (enterprise, non-enterprise, personal), application infrastructure elements, user access requests with full service-call chains, and directory changes — with telemetry feeding back into access decisions and step-up authentication."
confidence: "medium"
confidence_rationale: "MEDIUM. The requirements are comprehensive but aspirational — full call-chain monitoring across multi-cloud is a significant instrumentation"
claim_type: "implementation"
source_note: "[[NIST 800-207A — Cloud-Native Access Control]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist-207a.7: A ZTA monitoring framework must cover all resource categories (enterprise, non-enterprise, personal), application infrastructure elements, user access requests with full service-call chains, and directory changes — with telemetry feeding back into access decisions and step-up authentication.

**Source:** [[NIST 800-207A — Cloud-Native Access Control]] — NIST, *SP 800-207A — Cloud-Native Access Control*, 2023

## The Claim

Monitoring should cover "every user access request and the subsequent series of service calls needed to complete the user request as in microservices-based applications" (MON-CNA-REQ-3, lines 1126–1128).

## Evidence

- Four monitoring requirements (MON-CNA-REQ-1 through 4, lines 1120–1131): resource coverage, infrastructure element coverage, full call-chain coverage, directory change coverage.
- Two telemetry use cases (MON-DATA-USE-1 and 2, lines 1133–1160): behavioral context for access decisions, fine-tuning access rights via observe-and-adjust.
- Step-up authentication triggered by monitoring signals: "asking for more information from users or resorting to a stronger form of authentication" (lines 1157–1160).

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. The requirements are comprehensive but aspirational — full call-chain monitoring across multi-cloud is a significant instrumentation challenge. The observe-and-lock-down methodology (lines 1040–1044) — "utilizing this observe-and-lock-down methodology builds the organizational processes required to maintain the lifecycle of these policies over time" — is operationally sound but assumes monitoring maturity many organizations lack.

## Stakes

If monitoring is incomplete, the ZTA feedback loop breaks — you're enforcing policies without knowing if they're working, and you can't do the continuous improvement that ZTA requires.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[cloud|Monitoring telemetry feeds back into the service mesh's access decisions and step-up authentication, closing the policy]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The monitoring section establishes the right requirements but understates the implementation difficulty. The call-chain monitoring requirement (MON-CNA-REQ-3) is particularly ambitious — distributed tracing across microservices (e.g., Jaeger, Zipkin) can provide this, but it requires application instrumentation, not just infrastructure monitoring. The document's value here is in setting the bar rather than providing implementation guidance (which is deferred to SP 800-204A/B).
