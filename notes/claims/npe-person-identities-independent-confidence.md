---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-identity
  - topic/zt-architecture
  - topic/zt-governance
  - topic/zt-device
claim_id: "dod-ra-cap.4"
statement: "NPE and person identities are tracked independently, allowing separate paths for validating confidence levels — device and user confidence are independently developed and then aggregated at policy enforcement time, with access granted only if the combined confidence score exceeds a measured threshold that varies by data sensitivity."
confidence: "high"
confidence_rationale: "HIGH. The independent identity tracking and confidence scoring model is foundational to the DoD RA's enforcement architecture."
claim_type: "architectural"
source_note: "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-cap.4: NPE and person identities are tracked independently, allowing separate paths for validating confidence levels — device and user confidence are independently developed and then aggregated at policy enforcement time, with access granted only if the combined confidence score exceeds a measured threshold that varies by data sensitivity.

**Source:** [[DoD ZT Reference Architecture — Capabilities and Use Cases]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

NPE and person identities are tracked independently. Confidence levels for device and user are independently developed and then **aggregated** at policy enforcement time. (§3.2)

## Evidence

1. User/endpoint → Authentication DP → Authorization DP → Resource DP → Application DP → Data DP
2. At each enforcement point, logs are sent to the **SIEM**
3. Analytics develop a **confidence level** from SIEM data
4. **DLP** feeds the SIEM to ensure data is being used properly even after access is granted
5. If confidence drops below threshold → SOAR triggers policy changes → PEPs enforce new restrictions

**Supporting infrastructure capabilities:**

| Capability | Description |
|---|---|
| **Enterprise Identity Service (FEIS + AAP + MUR)** | Federated identity credentials across organizations; automatic account provisioning/deprovisioning; Master User Record for audit and threat detection |
| **Comply-to-Connect (C2C)** | Discovers, identifies, characterizes, and reports all connecting devices; orchestrates tools to prevent non-compliant device access |
| **Policy Engine & Automation (SOAR)** | Threat management, incident response, policy enforcement automation; works with analytics to develop confidence levels and push policy to PEPs |
| **Analytics & Confidence Scoring** | Statistical analysis of event/incident logs to produce confidence scores — the probability that a user/NPE is who they assert to be |
| **SIEM** | Aggregates and stores activity data; provides both security information management and security event management |

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The independent identity tracking and confidence scoring model is foundational to the DoD RA's enforcement architecture.

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
- [[the-network-agent-is-the-marriage-of-user|Independent confidence development for user and device provides the evidentiary mechanism that underpins the network age]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
