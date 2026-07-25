---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/bsi
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-trust
  - topic/zt-maturity
claim_id: "bsi-zt.5"
statement: "BSI specifies five mandatory prerequisites before ZT implementation can begin"
confidence: "high"
confidence_rationale: "HIGH. These prerequisites are methodologically sound and consistent with established ZT implementation guidance (Finney's five-step methodology step"
claim_type: "definitional"
source_note: "[[BSI — Zero Trust Position Paper]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# bsi-zt.5: BSI specifies five mandatory prerequisites before ZT implementation can begin

**Source:** [[BSI — Zero Trust Position Paper]] — BSI, *Zero Trust Position Paper*, 2023

## The Claim

Before any technical ZT measures can be planned, five prerequisites must be met (*Voraussetzungen*):

1. **Identify and prioritize central business processes** — requires a significantly more differentiated analysis of business processes than currently exists in most organizations, extending beyond IT support process definitions
2. **Identify all involved parties within the organization** — determines organizational units involved in each business process, deriving roles that serve as the basis for PDP access decisions
3. **Identify additional requirements from laws, regulations, or other legal influences** — these may affect which measures are implemented and in what order
4. **Identify all involved resources (especially data, systems, applications)** — derived from business processes; prerequisite for fine-grained access rules
5. **Formulate security policies containing ZT measures** — these serve as the basis for PDP access decisions and must be translatable into machine-readable attributes

## Evidence

_No evidence separable from the claim statement in the source note._

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These prerequisites are methodologically sound and consistent with established ZT implementation guidance (Finney's five-step methodology step 1 "Define the protect surface," Green-Ortiz's discovery workshop).

## Stakes

The BSI explicitly warns that "as long as an organization does not fulfill the basic prerequisites for integrating ZT principles, the probability that integration approaches will fail or potentially even adversely affect IT security is high." This is a stronger warning than any other national framework — the BSI is essentially saying that organizations that skip the business process analysis stage should not attempt ZT implementation at all.

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

Prerequisite 2 (involved parties) and 3 (legal requirements) are where the BSI model most clearly departs from US frameworks. The emphasis on organizational unit mapping and legal compliance before technical implementation reflects German organizational culture and regulatory environment. A US organization might start with technical pilots and backfill governance; the BSI model requires governance first. This is neither better nor worse, but it has significant implications for project planning: a BSI-compliant ZT implementation may have a longer pre-implementation phase than a CISA- or NIST-driven one.
