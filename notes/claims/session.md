---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/anssi-bsi
  - topic/zt-definition
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-governance
claim_id: "anssi-bsi.3"
statement: 'Session-level memory isolation is a critical ZT requirement for LLM systems — the failure to isolate sessions creates cross-session file leakage and persistent Prompt Injection vectors that violate the "no implicit trust" principle.'
confidence: "high"
confidence_rationale: "HIGH — The cross-session file leakage issue is a well-known vulnerability pattern in LLM platforms. The mitigations are specific and actionable."
claim_type: "definitional"
source_note: "[[ANSSI-BSI — LLM and Zero Trust]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# anssi-bsi.3: Session-level memory isolation is a critical ZT requirement for LLM systems — the failure to isolate sessions creates cross-session file leakage and persistent Prompt Injection vectors that violate the "no implicit trust" principle.

**Source:** [[ANSSI-BSI — LLM and Zero Trust]] — ANSSI/BSI, *LLM and Zero Trust*, 2024

## The Claim

The sandboxing principle requires strict isolation of LLM memory between sessions and users. The document identifies a concrete real-world vulnerability: "all sessions of a user share the same code interpreter container, making files between sessions non-isolated."

## Evidence

Risk scenarios include: infinite loops from component errors triggering recursive LLM invocations; malicious payload from compromised websites/infected components enabling backdoors and data theft; cross-session file leakage where files uploaded in one session are accessible in another via shared code interpreter containers; persistent Prompt Injection via shared memory between sessions. Mitigations include: memory isolation with sanitization and secure storage; emergency shutdown capability with data integrity backups; system isolation via predefined allowlists of external interactions; each task in a new inference session with only relevant information shared between instances; context window hygiene prohibiting sensitive information especially with internet access; environment segregation between dev, test, and production.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The cross-session file leakage issue is a well-known vulnerability pattern in LLM platforms. The mitigations are specific and actionable.

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

_Not addressed separately in the source note._
