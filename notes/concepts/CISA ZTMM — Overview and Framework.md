---
tags:
  - source/standards
  - cisa
  - zt-maturity
  - zt-pillars
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
confidence: very-high
source:
  title: "CISA Zero Trust Maturity Model"
  authors: "CISA"
  year: 2023
  version: "2.0"
  publisher: "Cybersecurity and Infrastructure Security Agency"
  local_file: "sources/standards/_txt/CISA_Zero_Trust_Maturity_Model_v2.txt"
related:
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[Concepts Index]]"
note_type: combined
combined_sections: "§§1-5"
justification: "§§1-5 (Introduction through ZTMM overview) form a single architectural overview: §1 sets the policy mandate, §2 frames the operational urgency, §3 anchors the NIST definition, §4 acknowledges adoption challenges, and §5 lays out the model's structure (pillars, maturity levels, cross-cutting capabilities). Together they constitute the framework layer that the pillar-specific tables (5.1-5.5) operationalize. The framework content across these sections is ~350 lines — too thin for 5 standalone notes but collectively the foundation for understanding the entire maturity model."
---

# CISA ZTMM — Overview and Framework

The Cybersecurity and Infrastructure Security Agency's Zero Trust Maturity Model (ZTMM) v2.0 (April 2023) is the U.S. federal government's roadmap for transitioning agency cybersecurity from perimeter-based, implicit-trust architectures to Zero Trust Architectures (ZTA). It operationalizes NIST SP 800-207's seven tenets into five measurable pillars with four progressive maturity levels, providing federal agencies (and by extension, all organizations) with a practical, incremental path to zero trust adoption in compliance with Executive Order 14028 and OMB Memorandum M-22-09.

## §1: Introduction — Policy Mandate and Purpose

### Claim 1: The ZTMM is a compliance instrument for EO 14028, not merely a best-practice guide

**CISA's claim:** "CISA's Zero Trust Maturity Model (ZTMM) provides an approach to achieve continued modernization efforts related to zero trust... in accordance with Executive Order (EO) 14028 'Improving the Nation's Cybersecurity' § (3)(b)(ii), which requires that agencies develop a plan to implement a Zero Trust Architecture (ZTA)."

**Evidence presented:** The ZTMM explicitly cites EO 14028 as the legal mandate. It references OMB M-22-09 (January 2022) which sets specific FY 2024 deadlines for agencies to meet cybersecurity objectives aligned with the ZTMM pillars. The document is published by CISA's Cybersecurity Division under TLP:CLEAR — it's a government operational document, not a vendor framework.

**Confidence:** VERY HIGH. The legal mandate is unambiguous: EO 14028 §3(b)(ii) requires agency ZTA plans. The ZTMM is CISA's answer to that requirement. OMB M-22-09 further hardens this by setting concrete deadlines.

**What's at stake:** If the ZTMM is merely advisory, federal agencies can ignore it. If it's a compliance instrument, every FCEB agency must assess maturity against these pillars and show progress. The FY 2024 OMB deadline makes the latter interpretation unavoidable — agencies must demonstrate advancement by the end of the fiscal year.

**Who disagrees:** No one disputes the mandate. The debate is over whether the maturity model is the BEST path to compliance. NSA's "Embracing a Zero Trust Security Model" (2021) takes a threat-model-driven approach rather than a maturity-model approach, and some agencies may argue their existing architectures already satisfy ZTA requirements under a different assessment framework.

**Alternative reading:** The ZTMM could be read as "one of many paths" (as CISA states) — a suggested approach rather than a required one. But OMB M-22-09's specific alignment with ZTMM pillars makes this reading practically untenable for FCEB agencies.

**My assessment:** The ZTMM is as mandatory as any federal guidance gets without being a formal regulation. The combination of EO mandate + OMB deadlines + CISA's operational authority creates a de facto compliance requirement. The document's own hedging ("one of many paths") is standard government language that shouldn't be mistaken for optionality.

---

## §2: Current Environment — Operational Urgency

### Claim 2: Recent nation-state cyber incidents made legacy perimeter-based security indefensible

**CISA's claim:** "Recent cyber incidents have highlighted the broad challenges of ensuring effective cybersecurity across the federal government... 'business as usual' approaches are no longer sufficient to defend the nation from cyber threats."

**Evidence presented:** The document cites Emergency Directive 21-01 (SolarWinds Orion compromise) and Emergency Directive 21-02 (Microsoft Exchange vulnerabilities) in footnotes — both major nation-state supply chain attacks that exploited implicit trust between systems. The SolarWinds attack (2020) specifically compromised federal agency networks through a trusted software update mechanism.

**Confidence:** VERY HIGH. These are publicly documented incidents. The SolarWinds attack compromised at least nine federal agencies including Treasury, State, and Commerce. The operational failure of perimeter-based defenses is not theoretical — it's demonstrated.

**What's at stake:** If the threat assessment is wrong (i.e., if perimeter defenses + patching were sufficient), then the entire ZTA transition is unnecessary overhead. If it's right, federal agencies are currently exposed to nation-state threat actors. The billions in ZTA investment across the federal government depend on this assessment being correct.

**Who disagrees:** No one seriously disputes the incident severity. Some security practitioners argue that better patching habits and network segmentation would have prevented SolarWinds without a full ZTA — i.e., the problem was execution, not architecture. CISA's counter-argument is that implicit trust is the root cause that made the attacks so damaging.

**Alternative reading:** The SolarWinds reference could be seen as rhetorical — invoking a high-profile incident to justify a pre-existing policy preference. But the operational details of SolarWinds (trusted software update → lateral movement → data exfiltration) map directly to ZTA principles of per-session access and continuous verification.

**My assessment:** The threat narrative is well-supported. SolarWinds is the canonical "assume breach" case study — the attackers were inside trusted networks for months. ZTA wouldn't have prevented the initial compromise, but it would have dramatically limited lateral movement. The incident strengthens rather than weakens the ZTA case.

---

## §3: What Is Zero Trust? — The NIST Anchor

### Claim 3: The ZTMM is built on NIST SP 800-207's operative definition — zero trust minimizes uncertainty, not risk

**CISA's claim:** The document reproduces NIST SP 800-207's definition verbatim: "Zero trust provides a collection of concepts and ideas designed to minimize uncertainty in enforcing accurate, least privilege per-request access decisions... in the face of a network viewed as compromised." It also cites the NSTAC description: "a cybersecurity strategy premised on the idea that no user or asset is to be implicitly trusted."

**Evidence presented:** The definition is quoted directly with the exact NIST SP 800-207 citation. The document synthesizes both NIST's formal definition and NSTAC's operational description, establishing a dual foundation: NIST provides the conceptual framework, NSTAC provides the operational framing ("assume breach, continual verification").

**Confidence:** VERY HIGH. This is a direct quote from the authoritative source. The ZTMM doesn't innovate on the definition — it inherits it and builds the assessment framework on top.

**What's at stake:** The ZTMM's legitimacy depends on its fidelity to NIST 800-207. If it diverges, agencies face conflicting guidance. If it faithfully extends NIST, it benefits from NIST's authority. The document's extensive NIST citations signal that CISA sees itself as an implementer, not a reinventor.

**Who disagrees:** ForgeRock's ZTX framework (2018, Cunningham) defines ZT across seven pillars including Automation & Orchestration as a separate dimension. The NSTAC report (2022) emphasizes identity management more heavily than NIST 800-207. These are differences in emphasis, not contradiction.

**Alternative reading:** The document could be read as cherry-picking from NIST — using the definition but not NIST's full component model (Policy Engine, Policy Administrator, Policy Enforcement Point). The ZTMM's pillar-based structure is closer to ZTX than to NIST 800-207's logical component architecture. This is a structural choice, not a fidelity violation — the pillars are an assessment framework, not an architecture specification.

**My assessment:** The ZTMM sits between NIST 800-207 (architecture) and ZTX (assessment) — it uses NIST's definition but ZTX's pillar structure. This is a practical synthesis that serves its purpose: giving agencies measurable capabilities to assess. The NIST component model appears in the background as the target architecture, but the ZTMM doesn't require agencies to implement specific components.

---

### Claim 4: Zero trust represents a fundamental shift from location-centric to identity/data-centric security

**CISA's claim:** "Zero trust presents a shift from a location-centric model to an identity, context, and data-centric approach with fine-grained security controls between users, systems, applications, data, and assets that change over time; for these reasons, adopting a ZTA is a non-trivial effort. This shift provides the visibility needed to support the development, implementation, enforcement, and evolution of security policies. Fundamentally, zero trust may require a change in an organization's cybersecurity philosophy and culture."

**Evidence presented:** The document explicitly contrasts the "old" model (perimeter-based, location = trust) with the "new" model (identity + context + data-centric, continuous verification). It acknowledges that this is not a technology swap — it's a culture change. The cost discussion notes that initial implementation adds costs, but long-term enables "more prudent allocation of security investments toward the most critical data and services."

**Confidence:** HIGH. Every major ZT framework (NIST, DoD, NSA, Google BeyondCorp) agrees on this shift. The cultural dimension is well-observed in practice — agencies that treat ZTA as a technology project fail; those that treat it as a cultural transformation succeed.

**What's at stake:** If the shift is overstated (i.e., ZTA is mostly a technology refresh), organizations can implement it as an IT project. If it's genuinely cultural, it requires executive sponsorship, organizational change management, and multi-year commitment. Underestimating the cultural dimension is the single most common failure mode in ZTA adoption.

**Who disagrees:** Vendors selling ZT products minimize the cultural dimension — their marketing suggests ZTA is a technology deployment. The "ZT is a journey not a destination" framing (used by both NIST and CISA) directly counters this. NSA's guidance is even more explicit: ZTA requires "a fundamental shift in how we architect networks."

**Alternative reading:** The cultural change argument could be self-serving for CISA — it justifies their continued involvement beyond initial guidance publication and explains why agencies can't just "buy ZT." But the evidence from large-scale ZTA deployments (Google BeyondCorp, which took ~7 years) supports the cultural argument.

**My assessment:** Claim is well-founded but hard to verify. The cultural dimension is real, but its importance varies by agency size and starting point. A small agency with cloud-native infrastructure may find the technical shift trivial and the cultural shift modest. A large legacy agency (DHS, DoD) will find both difficult. The ZTMM's maturity levels effectively accommodate this variance — you don't need to reach Optimal everywhere.

---

## §4: Challenges — Why This Is Hard

### Claim 5: Legacy implicit-trust systems are the primary obstacle to ZTA adoption

**CISA's claim:** "Legacy systems often rely on 'implicit trust,' in which access and authorization are infrequently assessed based on fixed attributes; this conflicts with the core principle of adaptive evaluation of trust within a ZTA. Existing infrastructures built on implicit trust will require investment to change systems to better align with zero trust principles."

**Evidence presented:** The document identifies several concrete challenges: (1) legacy systems with implicit trust, (2) stove-piped and siloed IT services and staff, (3) need for "agency-wide buy in for a common architecture and governance policies," (4) different starting points across agencies. The acknowledgment that "agencies are beginning their journeys to zero trust from different starting points" is strategically important — it normalizes partial progress.

**Confidence:** HIGH. This is consistent with every major ZTA implementation report. Google's BeyondCorp migration took years specifically because legacy applications assumed network location = trust. DoD's ZT Strategy (2022) identifies legacy systems as a primary risk.

**What's at stake:** If legacy systems are unchangeable (common in classified environments), ZTA may be practically impossible for certain high-security systems. The ZTMM doesn't fully address this — it assumes legacy systems CAN be migrated. NSA's guidance is more explicit about the need for compensating controls where migration isn't feasible.

**Who disagrees:** The "rip and replace" school argues that legacy systems should be decommissioned, not migrated. The "incremental" school (which the ZTMM represents) argues that gradual migration is practical. Both agree legacy systems are the problem; they disagree on the solution.

**Alternative reading:** The focus on legacy systems could be a convenient excuse — the real challenge is organizational resistance and funding, not technology. The ZTMM addresses this implicitly by requiring governance and culture change across pillars.

**My assessment:** Legacy implicit-trust systems are a real obstacle, but the framework's maturity model handles this well — Traditional level IS the legacy state, and Initial level is the first meaningful step. Agencies don't need to solve legacy systems to start; they need to start solving them.

---

## §5: The ZTMM Framework — Pillars, Levels, and Cross-Cutting Capabilities

### Claim 6: The five-pillar structure provides a comprehensive, independently-assessable decomposition of ZTA

**CISA's claim:** The ZTMM organizes zero trust into five distinct pillars: Identity, Devices, Networks, Applications and Workloads, and Data. "Each pillar can progress at its own pace and may progress more quickly than others until cross-pillar coordination is required."

**Evidence presented:** Each pillar gets its own detailed function table with maturity-level descriptions for each function (e.g., Identity has Authentication, Identity Stores, Risk Assessment, Access Management). The pillar definitions are:

- **Identity** (5.1): "An attribute or set of attributes that uniquely describes an agency user or entity, including non-person entities." Functions: authentication, identity stores, risk assessment, access management.
- **Devices** (5.2): "Any asset (including its hardware, software, firmware, etc.) that can connect to a network." Functions: policy enforcement & compliance monitoring, asset & supply chain risk management, resource access.
- **Networks** (5.3): "An open communications medium including internal networks, wireless networks, and the Internet." Functions: network segmentation, traffic management, traffic encryption, network resilience.
- **Applications and Workloads** (5.4): "Systems, computer programs, and services that execute on-premises, on mobile devices, and in cloud environments." Functions: application access, application threat protection, accessible applications, secure application development and deployment.
- **Data** (5.5): "All structured and unstructured files and fragments... as well as associated metadata." Functions: data inventory management, data categorization, data availability, data access.

**Confidence:** HIGH. The pillar structure is adopted from the ACT-IAC Zero Trust Cybersecurity Current Trends report (2019), which itself derives from Forrester's ZTX framework. It has proven durable — OMB M-22-09 organizes its requirements by the same pillars, and DoD's ZT Strategy uses a compatible (though not identical) decomposition.

**What's at stake:** If the pillars are mutually independent, agencies can optimize investments per pillar. If they're tightly coupled (which the document acknowledges: "cross-pillar coordination is required"), then pillar-by-pillar optimization produces suboptimal architectures. The tension between pillar independence and cross-pillar coordination is the central design challenge of the ZTMM.

**Who disagrees:** NIST 800-207 doesn't use pillars at all — it uses logical components (PE, PA, PEP) and three approach variations. Microsoft's ZT framework uses six pillars (adding Infrastructure). Forrester ZTX uses seven. The exact pillar count is less important than the recognition that ZTA is multi-dimensional.

**Alternative reading:** The five-pillar structure could be seen as artificially decomposing what is fundamentally a unified architecture. The "cross-cutting capabilities" section partially addresses this by providing integration mechanisms, but the pillar-by-pillar maturity tables still encourage siloed assessment.

**My assessment:** The pillar structure is a practical assessment tool, not an architecture specification. It works because it mirrors how federal agencies are organized (IAM team, Network team, AppDev team, etc.), making it actionable for existing organizational structures. The real risk is pillar-level optimization without cross-pillar coordination — the document warns about this but doesn't provide a strong enforcement mechanism.

---

### Claim 7: The four maturity levels define progressive capability from static/manual to dynamic/automated

**CISA's claim:** The four maturity stages are Traditional, Initial, Advanced, and Optimal, each representing "greater levels of protection, detail, and complexity for adoption."

**Evidence presented:** The document provides detailed criteria for each level:

| Level | Key Characteristics |
|-------|-------------------|
| **Traditional** | Manually configured lifecycles; static security policies; pillar-siloed enforcement; least privilege only at provisioning; manual incident response; limited log correlation |
| **Initial** | Starting automation of attribute assignment; initial cross-pillar solutions; some responsive least-privilege changes; aggregated visibility for internal systems |
| **Advanced** | Automated lifecycle controls with cross-pillar coordination; centralized visibility and identity control; policy enforcement integrated across pillars; risk/posture-based least privilege; building toward enterprise-wide awareness |
| **Optimal** | Fully automated, just-in-time lifecycles; self-reporting assets; dynamic policies from automated triggers; dynamic least privilege (just-enough); cross-pillar interoperability with continuous monitoring; centralized comprehensive situational awareness |

**Confidence:** HIGH. The maturity levels are internally consistent and follow a clear progression logic: manual → automated → dynamic. The descriptions are specific enough to be auditable — an assessor can identify which level a function currently occupies.

**What's at stake:** If Optimal is unrealistic (fully automated, just-in-time everything), agencies may view the entire model as aspirational and disengage. The document mitigates this by stating that different pillars can be at different levels — an agency doesn't need Optimal Identity before starting on Devices. But the risk of Optimal as an unattainable "perfect state" is real.

**Who disagrees:** Some practitioners argue that the Traditional → Initial → Advanced → Optimal progression implies a linear path when ZTA adoption is often non-linear — an agency might achieve Advanced in Data but remain Traditional in Devices. The document explicitly permits this ("each pillar can progress at its own pace"), but the four-level progression still visually implies linearity.

**Alternative reading:** The maturity levels could be read as a procurement roadmap rather than a technical assessment — Traditional justifies current spend, Initial justifies first investments, Advanced justifies major programs, and Optimal justifies indefinite sustainment funding. This reading is cynical but not inconsistent with how federal budget cycles work.

**My assessment:** The maturity levels are the most valuable part of the ZTMM because they're specific. "Traditional" for Authentication means "passwords or MFA with static access" — that's testable. "Advanced" means "phishing-resistant MFA with password-less FIDO2/PIV" — also testable. This specificity is what makes the ZTMM actionable where NIST 800-207 is architectural. The risk of Optimal-as-perfect is managed by the document's explicit permission for asynchronous pillar progress.

---

### Claim 8: The three cross-cutting capabilities unify the pillars and prevent siloed maturity

**CISA's claim:** "Visibility and Analytics, Automation and Orchestration, and Governance provide opportunities to integrate advancements across each of the five pillars." These capabilities "highlight activities to support interoperability of functions across pillars."

**Evidence presented:**

- **Visibility and Analytics:** "The observable artifacts that result from the characteristics of and events within enterprise-wide environments. The focus on cyber-related data analysis can help inform policy decisions, facilitate response activities, and build a risk profile to develop proactive security measures before an incident occurs."
- **Automation and Orchestration:** "Zero trust makes full use of automated tools and workflows that support security response functions across products and services while maintaining oversight, security, and interaction of the development process."
- **Governance:** "The definition and associated enforcement of agency cybersecurity policies, procedures, and processes, within and across pillars, to manage an agency's enterprise and mitigate security risks in support of zero trust principles and fulfillment of federal requirements."

Each capability has its own maturity table (Table 7) that progresses from manual/static to automated/dynamic across the four maturity levels.

**Confidence:** HIGH. These three capabilities are well-chosen — they correspond to the three operational dimensions that make ZTA actually work: you need to SEE what's happening (Visibility & Analytics), you need to ACT on what you see (Automation & Orchestration), and you need to GOVERN the whole system (Governance). Without all three, pillar-level maturity produces isolated capabilities that don't integrate.

**What's at stake:** If the cross-cutting capabilities are treated as optional additions to pillar maturity (which the separate Table 7 structure could encourage), agencies achieve check-box compliance without operational integration. The document attempts to prevent this by including cross-cutting capability considerations in each pillar's function tables, but the overall structure still separates them.

**Who disagrees:** Forrester's ZTX framework treats Automation & Orchestration as a separate pillar, not a cross-cutting capability. NIST 800-207 embeds visibility and policy enforcement in the architecture itself (through the Policy Engine and continuous diagnostics). The ZTMM's approach is more operational than architectural — it asks "do you have visibility?" rather than "where in your architecture does visibility live?"

**Alternative reading:** The cross-cutting capabilities could be read as CISA's way of saying "the pillars alone aren't enough — you need integration." This is a hedge against agencies that would otherwise treat the pillars as independent compliance checklists. The separate Table 7 could be seen as CISA giving itself an assessment mechanism for integration quality.

**My assessment:** The cross-cutting capabilities are the most underappreciated part of the ZTMM. In practice, agencies tend to focus on pillar maturity because the function tables are detailed and specific, while the cross-cutting capabilities feel abstract. But an agency with Advanced Identity and Traditional Visibility & Analytics has a gaping hole — it's authenticating users but can't see what they're doing. The cross-cutting capabilities deserve equal weight in assessment, and the document would benefit from making this expectation more explicit.

---

### Claim 9: The ZTMM operationalizes all seven NIST 800-207 tenets into measurable capabilities

**CISA's claim:** "This model reflects the seven tenets of zero trust as outlined in NIST SP 800-207." The document reproduces all seven tenets verbatim and maps the maturity model structure to them.

**Evidence presented:** The seven tenets are listed explicitly (lines 257-267):

1. All data sources and computing services are considered resources.
2. All communication is secured regardless of network location.
3. Access to individual enterprise resources is granted on a per-session basis.
4. Access to resources is determined by dynamic policy.
5. The enterprise monitors and measures the integrity and security posture of all owned and associated assets.
6. All resource authentication and authorization are dynamic and strictly enforced before access is allowed.
7. The enterprise collects as much information as possible about the current state of assets, network infrastructure, and communications and uses it to improve its security posture.

The mapping is implicit (the document doesn't provide a tenet-to-pillar matrix), but the alignment is clear: Tenet 1 → Data pillar; Tenet 2 → Networks pillar; Tenet 3 → Identity + Applications pillars; Tenet 4 → all pillars via cross-cutting capabilities; Tenet 5 → Devices pillar; Tenet 6 → Identity pillar; Tenet 7 → Visibility and Analytics cross-cutting capability.

**Confidence:** HIGH. The tenets are directly quoted and the ZTMM structure demonstrably covers them. What the ZTMM adds is NOT the tenets themselves but the operationalization: NIST says "access is determined by dynamic policy" (aspirational); the ZTMM says "at Advanced level, policy is automated with cross-pillar coordination; at Optimal, policy is fully dynamic based on automated triggers" (measurable).

**What's at stake:** If the ZTMM fails to cover a tenet, there's a gap in the federal ZTA assessment framework. If it covers all tenets but some are weaker than others, agencies will under-invest in those areas. The implicit mapping (no explicit tenet-to-function traceability) creates audit risk — an agency could claim compliance without demonstrating tenet coverage.

**Who disagrees:** No one disagrees that the seven tenets are the right foundation. The debate is over whether a maturity model is the right way to assess compliance with them. NSA prefers a threat-model-driven assessment ("does your architecture stop this attack pattern?"), while CISA prefers a capability-driven assessment ("do you have phishing-resistant MFA?"). Both approaches can cover the same tenets.

**Alternative reading:** The ZTMM's claim to reflect all seven tenets could be read as aspirational — it covers them at the framework level, but the specific function tables may not fully address every tenet. For example, Tenet 3 (per-session access) is partially covered by Identity's Access Management function, but per-session access to individual resources (as opposed to per-session authentication) isn't a distinct function in any pillar.

**My assessment:** The ZTMM successfully operationalizes the tenets, but the mapping is imperfect. The framework would benefit from an explicit tenet-to-function traceability matrix, which would make gaps visible and closeable. In its absence, agencies should perform this mapping themselves as part of their ZTA planning. The implicit coverage is good enough for assessment purposes but not rigorous enough for auditing.

---

## Framework Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| 1: ZTMM is a compliance instrument for EO 14028 | VERY HIGH | A court ruling that EO 14028's ZTA requirement is not enforceable |
| 2: Recent incidents made perimeter-based security indefensible | VERY HIGH | A major ZTA breach that shows ZTA is equally vulnerable |
| 3: ZTMM inherits NIST 800-207's definition without modification | VERY HIGH | NIST revising the operative definition; current definition is from 2020 |
| 4: ZTA requires a fundamental shift from location-centric to identity/data-centric | HIGH | Evidence that most agencies achieve adequate security without full cultural transformation |
| 5: Legacy implicit-trust systems are the primary obstacle | HIGH | Successful ZTA implementations that bypass rather than migrate legacy systems |
| 6: Five-pillar structure provides comprehensive, independently-assessable decomposition | HIGH | Evidence that pillar-level optimization produces worse outcomes than holistic ZTA |
| 7: Four maturity levels define progressive capability from static/manual to dynamic/automated | HIGH | Optimal proving unattainable → model loses credibility as assessment tool |
| 8: Cross-cutting capabilities unify pillars and prevent siloed maturity | HIGH | Agencies treating cross-cutting capabilities as optional → pillar silos persist |
| 9: ZTMM operationalizes all seven NIST tenets into measurable capabilities | HIGH | Missing explicit tenet-to-function mapping → audit gaps |

**Strongest section:** §5 (The ZTMM Framework) — the four maturity levels are the ZTMM's unique contribution. They're specific, testable, and provide a concrete bridge between NIST's aspirational tenets and agency procurement. No other federal guidance provides this level of operational specificity.

**Weakest section:** §4 (Challenges) — the challenges section is brief and generic. It identifies real problems (legacy systems, siloed teams, varied starting points) but doesn't provide specific mitigation strategies. The framework itself addresses these challenges implicitly (maturity levels accommodate varied starting points; cross-cutting capabilities address silos), but the Challenges section doesn't make these connections explicit.

**Key structural observation:** The ZTMM is an assessment framework, not an architecture specification. It tells you WHAT capabilities to measure, not HOW to build them. This is both its strength (technology-agnostic, durable) and its limitation (agencies still need reference architectures to guide implementation). The implicit assumption is that agencies will use NIST 800-207's component model (PE, PA, PEP) for architecture and the ZTMM for maturity assessment — but the document doesn't make this division of labor explicit, which creates a risk that agencies use the ZTMM as both, leading to pillar-optimized architectures without a coherent component model.

**Unanswered question:** What happens when an agency reaches Optimal across all pillars? The document doesn't define a post-Optimal state or a maintenance mode. The federal ZTA journey is framed as having an endpoint (Optimal), but practical ZTA is continuous — new threats, new technologies, and new attack surfaces mean the "Optimal" target moves. Future versions of the ZTMM should either define Optimal as an evolving target or add a fifth level for continuous adaptation.
