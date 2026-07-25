---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-1800-35
  - topic/zt-implementation
claim_id: "nist-1800-35.3"
statement: "The EIG crawl phase proved that legacy ICAM solutions can serve as PDPs for basic ZTA, but resource management (authenticating and verifying the health of the endpoint hosting the resource) is beyond current out-of-the-box integration capabilities."
confidence: "high"
confidence_rationale: "HIGH on the findings themselves — these are documented observations from real lab implementations. HIGH on the generalizability of the integration"
claim_type: "implementation"
source_note: "[[NIST 1800-35 — Implementing ZTA]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist-1800-35.3: The EIG crawl phase proved that legacy ICAM solutions can serve as PDPs for basic ZTA, but resource management (authenticating and verifying the health of the endpoint hosting the resource) is beyond current out-of-the-box integration capabilities.

**Source:** [[NIST 1800-35 — Implementing ZTA]] — NIST, *SP 1800-35 — Implementing a Zero Trust Architecture*, 2023

## The Claim

The EIG crawl phase proved that legacy ICAM solutions can serve as PDPs for basic ZTA, but resource management (authenticating and verifying the health of the endpoint hosting the resource) is beyond current out-of-the-box integration capabilities.

## Evidence

**EIG Crawl findings (lines 1381–1418):**

- **What worked:** All three EIG crawl builds (E1B1, E2B1, E3B1) could authenticate/reauthenticate users and endpoints, verify endpoint health, and make access decisions based on those factors. Periodic reauthentication and session termination on failure was demonstrated.
- **What didn't work:** None could authenticate the *resource-hosting* endpoint or verify its health. Resource management (steps R(1) and R(A)–R(D) in the ZTA reference architecture) was entirely absent. Devices were joined to the network manually — no network-level enforcement prevented non-authenticated devices from connecting.
- **Integration reality:** "Many of the vendor solutions used in the EIG crawl phase do not integrate with each other out-of-the-box in ways that are needed to enable the ICAM solutions to function as PDPs." Network-level PEPs (routers, switches, firewalls) generally don't integrate with ICAM unless they're identity-aware. Endpoint protection solutions don't typically integrate directly with ICAM — they integrate through MDM/UEM intermediaries.

**EIG Run findings (lines 1420–1472):**

- **What was gained over crawl:** Secure tunnels from endpoints to private resources (on-premises and cloud), proxy connectors for resource invisibility, direct cloud resource access without hairpinning through enterprise network, device discovery with policy-based blocking, cloud traffic monitoring/enforcement.
- **Gaps identified:** E1B2 (Zscaler) had no EPP — Zscaler's client connector does compliance checks but isn't a full endpoint protection platform. No automatic endpoint remediation. No confidence level/trust score calculation due to missing collaborator integration. E2B1 had no EPP at all — Cisco Duo provides limited device health info. E3B2 had one-way Forescout → Intune integration but couldn't pass Forescout-discovered endpoint issues back to Intune for Azure AD enforcement.
- **Core lesson:** "When planning a ZTA implementation, organizations should ensure that all of the ZTA core and supporting components that can integrate with each other are selected. This enables having end-to-end ZTA with full functionality." (lines 1460–1462)

**SDP/Microsegmentation/SASE findings (lines 1478–1512):**

- **Multi-PDP fragmentation:** "It is not unusual for a ZTA to have multiple PDPs... the policies that the ZTA enforces are not centrally located. Rather, they are configured and managed in association with each of the various PDPs. This makes it challenging to understand, articulate, and manage the ZTA's policies as a comprehensive whole." (lines 1482–1486)
- **PDP information silos:** Multiple PDPs don't share information — one PDP may know an endpoint is non-compliant, another may know the user exhibited suspicious behavior, but neither has the full picture. "Ideally, when a ZTA has multiple PDPs, it is desirable to have an integrated approach that enables the PDPs to share information so that they can each be more fully informed." (lines 1492–1494)
- **SIEM → PDP integration gap:** SIEM/SOAR components contain rich information useful for access decisions but "ideally... should send this information to the PDP in real-time, if possible" — implying this isn't standard today.
- **Resource management maturity gap:** SDP endpoint management solutions *can* manage resources by installing clients on them, but "solutions that are specifically designed to manage resources should be leveraged rather than the zero trust solutions that have the primary purpose of managing endpoints." PDP integration with resource management tools remains weak.
- **Endpoint compliance is non-negotiable:** "It is important to have tools that are capable of detecting when an endpoint is not compliant and ensuring that the endpoint is not permitted to access resources as a result." Automatic remediation should be integrated with configuration/patch management.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the findings themselves — these are documented observations from real lab implementations. HIGH on the generalizability of the integration gap findings — multi-vendor integration challenges are a universal enterprise problem, not specific to the NCCoE lab.

## Stakes

The integration gaps are the real barrier to ZTA adoption, not the conceptual framework. If PDPs can't share information, if resource management remains manual, if endpoint protection doesn't integrate with ICAM, the ZTA is incomplete regardless of how well-designed the architecture is. These findings should shape procurement requirements — organizations should prioritize integration capability over individual product features.

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

These findings are the most honest and valuable part of the document. NIST doesn't pretend everything worked perfectly — they document the gaps, the workarounds, and the ideal state. The multi-PDP fragmentation finding is particularly important: it identifies a genuine architectural tension in ZTA (distributed decision-making vs. centralized policy management) that no vendor has fully resolved. The SIEM→PDP real-time integration gap is the most actionable finding — security analytics information needs to flow into access decisions, not just sit in dashboards.
