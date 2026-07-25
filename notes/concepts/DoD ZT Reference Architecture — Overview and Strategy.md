---
tags:
  - source/standards
  - dod
  - zt-strategy
  - zt-pillars
  - zt-tenets
  - defense
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
claims_status: extracted
claims_extracted: 2026-07-24
confidence: high
source:
  title: "DoD Zero Trust Reference Architecture Version 2.0"
  authors: "DISA and NSA Zero Trust Engineering Team"
  year: 2022
  publisher: "Department of Defense"
  local_file: "sources/standards/_txt/DoD_ZT_Reference_Architecture_v2.txt"
related:
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[CISA ZTMM — Overview and Framework]]"
  - "[[NSA — Embracing a Zero Trust Security Model]]"
  - "[[Concepts Index]]"
---

# DoD ZT Reference Architecture — Overview and Strategy

The DoD Zero Trust Reference Architecture (v2.0, July 2022) is the Department's authoritative architectural guidance for Zero Trust. Prepared jointly by DISA and NSA, it translates the NIST 800-207 architectural framework into an operational, threat-centric doctrine for defense systems. Where NIST defines what ZT *is*, the DoD ZT RA defines how the DoD *does* ZT — reconfiguring, reprioritizing, and augmenting existing capabilities rather than starting from scratch.

## Chapter 1: Purpose and Strategic Goals

**Claim 1 —** DoD's ZT strategy is operational, not architectural → [[dod-zt-operational-not-architectural]]
---

**Claim 2 —** The DoD threat model is fundamentally different from civilian ZT → [[dod-threat-model-different-from-civilian]]
---

**Claim 3 —** ZT is an evolution of existing capabilities, not a greenfield deployment → [[zt-evolution-existing-capabilities-incremental]]
---

### High-Level Goals (CV-1)

The DoD enumerates five high-level goals for ZT adoption:

1. **Modernize Information Enterprise to Address Gaps and Seams.** Decades of decentralized development created organizational and technical seams that adversaries exploit. ZT must produce a unified common operating picture.

2. **Simplify Security Architecture.** Fragmented cybersecurity has created "excessive technical complexity, creating vulnerabilities in enterprise hygiene." Complexity is itself a vulnerability — a point NIST 800-207 doesn't make explicitly.

3. **Produce Consistent Policy.** Automated cybersecurity policies must be "consistently applied across environments for maximum effectiveness." This is a lesson learned from industry that the DoD has not yet internalized.

4. **Optimize Data Management Operations.** Disparate and inconsistently implemented data standards create interoperability challenges, system inefficiencies, and prevent full use of cloud/AI/ML capabilities.

5. **Provide Dynamic Credentialing and Authorization.** PKI/CAC, while secure, "has not kept pace with more user-friendly multi-factor authentication advances in industry." Non-person entities (NPEs), bots, and IoT are under-addressed.

**Assessment:** Goals 3 and 5 are the most operationally significant. Goal 3 (consistent policy) is the prerequisite for automated enforcement — you can't automate what isn't standardized. Goal 5 (dynamic credentialing) addresses the DoD's specific pain point: CAC is secure but inflexible, and the DoD has millions of NPEs that need identity management.

---

### Assumptions and Constraints

The DoD states seven core assumptions (§1.7) that drive ZT planning:

1. The CS RA remains authoritative; the ZT RA augments, not replaces, it
2. Technologies will exist and be mature for DoD-wide ZT migration
3. Communication encryption is mandated to the greatest extent possible
4. Multiple decentralized service pilots will require integration
5. No single device or capability produces ZT — it's a holistic approach
6. Security policies will be universally automated at the macro level, granular at the micro level
7. Interoperability standards must emerge to enhance data security

**Key insight:** Assumption 5 ("no single device or capability produces ZT") is the operational corollary to NIST's claim that "ZT is a strategy, not a product." The DoD states it more bluntly: no vendor can sell you ZT. This is a direct rebuttal to vendor marketing.

---

## Chapter 2: Pillars and Principles

**Claim 4 —** DoD's five tenets are threat-operational, NIST's seven tenets are architectural → [[dod-five-tenets-threat-operational]]
---

**Claim 5 —** DoD's seven pillars are identical to CISA's — the difference is implementation depth → [[dod-seven-pillars-identical-cisa]]
---

**Claim 6 —** DoD's seven RA principles are the architectural bridge between tenets and implementation → [[dod-seven-ra-principles-bridge]]
---

## Cross-Cutting Observations

### The Three-Layer Model

The DoD ZT RA introduces a three-layer conceptual model that doesn't exist in NIST 800-207:

| Layer | Content | Audience | Purpose |
|-------|---------|----------|---------|
| **Tenets** (5) | Assume Hostile Environment, Presume Breach, Never Trust/Always Verify, Scrutinize Explicitly, Apply Unified Analytics | Leadership, operators | *Why* ZT — operational philosophy |
| **Pillars** (7) | User, Device, Network, Apps/Workload, Data, Visibility/Analytics, Automation/Orchestration | Program managers, capability planners | *Where* to invest — functional domains |
| **Principles** (7) | No trusted zones, identity-based auth, M2M auth, risk-based auth, data encryption, continuous monitoring, centralized policy | Architects, engineers | *How* to design — architectural constraints |

This three-layer model is the DoD's most important architectural contribution to ZT thinking. NIST provides the *definition*; DoD provides the *decomposition*. Together they form a complete framework: NIST tells you what ZT is, DoD tells you how to organize your ZT program.

### Operational vs. Architectural Framing

| Dimension | NIST 800-207 | DoD ZT RA |
|-----------|-------------|-----------|
| Primary framing | Architectural (PDP/PEP) | Operational (capabilities, goals) |
| Threat posture | "Minimize uncertainty" | "Assume hostile environment, presume breach" |
| Tenet count | 7 (architectural) | 5 (operational) |
| Pillar count | Not explicit (implied in logical components) | 7 (aligned with CISA) |
| Principles | Embedded in tenets | 7 explicit architectural principles |
| Audience | Federal system architects | DoD Mission Owners |
| Implementation approach | Greenfield architecture design | Incremental evolution of existing capabilities |
| Key unique contribution | PDP/PEP model, logical components | Three-layer model (tenets/pillars/principles), M2M auth |

### Relationship to NSA Guidance

The DoD ZT RA was co-authored by NSA, and the intellectual lineage is clear:

- NSA's "Embracing a Zero Trust Security Model" (Feb 2021) introduced the "Assume Breach" framing that the DoD ZT RA elevates to Tenet 2
- NSA's three guiding principles map to DoD tenets 3, 1/2, and 4
- The DoD ZT RA's maturity model (Ch 8) directly anticipates CISA's four-level model
- NSA's pillar-specific guidance (2023-2024) operationalizes the seven pillars defined in the ZT RA

The NSA → DoD ZT RA → CISA ZTMM sequence represents the maturation of U.S. government ZT guidance over three years. NSA provided the threat rationale; DoD provided the architectural framework; CISA provided the assessment methodology.

---

## Chapter 1-2 Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| DoD's ZT strategy is operational, not architectural | HIGH | Over-emphasis on capabilities without architectural enforcement |
| DoD threat model is fundamentally different from civilian ZT | HIGH | Threat model may not apply to all DoD systems (e.g., admin networks) |
| ZT is an evolution of existing capabilities | HIGH | "Incremental progress" used to avoid hard architectural decisions |
| Five tenets are threat-operational, seven are architectural | VERY HIGH | Conflation of the two sets in acquisition requirements |
| Seven pillars identical to CISA's | HIGH | Divergence over time as DoD-specific requirements accumulate |
| Seven RA principles are the architectural bridge | HIGH | Principles without enforcement mechanisms are aspirational |

**Strongest section:** The three-layer model (tenets → pillars → principles). This is the DoD's most important contribution to ZT architecture — it provides a structured decomposition that NIST 800-207 lacks. Every ZT program should be organized this way: operational philosophy (why), functional domains (where), architectural constraints (how).

**Weakest section:** The relationship between the five tenets and NIST's seven tenets is never explicitly discussed. The DoD document doesn't acknowledge that it's using a different tenet model than the NIST standard it cites. This creates potential confusion for joint civilian-defense operations where both tenet sets may be referenced.

**Missing:** The document doesn't address how the ZT RA applies to classified systems. The seven principles speak of "networks" generically, but SIPRNet and JWICS have different trust assumptions than NIPRNet. NIST 800-207 explicitly excludes classified systems from scope; the DoD ZT RA is ambiguous.

**Most important for OSKG-ZeroTrust:** The three-layer model (tenets/pillars/principles) should inform how the knowledge graph structures ZT concepts. Tenets are the *philosophy* nodes; pillars are the *domain* nodes; principles are the *constraint* nodes. NIST contributes the *definition* node and the *architecture* (PDP/PEP) node. Each node type has different relationships and different evidentiary standards.
