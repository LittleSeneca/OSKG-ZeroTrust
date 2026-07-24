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

## The Three Core ZT Principles (as Applied to LLM Systems)

The document restates BSI's 2023 Zero Trust framework and maps it to LLM systems:

| ZT Principle | LLM System Application |
|-------------|----------------------|
| **Authentication & Authorization** | Every user, agent, and system component is uniquely authenticated and authorized for each interaction. No LLM-based authentication — LLMs are not designed for strict access control. |
| **Principle of Least Privilege** | Resources divided into small units; permissions granular. All actions taken by the LLM/agent execute within the initiating user's security context. RAG databases access scoped to user role. |
| **No Implicit Trust** | Internal and external networks not considered secure. Data breaches and insider threats are assumed. Indirect Prompt Injection is the primary threat vector that ZT must counter. |

---

## The LLM System Model

The document defines an LLM system as: **a central LLM + additional components** (databases, plugins, frontends, other AI models/agents) interacting via inputs and outputs, coordinated by an **orchestrator** (which may itself be an LLM).

Key architectural assumptions:
- Classical security components (logging, gateways, PKI, IAM) are "implicitly respected" but not detailed
- The orchestrator layer requires dedicated security analysis beyond the document's scope
- Systems may operate standalone or in multi-agent/multi-system environments
- Agentic LLM = "an LLM system capable of autonomous processes and adaptation" (OWASP definition)

---

## Six Design Principles

### 1. Authentication and Authorization

**Core requirement:** Every request to the LLM system, every data/resource access, and every interaction between system components is authenticated and authorized. Trust established only for short periods.

**Risk scenarios:**
- RAG systems exposing sensitive data via crafted prompts without role-scoped authorization
- Plugins with excessive privileges enabling data manipulation via Indirect Prompt Injection
- Temporary administrative permissions persisting across sessions (failure to revoke)
- Model Context Protocol (MCP) tool descriptions containing hidden Prompt Injections

**Mitigations** (9 measures):
- MFA for all users and agents, tying automated agent access to the initiating human's identity
- **No LLM-based authentication** — explicit prohibition
- Restrict plugin access to conversation history
- Least privilege: every user/agent/component gets minimum necessary rights
- Dynamic access control based on location, time, behavioral patterns, invocation frequency, request context, device type
- Attribute-Based Access Control (ABAC) with regular review and revocation of temporary privileges
- Continuous monitoring with clear traceability and ownership
- Documentation of all inter-component interactions
- **Autonomy restriction:** "For simple tasks, predefined workflows and direct code are often more efficient than agents, giving developers full control without unnecessary complexity"
- Multi-tenant architecture with tiered authentication aligned to data sensitivity (potentially different LLMs for different sensitivity levels)

### 2. Input and Output Restrictions

**Core requirement:** All inputs and outputs must be thoroughly validated, potentially cleaned or rejected. A gateway between the core LLM and its components — analogous to the Zero Trust PEP.

**Risk scenarios:**
- MCP tool description injection → exfiltration via malicious endpoint
- Preloading image Prompt Injection: markdown `![alt](URL)` where OCR-extracted text contains hidden instructions
- Plugin-injected markdown image links enabling data exfiltration via prerendering

**Mitigations** (6 measures):
- **Gateway:** Input validation through algorithmic + ML methods; allowed/disallowed word lists; regex; unusual syntax/keyword/length detection
- **Tags:** Distinguish trusted vs. untrusted input sources; ignore instructions from external systems (Prompt Injection defense); enable fine-grained permissions
- **Trust Algorithm:** Evaluate input trustworthiness via validator AI models or score calculation; weighted criteria (user history, device, time, previous request history); multiple thresholds with multiple dependencies
- **Output control:** Guardrails frameworks; formalized output for system commands; Human-in-the-Loop approval for critical actions; separate LLM to explain generated system commands before execution
- **External content policy:** Never automatically preload external content (markdown images, etc.); notify user of source/destination and transmitted data before retrieval
- **Critical enabler:** "The user must be able to approve all system inputs of the application and actions of the agent"

### 3. Sandboxing

**Core requirement:** Prevent the LLM system from interacting with external components or other LLM systems in unintended ways. Isolate execution environments and data between sessions and users.

**Risk scenarios:**
- Infinite loops from component errors triggering recursive LLM invocations
- Malicious payload from compromised websites/infected components → backdoors, data theft
- **Cross-session file leakage:** Files uploaded in one session accessible in another session via shared code interpreter container — "all sessions of a user share the same code interpreter container, making files between sessions non-isolated"
- Persistent Prompt Injection via shared memory between sessions

**Mitigations** (6 measures):
- Memory isolation: Strictly isolate LLM memory between sessions and users; sanitize, securely store, clearly define retained information
- Emergency shutdown capability with data integrity backups
- System isolation: Predefined list of allowed external interactions; disconnect sensitive-data systems from internet; whitelist website/app access; no untrusted plugins
- Session management: Each task in a new inference session; only relevant information shared between instances; context segmentation per user/agent
- Context window hygiene: No sensitive information in context window, especially with internet access; delete sensitive info per new session
- Environment segregation: Separate development, testing, and production environments

### 4. Monitoring, Reporting and Controlling

**Core requirement:** Continuous observation and logging of all requests; automated responses and real-time threat intelligence; token limits to prevent abuse.

**Risk scenarios:**
- Chatbot misuse (e.g., city chatbot used for spam generation or translation instead of its purpose)
- Endpoint repeatedly invoking LLM inappropriately → resource exhaustion, system instability
- Excessive token usage → overload, performance degradation, unexpected costs

**Mitigations** (5 measures):
- Anomaly detection for unusual request patterns; per-endpoint behavior monitoring; track CPU/GPU/API usage
- Automated predefined responses to known threats; real-time threat intelligence for situational awareness
- Token limits on users and devices
- Detailed audit logging of all interactions
- Regular automated testing against security policies

### 5. Threat Intelligence

**Core requirement:** Collection, analysis, and sharing of information about emerging and active AI-specific cyber threats — TTPs, IOCs, known vulnerabilities. Directly connected to Monitoring (Principle 4).

**Risk scenarios:**
- Failure to track evolving Prompt Injection techniques → defenses lagging behind novel obfuscation patterns
- Supply chain attack targeting external components/APIs the LLM system depends on

**Mitigations** (5 measures):
- Known attack pattern recognition from previous incidents
- Threat intelligence feeds integrated with access controls (automatically deny known malicious IPs/agents)
- Regular red-teaming tests
- Dynamic analysis: integration with security communities for LLM-specific threat exchange
- Compromised component removal and system reorganization

### 6. Awareness

**Core requirement:** Understanding of risks, threats, and vulnerabilities by all stakeholders throughout the LLM system lifecycle. "Awareness is thus an essential component of a comprehensive cybersecurity strategy and serves as the foundation for the successful implementation and continuous adaptation of Zero Trust principles in LLM systems."

**Risk scenarios:**
- Developers storing sensitive information in system prompts → exposed via targeted Prompt Injection
- Clickable hyperlink and data exfiltration attacks exploiting user lack of awareness

**Mitigations** (5 measures):
- Practical training: red-teaming exercises targeting users; simulated cyberattacks
- Case studies and examples in security workshops; awareness campaigns
- Clear security communication: **"Do not trust AI systems unconditionally"**
- Regular security updates and newsletters
- Explainability and transparency: make LLM decision-making processes interpretable

---

## The Conclusion: What the BSI/ANSSI Actually Recommend

> "A key message is that **blind trust in LLM systems is not advisable, and the fully autonomous operation of such systems without human oversight is not recommended.** It is improbable that such agents can ensure meaningful and reliable safety guarantees."

This is the document's strongest statement. It places ANSSI and BSI firmly in the **cautious deployment** camp — LLM systems should be bounded, sandboxed, and human-supervised. Full autonomy is inadvisable.

The document aligns with Beurer-Kellner et al. (2025), who reach the same conclusion independently.

---

## Relationship to the OSKG-ZeroTrust Graph

### Where This Document Fits

The ANSSI-BSI paper occupies a unique position: it is **neither a standard (like NIST 800-207) nor a practitioner book (like Gilman & Barth) nor an academic paper (like Dotse or Cao).** It is a **binational government guidance document** — normative but deployment-agnostic, authoritative but intentionally non-prescriptive about technology.

### Claims That Extend the Existing ZT Framework

| Existing ZT Claim | ANSSI-BSI Extension | Significance |
|-------------------|-------------------|-------------|
| "Never trust, always verify" | Applies to LLM outputs and automated agent actions — **an LLM's output must not be trusted without verification** | Extends ZT from network/identity to AI inference |
| Continuous monitoring | Extended to include LLM-specific threats: Prompt Injection patterns, token abuse, unexpected model invocations | Creates new monitoring dimensions beyond traditional ZT |
| Least privilege access | Applied to LLM system components: plugins can't access conversation history, RAG databases scoped to user role, agents execute in user's security context | Component-level granularity beyond what practitioner ZT books describe |
| Assume breach | Reframed for AI: **assume the LLM has been compromised** via Prompt Injection and design controls accordingly | The assume-breach principle now covers the AI model itself |
| Policy engine / PDP | Mapped to "Trust Algorithm" for input evaluation — weighted scoring of prompt trustworthiness | The PEP/PDP model gains an AI-specific evaluation layer |

### Claims That Challenge Practitioner Assumptions

| Practitioner Assumption | ANSSI-BSI Challenge |
|------------------------|---------------------|
| "Agentic AI is the future" (industry narrative) | "Fully autonomous operation... is not recommended" — BSI/ANSSI explicitly caution against it |
| "LLMs can be secured with traditional controls" | Six new design principles are required, several of which (input tagging, trust algorithms for prompts, session-level memory isolation) have no analog in traditional ZT |
| "The orchestrator can be an LLM" | The orchestrator security analysis is explicitly deferred — this is an open risk |
| "ZT is implementation-mature" | Even with full adherence to all six principles, "residual risks may remain" — the document does not claim completeness |

### The AI+ZT Evidence Gap

This document reveals a significant gap in the ZT knowledge base:

- **The ZT standards (NIST, CISA, NSA, DoD)** were written before LLM/agentic AI became a deployment reality. They do not address AI-specific attack surfaces.
- **The practitioner books** (Gilman & Barth 2017, Garbis & Chapman, Finney, Green-Ortiz 2024) barely mention AI, and none address LLM security within ZT.
- **The academic AI+ZT papers** (Cao et al.) focus on using AI *for* ZT automation, not securing AI *within* ZT.
- **ANSSI-BSI (2025)** is the first authoritative document to bridge this gap, and it is explicitly **preliminary and non-exhaustive.**

The AI+ZT intersection is the least-developed area of the ZT knowledge graph. The ANSSI-BSI paper is a starting point, not a comprehensive framework.

### Key Unresolved Questions for the OSKG Graph

1. How does the Trust Algorithm for input evaluation (weighted scoring of prompt trustworthiness) integrate with the NIST 800-207 PE trust algorithm? Are these the same algorithm applied to different inputs, or are they architecturally distinct?

2. If "no LLM-based authentication" is a principle, how do agentic systems authenticate to each other in multi-agent environments? What replaces the LLM in the auth chain?

3. The document defers orchestrator security — but if the orchestrator is itself an LLM, this is a recursive trust problem. What is the formal trust model for an LLM orchestrator?

4. How do the six design principles map to the CISA ZTMM maturity model? A maturity progression for AI+ZT does not yet exist.

5. Is the ANSSI-BSI caution against full autonomy a permanent architectural principle or a reflection of current LLM immaturity? Does ZT require human-in-the-loop permanently, or can future verified AI systems operate autonomously within ZT?
