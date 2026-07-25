---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-architecture
  - topic/zt-policy
  - topic/zt-implementation
  - topic/zt-network
claim_id: "nist207-ch3.2"
statement: "Eight data sources feed the Policy Engine's access decisions"
confidence: "high"
confidence_rationale: "HIGH — This data-source taxonomy is comprehensive and maps cleanly to real-world implementations. Every ZTA deployment needs these inputs, though the"
claim_type: "architectural"
source_note: "[[NIST 800-207 — Ch3 — Logical Components]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch3.2: Eight data sources feed the Policy Engine's access decisions

**Source:** [[NIST 800-207 — Ch3 — Logical Components]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

The PE makes decisions using inputs from: (1) Continuous Diagnostics and Mitigation (CDM) systems for asset posture, (2) Industry Compliance systems for regulatory rules, (3) Threat Intelligence feeds for external attack/vulnerability data, (4) Network and System Activity Logs for real-time security feedback, (5) Data Access Policies as the baseline authorization rules, (6) Enterprise PKI for certificate generation and management, (7) ID Management systems for user identity and attributes, and (8) SIEM systems for security-centric event analysis.

## Evidence

Enumerated descriptions of each data source with its role in access decisions. NIST distinguishes between local (enterprise-controlled) and external sources.

**Cross-reference table:**

| NIST Data Source | CISA Maturity Model Pillar | DoD ZT RA Mapping |
|---|---|---|
| CDM System | Device pillar | Device compliance / continuous monitoring |
| Industry Compliance | Governance pillar | Policy administration |
| Threat Intelligence | (Cross-cutting) | Threat intelligence integration |
| Activity Logs | Visibility & Analytics | SIEM / analytics plane |
| Data Access Policies | Data pillar | Data security policies |
| Enterprise PKI | Device + Identity pillars | PKI / certificate services |
| ID Management | Identity pillar | Identity, Credential, and Access Management (ICAM) |
| SIEM | Visibility & Analytics | Security analytics |

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — This data-source taxonomy is comprehensive and maps cleanly to real-world implementations. Every ZTA deployment needs these inputs, though the maturity and integration of each varies widely.

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

The data-source model holds up as a reference, but in practice, integration between these sources remains a major implementation challenge. The CISA Maturity Model effectively operationalizes this by defining progressive maturity levels for each data-source domain, from "manual" to "fully automated and integrated." The gap between NIST's ideal data-source integration and real-world deployments is where most ZT implementations fail.
