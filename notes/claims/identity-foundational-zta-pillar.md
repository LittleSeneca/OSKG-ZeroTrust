---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-identity
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-implementation
claim_id: "cisa-ztmm-id.1"
statement: "Identity is the foundational pillar of ZTA — without mature identity capabilities, a ZTA cannot make access decisions, and ICAM serves as the substrate beneath the entire pillar, as established by both CISA's maturity model and NIST 800-207 Chapter 6."
confidence: "high"
confidence_rationale: "HIGH. The foundational status of Identity is cross-validated by NIST, CISA, NSA, and DoD frameworks."
claim_type: "definitional"
source_note: "[[CISA ZTMM — Identity Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-id.1: Identity is the foundational pillar of ZTA — without mature identity capabilities, a ZTA cannot make access decisions, and ICAM serves as the substrate beneath the entire pillar, as established by both CISA's maturity model and NIST 800-207 Chapter 6.

**Source:** [[CISA ZTMM — Identity Pillar]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

Identity is the foundational pillar — without it, a ZTA cannot make access decisions. The pillar covers authentication, identity stores, risk assessments, and access management, each with four maturity levels: **Traditional**, **Initial**, **Advanced**, and **Optimal**.

## Evidence

- The pillar is organized around four operational functions (Authentication, Identity Stores, Risk Assessments, Access Management) plus three cross-cutting capabilities (Visibility & Analytics, Automation & Orchestration, Governance).
- The maturity progression mirrors the NSA User Pillar's four-phase framework (Preparation → Basic → Intermediate → Advanced), though CISA uses different labels and organizes around operational *functions* rather than ICAM sub-capabilities.
- As NIST 800-207 Chapter 6 makes explicit: *without mature ICAM, ZTA cannot function.* The Identity pillar is essentially a maturity framework for that ICAM substrate.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The foundational status of Identity is cross-validated by NIST, CISA, NSA, and DoD frameworks.

## Stakes

_Not addressed separately in the source note._

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
- [[access-mgmt-abac-least-privilege|ABAC, JIT/JEA, and PAM access decisions all require identity to be established and mature; least-privilege enforcement c]]
- [[cdm-visibility-prerequisite-zta|Identity-based access decisions depend on CDM providing answers to 'what is connected' and 'who is on the network' befor]]

**Supports:**
- [[user-identity-and-device-identity-are-separate-trust|A foundational identity pillar must handle separate user and device trust domains with independent trust scores.]]
- [[true-contextual-identity-is-never-just-a-device|Identity being the foundational pillar explains why multi-dimensional contextual profiling matters — without it, access]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
  - "[[ztmm-nist-800-207-definition-foundation]]"

## Assessment

_Not addressed separately in the source note._
