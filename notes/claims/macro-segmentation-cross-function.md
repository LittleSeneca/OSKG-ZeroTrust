---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-network-pillar
  - topic/zt-network
  - topic/zt-segmentation
  - topic/zt-architecture
  - topic/zt-definition
claim_id: "nsa-network.3"
statement: "Macro segmentation prevents lateral movement between business functions"
confidence: "high"
confidence_rationale: "HIGH. Macro segmentation is a mature concept (VLANs, VRFs, security zones) that predates Zero Trust by decades. NSA's contribution is positioning it"
claim_type: "implementation"
source_note: "[[NSA — Network Environment Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-network.3: Macro segmentation prevents lateral movement between business functions

**Source:** [[NSA — Network Environment Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the Network and Environment Pillar*, 2024

## The Claim

Macro segmentation "provides high-level control over traffic moving between various areas of an organization's network by breaking up a network into multiple discrete components with each supporting a different security requirement." It can be thought of as "the separation of sub-organizations within a company." These boundaries, "coupled with access controls, provide security by shrinking the attack surface to prevent lateral movement."

## Evidence

Four-phase maturity progression:

| Phase | Capability |
|-------|-----------|
| **Preparation** | Define different security levels on the network. Map the logical distinctions in network structure. |
| **Basic** | Segment networks based on business functions, locations, and asset criticality. Strengthen internal security controls within existing segments (e.g., VLANs). |
| **Intermediate** | Access policies restricting lateral movement between segments are defined and written into firewall rules based on security policies. |
| **Advanced** | Network further segmented into more granular components. Automated central management system integrated and configured to manage network growth. |

**Cross-reference to NIST 800-207 §3.2.2 (Enclave-Based Deployment):**

NIST's enclave-based model is essentially macro segmentation applied at the resource level — a gateway protects a collection of resources serving a single business function. NIST correctly identifies the key downside: "subjects may see resources they don't have access to." NSA's micro segmentation layer addresses exactly this limitation.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Macro segmentation is a mature concept (VLANs, VRFs, security zones) that predates Zero Trust by decades. NSA's contribution is positioning it as the *first layer* of a multi-layer segmentation strategy, not the only layer.

## Stakes

Many organizations stop at macro segmentation and consider their networks "segmented." The NSA's model makes clear that macro is necessary but insufficient — micro segmentation is the next required layer. The maturity progression from Basic (VLANs) to Intermediate (firewall-enforced access policies) to Advanced (automated central management) defines the gap between traditional network segmentation and ZT-grade macro segmentation.

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
  - "[[network-segmentation-micro-perimeters]]"

## Assessment

The key insight in NSA's maturity model is at the Intermediate level — the shift from "segment the network" (Basic) to "write access policies that restrict lateral movement between segments" (Intermediate). Many organizations have VLANs but no explicit lateral movement prevention rules between them. That gap is where the Target breach occurred.
