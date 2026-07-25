---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-cloud
claim_id: "finney-ch8-11.1"
statement: "The cloud is not one protect surface — it's many, and the real protect surface is the project management process"
confidence: "high"
confidence_rationale: "HIGH. This is one of the most operationally practical claims in the book. The insight that governance processes *are* protect surfaces is a natural"
claim_type: "implementation"
source_note: "[[Finney — Ch8-11 — Execution and Sustainability]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch8-11.1: The cloud is not one protect surface — it's many, and the real protect surface is the project management process

**Source:** [[Finney — Ch8-11 — Execution and Sustainability]] — George Finney, *Project Zero Trust*, 2022

## The Claim

Isabelle's key insight: "I don't think the cloud is a protect surface. It's a lot of different protect surfaces." Rather than trying to wrap security around the entire cloud ecosystem, the team should secure the **project management process** itself. By inserting security phase-gates into every project lifecycle — vendor due diligence, secure configuration requirements, SOC notification — security becomes the default, not an afterthought.

## Evidence

The Post-it note wall exercise revealed three categories of cloud services (AWS/Amazon, Azure, SaaS) spanning dozens of vendors. The purchasing department found even more via P-card spend. Shadow IT (Dropbox alongside sanctioned OneDrive, free PDF converters, Vimeo/YouTube/Twitch) proved that simply blocking unknown services breaks business processes. The project process as a protect surface means: every new vendor onboarding triggers security review, every project hits phase-gates before proceeding to production.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is one of the most operationally practical claims in the book. The insight that governance processes *are* protect surfaces is a natural extension of the ZT design methodology — it applies the same logic (define the surface, map flows, architect controls) to the organizational process layer.

## Stakes

If project governance isn't treated as a protect surface, every cloud service deployed outside the security review pipeline becomes a blind spot. The scale argument — you can't review every cloud service individually — is defeated by securing the *pipeline* instead.

## Disagreement

**Who disagrees:**

Most ZT literature (NIST, Gilman & Barth, Garbis & Chapman) focuses on technical protect surfaces. Finney extends the concept upward to organizational process — this is a distinctive contribution. NIST 800-207 Ch7 discusses migration planning but doesn't frame project governance as a protect surface per se.

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

This is Finney's most original architectural contribution. It bridges the gap between "ZT is a technical architecture" and "ZT requires organizational change." The project management protect surface is what keeps ZT sustainable beyond the initial implementation phase.
