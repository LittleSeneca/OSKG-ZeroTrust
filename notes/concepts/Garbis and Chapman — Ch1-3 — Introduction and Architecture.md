---
tags:
  - source/books
  - garbis-chapman
  - zt-introduction
  - zt-architecture
  - zt-definition
  - zt-deployment-models
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
claims_status: extracted
claims_extracted: 2026-07-24
confidence: high
source:
  title: "Zero Trust Security: An Enterprise Guide"
  authors: "Jason Garbis, Jerry W. Chapman"
  year: 2021
  publisher: "Apress"
  local_file: "sources/books/_txt/Zero_Trust_Security_An_Enterprise_Guide.txt"
  chapter_lines: "554–2217"
related:
  - "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[NIST 800-207 — Ch1 — Introduction]]"
  - "[[Concepts Index]]"
  - "[[Books Index]]"
  - topic/zt-architecture
  - topic/zt-definition
  - topic/zt-network
---

# Garbis & Chapman — Ch1–3: Introduction, ZT Definition, and Architecture

The foundational chapters of the most practical, enterprise-focused Zero Trust book in the field. Garbis & Chapman are practitioners who have worked with enterprises of varying sizes and maturities through their ZT journeys. These three chapters establish the book's philosophy, define Zero Trust in operational terms, and build an architectural framework that extends NIST SP 800-207 for real-world enterprise deployment. Their distinctive contribution is treating ZT as an *integrated security platform* — not just a network architecture — with identity at the core and automation as the binding agent.

---

## Ch1: Introduction — The Case for Zero Trust

**Claim 1 —** Traditional enterprise security is structurally broken — not merely insufficient, but actively perpetuating vulnerability. → [[traditional-enterprise-security-is-structurally-broken-not-merely]]

---

**Claim 2 —** "Zero Trust" is a misnomer — the real concept is "zero implicit trust" or "earned trust." → [[zero-trust-is-a-misnomer-the-real-concept]]

---

**Claim 3 —** Zero Trust is a philosophy, principles, and a journey — not a product, not a one-and-done project, and not a single architecture. → [[zero-trust-is-a-philosophy-principles-and-a]]

---

## Ch2: What Is Zero Trust? — History, Principles, and Definition

**Claim 4 —** Zero Trust amplifies existing security concepts (least privilege, RBAC) into a holistic, identity-centric, automated platform — this is what's new. → [[zero-trust-amplifies-existing-security-concepts-least-privilege]]

---

**Claim 5 —** The three core principles — secure all resources regardless of location, enforce least privilege, inspect/log all traffic — are universally necessary for any ZT implementation. → [[the-three-core-principles-secure-all-resources-regardless]]

---

**Claim 6 —** Three expanded principles — API integration, automation, and business value delivery — are equally necessary for enterprise-class ZT. → [[three-expanded-principles-api-integration-automation-and-business]]

---

**Claim 7 —** The working definition centers ZT as an "integrated security platform" — broader than network architecture. → [[the-working-definition-centers-zt-as-an-integrated]]

---

**Claim 8 —** The 14 platform requirements operationalize the principles into verifiable criteria. → [[the-14-platform-requirements-operationalize-the-principles-into]]

---

## Ch3: Zero Trust Architectures — Models, PEPs, and Policies

**Claim 9 —** The NIST PDP/PEP model is the correct foundation, but needs enterprise-specific refinement and extension. → [[the-nist-pdppep-model-is-the-correct-foundation]]

---

**Claim 10 —** There are three distinct types of PEPs, and understanding their differences is essential for architecture design. → [[there-are-three-distinct-types-of-peps-and]]

---

**Claim 11 —** A component is only a PEP if it enforces identity-centric, dynamic policies via an automated control channel — traditional firewalls alone don't qualify. → [[a-component-is-only-a-pep-if-it]]

---

**Claim 12 —** Four deployment models cover the ZT solution space, and each has distinct trade-offs that must be evaluated against enterprise requirements. → [[four-deployment-models-cover-the-zt-solution-space]]

---

**Claim 13 —** The implicit trust zone is the key architectural trade-off in ZT deployment. → [[the-implicit-trust-zone-is-the-key-architectural]]

---

## Ch3: Policy Model Foundation

**Claim 14 —** The policy structure of Subject Criteria + Action + Target + Condition provides a universal template for ZT policy definition. → [[the-policy-structure-of-subject-criteria-action-target]]

---

## Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| 1: Traditional security is structurally broken | HIGH | Effective perimeter-only architectures as counter-examples |
| 2: "Zero Trust" = "zero implicit trust" | HIGH | Literal interpretations persisting despite clarification |
| 3: ZT is philosophy/principles/journey, not product | HIGH | Platform vendors proving complete ZT "in a box" |
| 4: ZT amplifies existing security via holistic integration | HIGH | Argument that ZT requires fundamentally new primitives |
| 5: Three core principles are universally necessary | HIGH | Edge cases where a principle genuinely doesn't apply |
| 6: Three expanded principles are equally necessary | HIGH (4–5) / MEDIUM-HIGH (6) | Organizations achieving ZT without explicit business-value framing |
| 7: Working definition as "integrated security platform" | HIGH | Network-centric definitions proving more useful in practice |
| 8: 14 platform requirements operationalize the principles | HIGH | Requirements being too prescriptive for some environments |
| 9: NIST PDP/PEP extended with 3 PEP types and policy structure | HIGH | Service mesh architectures not cleanly mapping to centralized PDP |
| 10: Three PEP types (user agent, network, application) | HIGH | Overlap/fuzziness undermining the categorization's utility |
| 11: PEP requires identity-centric, dynamic, automated enforcement | VERY HIGH | Traditional firewalls with thin automation layers claiming PEP status |
| 12: Four deployment models cover the solution space | HIGH | New deployment models not covered by the taxonomy |
| 13: Implicit trust zone is the key architectural trade-off | VERY HIGH | Organizations accepting large trust zones as "good enough" |
| 14: Policy structure (Subject/Action/Target/Condition) | HIGH | Policy engines using fundamentally different structures |

**Strongest sections:**
- **Ch2 Core Principles** — The three core plus three expanded principles are the most actionable, testable ZT principle set in the literature. They bridge the gap between NIST's abstract tenets and an RFP checklist.
- **Ch3 PEP Definition (Claim 11)** — The criteria for what counts as a PEP draw the sharpest line between traditional security and Zero Trust. The automation overlay insight makes ZT adoption feasible without rip-and-replace.
- **Ch3 Deployment Models (Claim 12)** — The four-model framework with explicit pros/cons is the most practical vendor evaluation tool in ZT literature. It's concrete enough to use in procurement without being vendor-specific.

**Weakest sections:**
- **Ch1 Introduction** — While well-written, it's largely motivational and doesn't add much beyond what NIST and Gilman & Barth already cover. The "zero is a misnomer" clarification is valuable but brief.
- **Ch3 Enterprise Architecture** — The representative enterprise architecture walkthrough (VPN, NAC, IDS/IPS, etc.) is necessary scene-setting for the book but occupies significant space without advancing the conceptual framework. The pain-point analysis for each component is practically useful but analytically thin.

**Unique contribution to OSKG-ZeroTrust:**
Garbis & Chapman provide the *operational layer* that NIST abstracts and Gilman & Barth engineer. NIST defines what ZT *is*; Gilman & Barth define how ZT *works*; Garbis & Chapman define how ZT *is adopted*. Their contributions that are unique among the three:

1. **The "amplification" argument** — ZT doesn't invent new security; it scales and integrates existing security into a platform. This is the most effective answer to "what's new?"
2. **The "network access is a privilege" reframing** — The operational bridge between IAM and network security.
3. **The PEP qualification criteria** — "Can it enforce identity-centric dynamic policies automatically?" is the test that separates ZT from traditional security.
4. **The deployment model taxonomy** — Four models with trade-off analysis provides the procurement framework that NIST and Gilman & Barth don't offer.
5. **The "automation ≠ automatic" distinction** — Resolves the fear that ZT means removing human judgment from security.

**Comparison with related notes:**
- **vs. NIST 800-207 Ch2:** Garbis & Chapman's principles are more operational (6 principles with platform requirements) vs. NIST's more abstract (7 tenets). Both are correct; they serve different audiences. Garbis & Chapman are writing for the security leader who needs to buy/build; NIST is writing for the federal agency that needs to comply.
- **vs. Gilman & Barth Ch1:** Gilman & Barth's control plane/data plane split is the architectural DNA; Garbis & Chapman's PDP/PEP with three PEP types is the operational expression of that DNA in enterprise infrastructure. The books are complementary — Gilman & Barth explains the architecture, Garbis & Chapman explains how to map your existing infrastructure onto it.
- **vs. NIST 800-207 Ch3 (Logical Components):** NIST's logical component model is the starting point; Garbis & Chapman extend it with PEP types, policy structure, and deployment models. The extension from abstract components to concrete deployment models is the value add.

**Open Questions:**
- How do the four deployment models map to specific commercial products? (The authors deliberately avoid this, but it's the next question every reader asks.)
- Can the "integrated security platform" definition be achieved without a single-vendor platform? (The book is vendor-agnostic but the definition leans toward platform thinking.)
- How does the implicit trust zone concept interact with zero-trust network access (ZTNA) products that create per-application tunnels? (Each tunnel effectively creates a micro implicit trust zone.)
- The chapter defers detailed policy discussion to Ch17 — does the policy model ultimately resolve or reproduce the complexity it aims to simplify?
