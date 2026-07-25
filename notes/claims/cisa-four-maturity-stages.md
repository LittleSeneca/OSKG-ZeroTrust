---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-identity
  - topic/zt-maturity
  - topic/zt-governance
  - topic/zt-access-mgmt
claim_id: "cisa-ztmm-id.2"
statement: "CISA defines four maturity stages — Traditional (manual, static, perimeter-based), Initial (automation begins, some cloud integration, MFA required), Advanced (phishing-resistant MFA, dynamic risk assessments, session-based access), and Optimal (fully automated, continuous validation, JIT/JEA, behavior-based analytics) — that apply across all pillars."
confidence: "high"
confidence_rationale: "HIGH. These are direct definitions from the source document."
claim_type: "maturity"
source_note: "[[CISA ZTMM — Identity Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-id.2: CISA defines four maturity stages — Traditional (manual, static, perimeter-based), Initial (automation begins, some cloud integration, MFA required), Advanced (phishing-resistant MFA, dynamic risk assessments, session-based access), and Optimal (fully automated, continuous validation, JIT/JEA, behavior-based analytics) — that apply across all pillars.

**Source:** [[CISA ZTMM — Identity Pillar]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

CISA defines four maturity stages that apply across all pillars. (§5.1)

## Evidence

| Stage | Core Characteristic |
|-------|-------------------|
| **Traditional** | Manual processes, static policies, perimeter-based trust, legacy infrastructure. Passwords or basic MFA only. |
| **Initial** | Automation begins. Attribute-based policies, some cloud identity integration, MFA required but not necessarily phishing-resistant. |
| **Advanced** | Phishing-resistant MFA deployed; identity stores consolidated across environments; dynamic risk assessments inform access decisions; session-based and need-based access. |
| **Optimal** | Fully automated, continuous validation; just-in-time/just-enough access; real-time risk-based decisions; comprehensive cross-pillar interoperability; behavior-based analytics. |

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These are direct definitions from the source document.

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
- [[authentication-keystone-identity-function|The four maturity stages (Traditional through Optimal) provide the framework for understanding the authentication capabi]]
  - "[[cross-pillar-maturity-trajectory]]"

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[access-management-permanent-to-jit-jea|Provides the general four-stage maturity framework (Traditional→Optimal) that the access management progression specific]]

## Assessment

_Not addressed separately in the source note._
