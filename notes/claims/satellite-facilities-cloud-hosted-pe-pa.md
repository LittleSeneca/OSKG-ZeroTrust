---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-network
  - topic/zt-implementation
  - topic/zt-cloud
claim_id: "nist207-ch4.2"
statement: "For satellite facilities and remote workers, the PE/PA must be hosted as a cloud service to avoid hairpinning traffic through HQ — the MPLS link to HQ becomes a commodity transport, not a security boundary."
confidence: "high"
confidence_rationale: "VERY HIGH. This is the canonical ZT use case and the strongest architectural argument against VPNs."
claim_type: "implementation"
source_note: "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch4.2: For satellite facilities and remote workers, the PE/PA must be hosted as a cloud service to avoid hairpinning traffic through HQ — the MPLS link to HQ becomes a commodity transport, not a security boundary.

**Source:** [[NIST 800-207 — Ch4 — Deployment Scenarios]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

An enterprise with a headquarters and geographically dispersed locations not joined by an enterprise-owned physical network. Remote employees may use enterprise-owned or personally-owned devices. The enterprise wants to grant access to some resources (email, calendar) while denying or restricting access to more sensitive resources (HR database). This is the most common scenario and the one closest to ZTA's historical roots.

## Evidence

**How ZTA applies:**

- **PE/PA hosted as a cloud service** — avoids forcing remote traffic to hairpin through the enterprise HQ network. "It may not be most responsive to have the PE/PA(s) hosted on the enterprise local network as remote offices and workers must send all traffic back to the enterprise network to reach applications/services hosted by cloud services."
- **Endpoint agent or resource portal** — subjects access resources through an installed agent (Section 3.2.1) or a web gateway portal (Section 3.2.3). Both patterns appear: agents for managed devices, portals for unmanaged or limited-use devices.
- **MPLS bandwidth constraints** — NIST flags the practical problem: an MPLS link to HQ may not have adequate bandwidth for all traffic, and the enterprise may not *want* cloud-destined traffic to traverse HQ. This is the architectural rationale for cloud-hosted PE/PA.

**Cross-references:**

| Source | How It Relates |
|--------|---------------|
| **BeyondCorp** (Google) | This IS BeyondCorp's founding use case. Google's entire architecture was built to eliminate the distinction between "on-campus" and "remote" access. BeyondCorp's access proxy sits at the edge of every application, and device trust is continuously assessed — the canonical implementation of NIST 4.1. |
| **DoD ZT Reference Architecture v2** | The DoD RA addresses this through the User Pillar and Device Pillar — Continuous Multi-Factor Authentication (CMFA) and Comply-to-Connect for endpoints. But DoD frames it through technology pillars rather than deployment topology. |
| **Green-Ortiz (Cisco Press)** | Green-Ortiz covers branch/campus ZT deployment in Ch 3–4. Their "SBC Inc." case study (Appendix A) mirrors satellite facility challenges: 175 campuses and branches with contractor access, simplified through identity-based policy rather than per-firewall IP rules. |

**Operational implication:**

The satellite facility scenario is where the "death of the VPN" argument is strongest. If PE/PA is cloud-hosted and resources are accessed through agents/portals, the MPLS link to HQ becomes a commodity transport, not a security boundary.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This is the canonical ZT use case and the strongest architectural argument against VPNs.

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
  - [[zta-three-core-components-pe-pa-pep]]

**Extends:**

## Assessment

_Not addressed separately in the source note._
