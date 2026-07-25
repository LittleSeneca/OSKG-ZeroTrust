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
claim_id: "halley.1"
statement: "ZT is operationalized through three principles that apply differently per environment"
confidence: "high"
confidence_rationale: "HIGH. The environment-specific comparison is the book's strongest contribution — it addresses the gap between NIST's abstract architecture and the"
claim_type: "implementation"
source_note: "[[Halley — Zero Trust in Resilient Cloud]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# halley.1: ZT is operationalized through three principles that apply differently per environment

**Source:** [[Halley — Zero Trust in Resilient Cloud]] — Andrew Halley et al., *Zero Trust in Resilient Cloud*, 2023

## The Claim

Zero Trust rests on three core principles — Explicit Verification, Least-Privilege Access, and Assume Breach — but how each principle is implemented varies fundamentally between on-premises and cloud environments. On-prem ZT relies on NAC (ISE), 802.1x, TrustSec SGTs, and VLAN segmentation. Cloud ZT relies on IAM policies, security groups, service meshes (Istio), and API gateways. The principles are universal; the mechanisms are environment-specific.

## Evidence

The book dedicates substantial comparative analysis to each principle across deployment models (see Table 1-2 in Ch1). For Explicit Verification: on-premises uses Active Directory/LDAP + RADIUS + MFA; cloud uses AWS IAM / Azure Entra ID / Google Identity + OAuth + OIDC. For Least-Privilege Access: on-premises uses VLAN segmentation + ACLs + 802.1x dynamic VLAN assignment; cloud uses IAM roles + security groups + just-in-time access. For Assume Breach: on-premises uses microsegmentation (TrustSec SGTs) + NetFlow analytics; cloud uses Kubernetes network policies + Cilium + cloud-native SIEM.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The environment-specific comparison is the book's strongest contribution — it addresses the gap between NIST's abstract architecture and the concrete question "how do I actually do this in AWS vs. my data center?"

## Stakes

Organizations with hybrid environments often apply on-prem ZT patterns to cloud (e.g., extending VLANs to cloud) or cloud patterns to on-prem (e.g., expecting IAM roles to replace NAC). Both are mistakes. The principles are the same; the primitives are different.

## Disagreement

**Who disagrees:**

SASE/SSE vendors argue that a cloud-delivered security edge eliminates the on-prem/cloud distinction — all traffic routes through the same enforcement point regardless of where resources live. Halley acknowledges SASE but treats it as one deployment pattern among many, not a universal solution.

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

The environment-specific operationalization fills a real gap in ZT literature. NIST 800-207 says "deploy PEPs close to resources" but doesn't say how that differs for a Kubernetes pod vs. a campus switch port. Halley answers that question, which is why this book deserves Tier 4 placement even though its product references are vendor-specific.
