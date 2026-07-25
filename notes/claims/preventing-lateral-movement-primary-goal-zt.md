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
claim_id: "cccs-arch.3"
statement: "Preventing lateral movement is the *primary* goal of ZT"
confidence: "high"
confidence_rationale: "HIGH. This aligns with NIST's threat model and the Jericho Forum's original \"de-perimeterization\" thesis. CCCS's emphasis on lateral movement as"
claim_type: "architectural"
source_note: "[[CCCS — ZT Approach to Security Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cccs-arch.3: Preventing lateral movement is the *primary* goal of ZT

**Source:** [[CCCS — ZT Approach to Security Architecture]] — Canadian Centre for Cyber Security, *Zero Trust Approach to Security Architecture — ITSM.10.008*, 2023

## The Claim

"It's important to note that preventing lateral movement is the primary goal of ZT, not the elimination of the legacy boundary defence or bring your own device (BYOD). These are things that may be enabled by ZT but should not be seen as primary reason for doing ZT."

## Evidence

The document anchors its threat model in the lateral movement attack pattern: "We often hear of attacks that involve a compromised user account or device being used as an entry point... Once in, the attacker will then progress laterally in the network to gain access to credentials or other sensitive information."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This aligns with NIST's threat model and the Jericho Forum's original "de-perimeterization" thesis. CCCS's emphasis on lateral movement as *primary* goal (rather than continuous verification or least privilege) is a usefully concrete framing for organizations trying to measure ZT success: "Does this change reduce lateral movement?" is a more actionable metric than "Does this improve trust?"

## Stakes

If lateral movement prevention is the primary goal, then ZT investments should be evaluated against that criterion. Technologies that improve authentication but don't constrain lateral movement (e.g., MFA at the perimeter only) are insufficient.

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

This is the most operationally useful framing in the document. It gives organizations a clear success metric: can a compromised workload reach other workloads? It also explains why ZT is more than just strong authentication — authentication without microsegmentation still allows lateral movement from authenticated positions.
