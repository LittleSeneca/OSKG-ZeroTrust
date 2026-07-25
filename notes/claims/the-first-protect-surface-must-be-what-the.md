---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-implementation
  - topic/zt-cloud
  - topic/zt-architecture
claim_id: "finney-ch4-7.1"
statement: "The first protect surface must be what the business depends on to make money — not what's easiest for security to fix."
confidence: "high"
confidence_rationale: 'HIGH. This operationalizes the first ZT design principle ("Focus on business outcomes"). The narrative demonstrates that starting with'
claim_type: "implementation"
source_note: "[[Finney — Ch4-7 — Building the ZT Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch4-7.1: The first protect surface must be what the business depends on to make money — not what's easiest for security to fix.

**Source:** [[Finney — Ch4-7 — Building the ZT Strategy]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"We started with the Ides as the first of the primary protect surfaces for one main reason. And it's the first of the Zero Trust design principles. By starting with Ides, we're focusing on the business. We're forcing ourselves to understand how the business makes money."

## Evidence

Dylan's conversation with CFO Donna reveals the ERP system ("Ides," a nod to the Ides of March — "Beware") as the central nervous system of MarchFit's finances: vendor creation, invoice processing, payment authorization, and financial reporting all flow through it. The ERP is where money both enters and leaves the business. Donna's observation captures the symmetry: "I need Ides to understand how the business operates in real time to protect the business from going the wrong direction, and you need to understand how the business operates in order to protect Ides."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This operationalizes the first ZT design principle ("Focus on business outcomes"). The narrative demonstrates that starting with business-critical assets creates natural allies (Donna, finance team) and forces security to learn how the business actually works — rather than applying generic security controls from a distance.

## Stakes

If ZT initiatives start with low-stakes systems to build momentum, they risk demonstrating that security doesn't understand the business. Starting with what matters most signals that security is a strategic partner, not a compliance function.

## Disagreement

**Who disagrees:**

Some frameworks (including aspects of CISA's ZTMM) suggest starting with identity as the foundational pillar. Finney addresses this by having Aaron explain that identity work happens *within* the ERP protect surface first — "we're practicing identity now so it will be that much easier later on." The sequencing is ERP → Identity → DevOps → SOC, each building on the previous.

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

This is one of Finney's most important contributions: ZT methodology requires starting with *what creates business value*, not with what's architecturally convenient. The narrative makes this concrete — the ERP is complex, messy, and politically fraught, and that's exactly why it must be first. The alternative (starting with clean, modern cloud workloads that already have good security) teaches nothing about the organization's real risks.
