---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-implementation
  - topic/zt-network
  - topic/zt-cloud
  - topic/zt-architecture
claim_id: "nist207-ch4.4"
statement: 'Contracted services and nonemployee access should use the SDP "dark network" model — enterprise resources are obscured from network discovery, preventing lateral movement, with the PA ensuring nonenterprise assets can access the internet but cannot discover or reach enterprise resources.'
confidence: "high"
confidence_rationale: 'HIGH. The SDP dark network model is architecturally sound but deployment complexity can undermine the "invisible resources" property.'
claim_type: "implementation"
source_note: "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch4.4: Contracted services and nonemployee access should use the SDP "dark network" model — enterprise resources are obscured from network discovery, preventing lateral movement, with the PA ensuring nonenterprise assets can access the internet but cannot discover or reach enterprise resources.

**Source:** [[NIST 800-207 — Ch4 — Deployment Scenarios]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

On-site visitors and contracted service providers (e.g., smart HVAC technicians) need limited access to enterprise resources. The ZTA approach: allow these devices and technicians internet access while **obscuring enterprise resources** — preventing network discovery and lateral movement. This is the "untrusted guest on the enterprise LAN" problem.

## Evidence

**How ZTA applies:**

- **PE/PA hosted as cloud service or on LAN** — depending on cloud usage. If the enterprise primarily uses on-prem resources, the PE/PA sits on the LAN. If cloud-hosted resources dominate, PE/PA is cloud-hosted.
- **Agent or portal for enterprise assets** — enterprise-managed devices use agents; everything else can't access local resources at all. "The PA(s) ensures that all nonenterprise assets (those that do not have installed agents or cannot connect to a portal) cannot access local resources but may access the internet."
- **Network obscurity via SDP** — visitors "may not even be able to discover enterprise services via network scans (i.e., prevent active network reconnaissance/east-west movement)." This is the SDP "dark network" property: services are invisible until authenticated.

**Cross-references:**

| Source | How It Relates |
|--------|---------------|
| **BeyondCorp** (Google) | Google's "unprivileged network" is the canonical implementation of this scenario. The unprivileged network provides only internet access, DNS, NTP, and DHCP — no access to corporate applications. Contractors, guests, and BYOD devices land on the unprivileged network by default. Access to corporate resources goes through the access proxy with full device/user trust evaluation. |
| **DoD ZT Reference Architecture v2** | Addressed through the Device Pillar (Comply-to-Connect — devices must prove compliance before network access) and the User Pillar (identity-based, not IP-based, access). The DoD's "least privilege" principle maps directly to this scenario: contractors get exactly the access their role requires, nothing more. |
| **Green-Ortiz (Cisco Press)** | Appendix A (SBC Inc. case study) has extensive contractor access patterns: 350,000 firewall rules reduced to identity-based policy for contractors accessing Smart Building Central. Green-Ortiz shows the practical process: audit, identity-link, reduce, and replace IP-based rules with contextual identity policies (who, what, where, when, how). This is the operationalization of NIST's architectural prescription. |

**Operational implication:**

The contracted services scenario exposes the fragility of perimeter-based NAC solutions. If a contractor's laptop is on the LAN, NAC grants network access — but NIST's ZTA says *no* network access, only *resource-specific* access through a PEP. The contractor's device may have internet access on the same physical network without ever discovering enterprise resources.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The SDP dark network model is architecturally sound but deployment complexity can undermine the "invisible resources" property.

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
  - [[nist-control-data-plane-separation]]

**Extends:**
- [[endpoint-new-perimeter|The SDP dark network model extends the endpoint-as-perimeter concept to non-enterprise devices and contracted services,]]
- [[perimeter-security-model-core-assumptions-no-longer|The SDP dark network model—obscuring enterprise resources from network discovery—is the ZT alternative to perimeter-base]]

## Assessment

_Not addressed separately in the source note._
