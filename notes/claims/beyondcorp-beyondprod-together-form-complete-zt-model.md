---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/beyondprod
  - topic/zt-cloud
  - topic/zt-implementation
claim_id: "beyondprod.6"
statement: "BeyondCorp and BeyondProd together form a complete ZT model — BeyondCorp for the north-south axis (user-to-app) and BeyondProd for the east-west axis (service-to-service) — a distinction NIST 800-207 does not explicitly make."
confidence: "medium"
confidence_rationale: "MEDIUM — The north-south/east-west distinction is analytically useful but somewhat simplified. Real deployments have overlapping patterns (a service"
claim_type: "implementation"
source_note: "[[BeyondProd — Cloud-Native Security]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondprod.6: BeyondCorp and BeyondProd together form a complete ZT model — BeyondCorp for the north-south axis (user-to-app) and BeyondProd for the east-west axis (service-to-service) — a distinction NIST 800-207 does not explicitly make.

**Source:** [[BeyondProd — Cloud-Native Security]] — Google, *BeyondProd: Cloud-Native Security*, 2019

## The Claim

This is a meta-claim about the architectural relationship. Google's implementation separates user-to-application access (BeyondCorp: SSO + X.509 device certificates, Access Control Engine with Trust Inferer tiers) from service-to-service access (BeyondProd: ALTS mutual auth, service access management with end-user context tickets, BAB for code provenance).

## Evidence

The comparison table shows systematic mapping: BeyondCorp uses SSO + device certs for identity; BeyondProd uses ALTS + service identity. BeyondCorp authorizes via Access Control Engine + Trust Inferer; BeyondProd via Service Access Management + EUC tickets. BeyondCorp uses unprivileged VLANs + Access Proxy; BeyondProd uses all-RPC-over-ALTS + GFE edge. BeyondCorp verifies device state; BeyondProd verifies code provenance. BeyondCorp uses TPM for device certificates; BeyondProd uses Titan chip for host integrity.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM — The north-south/east-west distinction is analytically useful but somewhat simplified. Real deployments have overlapping patterns (a service can be both a BeyondCorp client and a BeyondProd server). NIST 800-207's abstract architecture accommodates both without making the distinction explicit, which can be seen as either a gap or deliberate generality.

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
