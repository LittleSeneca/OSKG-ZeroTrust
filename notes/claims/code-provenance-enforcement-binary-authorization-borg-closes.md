---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/beyondprod
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-network
  - topic/zt-governance
claim_id: "beyondprod.3"
statement: "Code provenance enforcement (Binary Authorization for Borg) closes a critical gap that most ZT frameworks overlook — ensuring that only reviewed, trusted-built code reaches production."
confidence: "high"
confidence_rationale: "HIGH — This is a documented Google production control. The code provenance concept maps to modern frameworks (SLSA, Sigstore/cosign) and addresses a"
claim_type: "implementation"
source_note: "[[BeyondProd — Cloud-Native Security]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondprod.3: Code provenance enforcement (Binary Authorization for Borg) closes a critical gap that most ZT frameworks overlook — ensuring that only reviewed, trusted-built code reaches production.

**Source:** [[BeyondProd — Cloud-Native Security]] — Google, *BeyondProd: Cloud-Native Security*, 2019

## The Claim

BAB enforces at deploy time that code changes were reviewed by a second engineer, binaries were verifiably built on dedicated trusted infrastructure, and the build process produces a signed verifiable build manifest certificate.

## Evidence

The enforcement chain: developer submits change → central code repository enforces two-person review → approved change goes to central trusted build system → produces package with signed verifiable build manifest certificate → at deployment time, BAB validates the signed certificate confirming the entire review/build chain was followed. BAB rollout follows the same audit-first-then-enforce pattern as BeyondCorp: audit-only mode first, service owners identify non-compliant workflows, then switch to enforcement mode.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — This is a documented Google production control. The code provenance concept maps to modern frameworks (SLSA, Sigstore/cosign) and addresses a gap in NIST 800-207 which does not explicitly address code trust.

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
