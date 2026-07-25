---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-network
  - topic/zt-segmentation
  - topic/zt-architecture
  - topic/zt-cloud
claim_id: "go-ch6-8.1"
statement: "True ZT segmentation requires enforcement at every OSI layer — layering is not optional but the ideal-world answer, pushing back against the firewall-centric mindset that considers one enforcement point sufficient."
confidence: "high"
confidence_rationale: "HIGH — The all-layers position is a specific, well-articulated thesis supported by detailed OSI-layer mapping. It distinguishes Green-Ortiz from"
claim_type: "implementation"
source_note: "[[Green-Ortiz — Ch6-8 — Implementation]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch6-8.1: True ZT segmentation requires enforcement at every OSI layer — layering is not optional but the ideal-world answer, pushing back against the firewall-centric mindset that considers one enforcement point sufficient.

**Source:** [[Green-Ortiz — Ch6-8 — Implementation]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

"In an ideal world, which segmentation methodology works best? The answer, simply put, is all of them." Green-Ortiz organizes segmentation across all seven OSI layers from physical cabling through application logic, arguing that no single technology is sufficient.

## Evidence

A comprehensive OSI-layer mapping: Layer 1 (Physical) — separate cabling, air-gapped networks for defense/manufacturing; Layer 2 (Data Link) — VLAN assignment, TrustSec SGT embedding in frame headers, private VLANs for east-west control; Layer 3 (Network) — IP-based ACLs, routing policies, VRF isolation; Layer 4 (Transport) — stateful firewalling, ACLs, cloud security groups, SGT-based policy; Layer 5 (Session) — dedicated control channels, protocol validation; Layer 6 (Presentation) — checksums, encryption, message integrity; Layer 7 (Application) — containers, application sandboxing, process isolation. The authors' emphasis is that the firewall-centric mindset considers one enforcement point sufficient — this is explicitly rejected.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The all-layers position is a specific, well-articulated thesis supported by detailed OSI-layer mapping. It distinguishes Green-Ortiz from sources that focus primarily on Layer 3/4 enforcement.

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
- [[east-west-segmentation-controlling-traffic-within-the-same-vlansubnet|Enforcement at every OSI layer — especially Layer 2 with SGTs — is how east-west segmentation within the same VLAN becom]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
