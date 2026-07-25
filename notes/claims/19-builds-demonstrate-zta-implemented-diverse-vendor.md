---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-1800-35
  - topic/zt-implementation
  - topic/zt-cloud
  - topic/zt-architecture
claim_id: "nist-1800-35.2"
statement: "The 19 builds demonstrate that ZTA can be implemented with diverse vendor combinations, but integration gaps between PDPs, PEPs, and supporting components remain the primary practical challenge — not the ZTA concept itself."
confidence: "high"
confidence_rationale: "HIGH on the build descriptions — these are documented implementations, not theoretical architectures. MEDIUM on generalization — the lab environment"
claim_type: "implementation"
source_note: "[[NIST 1800-35 — Implementing ZTA]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist-1800-35.2: The 19 builds demonstrate that ZTA can be implemented with diverse vendor combinations, but integration gaps between PDPs, PEPs, and supporting components remain the primary practical challenge — not the ZTA concept itself.

**Source:** [[NIST 1800-35 — Implementing ZTA]] — NIST, *SP 1800-35 — Implementing a Zero Trust Architecture*, 2023

## The Claim

The 19 builds demonstrate that ZTA can be implemented with diverse vendor combinations, but integration gaps between PDPs, PEPs, and supporting components remain the primary practical challenge — not the ZTA concept itself.

## Evidence

**The 19 builds organized by deployment approach:**

| Build | PE/PDP | Approach | Key Pattern |
|-------|--------|----------|-------------|
| **EIG Crawl Phase** | | | |
| E1B1 | Okta + Ivanti | EIG Crawl | Multi-vendor ICAM: Okta for identity federation, Ivanti for ZSO, SailPoint for IGA, Radiant Logic for identity data platform |
| E2B1 | Ping Identity | EIG Crawl | Single-vendor ICAM: PingFederate as PE, Cisco Duo as PEP |
| E3B1 | Microsoft (Azure AD) | EIG Crawl | Microsoft-centric: Azure AD Conditional Access, Defender for Endpoint, Intune |
| **EIG Run Phase** | | | |
| E1B2 | Zscaler | EIG Run | Cloud-delivered PE: Zscaler ZPA Central Authority as PE/PA/PEP, ZCC client connector |
| E3B2 | Microsoft + Forescout | EIG Run | Hybrid PE: Azure AD + Intune + Forescout eyeControl/eyeExtend |
| E4B3 | IBM Security Verify | EIG Run | IBM-centric: IBM Verify as PE, MaaS360 for UEM, QRadar for SIEM |
| **SDP/Microsegmentation/SASE Phase** | | | |
| E1B3 | Zscaler | SDP | ZPA as SDP controller — secure tunnels, resource darkening |
| E2B3 | Cisco + Ping | Microsegmentation | Cisco ISE + Secure Workload for network microsegmentation, PingFederate for identity |
| E3B3 | Microsoft + Forescout | SDP + Microseg | Combined approach: Microsoft Conditional Access + Forescout eyeSegment |
| E1B4 | Appgate | SDP | Pure-play SDP: Appgate SDP Controller, Gateway, Client |
| E2B4 | Broadcom (Symantec) | SDP + SASE | Symantec Cloud SWG + ZTNA + CASB — SASE with SDP overlay |
| E3B4 | F5 | SDP | Application-delivery-centric SDP: F5 BIG-IP + NGINX Plus |
| E4B4 | Broadcom (VMware) | SDP + Microseg + EIG | VMware Workspace ONE + NSX-T — comprehensive on-prem ZTA |
| E1B5 | Palo Alto Networks | Microseg + SASE | PAN NGFW + Prisma Access + Prisma SASE — network-centric approach |
| E2B5 | Lookout + Okta | SDP + SASE | Cloud-native SASE: Lookout SSE (SPA/SCA/SIA) + Okta Identity Cloud |
| E3B5 | Microsoft Entra + SSE | SDP + SASE | Microsoft-native SASE: Entra Conditional Access + Security Service Edge (Private Access, Internet Access) |
| E4B5 | AWS Verified Access + VPC Lattice | SDP + Microseg | Cloud-provider-native: AWS Verified Access for user-to-app, VPC Lattice for service-to-service |
| E1B6 | Ivanti nZTA | SDP + Microseg | Ivanti Neurons for Zero Trust Access as PE |
| E2B6 | Google CEP | SASE | Google Chrome Enterprise Premium — Access Context Manager as PE |

**Vendor landscape patterns observed:**

- **24 collaborators:** Appgate, AWS, Broadcom, Cisco, DigiCert, F5, Forescout, Google Cloud, IBM, Ivanti, Lookout, Mandiant, Microsoft, Okta, Omnissa, Palo Alto Networks, PC Matic, Ping Identity, Radiant Logic, SailPoint, Tenable, Trellix, Zimperium, Zscaler.
- **Vendor concentration:** Microsoft appears in 6 builds (most widely integrated). Okta appears in 7 builds as the identity federation layer. Tenable appears in nearly every build for vulnerability/asset context. Mandiant (MSV) is in every build for security validation. DigiCert provides certificates across all builds.
- **Architecture archetypes:**
  1. **Single-vendor stacks** (E3B1, E4B3, E1B5, E3B5, E4B5) — Microsoft, IBM, Palo Alto Networks, or AWS providing most ZTA components. Tighter integration, fewer gaps, but vendor lock-in risk.
  2. **Best-of-breed integrations** (E1B1, E2B3, E2B5) — Identity from one vendor (Okta/Ping), network from another (Cisco/Zscaler), endpoint from a third. Richer capability but integration gaps.
  3. **Cloud-provider-native** (E4B5, E2B6) — AWS Verified Access or Google CEP as the ZTA backbone. Leverages cloud provider's identity and network infrastructure.
- **Identity federation is universal.** Every build, regardless of approach, has an ICAM/PDP component. No ZTA exists without strong identity.
- **SIEM is universal.** IBM QRadar or Microsoft Sentinel in every build — monitoring is non-negotiable.
- **Certificate infrastructure is universal.** DigiCert in every build — PKI is the silent foundation of ZTA.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the build descriptions — these are documented implementations, not theoretical architectures. MEDIUM on generalization — the lab environment was clean and controlled; real enterprise environments have legacy constraints the lab doesn't capture.

## Stakes

The 19 builds demonstrate that ZTA is *buildable* with commercially available technology. This is the document's primary value — it refutes the claim that ZTA is theoretical or requires custom development. But the integration gaps documented in §5 show that *building* and *operating* are different challenges.

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

The build matrix is the document's center of gravity. It provides a menu of approaches that organizations can map to their existing vendor relationships and technical constraints. The patterns are more valuable than the individual builds — single-vendor vs. best-of-breed vs. cloud-native are genuine architectural choices with different tradeoffs. The document doesn't recommend one over another, which is appropriate but leaves organizations without clear decision criteria.
