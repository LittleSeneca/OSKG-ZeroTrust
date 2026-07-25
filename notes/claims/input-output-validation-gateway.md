---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/anssi-bsi
  - topic/zt-definition
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
claim_id: "anssi-bsi.2"
statement: 'Input and output validation through a gateway — analogous to the ZT PEP — is the most novel and critical of the six principles, introducing the concept of a "trust algorithm" for evaluating prompt trustworthiness.'
confidence: "high"
confidence_rationale: "HIGH — This is the most technically detailed section of the document. The PEP analogy is explicit and the mitigations are specific enough to"
claim_type: "definitional"
source_note: "[[ANSSI-BSI — LLM and Zero Trust]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# anssi-bsi.2: Input and output validation through a gateway — analogous to the ZT PEP — is the most novel and critical of the six principles, introducing the concept of a "trust algorithm" for evaluating prompt trustworthiness.

**Source:** [[ANSSI-BSI — LLM and Zero Trust]] — ANSSI/BSI, *LLM and Zero Trust*, 2024

## The Claim

The document's second design principle establishes a gateway between the core LLM and its components that validates, cleans, or rejects inputs and outputs. This gateway functions "analogous to the Zero Trust PEP." A "Trust Algorithm" evaluates input trustworthiness through weighted scoring of criteria including user history, device, time, and previous request history.

## Evidence

Six mitigations are specified: (1) Gateway input validation through algorithmic + ML methods, allowed/disallowed word lists, regex, unusual syntax detection; (2) Tags distinguishing trusted vs. untrusted input sources to enable Prompt Injection defense; (3) Trust Algorithm using validator AI models or score calculation with multiple thresholds and dependencies; (4) Output control via guardrails frameworks, formalized output for system commands, Human-in-the-Loop approval for critical actions; (5) External content policy prohibiting automatic preloading of external content (markdown images), with user notification of source/destination before retrieval; (6) The requirement that "the user must be able to approve all system inputs of the application and actions of the agent."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — This is the most technically detailed section of the document. The PEP analogy is explicit and the mitigations are specific enough to implement, though technology-agnostic.

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
