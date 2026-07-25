---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-policy
  - topic/zt-governance
claim_id: "go-ch6-8.8"
statement: "Top-down (business-aligned) and bottom-up (traffic-aligned) design approaches are complementary, not competing — use top-down for high-level architecture and bottom-up for validation and detailed policy creation."
confidence: "high"
confidence_rationale: 'HIGH — The top-down/bottom-up distinction resolves the "where do we start?" question that paralyzes most organizations. The three deployment'
claim_type: "governance"
source_note: "[[Green-Ortiz — Ch6-8 — Implementation]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch6-8.8: Top-down (business-aligned) and bottom-up (traffic-aligned) design approaches are complementary, not competing — use top-down for high-level architecture and bottom-up for validation and detailed policy creation.

**Source:** [[Green-Ortiz — Ch6-8 — Implementation]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

The chapter's core planning contribution distinguishes two design approaches: top-down (business-aligned — starts with executive buy-in and business drivers, defines segments by business function and regulatory compliance) and bottom-up (traffic-aligned — starts with traffic collection and identity mapping, determines segmentation based on observed communication patterns). "The implementation of segmentation may require that both of these strategies be utilized for the best results to be achieved."

## Evidence

Top-down is best for regulated industries with clear business-unit boundaries where endpoints cleanly map to organizational units. Bottom-up is best for consulting firms (one person spans multiple BUs), shared physical servers hosting multiple BU VMs, and politically siloed organizations where cross-department communication is unknown. Three deployment templates: (1) By Site Type — classify sites, build reusable patterns (Business Services, Building IoT, Infrastructure Management, Guest, Shared Services); (2) By Endpoint Category — homogeneous populations, healthcare example mapping Imaging/Pharma/Point of Care/Labs/Clinical VDI; (3) By Service Type — policy enforcement points at organizational boundaries (Partner VPN, Employee VPN, Partner Leased Lines, DMZ, Corporate WAN, Guest Internet, Unknown). Warning: "One organization went so far as to attempt to describe endpoints based on age" — categorizations must be actionable from available contextual identity data.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The top-down/bottom-up distinction resolves the "where do we start?" question that paralyzes most organizations. The three deployment templates provide concrete organizational structures for planning.

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

_Not addressed separately in the source note._
