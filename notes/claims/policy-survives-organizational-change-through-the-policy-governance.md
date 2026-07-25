---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-governance
  - topic/zt-policy
  - topic/zt-identity
  - topic/zt-implementation
claim_id: "go-ch3-5.5"
statement: "Policy survives organizational change through the Policy & Governance pillar — but mergers, acquisitions, and shadow IT constantly challenge it"
confidence: "medium"
confidence_rationale: "MODERATE. The role of governance in maintaining ZT policy is underdeveloped in the broader ZT literature (NIST's migration chapter mentions it"
claim_type: "governance"
source_note: "[[Green-Ortiz — Ch3-5 — Trust and Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch3-5.5: Policy survives organizational change through the Policy & Governance pillar — but mergers, acquisitions, and shadow IT constantly challenge it

**Source:** [[Green-Ortiz — Ch3-5 — Trust and Policy]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

The Policy & Governance pillar is the organizational anchor for ZT. Ch5 details two major threats to policy integrity: mergers/acquisitions (Ch5: "Onboarding: The Challenge of Merger Activity") and independent purchasing decisions (Ch5: "Onboarding: The Challenge of Independent Purchasing Decisions"). In both cases, the solution is formal policy enforced through the governance pillar: "Policies should be created and adhered to, and they should entail replacing equipment at the end of its useful life cycle" and "a well-defined policy allowing for purchase of devices so long as they are onboarded in a consistent manner and in alignment with organizational standards."

## Evidence

- **Mergers:** Organizational debt increases, technical debt accrues, skill gaps appear. The acquiring organization "has the responsibility, by utilizing the analysis tools and capabilities found within the respective pillar, to evaluate how organizational debt will be affected by the merger." Feedback from all pillars is critical. Due diligence questions include: "Does the organization have well-defined policies?" "Do competing policies, processes, and procedures create unresolvable conflicts?" "How will data be protected as it migrates across infrastructures?"
- **Shadow IT:** Two scenarios — the first (policy failure) where devices "do not allow for discovery" and create "shadow IT" blind spots; the second (political pressure) where "the decision comes down to when and not if the network can be ready for them." Solution: "a well-defined policy allowing for purchase of devices so long as they are onboarded in a consistent manner."
- **Onboarding process:** Three steps: (1) policy exception process with security level approval; (2) acquisition with bill of materials + test plan documenting operational modes; (3) policy creation addressing visibility, identity, context, and enforcement, with operational testing before sign-off.

## Confidence

**Rating:** MEDIUM
**Rationale:** MODERATE. The role of governance in maintaining ZT policy is underdeveloped in the broader ZT literature (NIST's migration chapter mentions it, Gilman & Barth don't address it). Green-Ortiz's treatment is more extensive than most, but it's still aspirational — actual governance implementations in complex organizations are far messier than the three-step onboarding process suggests.

## Stakes

Policy integrity over time is the single biggest threat to a ZT deployment. A perfectly enforced ZT architecture can be eroded by one merger that introduces thousands of unmanaged devices, or by shadow IT that creates undocumented access paths. Green-Ortiz correctly identifies this as a governance problem, not a technology problem — but the governance prescription is thin.

## Disagreement

**Who disagrees:**

Some argue that the solution to shadow IT and merger complexity is to make ZT enforcement so lightweight and automated that new devices can be onboarded without friction — making governance unnecessary. Green-Ortiz's position is that governance is unavoidable because business decisions (mergers, budget allocations, vendor selection) create trust boundary changes that technology alone cannot adjudicate.

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

This is the most important and least developed claim in Ch3-5. The governance problem is real and underappreciated. Green-Ortiz identifies the right threats but the solutions are templates rather than battle-tested patterns. The due diligence questions for mergers are the most actionable part — they can serve as a practical checklist for any organization undergoing M&A.
