---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cccs
  - topic/zt-architecture
  - topic/zt-implementation
  - topic/zt-cloud
  - topic/zt-network
claim_id: "cccs-arch.4"
statement: "Organizations should choose among NIST, CISA, and NCSC frameworks — not invent their own"
confidence: "high"
confidence_rationale: "HIGH. These are the three most-cited ZT frameworks globally, and the summaries are accurate."
claim_type: "architectural"
source_note: "[[CCCS — ZT Approach to Security Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cccs-arch.4: Organizations should choose among NIST, CISA, and NCSC frameworks — not invent their own

**Source:** [[CCCS — ZT Approach to Security Architecture]] — Canadian Centre for Cyber Security, *Zero Trust Approach to Security Architecture — ITSM.10.008*, 2023

## The Claim

The document provides an overview of "three commonly cited and trusted ZT frameworks/guidelines" and recommends organizations "choose which framework or set of guidelines aligns best with their business requirements and network infrastructure." The three are:

1. **NIST SP 800-207** (August 2020): Seven basic tenets, abstract logical architecture, technology-agnostic. "Helps agencies reduce implicit trust zones and better understand their network infrastructure."
2. **CISA ZTMM** (June 2021): Five pillars (Identity, Device, Network, Application Workload, Data) plus three cross-cutting capabilities, three maturity stages (Traditional → Advanced → Optimal). "One of many roadmaps to support the transition to ZT."
3. **NCSC** (UK, July 2021): Eight design principles for architecture review. "Most ZT approaches can be linked to these eight core principles."

## Evidence

The document provides detailed summaries of all three frameworks: the full seven NIST tenets, the five CISA pillars with maturity stage descriptions, and all eight NCSC principles. The level of detail for each is sufficient for a reader to make an informed choice without consulting the original documents.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These are the three most-cited ZT frameworks globally, and the summaries are accurate.

## Stakes

By curating the frameworks rather than creating a fourth, CCCS avoids fragmenting the ZT standards landscape while providing Canadian-specific context. This is the responsible approach for a national cyber agency.

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

This section is the document's primary value-add for the OSKG. It provides a single reference point that maps all three frameworks, including cross-cutting observations: NIST provides the *tenets* (what to believe), CISA provides the *maturity path* (how to progress), and NCSC provides the *design principles* (how to build). Organizations should use all three in combination, not pick one.
