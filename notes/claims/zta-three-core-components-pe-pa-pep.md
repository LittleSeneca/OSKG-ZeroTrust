---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-architecture
claim_id: "nist207-ch3.1"
statement: "ZTA has three core decision-making components (PE, PA, PEP)"
confidence: "high"
confidence_rationale: "HIGH — This is the canonical definition. Every major ZT framework (CISA, DoD, Forrester ZTX, Gartner CARTA) references or maps to this tripartite"
claim_type: "architectural"
source_note: "[[NIST 800-207 — Ch3 — Logical Components]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch3.1: ZTA has three core decision-making components (PE, PA, PEP)

**Source:** [[NIST 800-207 — Ch3 — Logical Components]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

A Zero Trust Architecture is built on three logical components: the Policy Engine (PE) which makes access decisions, the Policy Administrator (PA) which executes them by configuring communication paths, and the Policy Enforcement Point (PEP) which enables, monitors, and terminates connections between subjects and resources. The PE and PA together form the Policy Decision Point (PDP) from Figure 1. These components communicate on a separate control plane while application data travels on the data plane.

## Evidence

Architectural model (Figure 2) with enumerated component definitions. This is an ideal logical model — not a deployment specification. NIST explicitly notes that implementations may combine PE and PA into a single service, but separates them for conceptual clarity.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — This is the canonical definition. Every major ZT framework (CISA, DoD, Forrester ZTX, Gartner CARTA) references or maps to this tripartite model. The architecture has withstood five years of implementation experience without fundamental revision.

## Stakes

If this component model were fundamentally wrong, the entire ZT standards ecosystem — CISA Maturity Model, DoD Reference Architecture, NIST 800-207A, and every vendor ZTNA/SDP implementation — would need re-architecture. This claim is **load-bearing** for the entire domain.

## Disagreement

**Who disagrees:**

No serious disagreement exists on the conceptual components. Vendor implementations vary in where component boundaries fall (combined PE/PA services, split PEPs into client-side agent and resource-side gateway), but the logical separation is universally accepted. The closest to a counter-position is practitioners who argue the tripartite model is too abstract to guide implementation directly — but this is about utility, not correctness.

**Alternative reading:**

The PE/PA/PEP model could be seen as a restatement of the IETF AAA architecture (Authentication, Authorization, Accounting) with a new control-plane framing. The PDP/PEP split dates to IETF RFC 2753 (2000) and XACML (2003). NIST's contribution is integrating these existing concepts into a coherent ZT-specific architecture and adding the trust algorithm.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

Holds up strongly. The logical separation is both conceptually clean and practically useful. The fact that implementations routinely collapse PE and PA into one service while preserving the PEP as distinct confirms the model's flexibility. The weakest element is that NIST doesn't provide an interface specification between components — the model defines what the components do, not how they talk to each other.
