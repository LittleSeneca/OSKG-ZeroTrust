---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-architecture
  - topic/zt-governance
  - topic/zt-implementation
  - topic/zt-identity
claim_id: "cisa-ztmm-ov.8"
statement: "The three cross-cutting capabilities unify the pillars and prevent siloed maturity"
confidence: "high"
confidence_rationale: "HIGH. These three capabilities are well-chosen — they correspond to the three operational dimensions that make ZTA actually work: you need to SEE"
claim_type: "architectural"
source_note: "[[CISA ZTMM — Overview and Framework]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-ov.8: The three cross-cutting capabilities unify the pillars and prevent siloed maturity

**Source:** [[CISA ZTMM — Overview and Framework]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

"Visibility and Analytics, Automation and Orchestration, and Governance provide opportunities to integrate advancements across each of the five pillars." These capabilities "highlight activities to support interoperability of functions across pillars."

## Evidence

- **Visibility and Analytics:** "The observable artifacts that result from the characteristics of and events within enterprise-wide environments. The focus on cyber-related data analysis can help inform policy decisions, facilitate response activities, and build a risk profile to develop proactive security measures before an incident occurs."
- **Automation and Orchestration:** "Zero trust makes full use of automated tools and workflows that support security response functions across products and services while maintaining oversight, security, and interaction of the development process."
- **Governance:** "The definition and associated enforcement of agency cybersecurity policies, procedures, and processes, within and across pillars, to manage an agency's enterprise and mitigate security risks in support of zero trust principles and fulfillment of federal requirements."

Each capability has its own maturity table (Table 7) that progresses from manual/static to automated/dynamic across the four maturity levels.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These three capabilities are well-chosen — they correspond to the three operational dimensions that make ZTA actually work: you need to SEE what's happening (Visibility & Analytics), you need to ACT on what you see (Automation & Orchestration), and you need to GOVERN the whole system (Governance). Without all three, pillar-level maturity produces isolated capabilities that don't integrate.

## Stakes

If the cross-cutting capabilities are treated as optional additions to pillar maturity (which the separate Table 7 structure could encourage), agencies achieve check-box compliance without operational integration. The document attempts to prevent this by including cross-cutting capability considerations in each pillar's function tables, but the overall structure still separates them.

## Disagreement

**Who disagrees:**

Forrester's ZTX framework treats Automation & Orchestration as a separate pillar, not a cross-cutting capability. NIST 800-207 embeds visibility and policy enforcement in the architecture itself (through the Policy Engine and continuous diagnostics). The ZTMM's approach is more operational than architectural — it asks "do you have visibility?" rather than "where in your architecture does visibility live?"

**Alternative reading:**

The cross-cutting capabilities could be read as CISA's way of saying "the pillars alone aren't enough — you need integration." This is a hedge against agencies that would otherwise treat the pillars as independent compliance checklists. The separate Table 7 could be seen as CISA giving itself an assessment mechanism for integration quality.

## Edges

**Depends on:**

**Supports:**
  - "[[cross-cutting-capabilities-convergence]]"

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The cross-cutting capabilities are the most underappreciated part of the ZTMM. In practice, agencies tend to focus on pillar maturity because the function tables are detailed and specific, while the cross-cutting capabilities feel abstract. But an agency with Advanced Identity and Traditional Visibility & Analytics has a gaping hole — it's authenticating users but can't see what they're doing. The cross-cutting capabilities deserve equal weight in assessment, and the document would benefit from making this expectation more explicit.
