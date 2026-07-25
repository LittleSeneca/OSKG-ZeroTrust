---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-definition
  - topic/zt-trust
  - topic/zt-governance
  - topic/zt-architecture
claim_id: "nist207-ch2.2"
statement: "The operative definition establishes ZT as uncertainty minimization, not absolute security"
confidence: "high"
confidence_rationale: "VERY HIGH. This definition has held for 5+ years without revision. It survives because it's modest — it doesn't promise perfect security, just better "
claim_type: "definitional"
source_note: "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---

# nist207-ch2.2: The operative definition establishes ZT as uncertainty minimization, not absolute security

**Source:** [[NIST 800-207 — Ch2 — Zero Trust Basics]] — Scott Rose, Oliver Borchert, Stu Mitchell, Sean Connelly, *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

Zero trust (ZT) provides a collection of concepts and ideas designed to minimize uncertainty in enforcing accurate, least privilege per-request access decisions in information systems and services in the face of a network viewed as compromised.

## Evidence

The definition is carefully worded: "minimize uncertainty" (not eliminate), "least privilege per-request" (granularity), "network viewed as compromised" (assume breach). ZTA is defined as the *plan* — the architecture document — not the deployed system. The zero trust *enterprise* is the deployed result.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This definition has held for 5+ years without revision. It survives because it's modest — it doesn't promise perfect security, just better 

## Stakes

If the goal is "eliminate all uncertainty" ZTA is impossible (and unfundable). If the goal is "minimize uncertainty," ZTA is a continuous improvement program. This framing makes ZTA compatible with NIST's Risk Management Framework (see Ch 6).

## Disagreement

**Who disagrees:**

Vendor marketing routinely overpromises ("achieve Zero Trust"). NSA's guidance (Embracing a Zero Trust Security Model, 2021) takes a stronger "assume breach" position, emphasizing threat response over uncertainty minimization. The difference is emphasis, not contradiction.

**Alternative reading:**

"Minimize uncertainty" is a weasel phrase — it lets organizations claim progress without measurable outcomes. The CISA maturity model fixes this by defining specific capability levels.

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
- [[zt-no-implicit-trust-continuous-eval|Uncertainty minimization reframes assume-breach/continuous-auth in more precise, measurable terms.]]
- [[zt-assume-breach]]

## Assessment

This definition is the single most important sentence in Zero Trust literature. Everything else — CISA's pillars, DoD's reference architecture, NSA's threat model — builds on this foundation. If this definition changes, the entire regulatory stack changes.

## Zero Trust Taxonomy

### Topic tags
`topic/zt-definition` `topic/zt-trust`

### Evidence tags
`evidence/primary-standard`
