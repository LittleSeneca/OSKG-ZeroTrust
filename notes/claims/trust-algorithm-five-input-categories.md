---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-trust
  - topic/zt-policy
  - topic/zt-architecture
  - topic/zt-governance
claim_id: "nist207-ch3.5"
statement: "The Trust Algorithm is the PE's decision-making process with five input categories"
confidence: "high"
confidence_rationale: "HIGH — The input taxonomy is comprehensive. Every ZT implementation uses some version of these inputs. The distinction between Subject Database (who"
claim_type: "architectural"
source_note: "[[NIST 800-207 — Ch3 — Logical Components]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch3.5: The Trust Algorithm is the PE's decision-making process with five input categories

**Source:** [[NIST 800-207 — Ch3 — Logical Components]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

The trust algorithm (TA) is "the brain" of the ZTA — the process the PE uses to grant or deny access. It takes five categories of input: (1) Access Request (resource requested, requester info, OS/patch level), (2) Subject Database (who is requesting, attributes, privileges, historical behavior), (3) Asset Database (known vs. observable asset status, OS, software integrity, location, patch level), (4) Resource Requirements (minimum requirements including authenticator assurance levels, network location constraints, data sensitivity), and (5) Threat Intelligence (external/internal feeds about active threats, malware, vulnerabilities).

## Evidence

Conceptual model (Figure 7) with categorized inputs. NIST notes that input weights may be proprietary or enterprise-configured.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The input taxonomy is comprehensive. Every ZT implementation uses some version of these inputs. The distinction between Subject Database (who you are) and Asset Database (what you're on) captures the two primary dimensions of access decisions.

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

This is one of NIST's most durable contributions — the five-category input model provides a template against which any ZT product's decision inputs can be evaluated. The CISA Maturity Model operationalizes each input category through its pillar structure. The DoD Reference Architecture adds mission-criticality and operational tempo as additional context inputs.
