---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-governance
  - topic/zt-monitoring
  - topic/zt-definition
  - topic/zt-identity
claim_id: "nist207-ch6.4"
statement: "Privacy Framework — ZTA's \"inspect everything\" tenet creates an explicit tension with privacy obligations; traffic inspection and metadata logging may capture PII, requiring formal privacy risk management via the NIST Privacy Framework [NISTPRIV]."
confidence: "high"
confidence_rationale: "HIGH. The tension is architecturally inevitable — more inspection means more privacy exposure. NIST acknowledges this explicitly."
claim_type: "governance"
source_note: "[[NIST 800-207 — Ch6 — Federal Guidance]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch6.4: Privacy Framework — ZTA's "inspect everything" tenet creates an explicit tension with privacy obligations; traffic inspection and metadata logging may capture PII, requiring formal privacy risk management via the NIST Privacy Framework [NISTPRIV].

**Source:** [[NIST 800-207 — Ch6 — Federal Guidance]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

ZTA mandates traffic inspection (or metadata logging when decryption is impossible), but some traffic contains PII or other private information. The Privacy Framework provides the formal process to identify, measure, and mitigate these risks. (§6.2)

## Evidence

- Core tension: security visibility vs. privacy protection.
- Mitigations include: user notification (login banners), consent mechanisms, and user education.
- NISTIR 8062 is cited as a companion resource for privacy risk identification in network monitoring contexts.
- Biometric attributes used in access evaluations are flagged as a specific privacy concern.

**Implication for OSKG-ZeroTrust:**

"Inspect everything" is a ZTA tenet, but it creates a privacy-compliance surface that the enterprise must formally manage. This is a tension point, not a resolved tradeoff.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The tension is architecturally inevitable — more inspection means more privacy exposure. NIST acknowledges this explicitly.

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
