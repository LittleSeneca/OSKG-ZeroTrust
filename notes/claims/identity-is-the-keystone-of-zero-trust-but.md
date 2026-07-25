---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-identity
claim_id: "gc-iam-policy.5"
statement: "Identity is the keystone of Zero Trust — but perfection is not a prerequisite"
confidence: "high"
confidence_rationale: "VERY HIGH. This claim is echoed by CISA ZTMM (Identity is Pillar 1), NIST 800-207 (identity as input to the trust algorithm), and the NSA User Pillar"
claim_type: "implementation"
source_note: "[[Garbis and Chapman — Practice IAM Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-iam-policy.5: Identity is the keystone of Zero Trust — but perfection is not a prerequisite

**Source:** [[Garbis and Chapman — Practice IAM Policy]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"Identity — and a reasonably well-run identity management program — is the key to success with a Zero Trust program... organizations should not and cannot hold themselves to an unreasonable standard, or require perfection from their identity teams and systems before embarking on their Zero Trust journey."

## Evidence

ZT at its heart is an identity-centric approach to security. IAM systems serve as the authoritative source for identity information and context (roles, attributes) used by the PDP. Even organizations with multiple incompatible directories can start ZT — ZT as an "overlay system" can bridge gaps between disparate identity systems. ZT platforms must support standard protocols (LDAP, SAML) for authentication and attribute retrieval.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This claim is echoed by CISA ZTMM (Identity is Pillar 1), NIST 800-207 (identity as input to the trust algorithm), and the NSA User Pillar guidance. Every ZT architecture document positions identity as foundational.

## Stakes

If organizations believe they need perfect IAM before starting ZT, many will never start. The "good enough IAM" claim removes the biggest procedural blocker. Conversely, if IAM is genuinely broken (orphaned accounts, no lifecycle management), ZT can't compensate.

## Disagreement

**Who disagrees:**

The NSA Embracing ZT guidance emphasizes that IAM shortcomings are an attack surface — implying higher standards than "reasonably well-run." However, even the NSA doesn't say perfection is required.

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

The authors' pragmatism here is essential. They explicitly state that an identity management program "cannot be 'broken'" but also "doesn't have to be perfect." The distinction between "imperfect" and "broken" is doing real work: imperfect means some extra users get access until group mappings are fixed; broken means no lifecycle management at all.
