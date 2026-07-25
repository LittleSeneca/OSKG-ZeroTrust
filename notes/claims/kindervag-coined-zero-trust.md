---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-architecture
claim_id: "nist207-ch1.6"
statement: 'John Kindervag at Forrester coined the term "zero trust," which then became the dominant term for security solutions that evaluate trust per-transaction rather than by network location.'
confidence: "high"
confidence_rationale: 'HIGH on Kindervag coining the term — this is well-documented and universally acknowledged in the literature. MEDIUM on "private industry and higher'
claim_type: "definitional"
source_note: "[[NIST 800-207 — Ch1 — Introduction]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch1.6: John Kindervag at Forrester coined the term "zero trust," which then became the dominant term for security solutions that evaluate trust per-transaction rather than by network location.

**Source:** [[NIST 800-207 — Ch1 — Introduction]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

"The concepts of de-perimeterization evolved and improved into the larger concept of zero trust, which was later coined by John Kindervag while at Forrester. Zero trust then became the term used to describe various cybersecurity solutions that moved security away from implied trust based on network location and instead focused on evaluating trust on a per-transaction basis. Both private industry and higher education have also undergone this evolution from perimeter-based security to a security strategy based on zero trust principles." (lines 397–402)

## Evidence

- Kindervag at Forrester as the source of the term (footnote cites https://go.forrester.com/blogs/next-generation-access-and-zero-trust/).
- NIST explicitly notes its non-endorsement of commercial products (footnote 2, lines 424–425) — distancing itself from Forrester as a commercial entity while crediting the intellectual contribution.
- The claim that "both private industry and higher education" adopted ZT is asserted without evidence.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on Kindervag coining the term — this is well-documented and universally acknowledged in the literature. MEDIUM on "private industry and higher education have also undergone this evolution" — NIST provides no evidence for the breadth or depth of private-sector adoption.

## Stakes

Crediting Kindervag establishes ZT's origin as an industry analyst concept rather than an academic or government one — this shapes the intellectual history. If Kindervag's contribution is overstated, the concept may have deeper roots that would change how we evaluate ZT's theoretical foundations. The footnote disclaimer about commercial endorsement reflects NIST's institutional caution about appearing to promote Forrester.

## Disagreement

**Who disagrees:**

Some argue that ZT's real intellectual father is the Jericho Forum, and Kindervag's contribution was marketing/branding rather than conceptual innovation. Others point to earlier academic work on capability-based security and least-privilege architectures that anticipated ZT principles. Chase Cunningham (Kindervag's successor at Forrester) has positioned himself as extending and operationalizing Kindervag's concept, not merely inheriting it.

**Alternative reading:**

Kindervag didn't "coin" ZT so much as synthesize existing ideas (de-perimeterization, least privilege, need-to-know) under a memorable brand. The term's power was in making an abstract security philosophy sellable to CISOs — it was a marketing triumph as much as a conceptual one.

## Edges

**Depends on:**

**Supports:**
- [[nist-document-structure-framework|Crediting Kindervag's coinage of the term is an element of the historical grounding that nist207-ch1.8 identifies as par]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

NIST's attribution is correct and appropriately hedged. The footnote disclaimer is telling — NIST is careful to credit the intellectual contribution without endorsing Forrester's commercial ecosystem. The claim about private industry and higher education adoption is the weakest part — it's asserted without evidence and serves primarily to broaden ZT's legitimacy beyond the federal context. For a fuller account of Kindervag's contribution, see the Forrester papers indexed in [[Papers Index]].
