---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-implementation
  - topic/zt-cloud
  - topic/zt-architecture
claim_id: "go-intro.7"
statement: "Enforcement must be layered and applied as close to the source as possible"
confidence: "medium"
confidence_rationale: "MEDIUM. Confidence not explicitly stated in source."
claim_type: "implementation"
source_note: "[[Green-Ortiz — Intro Ch1-2 — Foundations]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-intro.7: Enforcement must be layered and applied as close to the source as possible

**Source:** [[Green-Ortiz — Intro Ch1-2 — Foundations]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

Enforcement must be layered and applied as close to the source as possible

## Evidence

Detailed treatment of CASB (shadow IT visibility, cloud access governance), DDoS protection, DLP (data creation, movement, storage, backup, destruction), DNSSEC, email security, firewalls (packet filtering, NGFW with DPI, NAT, SMLI inspecting all seven OSI layers), IPS (signature/anomaly/policy-based; NIPS/HIPS/NBA/WIPS platforms), proxy (forward for outbound control, reverse for inbound services), VPN (MPLS, RA VPN, VRF for traffic isolation), SOAR (automated policy orchestration across tools), FIM (file change detection triggering trust status changes), and segmentation (identifying and isolating sets of systems into enclaves).

**Green-Ortiz's claim:**

Enforcement is the goal of ZT, but it must be layered throughout the network — from the application layer down through TrustSec tags, downloadable ACLs, firewall rules, and VRF segmentation. No single enforcement point should carry the full burden. Enforcement mechanisms should be applied "as close to the source of the communication as possible" to minimize lateral movement opportunities.

**Key dynamics:**

- **The four firewall types serve different ZT roles.** Packet filtering for basic boundary control, NGFW for deep packet inspection and threat prevention, NAT for IP obfuscation, SMLI for full-stack inspection.
- **SOAR enables automated policy response.** Tie vulnerability management to NAC: if a device is found vulnerable, SOAR can automatically restrict its network access until remediation. This is the automation that makes ZT scalable.
- **FIM + SOAR enables real-time trust status changes.** Unexpected file changes on a server can trigger automatic isolation via orchestrated enforcement actions.
- **Segmentation is the art of defining enclaves.** "The foundational process for identification and classification of corporate assets is essential to creating a Zero Trust Architecture, where defining segments or enclaves is used to establish trusts to other enclaves."

**Cross-reference — NIST 800-207 Ch3:**

NIST's PEP (Policy Enforcement Point) is the logical abstraction. Green-Ortiz's Enforcement pillar enumerates the concrete technologies that can serve as PEPs — firewalls, proxies, VPN concentrators, NAC systems, SOAR platforms. NIST defines the function; Green-Ortiz catalogs the implementations.

**Cross-reference — Gilman & Barth Ch1:**

Gilman & Barth's control plane / data plane split maps Enforcement to the data plane — "the data plane accepts configuration from the control plane and enforces it." Green-Ortiz adds the operational layer: which enforcement technologies to deploy where, and how to layer them for defense-in-depth.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. Confidence not explicitly stated in source.

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

The Enforcement pillar is the most Cisco-specific section of the book — many of the technologies described (TrustSec tags, ISE-based NAC, Cisco firewalls) reflect Cisco's product portfolio. However, the *principles* (layered enforcement, source-close application, SOAR-driven automation) are vendor-neutral and well-articulated. The segmentation discussion in particular foreshadows Chapter 6 which provides the book's most detailed technical content.
