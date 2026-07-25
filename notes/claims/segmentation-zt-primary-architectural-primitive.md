---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/halley-resilient-cloud
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
claim_id: "halley.2"
statement: "Segmentation is ZT's primary architectural primitive — macro for trust zones, micro for workload isolation"
confidence: "high"
confidence_rationale: "HIGH for the segmentation taxonomy; MODERATE for the claim that SGTs are the optimal mechanism (this is Cisco's product position)."
claim_type: "implementation"
source_note: "[[Halley — Zero Trust in Resilient Cloud]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# halley.2: Segmentation is ZT's primary architectural primitive — macro for trust zones, micro for workload isolation

**Source:** [[Halley — Zero Trust in Resilient Cloud]] — Andrew Halley et al., *Zero Trust in Resilient Cloud*, 2023

## The Claim

Segmentation is *the* mechanism for enforcing least-privilege access and containing breaches. Macrosegmentation (VRFs, VLANs, VPCs) defines high-level trust zones (corporate users, guests, contractors, OT, PCI). Microsegmentation (TrustSec SGTs, Kubernetes network policies, security groups) enforces per-workload access control within zones. The architectural progression is: no segmentation → macro → micro → identity-based micro.

## Evidence

The book traces the evolution from physical segmentation (separate switches) → VLANs → VRFs → SDN-based segmentation (ACI, SD-Access) → cloud-native segmentation (security groups, Kubernetes policies, service mesh). TrustSec's Scalable Group Tags (SGTs) are presented as the on-premises implementation of identity-based microsegmentation — a packet carries the source group tag, and enforcement points along the path apply policy based on source group × destination group. In cloud, the equivalent is Kubernetes NetworkPolicy + Cilium or Istio AuthorizationPolicy.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH for the segmentation taxonomy; MODERATE for the claim that SGTs are the optimal mechanism (this is Cisco's product position).

## Stakes

Segmentation is the bridge between ZT architecture (NIST's logical components) and network engineering. Without segmentation, "least privilege" is a policy statement with no enforcement mechanism. With segmentation, policy becomes topology.

## Disagreement

**Who disagrees:**

Application-layer ZT proponents (service mesh, API gateway) argue that network segmentation is insufficient — applications need application-layer authorization regardless of network topology. Halley addresses this with the cloud-native security stack (Ch15-16), arguing for defense in depth: network segmentation + application-layer auth + API security.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[cloud|Segmentation as ZT's primary architectural primitive aligns with the service mesh acting as the enforcement point for id]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The segmentation taxonomy is useful for OSKG-ZeroTrust because it maps the architectural primitive to the NIST 800-207 logical components. Where NIST says "PEP," Halley says "here's what a PEP looks like in a campus, data center, and cloud."
