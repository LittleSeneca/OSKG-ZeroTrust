---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-definition
  - topic/zt-threats
  - topic/zt-network
  - topic/zt-architecture
claim_id: "go-intro.1"
statement: "Zero Trust originated from the Morris Worm and Stephen Marsh's thesis, not from a vendor marketing campaign"
confidence: "high"
confidence_rationale: "HIGH. This historical account is consistent across multiple sources and independently verifiable."
claim_type: "definitional"
source_note: "[[Green-Ortiz — Intro Ch1-2 — Foundations]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-intro.1: Zero Trust originated from the Morris Worm and Stephen Marsh's thesis, not from a vendor marketing campaign

**Source:** [[Green-Ortiz — Intro Ch1-2 — Foundations]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

Zero Trust originated from the Morris Worm and Stephen Marsh's thesis, not from a vendor marketing campaign

## Evidence

The FBI's public reporting on the Morris Worm, Marsh's thesis (University of Stirling, 1994), Jericho Forum's merger into The Open Group Security Forum (2014), and Google's published BeyondCorp papers. The historical timeline (Figure 1-1) shows a clear progression from reactive incident → academic formalization → industry forum → analyst articulation → implementation.

**Green-Ortiz's claim:**

The concept of Zero Trust traces to the 1988 Morris Worm, which exploited implicit trust in Unix remote services (rexec, rsh, sendmail, finger) to propagate to 10% of Internet-connected computers within 24 hours. Stephen Paul Marsh's 1994 doctoral thesis "Formalizing Trust as a Computational Concept" explicitly identified implicit trust as "unreasonable and misguided," providing the first formal treatment of trust in digital systems. The Jericho Forum (2003) advanced "de-perimeterization," and John Kindervag at Forrester (2009) popularized the modern basis. Google's BeyondCorp initiative (2009) provided the first large-scale implementation and lessons learned.

**Cross-reference — Gilman & Barth Ch1:**

Gilman & Barth trace perimeter security's failure to a different historical accident: RFC 1597 creating private address space, the DMZ emerging as a side effect, and NAT providing inadvertent firewall properties. Both histories converge on the same conclusion — security models based on location (inside/outside) were never designed; they accreted. Gilman & Barth's narrative is about *network architecture*, Green-Ortiz's is about *the trust concept itself*. Together they provide both the network-level and the conceptual-level origin stories.

**Cross-reference — NIST 800-207:**

NIST 800-207 does not provide a historical origin narrative. Its ZT definition is presented as a response to enterprise architectural evolution (Chapter 1), not as a lineage. Green-Ortiz fills a gap the standards literature leaves open.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This historical account is consistent across multiple sources and independently verifiable.

## Stakes

This lineage makes ZT a 30-year response to a well-understood problem (implicit trust is exploitable), not a vendor narrative. The invocation of Marsh's 1994 thesis as the intellectual root is distinctive to Green-Ortiz and adds academic credibility absent from most industry accounts.

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

The Marsh → Jericho → Kindervag → BeyondCorp lineage is the most complete origin story in the ZT literature. It's better than the common "Forrester invented ZT in 2010" simplification found in marketing collateral. The four-phase progression (incident → theory → industry consensus → implementation) makes ZT adoption feel like maturation rather than trend-chasing.
