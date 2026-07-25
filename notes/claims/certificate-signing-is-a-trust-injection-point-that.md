---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-access-mgmt
  - topic/zt-encryption
  - topic/zt-identity
  - topic/zt-implementation
claim_id: "gb-ch4-6.6"
statement: "Certificate signing is a trust injection point that must be secured with multi-party authorization"
confidence: "high"
confidence_rationale: "HIGH. The multi-party signing model is well-established. NIST 800-207 expects the PA to evaluate multiple attributes from multiple sources before"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch4-6 — Authorization Devices Users]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch4-6.6: Certificate signing is a trust injection point that must be secured with multi-party authorization

**Source:** [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"By splitting these responsibilities and requiring multiple systems to assert validity, we can safely (well, as safely as is possible) remove humans from the loop."

## Evidence

The authors analyze three trust sources for certificate signing: (a) humans (with TOTP — secure but doesn't scale), (b) resource managers (can assert "I turned this host on"), (c) image/device credentials (baked into image or TPM-backed). Their recommended approach: combine resource manager + image/device credentials with multiple validation points (registered TPM key, correct IP, TOTP from resource manager, expected certificate properties). They cite the DigiNotar CA breach (2011) as the cautionary tale.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The multi-party signing model is well-established. NIST 800-207 expects the PA to evaluate multiple attributes from multiple sources before granting access. Practices like SPIFFE (workload identity) implement this pattern for service-to-service authentication.

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

This claim generalizes beyond certificate signing to all ZT trust injection. Every trust anchor needs multiple corroborating signals. The specific mechanisms (TOTP, resource manager attestation) are implementation details of a deeper principle: no single assertion is sufficient to establish trust.
