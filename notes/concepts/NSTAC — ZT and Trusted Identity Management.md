---
tags:
  - source/standards
  - nstac
  - zt-identity
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
confidence: high
source:
  title: "NSTAC Report to the President: Zero Trust and Trusted Identity Management"
  author: "President's National Security Telecommunications Advisory Committee"
  year: 2022
  date: "February 23, 2022"
  local_file: "sources/standards/_txt/NSTAC_Report_ZT_Trusted_Identity_Management.txt"
related:
  - "[[NIST 800-207 — Ch1 — Introduction]]"
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[DoD — ZT Strategy and Roadmap]]"
  - "[[Concepts Index]]"
---

# NSTAC — Zero Trust and Trusted Identity Management

The President's National Security Telecommunications Advisory Committee (NSTAC) report to the President on Zero Trust and Trusted Identity Management (February 2022) is the most comprehensive industry-to-government advisory document on federal Zero Trust adoption. Commissioned in the aftermath of EO 14028 and the SolarWinds/Colonial Pipeline incidents, the report makes 14 recommendations — including 9 key priority actions — organized across three domains: federal implementation barriers/enablers, governance and institutionalization, and incentivizing non-federal ZT adoption. Its central thesis is that without sustained, institutionalized commitment measured in decades (not the 2½-year horizon of OMB's Federal ZT Strategy), ZT risks becoming "an incomplete experiment — a collection of disjointed technical security projects measured in years — rather than the foundation of an enduring, coherent, and transformative strategy measured in decades."

---

## Claim 1: The Federal Government's current 2½-year ZT strategy is appropriately scoped for jump-starting action but insufficient for long-term transformation — absent additional institutionalization, ZT will fail.

**NSTAC's claim:** "Current U.S. Government policies such as the Federal Zero Trust Strategy are well grounded in industry best practices but deliberately restrained in scope to cover directed actions over just a 2½-year period. This short-term focus is appropriate, as many federal agencies are early in their zero trust journeys and need to be accountable to concrete, short-term actions to build momentum. However, absent additional significant action, the U.S. Government risks zero trust becoming an incomplete experiment — a collection of disjointed technical security projects measured in years — rather than the foundation of an enduring, coherent, and transformative strategy measured in decades."

**Evidence presented:** The report acknowledges that the Federal ZT Strategy's specific actions (e.g., "identify at least one internal-facing FISMA Moderate application and make it fully operational and accessible over the public internet") are necessary for momentum. But it argues that "over-focusing on near-term tactical goals can distract from the big-picture cultural shift that zero trust requires for long-term, sustained impact." The report distinguishes between "achievement of action-oriented goals" and genuine institutional transformation.

**Confidence:** HIGH. This diagnosis is validated by the history of federal cybersecurity initiatives that became checkbox compliance exercises (FISMA reporting is the canonical example). The NSTAC's institutional memory — its members have witnessed these patterns across administrations — gives this claim weight.

**What's at stake:** If the NSTAC is right, the OMB strategy's FY2024 deadline will produce a flurry of activity followed by atrophy. If wrong (i.e., the short-term actions catalyze self-sustaining momentum), additional institutionalization is unnecessary overhead. The NSTAC's bet is that without structural changes, ZT becomes "just another new federal requirement."

**My assessment:** This is the report's most important warning and its unifying thesis. It reframes the entire ZT conversation from "what should agencies do by FY2024?" to "what must be done NOW to ensure ZT survives the FY2024 deadline?" The report's 14 recommendations are all answers to this question — they are institutionalization mechanisms, not technical guidance. The warning is particularly acute given that the OMB strategy's own language calls itself "a starting point, not a comprehensive guide to a fully mature zero trust architecture."

---

## Claim 2: Industry best practices — the Five-Step Process and the Kipling Method — should be the basis for federal ZT accountability metrics, not just technical checkbox completion.

**NSTAC's claim:** "Rather than propose technical success metrics, NSTAC strongly encourages federal agencies to reference the industry best-practice models in Section 2. These process-oriented principles, if firmly rooted in federal organizations after 2½ years, will be the best predictor of long-term success and sustained commitment to zero trust."

**Evidence presented:** The report maps the Five-Step Process (Define Protect Surface → Map Transaction Flows → Build ZT Architecture → Create ZT Policy → Monitor and Maintain) to quantifiable progress metrics with reporting requirements at the agency CISO level or above:

| Step | Quantifiable Metric |
|------|-------------------|
| 1. Define Protect Surface | Organizational inventory of total DAAS elements on the ZT roadmap |
| 2. Map Transaction Flows | Percentage of instrumented and validated traffic flows |
| 3. Build ZT Architecture | Percentage of DAAS elements protected by an enforcement point |
| 4. Create ZT Policy | Percentage of DAAS elements protected by a defined ZT policy |
| 5. Monitor and Maintain | Month-over-month true/false positive percentages for security incidents |

An additional sixth tenet — "Commit to Transparency and Continuous Improvement" — requires each agency to publish at least one ZT use case annually documenting implementation lessons learned.

**Confidence:** HIGH on the validity of the Five-Step Process as an industry standard. MEDIUM on whether federal agencies can meaningfully produce the quantifiable metrics without significant investment in asset discovery and instrumentation first.

**What's at stake:** Process-based metrics prevent ZT from being reduced to a technology procurement checklist. But they require agencies to have basic visibility of their assets — something the report itself acknowledges many agencies lack: "some federal agencies... lack basic visibility of the data, assets, applications, and services in their organization, and as a result, are not yet ready to begin their zero trust journey."

**My assessment:** The Five-Step Process metrics are the right kind of metrics — they measure progress on the journey, not arrival at a destination. The inclusion of "month-over-month true/false positive percentages" as a feedback loop metric is sophisticated: it measures whether ZT policies are actually improving security outcomes, not just whether they exist. The transparency tenet (annual use case publication) is a clever institutionalization mechanism — it creates peer pressure and shared learning across agencies.

---

## Claim 3: Governance is the critical gap — the Federal Government must integrate ZT into existing structures (FISMA, CDM, NIST 800-53, procurement) rather than treating it as a standalone initiative.

**NSTAC's claim:** "To realize zero trust as a true strategy that meaningfully transforms cybersecurity outcomes over the next decade and beyond, the U.S. Government must take a series of policy actions now to institutionalize a culture of zero trust. Zero trust principles must be fully integrated into existing and new federal governance structures, policies, and programs and not be viewed as a standalone initiative."

**Evidence presented:** The report identifies several specific governance integration gaps:

1. **FISMA/NIST 800-53 Mapping Gap:** Agencies may see ZT as conflicting with FISMA compliance — which carries penalty potential — if the alignment is not clarified. NSTAC recommends OMB issue a memo mapping ZT to NIST 800-53 controls and task NIST with a dedicated special publication.

2. **CDM Program Alignment Gap:** The Continuous Diagnostics and Mitigation program is "the vehicle by which most federal agencies have procured and implemented core capabilities that help form a foundation for achieving zero trust." But the alignment is not explicit.

3. **Procurement Vehicle Gap:** Federal acquisition vehicles must broaden scope to support the full ZT lifecycle (strategy, architecture, DevSecOps, operations) rather than point-solution procurement.

4. **Budget Process Gap:** ZT requires multi-year funding flexibility; annual appropriations cycles are misaligned with multi-year ZT journeys.

**Confidence:** VERY HIGH. This is the report's strongest and most actionable claim. The governance integration argument is the bridge between "ZT is important" and "ZT will actually happen."

**What's at stake:** Without FISMA alignment, ZT competes with compliance requirements for agency attention — and compliance always wins because it carries penalty risk. Without CDM alignment, agencies have no procurement path. Without budget process reform, ZT initiatives get defunded in annual appropriations cycles.

**My assessment:** The governance integration recommendations are the most politically sophisticated part of the report. They recognize that in federal bureaucracy, what gets measured (FISMA), what gets funded (CDM/procurement), and what gets penalized (compliance) are the real drivers of behavior. The recommendation to "keep [ZT] from being seen as just another new federal requirement by integrating its principles into existing workstreams" is the single most important sentence in the report for practitioners.

---

## Claim 4: The Federal Government needs two dedicated ZT Program Offices — a Civilian Office (at CISA) and coordination with the existing Defense Office (at DoD) — to provide sustained institutional capacity.

**NSTAC's claim:** "CISA should establish a dedicated Zero Trust Program Office for federal civilian agencies to host implementation guidance, reference architectures, capability catalogs, training modules, and generally serve as a civilian government knowledge management center of excellence for zero trust."

**Evidence presented:** The report notes that "CISA's zero trust-relevant guidance and shared service offerings are not centrally located in a way that is conducive to civilian agency access." It also recommends the civilian office coordinate with the DoD ZT Program Office (already established in fall 2021) on: a single set of ZT pillars, a common lexicon, joint federal milestones, and a unified maturity measurement method.

**Confidence:** HIGH on the need for institutional capacity. The DoD had already created its PfMO by the time of this report (January 2022); the NSTAC is essentially recommending civilians get the same capability.

**What's at stake:** Without a dedicated program office, ZT guidance fragments across CISA divisions, no single entity owns the civilian ZT journey, and agency CISOs have no single point of contact for ZT implementation support. The DoD's PfMO provides a proven model.

**My assessment:** This recommendation was partially vindicated — CISA did release a ZT Maturity Model and has increased ZT guidance, but a dedicated "Civilian Zero Trust Program Office" as the NSTAC envisioned remains a work in progress. The coordination recommendation between civilian and defense offices is particularly important: without it, the federal government develops two ZT ecosystems that can't interoperate, defeating the purpose of a "whole-of-government" approach.

---

## Claim 5: Internet-accessible asset discovery is a foundational prerequisite for ZT that many agencies lack — CISA should provide it as a shared service.

**NSTAC's claim:** "A fundamental prerequisite to zero trust is a comprehensive understanding of critical systems and their exposures to determine where to enforce zero trust policies in a risk-prioritized manner. CISA can empower civilian agency zero trust implementation through a shared services offering for this type of internet-accessible asset discovery capability."

**Evidence presented:** The report quotes the Federal ZT Strategy itself: "To effectively implement a zero trust architecture, an organization must have a complete understanding of its internet-accessible assets." It recommends the shared service provide "continuous and dynamic asset mapping as static data pulls will have limited utility in a constantly evolving threat environment."

**Confidence:** VERY HIGH. Asset discovery is genuinely prerequisite — you can't protect what you don't know you have. CISA is the natural provider given its existing .gov scanning authority and CDM program infrastructure.

**What's at stake:** Agencies that don't know their internet-accessible attack surface cannot begin ZT. A shared service lowers the barrier for under-resourced agencies. Without it, ZT becomes a capability only available to well-resourced agencies — widening the federal cybersecurity gap.

**My assessment:** This is the report's most concrete and immediately actionable recommendation. It identifies a specific capability gap (internet-accessible asset discovery), a specific provider (CISA), and a specific mechanism (shared service). The requirement for "continuous and dynamic" rather than "static" discovery is sophisticated — static asset inventories are obsolete the moment they're completed.

---

## Claim 6: The U.S. Government must incentivize non-federal ZT adoption through grants, procurement preferences, international standards, and regulatory relief — not just lead by example.

**NSTAC's claim:** The U.S. Government has "broad opportunity and responsibility to help catalyze cybersecurity transformation through zero trust adoption" beyond the federal enterprise — including state/local/tribal/territorial governments and critical infrastructure.

**Evidence presented:** Specific mechanisms recommended:

1. **Grant funding:** CISA should prioritize ZT projects in the $1B State and Local Cybersecurity Improvement Act (IIJA) funding through 2026. Transportation, Commerce, and Energy secretaries should require "sound cybersecurity practices" (including ZT) as condition of infrastructure funding.

2. **International standards:** NIST should lead a "multi-year path to advance zero trust within international standards bodies" — evolving guidelines into consensus-based international standards, following the NIST Cybersecurity Framework model.

3. **Procurement preferences:** Consider federal procurement preferences for vendors/products demonstrating ZT alignment.

4. **Regulatory relief:** Consider regulatory relief actions for entities that adopt ZT principles.

**Confidence:** HIGH on the strategic importance. MEDIUM on the political feasibility of using infrastructure funding conditions for ZT — this would face industry pushback.

**What's at stake:** Federal ZT adoption alone doesn't protect the broader national ecosystem. Critical infrastructure, state/local governments, and the defense industrial base all need ZT adoption. The IIJA's $1B in state/local cybersecurity grants is a once-in-a-generation funding opportunity.

**My assessment:** The international standards recommendation is the most strategically significant — it positions ZT as an exportable U.S. cybersecurity framework in the model of the NIST Cybersecurity Framework, which has been adopted globally. The infrastructure funding condition recommendation is politically ambitious but logically consistent: if the federal government is funding infrastructure, it should require baseline cybersecurity. The report's acknowledgment that ZT must not become a "regulatory burden" shows sophisticated awareness of industry concerns.

---

## Claim 7: Technology interoperability is the hidden risk — without component-level interface standards, ZT creates vendor lock-in and "a proliferation of multiple solutions [that] increases management complexity."

**NSTAC's claim:** "The lack of interoperability-focused standards for zero trust technologies could negatively impact Zero Trust deployment efforts in the long term if not properly addressed. Existing zero trust guidelines such as NIST SP 800-207 provide the necessary high-level framework for deploying zero trust-based systems, but do not address the component-level interfaces needed to enable true plug-and-play of multi-vendor zero trust solutions."

**Evidence presented:** The report observes that the "noisy" private sector security market has many vendors "re-branding technologies to narrowly apply to one discrete function of a comprehensive zero trust architecture." The burden of manual integration is "too often placed on the end user," creating friction that disincentivizes progressive ZT adoption. The report recommends NIST's NCCoE produce a special publication documenting where interoperability breaks down in the ZT technology ecosystem.

**Confidence:** HIGH. This is a genuine risk validated by the history of enterprise security products (SIEM integration, SOAR playbooks). The NCCoE is the right entity to assess this.

**What's at stake:** Without interoperability standards, agencies become locked into single-vendor ZT stacks, defeating the "best-in-class" promise of componentized ZT architectures. Integration friction slows adoption and creates brittle, hard-to-maintain security postures.

**My assessment:** The interoperability warning is the report's most technically astute observation. While NIST SP 800-207 defines the logical components (PDP, PEP, etc.), it doesn't specify how they communicate — the API contracts, data formats, and protocols that would enable multi-vendor integration. The report's call for component-level interface standardization anticipates a problem that will become acute as ZT deployments mature and agencies seek to swap or upgrade individual components.

---

## Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| 1: 2½-year strategy is necessary but insufficient without institutionalization | HIGH | OMB strategy's short-term actions catalyzing self-sustaining momentum |
| 2: Five-Step Process metrics should drive federal ZT accountability | HIGH (validity) / MEDIUM (federal capacity) | Agencies lacking basic asset visibility to produce the metrics |
| 3: Governance integration (FISMA, CDM, procurement) is the critical gap | VERY HIGH | Bureaucratic resistance to changing existing compliance/ procurement frameworks |
| 4: Dedicated Civilian ZT Program Office needed at CISA | HIGH | CISA resource constraints; mission overlap with existing divisions |
| 5: Internet-accessible asset discovery is a foundational prerequisite | VERY HIGH | CISA's scanning authority limitations; agency resistance to external scanning |
| 6: Non-federal ZT incentivization through grants/standards/procurement | HIGH (strategy) / MEDIUM (politics) | Industry pushback on ZT conditions for infrastructure funding |
| 7: Technology interoperability requires component-level interface standards | HIGH | Vendor resistance to interoperability standards that commoditize products |

**Strongest sections:**
- **Governance integration thesis (Claim 3)** — The report's most actionable insight: ZT must be embedded in FISMA, CDM, NIST 800-53, and procurement, not treated as standalone. This is the difference between sustainable transformation and a temporary initiative.
- **Five-Step Process with quantifiable metrics (Claim 2)** — Provides a concrete, industry-validated accountability framework that goes beyond "have you deployed MFA yet?"
- **Asset discovery as prerequisite (Claim 5)** — Identifies a specific, solvable capability gap with a specific provider (CISA) and mechanism (shared service).

**Weakest sections:**
- **Technology capability descriptions (Section 2.2)** — The 5G example is interesting but not representative of most federal agency environments. The report's deliberate refusal to advocate specific technologies is principled but leaves practitioners without concrete procurement guidance.
- **Trusted Identity Management depth** — Despite being in the report's title, identity management receives less attention than governance and institutionalization. The report focuses more on "how to sustain ZT as a strategy" than "how to implement trusted identity management specifically."

**Unique contribution to OSKG-ZeroTrust:**
The NSTAC Report is the only document in the federal ZT canon that:
1. **Explicitly warns that ZT will fail without institutionalization beyond the FY2024 deadline** — A direct, unambiguous challenge to OMB's short-horizon approach.
2. **Provides a process-based accountability framework (Five-Step Process + Kipling Method)** — More sophisticated than checklist compliance; measures journey progress rather than destination arrival.
3. **Recommends a complete governance integration pathway** — FISMA mapping, CDM alignment, procurement reform, budget process adaptation — the institutional "plumbing" without which ZT is just another policy memo.
4. **Identifies technology interoperability as a strategic risk** — The call for component-level interface standards is technically prescient and politically difficult (vendors benefit from lock-in).
5. **Extends ZT incentivization beyond federal boundaries** — IIJA grants, international standards, procurement preferences — recognizes that federal ZT alone doesn't secure the national ecosystem.

**Comparison with related notes:**
- **vs. DoD ZT Strategy:** The DoD Strategy is an execution document (what DoD will do by FY2027). The NSTAC Report is an advisory document (what the entire federal government should do, including civilian agencies, over the next decade). The NSTAC's recommendation for a Civilian ZT Program Office mirrors the DoD's already-existing PfMO.
- **vs. NIST 800-207:** NIST defines the architecture; NSTAC defines the governance and institutionalization required to make that architecture real across 100+ federal agencies with vastly different maturity levels.
- **vs. OMB M-22-09:** OMB provides the tactical 2½-year plan; NSTAC provides the strategic critique that the tactical plan is necessary but insufficient — and recommends exactly what must be added to prevent ZT from becoming "an incomplete experiment."

**Open Questions:**
- Has CISA established a dedicated Civilian ZT Program Office as recommended? (The report's publication date predates current CISA organizational structure.)
- Has NIST produced the recommended SP 800-53-to-ZT mapping special publication?
- How many of the 14 recommendations have been implemented vs. remain aspirational?
- Did the IIJA state/local cybersecurity grants actually prioritize ZT projects?
- Has component-level interface standardization for ZT technologies progressed at NCCoE?
