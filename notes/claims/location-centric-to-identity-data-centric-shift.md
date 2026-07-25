---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-definition
  - topic/zt-identity
  - topic/zt-architecture
claim_id: "cisa-ztmm-ov.4"
statement: "Zero trust represents a fundamental shift from location-centric to identity/data-centric security"
confidence: "high"
confidence_rationale: "HIGH. Every major ZT framework (NIST, DoD, NSA, Google BeyondCorp) agrees on this shift. The cultural dimension is well-observed in practice"
claim_type: "definitional"
source_note: "[[CISA ZTMM — Overview and Framework]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-ov.4: Zero trust represents a fundamental shift from location-centric to identity/data-centric security

**Source:** [[CISA ZTMM — Overview and Framework]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

"Zero trust presents a shift from a location-centric model to an identity, context, and data-centric approach with fine-grained security controls between users, systems, applications, data, and assets that change over time; for these reasons, adopting a ZTA is a non-trivial effort. This shift provides the visibility needed to support the development, implementation, enforcement, and evolution of security policies. Fundamentally, zero trust may require a change in an organization's cybersecurity philosophy and culture."

## Evidence

The document explicitly contrasts the "old" model (perimeter-based, location = trust) with the "new" model (identity + context + data-centric, continuous verification). It acknowledges that this is not a technology swap — it's a culture change. The cost discussion notes that initial implementation adds costs, but long-term enables "more prudent allocation of security investments toward the most critical data and services."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Every major ZT framework (NIST, DoD, NSA, Google BeyondCorp) agrees on this shift. The cultural dimension is well-observed in practice — agencies that treat ZTA as a technology project fail; those that treat it as a cultural transformation succeed.

## Stakes

If the shift is overstated (i.e., ZTA is mostly a technology refresh), organizations can implement it as an IT project. If it's genuinely cultural, it requires executive sponsorship, organizational change management, and multi-year commitment. Underestimating the cultural dimension is the single most common failure mode in ZTA adoption.

## Disagreement

**Who disagrees:**

Vendors selling ZT products minimize the cultural dimension — their marketing suggests ZTA is a technology deployment. The "ZT is a journey not a destination" framing (used by both NIST and CISA) directly counters this. NSA's guidance is even more explicit: ZTA requires "a fundamental shift in how we architect networks."

**Alternative reading:**

The cultural change argument could be self-serving for CISA — it justifies their continued involvement beyond initial guidance publication and explains why agencies can't just "buy ZT." But the evidence from large-scale ZTA deployments (Google BeyondCorp, which took ~7 years) supports the cultural argument.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

Claim is well-founded but hard to verify. The cultural dimension is real, but its importance varies by agency size and starting point. A small agency with cloud-native infrastructure may find the technical shift trivial and the cultural shift modest. A large legacy agency (DHS, DoD) will find both difficult. The ZTMM's maturity levels effectively accommodate this variance — you don't need to reach Optimal everywhere.
