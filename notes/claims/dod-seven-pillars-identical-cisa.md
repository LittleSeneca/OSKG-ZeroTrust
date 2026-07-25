---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-architecture
  - topic/zt-governance
  - topic/zt-implementation
  - topic/zt-network
claim_id: "dod-ra-ov.5"
statement: "DoD's seven pillars are identical to CISA's — the difference is implementation depth"
confidence: "high"
confidence_rationale: "HIGH. The pillar structure is now universal across U.S. government ZT guidance — CISA, DoD, and NSA all use the same seven-pillar taxonomy. This"
claim_type: "architectural"
source_note: "[[DoD ZT Reference Architecture — Overview and Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-ov.5: DoD's seven pillars are identical to CISA's — the difference is implementation depth

**Source:** [[DoD ZT Reference Architecture — Overview and Strategy]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

The seven Pillars are "in alignment with the common industry identification of ZT Pillars":

| Pillar | DoD ZT RA Emphasis |
|--------|-------------------|
| **User** | MFA, PAM, continuous authentication/authorization/monitoring of activity patterns |
| **Device** | Continuous real-time authentication, inspection, assessment, patching; Comply-to-Connect; TPM |
| **Network/Environment** | Macro- and micro-segmentation; control privileged access; prevent lateral movement |
| **Applications and Workload** | Full stack from application layer to hypervisor; DevSecOps; proxy technologies; source code vetting |
| **Data** | Categorization by mission criticality; DRM, DLP, data tagging; encryption at rest and in transit |
| **Visibility and Analytics** | UEBA, sensor data, telemetry, deep packet inspection; ML-based anomaly detection |
| **Automation and Orchestration** | SOAR, SIEM integration, policy-based automated response; centralized policy enforcement |

## Evidence

These seven pillars are identical to CISA's five-pillar model (CISA groups Network, Applications & Workload, and Data under a broader "Network/Environment" category but organizes maturity assessments around the same seven areas). The DoD adds specific defense-relevant technologies: Comply-to-Connect (C2C), PKI/CAC, JRSS, and explicit DevSecOps integration for the Applications pillar.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The pillar structure is now universal across U.S. government ZT guidance — CISA, DoD, and NSA all use the same seven-pillar taxonomy. This convergence is deliberate; it enables cross-agency maturity comparison.

## Stakes

If pillars differ across agencies, cross-agency collaboration (e.g., DoD sharing data with DHS) becomes architecturally impossible. If pillars are consistent, joint operations can align ZT implementations. This is not theoretical — the DoD routinely shares classified data with civilian agencies.

## Disagreement

**Who disagrees:**

Sounil Yu's Cyber Defense Matrix uses a different taxonomy (five asset classes across five security functions). Forrester's ZTX framework uses seven pillars but organizes them differently. The industry hasn't fully converged, but the U.S. government has.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[five-pillar-comprehensive-decomposition|DoD independently converged on the identical pillar structure (seven pillars mapping to CISA's five), corroborating that]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The pillar convergence is one of the unsung achievements of U.S. government Zero Trust policy. NIST, CISA, DoD, and NSA all using the same taxonomy means a vendor can build once and sell to everyone, and an assessor can evaluate any agency using the same framework. This is the standardization that Goal 3 (consistent policy) demands.
