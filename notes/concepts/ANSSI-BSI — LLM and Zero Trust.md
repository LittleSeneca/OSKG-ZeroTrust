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

### Claim 1: LLM systems require their own dedicated Zero Trust design principles — the six principles defined by ANSSI/BSI extend traditional ZT into a domain where none of the existing ZT standards (NIST, CISA, NSA) provide guidance.

**Author's claim:** ANSSI and BSI assert that LLM and agentic AI architectures introduce novel attack surfaces — Indirect Prompt Injection, cross-session file leakage, MCP tool description injection, and persistent memory poisoning — that traditional security models and existing ZT frameworks do not address. Six principles specifically for LLM systems are required.

**Evidence presented:** The document restates BSI's 2023 Zero Trust framework and maps its three core principles to LLM systems: (1) Authentication & Authorization — every user, agent, and system component uniquely authenticated for each interaction, with explicit prohibition of LLM-based authentication; (2) Principle of Least Privilege — all LLM/agent actions execute within the initiating user's security context, RAG databases scoped to user role; (3) No Implicit Trust — Indirect Prompt Injection is identified as "the primary threat vector that ZT must counter."

**Confidence:** HIGH — This is a binational government guidance document from two of Europe's premier cybersecurity agencies. The identification of the AI+ZT gap in existing standards is independently verifiable by examining NIST 800-207, CISA ZTMM, and DoD ZT RA, none of which address LLM security.

---

### Claim 2: Input and output validation through a gateway — analogous to the ZT PEP — is the most novel and critical of the six principles, introducing the concept of a "trust algorithm" for evaluating prompt trustworthiness.

**Author's claim:** The document's second design principle establishes a gateway between the core LLM and its components that validates, cleans, or rejects inputs and outputs. This gateway functions "analogous to the Zero Trust PEP." A "Trust Algorithm" evaluates input trustworthiness through weighted scoring of criteria including user history, device, time, and previous request history.

**Evidence presented:** Six mitigations are specified: (1) Gateway input validation through algorithmic + ML methods, allowed/disallowed word lists, regex, unusual syntax detection; (2) Tags distinguishing trusted vs. untrusted input sources to enable Prompt Injection defense; (3) Trust Algorithm using validator AI models or score calculation with multiple thresholds and dependencies; (4) Output control via guardrails frameworks, formalized output for system commands, Human-in-the-Loop approval for critical actions; (5) External content policy prohibiting automatic preloading of external content (markdown images), with user notification of source/destination before retrieval; (6) The requirement that "the user must be able to approve all system inputs of the application and actions of the agent."

**Confidence:** HIGH — This is the most technically detailed section of the document. The PEP analogy is explicit and the mitigations are specific enough to implement, though technology-agnostic.

### Claim 3: Session-level memory isolation is a critical ZT requirement for LLM systems — the failure to isolate sessions creates cross-session file leakage and persistent Prompt Injection vectors that violate the "no implicit trust" principle.

**Author's claim:** The sandboxing principle requires strict isolation of LLM memory between sessions and users. The document identifies a concrete real-world vulnerability: "all sessions of a user share the same code interpreter container, making files between sessions non-isolated."

**Evidence presented:** Risk scenarios include: infinite loops from component errors triggering recursive LLM invocations; malicious payload from compromised websites/infected components enabling backdoors and data theft; cross-session file leakage where files uploaded in one session are accessible in another via shared code interpreter containers; persistent Prompt Injection via shared memory between sessions. Mitigations include: memory isolation with sanitization and secure storage; emergency shutdown capability with data integrity backups; system isolation via predefined allowlists of external interactions; each task in a new inference session with only relevant information shared between instances; context window hygiene prohibiting sensitive information especially with internet access; environment segregation between dev, test, and production.

**Confidence:** HIGH — The cross-session file leakage issue is a well-known vulnerability pattern in LLM platforms. The mitigations are specific and actionable.

### Claim 4: Autonomous agentic operation without human oversight is inadvisable — this is the document's strongest claim and places ANSSI/BSI firmly in the "cautious deployment" camp for LLM systems.

**Author's claim:** The document's conclusion states: "A key message is that blind trust in LLM systems is not advisable, and the fully autonomous operation of such systems without human oversight is not recommended. It is improbable that such agents can ensure meaningful and reliable safety guarantees."

**Evidence presented:** This position is reinforced throughout all six principles: Principle 2 requires Human-in-the-Loop for critical actions and separate LLM explanation of system commands before execution; Principle 4 requires continuous monitoring with automated predefined responses; Principle 6 demands explainability and transparency. The document aligns with Beurer-Kellner et al. (2025), who reach the same conclusion independently. The authors further warn: "For simple tasks, predefined workflows and direct code are often more efficient than agents, giving developers full control without unnecessary complexity."

**Confidence:** HIGH — This is the explicit, unambiguous conclusion of a binational government guidance document. The consistency across all six principles demonstrates this is a foundational position, not a sidebar caveat.

### Claim 5: The AI+ZT intersection is the least-developed area of the ZT knowledge graph — existing standards were written before LLM/agentic AI became a deployment reality, and ANSSI-BSI (2025) is the first authoritative document to bridge the gap.

**Author's claim:** This is a meta-claim about the evidence landscape. The document reveals a significant gap: ZT standards (NIST, CISA, NSA, DoD) predate LLM deployment; practitioner books barely mention AI; academic AI+ZT papers focus on using AI *for* ZT automation, not securing AI *within* ZT. ANSSI-BSI is the first authoritative bridge.

**Evidence presented:** Five key unresolved questions are identified: (1) How does the Trust Algorithm for input evaluation integrate with the NIST 800-207 PE trust algorithm? (2) If "no LLM-based authentication" is a principle, how do agentic systems authenticate in multi-agent environments? (3) The orchestrator security is deferred — if the orchestrator is itself an LLM, what is the formal trust model? (4) How do the six principles map to CISA ZTMM maturity model? (5) Is the caution against full autonomy a permanent architectural principle or a reflection of current LLM immaturity?

**Confidence:** MEDIUM — The claim that this is the least-developed area is verifiable by examining the publication dates and content of the referenced standards. However, the characterization of "least-developed" is a comparative judgment rather than a measured finding. The gap identification is sound; the assessment of its severity is inferential.

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
