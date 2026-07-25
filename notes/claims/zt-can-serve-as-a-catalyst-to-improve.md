---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-implementation
  - topic/zt-identity
claim_id: "gc-iam-policy.8"
statement: "ZT can serve as a catalyst to improve IAM — not just consume it"
confidence: "medium"
confidence_rationale: "MODERATE. The claim that ZT can _improve_ IAM (rather than just consume it) is aspirational. The evidence is hypothetical — no case study in Ch4"
claim_type: "implementation"
source_note: "[[Garbis and Chapman — Practice IAM Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-iam-policy.8: ZT can serve as a catalyst to improve IAM — not just consume it

**Source:** [[Garbis and Chapman — Practice IAM Policy]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"Zero Trust projects are an excellent opportunity for organizations to incrementally improve or significantly transform their identity systems... Zero Trust can simplify security and operations, by acting as a homogenizing layer which masks the underlying complexity."

## Evidence

Organizations with multiple incompatible directories (from acquisitions, departmental initiatives, legacy) can use ZT to normalize across them without waiting for directory consolidation. ZT can also help "simplify and streamline identity operations, and reduce complexity of the overall identity program, without requiring wholesale or disruptive changes."

## Confidence

**Rating:** MEDIUM
**Rationale:** MODERATE. The claim that ZT can _improve_ IAM (rather than just consume it) is aspirational. The evidence is hypothetical — no case study in Ch4 shows this happening. The SDP case study integrated with both AD and a SAML IdP concurrently, which is consumption, not improvement.

## Stakes

If ZT is seen as purely a consumer of IAM data, identity teams may resist it as adding workload. If ZT is positioned as a catalyst for IAM modernization, identity teams become partners.

## Disagreement

**Who disagrees:**

The CISA ZTMM Identity Pillar treats IAM maturity as an input to ZT maturity, not an output. The implicit assumption is that IAM must improve _before_ ZT can advance, not _because_ ZT drives improvement.

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

The catalyst framing is politically smart but technically thin. ZT can normalize across identity silos (acting as a "blanket of snow") but doesn't fix the underlying directories. The real catalyst effect is organizational: ZT creates demand for better identity data because policies depend on it.
