---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/bsi
  - topic/zt-definition
  - topic/zt-governance
claim_id: "bsi-zt.7"
statement: "BSI is the first national agency to provide detailed guidance on integrating real-time signals into ZT access decisions"
confidence: "high"
confidence_rationale: "HIGH for the architectural patterns. MEDIUM for the specific Shared Signals/CAEP adoption timeline — these standards were in draft at publication"
claim_type: "definitional"
source_note: "[[BSI — Zero Trust Position Paper]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# bsi-zt.7: BSI is the first national agency to provide detailed guidance on integrating real-time signals into ZT access decisions

**Source:** [[BSI — Zero Trust Position Paper]] — BSI, *Zero Trust Position Paper*, 2023

## The Claim

The document describes two scenarios for extending ZT with real-time information sources (*echtzeitfähige Informationsquellen*):

1. **Identity provider event integration:** When an identity provider deactivates a user account (due to detected unusual behavior, HR system termination event, etc.), the application should immediately terminate active sessions rather than waiting for session timeout. The BSI references the **OpenID Shared Signals Framework** [3] and **Continuous Access Evaluation Profile (CAEP)** [4] as emerging standards for this.

2. **Device management event integration:** When a device management system detects a compliance status change (e.g., missing security patch, detected malware), applications should receive real-time events and can terminate specific sessions from non-compliant devices while maintaining sessions from compliant devices.

## Evidence

Detailed sequence diagrams (Figures 8 and 9 in the original) show the communication flow between identity provider, device management, application, and user sessions. Access scenario tables (Tables 1 and 2) show example conditions for network access and resource access decisions.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH for the architectural patterns. MEDIUM for the specific Shared Signals/CAEP adoption timeline — these standards were in draft at publication time.

## Stakes

Real-time signal integration is the frontier of ZT implementation. Most current ZT deployments use *session-start* evaluation (check trust at session initiation, don't re-evaluate until session timeout). The BSI is describing *continuous* evaluation where trust loss events from any infrastructure component immediately propagate to access decisions. This requires integration between identity providers, device management, SIEM, HR systems, and every application — a level of architectural integration that few organizations currently achieve.

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

This section makes the BSI paper the most forward-looking government ZT publication. The Shared Signals Framework and CAEP references are technically accurate and well-chosen — these are the emerging standards for exactly this capability. The BSI is effectively saying: "ZT's ultimate form requires real-time event propagation across all infrastructure components, and here are the standards that will enable it." The candid acknowledgment that these scenarios are "currently only singularly implementable" and that "complexity increases rapidly when multiple applications must be secured" is appropriately cautionary.
