---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-architecture
  - topic/zt-trust
  - topic/zt-implementation
  - topic/zt-definition
claim_id: "go-ch3-5.1"
statement: "Trust assessment is spatial — the architecture location determines trust data availability and granularity"
confidence: "high"
confidence_rationale: "HIGH. The spatial differentiation of trust assessment is a practical contribution that complements the abstract policy engine model of NIST 800-207"
claim_type: "architectural"
source_note: "[[Green-Ortiz — Ch3-5 — Trust and Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch3-5.1: Trust assessment is spatial — the architecture location determines trust data availability and granularity

**Source:** [[Green-Ortiz — Ch3-5 — Trust and Policy]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

Different architectural locations (branch, campus, core, WAN, data center, cloud) present fundamentally different trust signals, different enforcement capabilities, and different blind spots. Trust assessment must be tailored to the location, not applied uniformly. The branch is the "easiest" to assess but has consumer-grade enforcement; the campus has richer enforcement but greater endpoint diversity; the data center's virtualized nature creates identity and enforcement gaps; the cloud requires adapting on-premises trust models.

## Evidence

The chapter-by-location walkthrough in Ch3 provides specific trust assessment capabilities for each architectural area:
- **Branch:** Identity via RADIUS to policy server, posture via installed/ephemeral agents, traffic analysis via NetFlow/taps. Classification by business priority and impact. Key limitation: consumer/prosumer-grade network access devices with limited security features.
- **Campus:** Richer ID enforcement at access layer, MACSec for switch-to-switch authenticated encryption, external scanners for non-PC posture. L3 enforcement at VLAN/subnet boundaries. Key advantage: large number of enforcement points enables gradual rollout.
- **Core network:** Network access device identity via loopback IP + metadata (hostname, model, location, function). TACACS+ with command-level authorization. NetFlow/taps for traffic analysis.
- **WAN:** Overlay-based trust (SD-WAN, DMVPN, GETVPN, IPsec). Segmentation tags (TrustSec) carried through tunnels. Man-in-the-middle is the primary threat.
- **Data center:** Machine identity + service accounts. Virtual server enforcement via hypervisor-hosted switches or host agents. Legacy system compensating controls via segmentation.
- **Cloud:** Metadata tagging for contextual identity. Dynamic contextual metadata. SASE/SSE for cloud-delivered security controls. Baseline audit before ZT deployment.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The spatial differentiation of trust assessment is a practical contribution that complements the abstract policy engine model of NIST 800-207 and the control-plane/data-plane model of Gilman & Barth. It addresses the question those frameworks don't: *where do trust signals come from and how do they vary by network segment?*

## Stakes

If trust assessment is treated as uniform, organizations either under-assess in some locations (leaving blind spots) or over-engineer in others (wasting resources). The spatial model makes trust assessment deployment-operational: you start where enforcement is easiest (branch), learn there, and scale.

## Disagreement

**Who disagrees:**

Gilman & Barth's model treats trust assessment as a property of the control plane, independent of network topology — the trust engine receives signals from agents regardless of where they are on the network. This is architecturally cleaner but less useful for brownfield migration planning. Green-Ortiz's spatial model is messier but more actionable for organizations that have a physical network infrastructure.

**Alternative reading:**

The spatial model could be read as a Cisco-specific framing — the emphasis on RADIUS, TrustSec, Cisco ISE, and Cisco SD-WAN reflects the book's publisher. But the underlying principle (trust signals differ by architecture location) is vendor-neutral and widely applicable.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[zt-control-data-plane-split|Spatial trust assessment refines the control plane's function by showing that trust data availability and granularity va]]

## Assessment

This is the most underappreciated contribution of Green-Ortiz. Most ZT literature treats the network as an abstract hostile medium. Green-Ortiz treats it as a concrete physical infrastructure with varying capabilities — and maps ZT trust assessment onto it. For organizations with brownfield networks, this is more actionable than the abstract models.
