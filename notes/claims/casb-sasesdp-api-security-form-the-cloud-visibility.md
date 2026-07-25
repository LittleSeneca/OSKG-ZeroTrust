---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-monitoring
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-network
claim_id: "finney-ch8-11.3"
statement: "CASB + SASE/SDP + API security form the cloud visibility and control triad"
confidence: "high"
confidence_rationale: "HIGH. This triad is pragmatic and maps to real product categories. The API layer is correctly identified as the biggest blind spot — most orgs have a"
claim_type: "implementation"
source_note: "[[Finney — Ch8-11 — Execution and Sustainability]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch8-11.3: CASB + SASE/SDP + API security form the cloud visibility and control triad

**Source:** [[Finney — Ch8-11 — Execution and Sustainability]] — George Finney, *Project Zero Trust*, 2022

## The Claim

Three technology layers are needed for cloud ZT: (1) CASB for SaaS visibility (proxy or API-based), (2) SASE/SSE with SDP agents for endpoint-to-cloud policy enforcement and remote browser isolation, and (3) API security tools for discovering and monitoring the API layer that interconnects everything.

## Evidence

- **CASB:** Dave describes proxy-mode (all traffic flows through, enables logging) and API-mode (native integrations for OneDrive, SharePoint, Box, Salesforce — easier to deploy but less coverage). Can detect sensitive data in cloud storage.
- **SASE/SDP:** Aaron maps it to NIST 800-207's policy engine concept — agent on client connects to policy engine, allows/denies per role. Also provides device isolation (prevents lateral movement) and remote browser isolation (malware detonated in cloud sandbox).
- **API security:** APIs are both protect surface AND control. OWASP API Top 10 vulnerabilities (broken object-level auth, excessive data exposure, mass assignment) have caused breaches at Peloton, Parler, Facebook. Need API discovery scans, continuous monitoring, long-term data retention for threat hunting.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This triad is pragmatic and maps to real product categories. The API layer is correctly identified as the biggest blind spot — most orgs have a WAF for the front end but nothing for the back-end API traffic.

## Stakes

Without API visibility, ZT in the cloud is incomplete. Attackers can bypass front-end controls entirely by targeting the API layer.

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

_Not addressed separately in the source note._
