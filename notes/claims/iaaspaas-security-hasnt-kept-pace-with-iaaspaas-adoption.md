---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-cloud
  - topic/zt-threats
  - topic/zt-network
  - topic/zt-implementation
claim_id: "gc-cloud.1"
statement: "IaaS/PaaS security hasn't kept pace with IaaS/PaaS adoption"
confidence: "high"
confidence_rationale: "HIGH. This matches NIST 800-207's analysis (Ch4 deployment scenarios, multi-cloud/cross-boundary access) and the DoD ZT RA's emphasis on cross-pillar"
claim_type: "definitional"
source_note: "[[Garbis and Chapman — Cloud IaaS SaaS]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-cloud.1: IaaS/PaaS security hasn't kept pace with IaaS/PaaS adoption

**Source:** [[Garbis and Chapman — Cloud IaaS SaaS]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

Cloud platforms "have transformed the way that much of our software is built, deployed, and accessed" but "don't believe that these platforms have yet had a similarly broad and significant impact on security." CSP security models are designed to protect services *within* their cloud environments, not to serve as broad enterprise security solutions across heterogeneous environments. Microsoft is the exception — leveraging identity, desktop OS, and cloud computing together.

## Evidence

Google pioneered ZT internally and now offers Identity-Aware Proxy, but it's GCP-scoped. AWS and Azure have sophisticated IAM and network security groups, but they're cloud-native, not enterprise-wide. The CSPs' access control models are powerful but network/IP-centric rather than identity-centric — they "definitely do not have the ability to define and enforce the types of Zero Trust policies that we need, across our heterogeneous and diverse enterprise environments."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This matches NIST 800-207's analysis (Ch4 deployment scenarios, multi-cloud/cross-boundary access) and the DoD ZT RA's emphasis on cross-pillar integration. The CSPs themselves have acknowledged this gap with products like AWS Verified Access and Azure Global Secure Access, which emerged after this book's publication.

## Stakes

If CSP-native security is treated as sufficient, enterprises build siloed, cloud-specific security models that don't interoperate. If it's treated as worthless, enterprises miss the genuinely useful metadata, service identity, and IAM capabilities that CSPs provide.

## Disagreement

**Who disagrees:**

Cloud-native security advocates argue that CSP IAM + service mesh + Policy-as-Code (OPA, Cedar) *can* provide enterprise-grade ZT without an external platform. The BeyondCorp papers show Google doing exactly this with internal tooling. The tension is between "buy an external ZT platform" and "build ZT from cloud-native primitives."

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

Garbis & Chapman's framing is a product of its time (2021), when ZTNA vendors were positioning against CSP-native tooling. In 2026, the line has blurred significantly — CSPs now offer ZTNA-like services and ZTNA vendors offer cloud-native deployment. The enduring insight is that *someone* needs to provide cross-boundary, identity-centric policy — whether that's a third-party platform or a well-architected CSP-native stack.
