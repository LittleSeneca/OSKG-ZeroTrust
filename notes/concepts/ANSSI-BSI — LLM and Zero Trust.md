---
tags:
  - source/papers
  - anssi
  - bsi
  - llm
  - zt-ai
  - oskg-zerotrust
  - type/reading-note
created: 2026-07-24
related:
  - "[[Concepts Index]]"
  - "[[../Notes Index]]"
  - "[[Academic — ZT Research Papers]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
sources:
  - title: "Design Principles for LLM-based Systems with Zero Trust: Foundation for Secure Agentic Systems"
    author: "Federal Office for Information Security (BSI, Germany) / Agence nationale de la sécurité des systèmes d'information (ANSSI, France)"
    year: 2025
    publisher: "BSI / ANSSI"
    local_file: "sources/standards/_txt/ANSSI_BSI_LLM_Zero_Trust_2025.txt"
claims_status: extracted
claims_extracted: 2026-07-24
  - topic/zt-definition
  - topic/zt-implementation
  - topic/zt-governance
---

# ANSSI-BSI — LLM and Zero Trust

Joint guidance from the German Federal Office for Information Security (BSI) and the French National Agency for Information Systems Security (ANSSI), published August 2025. This is the first major **binational government standard** applying Zero Trust principles specifically to LLM-based systems. It is deployment-independent and focused on the application layer.

The document's central premise: **LLM systems and agentic AI architectures introduce novel attack surfaces that traditional security models cannot address. Zero Trust — continuous verification, least privilege, no implicit trust — is the appropriate architectural response.**

---

## Scope and Positioning

- **Level:** Application layer of the AI system (aligned with NSA's Application and Workload Pillar)
- **Out of scope:** Training/development phase, cloud-specific risks (deferred to BSI C5), infrastructure-level ZT (assumed already in place)
- **Audience:** System architects, operators, and government authorities
- **Status:** Foundational, not exhaustive — residual risks remain even with full adherence
- **Key constraint:** "This document intentionally avoids prescribing specific technologies or products"

---

**Claim 1 —** LLM systems require their own dedicated Zero Trust design principles — the six principles defined by ANSSI/BSI extend traditional ZT into a domain where none of the existing ZT standards (NIST, CISA, NSA) provide guidance. → [[llm-systems-require-their-own-dedicated-zero]]
---

**Claim 2 —** Input and output validation through a gateway — analogous to the ZT PEP — is the most novel and critical of the six principles, introducing the concept of a "trust algorithm" for evaluating prompt trustworthiness. → [[input-output-validation-gateway]]
**Claim 3 —** Session-level memory isolation is a critical ZT requirement for LLM systems — the failure to isolate sessions creates cross-session file leakage and persistent Prompt Injection vectors that violate the "no implicit trust" principle. → [[session]]
**Claim 4 —** Autonomous agentic operation without human oversight is inadvisable — this is the document's strongest claim and places ANSSI/BSI firmly in the \"cautious deployment\" camp for LLM systems. → [[autonomous-agentic-operation-without-human-oversight-inadvisable]]
**Claim 5 —** The AI+ZT intersection is the least-developed area of the ZT knowledge graph — existing standards were written before LLM/agentic AI became a deployment reality, and ANSSI-BSI (2025) is the first authoritative document to bridge the gap. → [[ai-zt-intersection-least]]
---

## Relationship to the OSKG-ZeroTrust Graph

### Where This Document Fits

The ANSSI-BSI paper occupies a unique position: it is **neither a standard (like NIST 800-207) nor a practitioner book (like Gilman & Barth) nor an academic paper (like Dotse or Cao).** It is a **binational government guidance document** — normative but deployment-agnostic, authoritative but intentionally non-prescriptive about technology.

### Claims That Extend the Existing ZT Framework

| Existing ZT Claim | ANSSI-BSI Extension | Significance |
|---|---|---|
| "Never trust, always verify" | Applies to LLM outputs and automated agent actions — **an LLM's output must not be trusted without verification** | Extends ZT from network/identity to AI inference |
| Continuous monitoring | Extended to include LLM-specific threats: Prompt Injection patterns, token abuse, unexpected model invocations | Creates new monitoring dimensions beyond traditional ZT |
| Least privilege access | Applied to LLM system components: plugins can't access conversation history, RAG databases scoped to user role, agents execute in user's security context | Component-level granularity beyond what practitioner ZT books describe |
| Assume breach | Reframed for AI: **assume the LLM has been compromised** via Prompt Injection and design controls accordingly | The assume-breach principle now covers the AI model itself |
| Policy engine / PDP | Mapped to "Trust Algorithm" for input evaluation — weighted scoring of prompt trustworthiness | The PEP/PDP model gains an AI-specific evaluation layer |

### Claims That Challenge Practitioner Assumptions

| Practitioner Assumption | ANSSI-BSI Challenge |
|---|---|
| "Agentic AI is the future" (industry narrative) | "Fully autonomous operation... is not recommended" — BSI/ANSSI explicitly caution against it |
| "LLMs can be secured with traditional controls" | Six new design principles are required, several of which (input tagging, trust algorithms for prompts, session-level memory isolation) have no analog in traditional ZT |
| "The orchestrator can be an LLM" | The orchestrator security analysis is explicitly deferred — this is an open risk |
| "ZT is implementation-mature" | Even with full adherence to all six principles, "residual risks may remain" — the document does not claim completeness |
