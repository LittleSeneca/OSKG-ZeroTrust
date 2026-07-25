---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-authentication
  - topic/zt-identity
  - topic/zt-governance
  - topic/zt-device
claim_id: "dod-ra-cap.10"
statement: "Authentication and Authorization (Use Cases 14–17) — authentication must become dynamic and continuous, driven by UEBA-based confidence scoring that triggers real-time access changes (deny, challenge, re-authenticate, downgrade) throughout sessions; authorization is no longer binary (yes/no) but scalar — a confidence score compared against a threshold that varies by data sensitivity, with the same user potentially authorized for unclassified but denied for classified data in the same session."
confidence: "high"
confidence_rationale: "HIGH. The authentication/authorization flows are among the most detailed in the document."
claim_type: "implementation"
source_note: "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-cap.10: Authentication and Authorization (Use Cases 14–17) — authentication must become dynamic and continuous, driven by UEBA-based confidence scoring that triggers real-time access changes (deny, challenge, re-authenticate, downgrade) throughout sessions; authorization is no longer binary (yes/no) but scalar — a confidence score compared against a threshold that varies by data sensitivity, with the same user potentially authorized for unclassified but denied for classified data in the same session.

**Source:** [[DoD ZT Reference Architecture — Capabilities and Use Cases]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

Conventional authentication uses persona-based identities, credentials, and attributes that are not dynamic or context-aware. Traditional authorization does not consider dynamic context. ZT requires multi-attribute-based confidence levels enabling continuous authentication and conditional authorization under least-privilege. (§4.14–4.17)

## Evidence

1. User/NPE requests access → provides attribute data (CAC, certificate, biometric) to identity agent
2. Throughout the session, **behavior data** is collected at PDPs: time of day, resource/operation requested
3. Behavior data is logged to SIEM → feeds **UEBA engine** for analysis
4. UEBA develops a **confidence score** distributed to policy enforcement points
5. If confidence drops → SOAR can deny, challenge, re-authenticate, or downgrade access

**Entity authentication types:**

| Entity Type | Examples | Authentication Mechanism |
|---|---|---|
| **User Device** (with loadable services) | Laptop, mobile, desktop | User identity + device identity |
| **Resource Device** (with loadable services) | Servers, network infrastructure | NPE identity via device manager |
| **IoT/Sensor** (ID and interface only) | Sensors, embedded devices | Unique ID via embedded service |
| **User Proxy** | Application standing in for user | Proxy identity to authentication service |
| **Device Management Proxy** | Device manager representing device | Unique device ID to auth service |
| **Application Service** | Software with unique instance ID | Instance-specific authentication |

**Conditional authorization flow (OV-2 step-by-step):**

| Step | What Happens | Capabilities Involved |
|---|---|---|
| **Step 0** (continuous) | Device sends inventory, system information, scans, and status to PDP | Device Hygiene, C2C, Continuous Authentication |
| **Step 0** (continuous) | ZT Policy Controller constantly sends updated policy to PDP | Automation & Orchestration |
| **Step 1** | User sends access request from device → if device passed Step 0, hits PEP | Conditional Authorization |
| **Step 2** | User provides sign-on credentials → multi-attribute evaluation begins | Authentication, UEBA |
| **Step 3** | Multiple controllers score the request: RBAC, ABAC, C2C, NAC, hygiene diagnostics, application sensitivity, data tags | All pillars |
| **Step 4** | PDP computes final confidence score from all controller inputs | Analytics & Confidence Scoring |
| **Step 5** | If score meets organizational threshold → authorization granted | Conditional Authorization |

**Multi-attribute scoring inputs:**

RBAC, ABAC, C2C, NAC, hygiene diagnostics, application sensitivity, data tags.

**Cross-reference — NIST 800-207:**

NIST mentions continuous authentication as a desirable property. DoD makes it a first-class capability with a defined process flow, UEBA integration, and confidence scoring that triggers real-time access changes.

**Cross-reference — CISA ZTMM:**

CISA's Identity and Device pillar maturity stages track the progression from static RBAC (Traditional) to fully dynamic, risk-adaptive ABAC with continuous validation (Optimal). DoD's conditional authorization describes the Optimal-level end state.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The authentication/authorization flows are among the most detailed in the document.

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
- [[mfa-is-necessary-but-insufficient-attackers-have-at|Dynamic continuous authentication with UEBA confidence scoring evolves beyond point-in-time MFA — the exact insufficienc]]

## Assessment

_Not addressed separately in the source note._
