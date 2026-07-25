---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/beyondprod
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
claim_id: "beyondprod.1"
statement: "Perimeter security breaks down for microservices because services are mobile, ephemeral, share infrastructure, and change at extreme velocity — BeyondProd replaces network-location trust with verifiable attributes (identity, code provenance, hardware integrity)."
confidence: "high"
confidence_rationale: "HIGH — This is Google's production architecture, actively operating at the scale of billions of containers per week. The problem statement is"
claim_type: "implementation"
source_note: "[[BeyondProd — Cloud-Native Security]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondprod.1: Perimeter security breaks down for microservices because services are mobile, ephemeral, share infrastructure, and change at extreme velocity — BeyondProd replaces network-location trust with verifiable attributes (identity, code provenance, hardware integrity).

**Source:** [[BeyondProd — Cloud-Native Security]] — Google, *BeyondProd: Cloud-Native Security*, 2019

## The Claim

Google argues that traditional perimeter-based security fails in a cloud-native environment because: (1) microservices are deployed across heterogeneous hosts, rescheduled constantly, and lack fixed IP addresses; (2) in a monolithic app, internal components implicitly trust each other, but in microservices each service is independently developed and deployed — mutual trust must be explicitly established; (3) multiple workloads from different tenants share the same physical hosts, making network segmentation alone insufficient; (4) Borg deploys several billion containers per week, requiring security that scales at the same velocity.

## Evidence

Four failure modes of perimeter security in microservice environments are enumerated. The solution is six integrated security services that together form the BeyondProd trust stack: GFE (network edge), ALTS (service-to-service auth), BAB (code provenance), Host Integrity (hardware-rooted machine trust), Service Access Management + End-User Context Tickets (policy enforcement), and gVisor (workload isolation).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — This is Google's production architecture, actively operating at the scale of billions of containers per week. The problem statement is grounded in operational reality.

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
