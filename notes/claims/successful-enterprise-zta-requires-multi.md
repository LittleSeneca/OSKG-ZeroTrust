---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207a
  - topic/zt-cloud
  - topic/zt-implementation
claim_id: "nist-207a.3"
statement: "A successful enterprise ZTA requires multi-tier policies combining network-tier (coarse + fine-grained) and identity-tier policies — neither tier alone is sufficient."
confidence: "high"
confidence_rationale: "HIGH. This is the document's most valuable and least controversial contribution. The multi-tier framework accurately reflects operational reality"
claim_type: "implementation"
source_note: "[[NIST 800-207A — Cloud-Native Access Control]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist-207a.3: A successful enterprise ZTA requires multi-tier policies combining network-tier (coarse + fine-grained) and identity-tier policies — neither tier alone is sufficient.

**Source:** [[NIST 800-207A — Cloud-Native Access Control]] — NIST, *SP 800-207A — Cloud-Native Access Control*, 2023

## The Claim

"A successful enterprise ZTA requires multi-tier policies that combine network-tier and identity-tier policies." (§3, lines 679–680)

## Evidence

- Network-tier alone can't handle the dynamism of cloud-native workloads — firewall rules "have to be continuously changed" as containers migrate and scale (lines 708–709).
- Identity-tier alone can't satisfy compliance requirements (PCI/DSS) that mandate network-level segmentation (lines 673–675).
- Identity-tier alone can't capture location-based risk — "purely identity-based enforcement should be augmented by other factors (e.g., network location) to evaluate risk when performing context-based authorization" (lines 660–662).
- Multi-tier policies provide flexibility: "network-tier policies can be relatively static while identity-tier policies higher up in the stack... can be dynamic" (lines 710–712).

**Policy tier taxonomy** (lines 828–884):
1. **Coarse-grained network-tier** — Firewall rules specifying allowed IP/subnet/port combinations (e.g., "allow 10.100.2.3/30:15443 → 10.1.2.3/30:15443"). Static perimeter controls.
2. **Fine-grained network-tier** — Microsegmentation policies specifying traffic pathways through gateways, proxies, and network segments. East-west traffic control inside the perimeter.
3. **Identity-tier (mesh-level)** — Service-to-service authorization based on cryptographic identities. Example: "Service-1 can call Service-2 on port 443, GET method, /public path only" — enforced at the application request level via the service mesh.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is the document's most valuable and least controversial contribution. The multi-tier framework accurately reflects operational reality — most enterprises have firewalls (can't remove them), need microsegmentation (compliance), and want identity-based controls (cloud-native agility). The framework accommodates incremental adoption without requiring wholesale replacement.

## Stakes

If multi-tier is accepted as necessary, ZTA procurement and architecture must address all three tiers. Organizations can't buy a "ZTA product" that only does identity-tier — they need integration across firewalls, network segmentation tools, and service mesh/IAM infrastructure. This raises the integration complexity bar significantly.

## Disagreement

**Who disagrees:**

Pure-play ZTNA vendors (Zscaler, Appgate) argue their approach *replaces* network-tier controls with identity-based tunnels, making network-tier policies obsolete for access control. NIST's compliance argument (PCI/DSS) is the strongest counter: you can't deregister your firewalls just because you have ZTNA. Pure SASE proponents argue the convergence happens in the cloud edge, not in enterprise infrastructure.

**Alternative reading:**

Multi-tier is a transition strategy, not an end state. As identity infrastructure matures and compliance frameworks adapt, the network tier can atrophy. ZTNA + microsegmentation via identity may eventually make network-tier policies vestigial.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The multi-tier framework is the document's most pragmatic contribution. It gives organizations permission to keep their firewalls while adding identity controls — politically essential for enterprise adoption. The risk is that organizations treat multi-tier as an excuse to avoid the hard identity work and just rebrand their existing network segmentation as "ZT." The compliance argument is double-edged: it grounds the framework in regulatory reality but may also anchor it to legacy requirements that will eventually evolve.
