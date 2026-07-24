---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/practitioner
  - source/gilman-barth
  - topic/zt-definition
  - topic/zt-network
claim_id: "gilmanbarth-ch1.1"
statement: "The five fundamental assertions define ZT operationally, not abstractly"
confidence: "high"
confidence_rationale: "HIGH. These assertions have held up as the pragmatic, engineering-level complement to NIST's seven abstract tenets. They're more operational than NIST"
claim_type: "definitional"
source_note: "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---

# gilmanbarth-ch1.1: The five fundamental assertions define ZT operationally, not abstractly

**Source:** [[Gilman and Barth — Ch1 — Zero Trust Fundamentals]] — Evan Gilman, Doug Barth, *Zero Trust Networks: Building Secure Systems in Untrusted Networks*, 2017

## The Claim

A zero trust network is built upon five fundamental assertions: (1) The network is always assumed to be hostile. (2) External and internal threats exist on the network at all times. (3) Network locality is not sufficient for deciding trust. (4) Every device, user, and network flow is authenticated and authorized. (5) Policies must be dynamic and calculated from as many sources of data as possible.

## Evidence

These five assertions are derived from engineering practice at Netflix and PagerDuty, not from theoretical analysis. The book is written by practitioners who built ZT systems. Each assertion maps to a specific engineering decision: assertion 1 → always encrypt, assertion 4 → no unauthenticated traffic anywhere, assertion 5 → policy engines fed by multiple data sources.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These assertions have held up as the pragmatic, engineering-level complement to NIST's seven abstract tenets. They're more operational than NIST

## Stakes

If the assertions are the right decomposition, ZT is fundamentally about network architecture. If they're too narrowly focused on network-level concerns, they miss organizational, identity, and data-centric dimensions. CISA's five-pillar model explicitly expands beyond network concerns.

## Disagreement

**Who disagrees:**

NIST 800-207's seven tenets are broader — they include resource definition, continuous monitoring, and data collection (Tenets 1, 5, 7) that Gilman & Barth's assertions don't directly address. NSA adds "assume breach" as a separate organizing principle. CISA adds cross-cutting capabilities (Visibility, Automation, Governance) that span all five assertions.

**Alternative reading:**

The five assertions could be read as a network engineer's manifesto — they're about what happens on the wire. A data-centric ZT approach would start with "all data is classified" rather than "the network is hostile." Both are correct; they're different entry points to the same architecture.

## Edges

**Depends on:**
<!-- Claims this one requires to be true -->

**Supports:**
- [[zt-control-data-plane-split]]

**Contradicts:**
<!-- Claims that cannot be true if this one is -->

**Challenged by:**
<!-- Evidence or arguments that weaken this claim -->

**Operationalizes:**
<!-- Standards/implementations that put this claim into practice -->

**Extends:**
- [[zt-positive-tenets]]
- [[zt-three-guiding-principles]]

## Assessment

These five assertions are the most readable, most actionable expression of Zero Trust principles in the field. They're what you put on a whiteboard. NIST's seven tenets are what you put in an RFP. Both needed.

## Zero Trust Taxonomy

### Topic tags
`topic/zt-definition` `topic/zt-network`

### Evidence tags
`evidence/practitioner`
