---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-app
  - topic/zt-cloud
claim_id: "finney-ch8-11.4"
statement: "Container security standards must be enforced as code, with negative checks"
confidence: "medium"
confidence_rationale: "MEDIUM. Confidence not explicitly stated in source."
claim_type: "implementation"
source_note: "[[Finney — Ch8-11 — Execution and Sustainability]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch8-11.4: Container security standards must be enforced as code, with negative checks

**Source:** [[Finney — Ch8-11 — Execution and Sustainability]] — George Finney, *Project Zero Trust*, 2022

## The Claim

Boris and Dylan define container security requirements that can be enforced programmatically in the CI/CD pipeline: Unix sockets (not TCP), no privileged mode, no privilege escalation, resource limits, no inter-container communication, read-only filesystem, and automated validation of third-party images.

## Evidence

The conversation is practical and developer-facing. Docker's security model allows these controls, but they must be explicitly configured. The "negative check" concept — test that something *isn't* present (e.g., privileged mode flag) — is the most operationally valuable idea here.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. Confidence not explicitly stated in source.

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

This section is thin compared to Gilman & Barth's treatment of application trust (Ch7), but it serves the narrative purpose — showing security being pushed left into the development pipeline.
