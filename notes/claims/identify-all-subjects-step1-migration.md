---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-migration
  - topic/zt-identity
claim_id: "nist207-ch7.5"
statement: "All enterprise subjects — human users and Non-Person Entities (service accounts, automated processes) — must be identified, with special-privilege users requiring additional scrutiny and stricter confidence levels under ZTA rather than blanket trust."
confidence: "high"
confidence_rationale: "HIGH. The inversion of privileged account treatment — from most trusted to most scrutinized — is a fundamental ZTA principle."
claim_type: "migration"
source_note: "[[NIST 800-207 — Ch7 — Migration]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch7.5: All enterprise subjects — human users and Non-Person Entities (service accounts, automated processes) — must be identified, with special-privilege users requiring additional scrutiny and stricter confidence levels under ZTA rather than blanket trust.

**Source:** [[NIST 800-207 — Ch7 — Migration]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

The Policy Engine must have knowledge of **all enterprise subjects** — both human users and Non-Person Entities (NPEs). Special-privilege users (developers, system administrators) require **additional scrutiny**. (§7.3.1)

## Evidence

- In legacy architectures, privileged accounts often have **blanket permission** to access all enterprise resources.
- ZTA should instead allow sufficient flexibility while using **logs and audit actions** to identify access behavior patterns.
- Administrators may need to satisfy a more stringent confidence level, as outlined in [[NIST SP 800-63A]], Section 5.
- Key shift: from *privileged accounts have implicit trust* to *privileged accounts have stricter verification requirements*.

**Cross-reference:**

Finney's [[Project Zero Trust]] frames this as the "identity is the new perimeter" problem. The [[DoD ZT Strategy]] emphasizes identity as Pillar 1 and requires attribute-based access control (ABAC) for all user authorizations.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The inversion of privileged account treatment — from most trusted to most scrutinized — is a fundamental ZTA principle.

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
