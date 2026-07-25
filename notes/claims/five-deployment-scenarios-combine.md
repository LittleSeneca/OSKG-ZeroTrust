---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-architecture
  - topic/zt-implementation
  - topic/zt-cloud
  - topic/zt-network
claim_id: "nist207-ch4.1"
statement: "The five scenarios are not mutually exclusive — real enterprises combine them"
confidence: "high"
confidence_rationale: "HIGH. The chapter opens with this disclaimer explicitly. Real federal agencies combine all five scenarios daily."
claim_type: "architectural"
source_note: "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch4.1: The five scenarios are not mutually exclusive — real enterprises combine them

**Source:** [[NIST 800-207 — Ch4 — Deployment Scenarios]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

"Any enterprise environment can be designed with zero trust tenets in mind... ZTA is not explicitly indicated since the enterprise likely has both perimeter-based and possibly ZTA infrastructures" (4.0). NIST acknowledges that most enterprises will operate in a hybrid state (see Ch 7.2) where ZTA and perimeter-based security coexist.

## Evidence

The five scenarios are presented as lenses, not silos. An enterprise with satellite facilities (4.1) may also use multiple clouds (4.2), host contractors (4.3), collaborate with partners (4.4), and serve public-facing applications (4.5). The scenarios compound.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The chapter opens with this disclaimer explicitly. Real federal agencies combine all five scenarios daily.

## Stakes

Treating scenarios as silos leads to fragmented ZT deployment — a different architecture per scenario rather than a unified PDP/PA/PEP infrastructure. NIST's framing allows one policy engine to govern multiple scenarios simultaneously.

## Disagreement

**Who disagrees:**

Vendor ZTNA products often address only scenarios 4.1 and 4.4 (remote access and cross-enterprise). The other scenarios are left to different product categories (CASB for cloud, NAC for contractors, WAF for public-facing). This is a product taxonomy problem, not an architectural one — NIST shows the same logical components apply everywhere.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[zt-implementation-faces-significant-organizational-technical-challenges|Because enterprises compound multiple deployment scenarios, ZT implementation faces compounded organizational and techni]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[four-deployment-models-zta|Since enterprises combine multiple deployment scenarios, they need multiple NIST deployment models simultaneously rather]]
- [[four-deployment-models-cover-the-zt-solution-space|Because the five NIST deployment scenarios compound in real enterprises, the four deployment models must cover the full]]

## Assessment

_Not addressed separately in the source note._
