---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-definition
  - topic/zt-tenets
  - topic/zt-governance
  - topic/zt-architecture
claim_id: "nist207-ch2.1"
statement: "Zero Trust is defined by its positive tenets, not by what it excludes"
confidence: "high"
confidence_rationale: "VERY HIGH. This is the canonical government definition, adopted by CISA, DoD, NSA, and referenced by every subsequent standard."
claim_type: "definitional"
source_note: "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---

# nist207-ch2.1: Zero Trust is defined by its positive tenets, not by what it excludes

**Source:** [[NIST 800-207 — Ch2 — Zero Trust Basics]] — Scott Rose, Oliver Borchert, Stu Mitchell, Sean Connelly, *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

Many definitions and discussions of ZT stress the concept of removing wide-area perimeter defenses... However, most of these definitions continue to define themselves in relation to perimeters in some way... The following is an attempt to define ZT and ZTA in terms of basic tenets that should be involved rather than what is excluded.

## Evidence

The seven tenets are technology-agnostic and stated positively — what ZTA DOES, not what it eliminates. The authors explicitly note that perimeter-based defenses (like micro-segmentation) are still part of ZTA, just not the organizing principle.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This is the canonical government definition, adopted by CISA, DoD, NSA, and referenced by every subsequent standard.

## Stakes

If ZT is defined by what it excludes (firewalls, VPNs, perimeter), vendors can claim "we're ZT because we don't use firewalls." If defined by positive tenets, the burden shifts to implementation evidence. The entire regulatory framework depends on this distinction.

## Disagreement

**Who disagrees:**

Chase Cunningham's ZTX framework (2018) defines ZT more expansively across seven pillars. Google BeyondCorp doesn't use the term "tenets" at all — it defines ZT through implementation. Kindervag's original formulation emphasized "no more chewy centers" — eliminating the trusted interior. NIST's positive-tenet framing is less dramatic but more enforceable.

**Alternative reading:**

The positive-tenet approach could be seen as political compromise — making ZTA compatible with existing perimeter investments to increase adoption. A stricter reading would demand elimination of all implicit trust zones, including those created by micro-segmentation.

## Edges

**Depends on:**
- [[bsi-provides-formal-three|BSI's three-part definition explicitly derives from and extends NIST's tenet-based framework, so it logically presuppose]]

**Supports:**
- [[nist-document-structure-framework|The seven positive tenets are the core content delivered by the document structure that nist207-ch1.8 claims is the esse]]
- [[zt-five-fundamental-assertions]]

**Contradicts:**
<!-- Claims that cannot be true if this one is -->

**Challenged by:**
<!-- Evidence or arguments that weaken this claim -->

**Operationalizes:**
<!-- Standards/implementations that put this claim into practice -->

**Extends:**
<!-- Claims this one builds upon or elaborates -->

## Assessment

The positive-tenet framing is the right call for a government standard. "Thou shalt not" definitions invite loopholes. "Thou shalt" definitions are auditable. CISA's maturity model operationalizes this perfectly: each tenet maps to capabilities at each maturity level.

## Zero Trust Taxonomy

### Topic tags
`topic/zt-definition` `topic/zt-tenets`

### Evidence tags
`evidence/primary-standard`
