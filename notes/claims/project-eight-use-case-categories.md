---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-1800-35
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-governance
claim_id: "nist-1800-35.5"
statement: "The project's eight use case categories (A–H) provide a comprehensive ZTA testing framework — from discovery through data-level security — that organizations can adapt for their own validation."
confidence: "high"
confidence_rationale: "HIGH on the comprehensiveness of the use case framework — covers the full identity spectrum (enterprise, federated, external, guest), both human and"
claim_type: "implementation"
source_note: "[[NIST 1800-35 — Implementing ZTA]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist-1800-35.5: The project's eight use case categories (A–H) provide a comprehensive ZTA testing framework — from discovery through data-level security — that organizations can adapt for their own validation.

**Source:** [[NIST 1800-35 — Implementing ZTA]] — NIST, *SP 1800-35 — Implementing a Zero Trust Architecture*, 2023

## The Claim

The project's eight use case categories (A–H) provide a comprehensive ZTA testing framework — from discovery through data-level security — that organizations can adapt for their own validation.

## Evidence

_No evidence separable from the claim statement in the source note._

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the comprehensiveness of the use case framework — covers the full identity spectrum (enterprise, federated, external, guest), both human and non-person entities, session lifecycle management, and data sensitivity. The framework can serve as a ZTA testing template.

## Stakes

_Not addressed separately in the source note._

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

The use case framework may be the document's most exportable artifact. Organizations can take these eight categories and map them to their own environments, creating a ZTA testing/validation suite. The stolen credential scenarios (B-3, C-7, D-3) are particularly valuable — they test whether ZTA controls actually work against the attack they're designed to prevent. Use Case G (service-to-service) is a strong complement to SP 800-207A's identity-tier policy framework — it operationalizes the concept with specific test scenarios.
