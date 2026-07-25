---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-1800-35
  - topic/zt-implementation
claim_id: "nist-1800-35.1"
statement: "ZTA implementation is not a single architecture but a spectrum of deployment approaches — EIG, SDP, Microsegmentation, and SASE — each appropriate for different organizational contexts and maturity levels. The most complete ZTAs combine multiple approaches."
confidence: "high"
confidence_rationale: "HIGH. The four-approach taxonomy is consistent with SP 800-207's deployment models and reflects real market segmentation. The phased"
claim_type: "implementation"
source_note: "[[NIST 1800-35 — Implementing ZTA]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist-1800-35.1: ZTA implementation is not a single architecture but a spectrum of deployment approaches — EIG, SDP, Microsegmentation, and SASE — each appropriate for different organizational contexts and maturity levels. The most complete ZTAs combine multiple approaches.

**Source:** [[NIST 1800-35 — Implementing ZTA]] — NIST, *SP 1800-35 — Implementing a Zero Trust Architecture*, 2023

## The Claim

ZTA implementation is not a single architecture but a spectrum of deployment approaches — EIG, SDP, Microsegmentation, and SASE — each appropriate for different organizational contexts and maturity levels. The most complete ZTAs combine multiple approaches.

## Evidence

**Author's structure:**

The project organized 19 builds across four simulated enterprises, each representing a different organizational starting point. Each enterprise could host multiple builds with different vendor combinations:

**Four ZTA deployment approaches:**

1. **Enhanced Identity Governance (EIG)** — Leverages ICAM solutions as Policy Decision Points. The identity-centric approach — authenticate users and devices, make access decisions based on identity attributes and endpoint health. Foundation of ZTA. Two phases: Crawl (on-premises only) and Run (adds cloud capabilities).
2. **Software-Defined Perimeter (SDP)** — Reconfigures network connectivity based on access decisions. Establishes secure tunnels between requesting endpoints and resources. Application-layer SDP uses agents on endpoints; network-layer SDP uses gateway appliances. "Darkens" resources — they're not discoverable until access is granted.
3. **Microsegmentation** — Places resources on unique network segments protected by gateway components and/or host-based agents. Fine-grained east-west traffic control within the perimeter. Can be network-based (VLANs, firewall rules) or host-based (software agents on endpoints).
4. **Secure Access Service Edge (SASE)** — Converged network + security delivered as a cloud service. Includes SD-WAN, SWG, CASB, NGFW, and ZTNA. Primarily cloud-delivered; enables identity-based zero trust access with real-time context.

**Three implementation phases:**

- **EIG Crawl** (3 builds) — Minimum viable ZTA: ICAM + endpoint security + SIEM. On-premises only. No cloud, no SDP, no microsegmentation. Demonstrates what organizations can achieve with legacy ICAM without adding ZTA-specific capabilities.
- **EIG Run** (3 builds) — Adds cloud-hosted resources, device discovery with enforcement, secure tunnels to private resources, proxy connectors for resource invisibility. Cloud capabilities without full SDP/SASE investment.
- **SDP, Microsegmentation, and SASE** (13 builds) — Unconstrained ZTA reference architecture. All four deployment approaches, singly and in combination. Full supporting component integration (data security, security analytics, advanced endpoint protection).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The four-approach taxonomy is consistent with SP 800-207's deployment models and reflects real market segmentation. The phased crawl→run→advanced approach is the document's most important architectural contribution — it gives organizations a clear maturity ladder.

## Stakes

If organizations treat the approaches as mutually exclusive, they'll miss the integration value. The builds that combine approaches (SDP + Microsegmentation, SDP + SASE) demonstrated richer ZTA functionality than single-approach builds. The phased approach counters vendor claims that ZTA requires wholesale replacement.

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

The four-approach taxonomy is the document's conceptual backbone and will age well. The market is evolving toward convergence (SASE incorporating SDP; microsegmentation incorporating identity), but the taxonomy captures distinct architectural patterns that remain useful for planning. The crawl→run→advanced phasing is the most important takeaway for organizations — it directly refutes "ZTA is too hard/complex/expensive" objections.
