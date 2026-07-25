---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-definition
  - topic/zt-trust
  - topic/zt-architecture
  - topic/zt-access-mgmt
claim_id: "gc-ch1-3.2"
statement: '"Zero Trust" is a misnomer — the real concept is "zero implicit trust" or "earned trust."'
confidence: "high"
confidence_rationale: 'HIGH as a definitional clarification. The authors are providing a corrective to the literal reading of "zero" that causes confusion among executives'
claim_type: "definitional"
source_note: "[[Garbis and Chapman — Ch1-3 — Introduction and Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-ch1-3.2: "Zero Trust" is a misnomer — the real concept is "zero implicit trust" or "earned trust."

**Source:** [[Garbis and Chapman — Ch1-3 — Introduction and Architecture]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"The 'zero' in Zero Trust is a bit of a misnomer — it's not about literally 'zero' trust, but about zero inherent or implicit trust... It could perhaps have been called 'earned trust' or 'adaptive trust' or 'zero implicit trust,' and these would have suited the movement better, but 'Zero Trust' has more sizzle, and it stuck."

## Evidence

The authors note that Zero Trust is about "carefully building a foundation of trust, and growing that trust to ultimately permit an appropriate level of access at the right time." The framing is definitional, not empirical.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH as a definitional clarification. The authors are providing a corrective to the literal reading of "zero" that causes confusion among executives and end users.

## Stakes

Misunderstanding "zero" leads to two errors: (1) thinking ZT means no one is ever trusted (making it seem impossible), and (2) thinking ZT is an absolute state you achieve rather than a continuous process. The "earned trust" framing makes ZT comprehensible and adoptable.

## Disagreement

**Who disagrees:**

No one disputes that ZT is about eliminating *implicit* trust. But the branding debate matters — some organizations avoid the term "Zero Trust" internally because "we don't trust you" is a negative message to employees (the authors note this themselves).

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[zt-no-implicit-trust-continuous-eval|The semantic clarification that ZT means 'zero implicit trust' aligns directly with NIST's operational definition of eli]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

This is the most pragmatic framing of ZT in the literature. NIST defines ZT abstractly; Gilman & Barth define it architecturally; Garbis & Chapman define it *operationally* — as something you do, not something you are. The "earned trust" reframe resolves the absolutist/pragmatic tension that runs through NIST's work.
