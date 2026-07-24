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

### Claim 1: DoD's ZT strategy is operational, not architectural

**DoD's claim:** The ZT RA is "an authoritative source of information about a specific subject area that guides and constrains the instantiations of multiple architectures and solutions." It is a *capability-centric* description — not a blueprint, but a framework for capability planning, portfolio management, and IT investment decisions.

**Evidence presented:** The RA uses DoDAF operational views (OV-1, OV-2, CV-1, CV-2) rather than technical specifications. Artifacts are intentionally informal — "informal drawings are easier to understand by a wide audience." The document's organization prioritizes Strategy and Vision → Pillars and Principles → Conceptual Capability Architecture → Use Cases. The architecture is the *last* concern, not the first. This is the opposite of NIST 800-207, which leads with the PDP/PEP logical architecture.

**Confidence:** HIGH. The operational framing is explicit throughout: the document's primary audience is Mission Owners, not architects. The ZT RA tells MOs *what capabilities to build*, not how to build them.

**What's at stake:** If ZT is framed architecturally (NIST), implementation starts with policy engine design. If framed operationally (DoD), implementation starts with capability inventory and gap analysis. The DoD approach is more realistic for an organization with 3M+ endpoints and 4,000+ systems that can't be rebuilt from scratch.

**Who disagrees:** NIST 800-207 is explicitly architectural — the PDP/PEP model is the centerpiece. CISA's maturity model synthesizes both: it measures operational maturity (DoD's concern) against architectural capabilities (NIST's concern).

**Alternative reading:** The operational framing could be read as political necessity — the DoD can't mandate specific architectures across all services, so it provides operational guidance that each service interprets. A stricter reading would demand architectural conformity.

**My assessment:** The operational framing is the right call for the DoD's federated command structure. DISA can't tell the Army how to architect its networks, but it can tell all services what ZT capabilities they must demonstrate. The CISA maturity model operationalizes this for civilian agencies; the DoD ZT RA does the same for defense.

---

### Claim 2: The DoD threat model is fundamentally different from civilian ZT

**DoD's claim:** "State-funded hackers are well trained, well-resourced, and persistent. The use of new tactics, techniques, and procedures combined with more invasive malware can enable motivated malicious personas to move with previously unseen speed and accuracy."

**Evidence presented:** The threat discussion in §1.4.1 is specific and adversarial — not generic "cyber threats" but named adversaries with known capabilities. The problem statement (§1.5) emphasizes *insider threats* and *lateral movement* as primary concerns, reflecting the DoD's experience with APT-level adversaries. Compare NIST 800-207 Ch 1, which discusses threats in terms of "network complexity" and "cloud adoption" — civilian concerns.

**Confidence:** HIGH. The threat model difference is visible in every section: "Assume a Hostile Environment" and "Presume Breach" are the DoD's first two tenets (§2.2) — neither appears in NIST's seven tenets.

**What's at stake:** If the threat model is APT-level adversaries with persistent access, ZT must assume breach *operationally*, not just architecturally. This means continuous monitoring isn't optional — it's the primary control. For civilian agencies facing compliance risk more than APT risk, monitoring can be less urgent.

**Who disagrees:** NSA's "Embracing a Zero Trust Security Model" (2021) uses the same threat-centric framing — unsurprising since NSA co-authored the ZT RA. CISA's maturity model is threat-agnostic; it measures capability regardless of threat model.

**Alternative reading:** The threat emphasis could be read as institutional bias — DISA and NSA are defense/intelligence agencies that think in adversary-centric terms. NIST's "minimize uncertainty" framing may be equally valid for organizations that face different threat profiles.

**My assessment:** The threat model difference is the single most important distinction between DoD and civilian ZT. Every subsequent design decision — from micro-segmentation requirements to continuous authentication cadence — flows from the assumption that the adversary is already inside the network. This is not paranoia; it's the operational reality of defending the DoDIN against APT actors.

---

### Claim 3: ZT is an evolution of existing capabilities, not a greenfield deployment

**DoD's claim:** "By reconfiguring, reprioritizing, and augmenting existing DoD capabilities, the DoD will be able to evolve towards a next-generation security architecture." The strategy is explicitly incremental — "ZT supports an incremental migration approach to cybersecurity with an end state of an interoperable, fully functioned, optimized cybersecurity architecture."

**Evidence presented:** The document identifies existing DoD capabilities that serve as ZT baselines: JRSS (Joint Regional Security Stack), PKI/CAC for ICAM, Comply-to-Connect for device posture, SDN/SDE for network virtualization. The transition architecture (Ch 8) maps a maturity model with baseline → transition → target phases. This is not "rip and replace" — it's "reconfigure what you have."

**Confidence:** HIGH. The incremental approach is consistent with the DoD ZT Strategy (also July 2022) and the CISA maturity model. No one advocates greenfield ZT for organizations of this scale.

**What's at stake:** If ZT requires greenfield, it's unfundable (the DoD can't replace 4,000+ systems). If ZT is incremental, every dollar spent on existing capabilities (JRSS, ICAM, C2C) is a step toward the target. The framing matters for budget justification.

**Who disagrees:** Purists argue that incremental ZT is an oxymoron — if you still have implicit trust zones, you don't have ZT. The DoD implicitly acknowledges this by describing a "journey" (a word used throughout the ZT Strategy) rather than a destination.

**My assessment:** The incremental framing is pragmatically necessary but analytically dangerous. The risk is that organizations claim "ZT progress" while preserving the implicit trust zones that ZT is supposed to eliminate. The CISA maturity model mitigates this by requiring specific capability demonstrations at each level. The DoD ZT RA's maturity model (Ch 8) serves the same function.

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

### Claim 4: DoD's five tenets are threat-operational, NIST's seven tenets are architectural

**DoD's claim:** ZT has five major tenets that "represent the foundational elements and influence all aspects within ZT":

1. **Assume a Hostile Environment.** "There are malicious personas both inside and outside the environment. All users, devices, applications, environments, and all other NPEs are treated as untrusted."

2. **Presume Breach.** "Consciously operate and defend resources with the assumption that an adversary has presence within your environment. Enhanced scrutiny of access and authorization decisions to improve response outcomes."

3. **Never Trust, Always Verify.** "Deny access by default. Every device, user, application/workload, and data flow are authenticated and explicitly authorized using least privilege, multiple attributes, and dynamic cybersecurity policies."

4. **Scrutinize Explicitly.** "All resources are consistently accessed in a secure manner using multiple attributes (dynamic and static) to derive confidence levels for contextual access to resources."

5. **Apply Unified Analytics.** "Apply unified analytics for Data, Applications, Assets, Services (DAAS) to include behavioristics, and log each transaction."

**Evidence presented:** Compare to NIST's seven tenets (see [[NIST 800-207 — Ch2 — Zero Trust Basics]]). NIST's tenets describe what a ZT architecture *does* — consider all data sources as resources, secure all communication, grant per-session access, use dynamic policy, monitor all assets, enforce strict authentication, collect telemetry. DoD's tenets describe what a ZT operator *assumes and does* — assume the environment is hostile, presume you're already breached, never trust, scrutinize everything, apply analytics.

**Confidence:** VERY HIGH. The difference in framing is consistent and intentional. DoD's tenets 1 and 2 ("Assume Hostile Environment," "Presume Breach") have no NIST equivalent. DoD's tenet 5 ("Apply Unified Analytics") has no direct NIST equivalent (NIST's tenet 7 is about collecting information, not applying analytics). The overlap is in tenets 3 and 4, which map to NIST's tenets 2-6.

**What's at stake:** If ZT is defined by NIST's architectural tenets, the focus is on building a policy engine. If defined by DoD's operational tenets, the focus is on threat hunting and continuous monitoring. Both are necessary, but the emphasis determines resource allocation.

**Who disagrees:** NSA's three guiding principles ("Never Trust, Always Verify"; "Assume Breach"; "Verify Explicitly") align more closely with DoD's tenets — unsurprising, as NSA co-authored both documents. CISA's maturity model is tenet-agnostic — it measures capabilities, not adherence to any specific tenet set.

**Alternative reading:** The DoD's five tenets could be seen as a *subset* of NIST's seven, repackaged for operational audiences. But tenets 1 and 2 ("Assume Hostile Environment," "Presume Breach") add an adversarial framing that NIST deliberately avoids — NIST's "minimize uncertainty" is risk-management language, not threat-operational language.

**My assessment:** The DoD's five tenets are better for briefing commanders. NIST's seven tenets are better for briefing architects. Both sets are correct; they describe the same thing from different perspectives. The CISA maturity model synthesizes both by measuring capability maturity against a threat-informed baseline.

---

### Claim 5: DoD's seven pillars are identical to CISA's — the difference is implementation depth

**DoD's claim:** The seven Pillars are "in alignment with the common industry identification of ZT Pillars":

| Pillar | DoD ZT RA Emphasis |
|--------|-------------------|
| **User** | MFA, PAM, continuous authentication/authorization/monitoring of activity patterns |
| **Device** | Continuous real-time authentication, inspection, assessment, patching; Comply-to-Connect; TPM |
| **Network/Environment** | Macro- and micro-segmentation; control privileged access; prevent lateral movement |
| **Applications and Workload** | Full stack from application layer to hypervisor; DevSecOps; proxy technologies; source code vetting |
| **Data** | Categorization by mission criticality; DRM, DLP, data tagging; encryption at rest and in transit |
| **Visibility and Analytics** | UEBA, sensor data, telemetry, deep packet inspection; ML-based anomaly detection |
| **Automation and Orchestration** | SOAR, SIEM integration, policy-based automated response; centralized policy enforcement |

**Evidence presented:** These seven pillars are identical to CISA's five-pillar model (CISA groups Network, Applications & Workload, and Data under a broader "Network/Environment" category but organizes maturity assessments around the same seven areas). The DoD adds specific defense-relevant technologies: Comply-to-Connect (C2C), PKI/CAC, JRSS, and explicit DevSecOps integration for the Applications pillar.

**Confidence:** HIGH. The pillar structure is now universal across U.S. government ZT guidance — CISA, DoD, and NSA all use the same seven-pillar taxonomy. This convergence is deliberate; it enables cross-agency maturity comparison.

**What's at stake:** If pillars differ across agencies, cross-agency collaboration (e.g., DoD sharing data with DHS) becomes architecturally impossible. If pillars are consistent, joint operations can align ZT implementations. This is not theoretical — the DoD routinely shares classified data with civilian agencies.

**Who disagrees:** Sounil Yu's Cyber Defense Matrix uses a different taxonomy (five asset classes across five security functions). Forrester's ZTX framework uses seven pillars but organizes them differently. The industry hasn't fully converged, but the U.S. government has.

**My assessment:** The pillar convergence is one of the unsung achievements of U.S. government Zero Trust policy. NIST, CISA, DoD, and NSA all using the same taxonomy means a vendor can build once and sell to everyone, and an assessor can evaluate any agency using the same framework. This is the standardization that Goal 3 (consistent policy) demands.

---

### Claim 6: DoD's seven RA principles are the architectural bridge between tenets and implementation

**DoD's claim:** Seven Reference Architecture Principles (OV-6a) guide "the creation of the RA and other future documents":

1. **No implicit or explicit trusted zone in networks.** Goes beyond NIST (which says "no *implicit* trust" based on location) to also reject *explicit* trust zones. Every trust relationship must be continuously verified.

2. **Identity-based authentication and authorization strictly enforced for all connections.** Covers user-to-resource and user-to-infrastructure access. This operationalizes tenet 3 ("Never Trust, Always Verify").

3. **Machine-to-machine authentication and authorization strictly enforced.** This is a DoD-specific addition. NIST 800-207's tenets don't explicitly address M2M communication. In DoD environments, server-to-server and application-to-database flows are as critical as user-to-server flows.

4. **Risk profiles from near-real-time monitoring used in authorization.** Operationalizes tenet 4 ("Scrutinize Explicitly") and tenet 5 ("Apply Unified Analytics"). Risk is dynamic, not static — access decisions change as risk profiles change.

5. **All sensitive data encrypted in transit and at rest.** NIST's tenet 2 ("all communication is secured") is broader; DoD's principle is more specific and actionable.

6. **All events continuously monitored, collected, stored, and analyzed.** Operationalizes tenet 5 ("Apply Unified Analytics") and the Visibility & Analytics pillar. Compliance with security policies is demonstrated through telemetry, not assertions.

7. **Policy management and distribution is centralized.** This is the most architecturally significant principle. Decentralized policy management creates gaps and seams (Goal 1). Centralized policy enables consistent enforcement (Goal 3).

**Evidence presented:** These seven principles are distinct from both the five tenets and the seven pillars. The tenets are *operational philosophy*; the pillars are *functional domains*; the principles are *architectural constraints*. This three-layer structure (tenets → pillars → principles) is more sophisticated than NIST's single-layer tenet model.

**Confidence:** HIGH. The principles provide specific, auditable guidance that the tenets alone don't. "Assume a Hostile Environment" is a mindset; "No implicit or explicit trusted zone in networks" is a design rule.

**What's at stake:** Without principles, tenets are too abstract to guide implementation. With principles, every architectural decision can be tested: "Does this design create an implicit or explicit trust zone? Does it enforce identity-based authentication? Does it encrypt sensitive data?" This is how architecture becomes auditable.

**Who disagrees:** NIST 800-207 doesn't have a separate principles layer — the seven tenets serve both as philosophy and as architectural guidance. The DoD's three-layer model is more complex but provides clearer separation of concerns. CISA's maturity model effectively adds a fourth layer (maturity levels) on top.

**Alternative reading:** The seven principles could be seen as redundant with the five tenets and seven pillars. But the repetition is intentional — each layer serves a different audience. Tenets are for leadership (why we're doing this). Pillars are for program managers (where we're investing). Principles are for architects (how we design). This is good communication design.

**My assessment:** M2M authentication (Principle 3) is the most important DoD-specific contribution. NIST 800-207 barely addresses service-to-service communication. In DoD environments, a compromised application server can move laterally through databases and APIs just as easily as a compromised user can. M2M ZT is the next frontier, and the DoD is ahead of civilian guidance on this point.

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
