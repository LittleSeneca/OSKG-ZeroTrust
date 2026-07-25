---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cccs
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-architecture
claim_id: "cccs-model.1"
statement: "ZT is defined through the CISA five-pillar model rather than NIST tenets"
confidence: "high"
confidence_rationale: "HIGH. The CISA model is the most cited ZT framework for maturity progression, and using it simplifies ZT communication to non-technical audiences"
claim_type: "definitional"
source_note: "[[CCCS — Zero Trust Security Model]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cccs-model.1: ZT is defined through the CISA five-pillar model rather than NIST tenets

**Source:** [[CCCS — Zero Trust Security Model]] — Canadian Centre for Cyber Security, *Zero Trust Security Model — ITSAP.10.008*, 2023

## The Claim

"The term 'Zero Trust' (ZT) does not apply to a single product, technology, or architecture layer. Rather, it represents a security framework for protecting infrastructure and data. ZT's central tenet is that no subject (application, user, or device) in an information system is trusted by default. Trust must be re-assessed and verified every time a subject requests access to a new resource."

## Evidence

Unlike ITSM.10.008 (which uses NIST's seven tenets), ITSAP.10.008 organizes ZT understanding around CISA's five pillars — Identity, Device, Network/Environment, Application Workload, and Data — plus three cross-cutting capabilities (Visibility & Analytics, Automation & Orchestration, Governance). Each pillar is given a single-paragraph description at the Traditional-to-Optimal maturity spectrum.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The CISA model is the most cited ZT framework for maturity progression, and using it simplifies ZT communication to non-technical audiences. The choice of CISA over NIST reflects the document's awareness purpose — CISA's pillar model is more visually intuitive and easier to remember than NIST's seven tenets.

## Stakes

If readers take the five pillars as *the* definition of ZT rather than one framework among several, they may treat ZT as a checklist of five technology domains rather than an architectural philosophy.

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

This is a defensible editorial choice for an awareness document. The five pillars are concrete domains that non-technical readers can map to their organization (Identity = HR/IT, Device = endpoint management, Network = infrastructure, Application = development, Data = information management). NIST's tenets ("all data sources and computing services are considered a resource") are conceptually deeper but harder to operationalize for a general audience.
