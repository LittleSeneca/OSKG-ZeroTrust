---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-governance
  - topic/zt-policy
  - topic/zt-implementation
  - topic/zt-architecture
claim_id: "go-intro.4"
statement: 'Policy & Governance is the "badge and shield" — it authorizes enforcement and defines the rules'
confidence: "medium"
confidence_rationale: "MEDIUM. Confidence not explicitly stated in source."
claim_type: "definitional"
source_note: "[[Green-Ortiz — Intro Ch1-2 — Foundations]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-intro.4: Policy & Governance is the "badge and shield" — it authorizes enforcement and defines the rules

**Source:** [[Green-Ortiz — Intro Ch1-2 — Foundations]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

Policy & Governance is the "badge and shield" — it authorizes enforcement and defines the rules

## Evidence

Detailed treatment of each sub-capability with operational guidance. The key insight is that Policy & Governance must be "strict enough to act as the badge and shield allowing for enforcement actions to be taken" while "striking the right balance between allowing devices to perform their business purpose... while maintaining least privileged access."

**Green-Ortiz's claim:**

Policy & Governance is the foundational pillar because it establishes what can and cannot be done within the organization. It encompasses change control (ITIL-based), data governance (classification: PII, ePHI, PCI, restricted IP), data retention (legal/compliance-driven), QoS (prioritization of control plane traffic during congestion), redundancy (control plane + data plane), replication (encrypted, automated backups), business continuity (BCP with tabletop exercises), disaster recovery (RPO/RTO definitions), and risk classification. Finding the right balance between security and business enablement is the central tension.

**Cross-reference:**

NIST 800-207's "Data Access Policies" and "Industry Compliance" data sources (Ch3, Claim 2) are the closest equivalents. Gilman & Barth treat policy as an output of the trust engine, not as a standalone governance function. Green-Ortiz's treatment of governance as a separate, foundational pillar reflects the enterprise reality that policy precedes architecture.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. Confidence not explicitly stated in source.

## Stakes

Without Policy & Governance, enforcement has no authority. Without DR/BCP, a ZT environment can't recover from a successful attack. The authors argue that "without a business continuity plan and a disaster recovery plan, there cannot be a valid and implemented Zero Trust strategy" — a stronger claim than any other ZT source makes.

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
- [[the-service-desk-ticket-condition-represents-a-paradigm|The ticket-condition JIT access model is a concrete mechanism for Policy & Governance acting as the badge and shield — p]]
- [[policy-survives-organizational-change-through-the-policy-governance|The badge-and-shield function — authorizing enforcement and defining rules — is what enables policy to survive mergers,]]

## Assessment

_Not addressed separately in the source note._
