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
claim_id: "anssi-bsi.1"
statement: "LLM systems require their own dedicated Zero Trust design principles — the six principles defined by ANSSI/BSI extend traditional ZT into a domain where none of the existing ZT standards (NIST, CISA, NSA) provide guidance."
confidence: "high"
confidence_rationale: "HIGH — This is a binational government guidance document from two of Europe's premier cybersecurity agencies. The identification of the AI+ZT gap in"
claim_type: "definitional"
source_note: "[[ANSSI-BSI — LLM and Zero Trust]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# anssi-bsi.1: LLM systems require their own dedicated Zero Trust design principles — the six principles defined by ANSSI/BSI extend traditional ZT into a domain where none of the existing ZT standards (NIST, CISA, NSA) provide guidance.

**Source:** [[ANSSI-BSI — LLM and Zero Trust]] — ANSSI/BSI, *LLM and Zero Trust*, 2024

## The Claim

ANSSI and BSI assert that LLM and agentic AI architectures introduce novel attack surfaces — Indirect Prompt Injection, cross-session file leakage, MCP tool description injection, and persistent memory poisoning — that traditional security models and existing ZT frameworks do not address. Six principles specifically for LLM systems are required.

## Evidence

The document restates BSI's 2023 Zero Trust framework and maps its three core principles to LLM systems: (1) Authentication & Authorization — every user, agent, and system component uniquely authenticated for each interaction, with explicit prohibition of LLM-based authentication; (2) Principle of Least Privilege — all LLM/agent actions execute within the initiating user's security context, RAG databases scoped to user role; (3) No Implicit Trust — Indirect Prompt Injection is identified as "the primary threat vector that ZT must counter."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — This is a binational government guidance document from two of Europe's premier cybersecurity agencies. The identification of the AI+ZT gap in existing standards is independently verifiable by examining NIST 800-207, CISA ZTMM, and DoD ZT RA, none of which address LLM security.

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
