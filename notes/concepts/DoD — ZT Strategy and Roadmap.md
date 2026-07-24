---
tags:
  - source/standards
  - dod
  - zt-strategy
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
confidence: high
source:
  title: "DoD Zero Trust Strategy"
  author: "DoD CIO Zero Trust Portfolio Management Office"
  year: 2022
  date: "October 21, 2022"
  local_file: "sources/standards/_txt/DoD_ZT_Strategy_Roadmap.txt"
related:
  - "[[NIST 800-207 — Ch1 — Introduction]]"
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[NSTAC — ZT and Trusted Identity Management]]"
  - "[[Concepts Index]]"
---

# DoD — Zero Trust Strategy and Roadmap

The Department of Defense's first enterprise-wide Zero Trust strategy, issued October 2022, defines the Department's vision for achieving ZT across the DoD Information Enterprise by FY2027. Distinct from the DoD Zero Trust Reference Architecture (which specifies technical design tenets), the Strategy addresses the full spectrum of Doctrine, Organization, Training, Materiel, Leadership and Education, Personnel, Facilities, and Policy (DOTmLPF-P) — recognizing that ZT is a cultural transformation as much as a technical one. The Strategy is orchestrated by the ZT Portfolio Management Office (PfMO), established January 2022 under DoD CIO, and provides the framework for Component-level execution plans, resource prioritization, and accountability.

---

## Claim 1: Zero Trust is not an IT solution or product — it requires cultural transformation across the entire Department, not just the cybersecurity workforce.

**DoD's claim:** "Zero Trust is much more than an IT solution. Zero Trust may include certain products but is not a capability or device that may be bought. The journey to Zero Trust requires all DoD Components to adopt and integrate Zero Trust capabilities, technologies, solutions, and processes across their architectures, systems, and within their budget and execution plans. Perhaps most importantly, they must also address Zero Trust requirements within their staffing, training, and professional development processes as well."

**Evidence presented:** The Strategy structures itself around DOTmLPF-P — the full scope of military organizational change — not just technical capabilities. The first of four strategic goals is "Zero Trust Cultural Adoption," prioritized alongside technical goals. The Foreword explicitly states: "'never trust, always verify' mindset requires us to take responsibility for the security of our devices, applications, assets, and services; users are granted access to only the data they need and when needed. We all must play a role."

**Confidence:** HIGH. This aligns with every major ZT framework (NIST SP 800-207, CISA Maturity Model) that emphasizes culture over technology. The DoD's DOTmLPF-P framing is unique among federal ZT documents and makes the cultural requirement institutionally legible to military audiences.

**What's at stake:** If ZT is treated as a technology procurement exercise, it fails. The DoD's explicit framing of culture as Goal 1 — before securing systems (Goal 2) or accelerating technology (Goal 3) — signals that culture is prerequisite, not afterthought.

**My assessment:** The DoD's cultural framing is the Strategy's most distinctive and institutionally sophisticated contribution. By embedding ZT in DOTmLPF-P, the Strategy speaks the language of military organizational change — making culture change auditable through doctrine updates, training requirements, and personnel standards rather than just "awareness campaigns." This is a more rigorous approach to culture than any civilian federal ZT document.

---

## Claim 2: The seven DoD ZT Pillars (User, Device, Applications/Workloads, Data, Network/Environment, Automation/Orchestration, Visibility/Analytics) provide the organizing construct for all ZT capabilities, with Data at the center.

**DoD's claim:** "Zero Trust capabilities across the IE must be developed, deployed, and operated within an organizing construct defined by seven DoD Zero Trust Pillars... These pillars provide the foundational areas for the DoD Zero Trust Security Model and the DoD Zero Trust Architecture. All capabilities within the Pillars must work together in an integrated fashion to secure effectively the Data Pillar, which is central to the model."

**Evidence presented:** Each pillar has specific capability outcomes that Components must achieve. The pillars are directly inherited from the DoD ZT Reference Architecture v2.0 and map to the CISA ZT Maturity Model's five pillars plus cross-cutting enablers (Visibility & Analytics, Automation & Orchestration). The Strategy also identifies execution enablers — cross-cutting, non-technical capabilities addressing culture, governance, and DOTmLPF-P elements.

**Confidence:** HIGH. These seven pillars are institutionally consistent with the DoD ZT RA and CISA's framework. The centrality of Data is consistent with NIST's resource-centric approach.

**What's at stake:** The pillar structure determines how Components organize their ZT execution plans and procurement. Misalignment between Component plans and the seven-pillar framework would fragment DoD's ZT efforts.

**My assessment:** The seven-pillar model is a pragmatic evolution of the five-pillar CISA model. The addition of Automation/Orchestration and Visibility/Analytics as standalone pillars (rather than cross-cutting enablers) gives them institutional weight and dedicated funding lines. The Data-centric model is theoretically correct but practically the hardest pillar to execute — data tagging, labeling, and encryption at DoD scale is enormously complex.

---

## Claim 3: Target Level ZT must be achieved by end of FY2027 as the minimum security baseline; Advanced ZT represents the next-generation adaptive security state.

**DoD's claim:** "The Target Level ZT is the minimum set of ZT capability outcomes and activities necessary to secure and protect the Department's DAAS to manage risks from currently known threats... With the Target Level achieved, the ZT PfMO will monitor continued compliance and guide movement to Advanced ZT as current risks are mitigated."

**Evidence presented:** The Strategy defines two maturity tiers: Target Level (the mandatory minimum, achieved by FY2027) and Advanced ZT (adaptive responses, continuous refinement). Appendices A–C map capabilities and activities to pillars by fiscal year. The Strategy acknowledges that "reaching an 'advanced' state does not mean an end to maturing ZT; instead, protection of attack surfaces will continue to adapt and refine."

**Confidence:** HIGH that the two-tier model is the official approach. MEDIUM on whether all Components will achieve Target Level by FY2027 given the historical pace of DoD IT modernization — the Strategy itself provides a waiver process for legacy systems that cannot comply.

**What's at stake:** Target Level defines the mandatory bar. Components that fail to meet it create systemic vulnerability across the DoD Information Enterprise. The waiver process for legacy systems is a necessary escape valve but risks creating a two-tier security posture.

**My assessment:** The Target/Advanced distinction solves a real problem — how to mandate progress while acknowledging differential starting points. However, the Strategy's "as soon as possible" language for Target Level is deliberately flexible. The FY2027 deadline for Target Level gives Components five years, which is ambitious but not unreasonable for the largest IT enterprise in the world. The real risk is that legacy systems — which "may not require or justify immediate ZT retrofit" — become permanent exceptions rather than temporary ones.

---

## Claim 4: The four strategic goals (Cultural Adoption, Systems Secured/Defended, Technology Acceleration, Zero Trust Enablement) address the full lifecycle of ZT transformation from mindset to sustainment.

**DoD's claim:** "These goals are synergistic and address the cultural, technological, and environmental requirements for the successful adoption and implementation of ZT."

**Evidence presented:**

| Goal | Focus | Key Deadline |
|------|-------|-------------|
| **1: ZT Cultural Adoption** | Mindset, training, workforce development, outreach | FY2023–FY2025 |
| **2: DoD Information Systems Secured & Defended** | All seven pillar capabilities; Component execution plans | Execution plans by Sep 2023; Target Level by end FY2027 |
| **3: Technology Acceleration** | Deploy at pace equal/exceeding industry; architecture alignment; interoperability | FY2023–FY2027 |
| **4: Zero Trust Enablement** | Policy, planning, programming, funding, acquisition, performance metrics | FY2023–FY2027 |

Each goal has measurable SMART objectives. Goal 4 is explicitly framed as the "tail" to the ZT "tooth" — the sustainment infrastructure without which technical ZT cannot succeed.

**Confidence:** HIGH. The four-goal structure is comprehensive and internally consistent. The explicit recognition of Goal 4 (Enablement) — funding, acquisition, policy integration — addresses the most common failure mode of ZT initiatives: under-resourcing the sustainment tail.

**What's at stake:** Goal 4 is the most politically difficult because it requires reprogramming DoD budget processes (PPBE) and acquisition strategies. Without it, Goals 2–3 become unfunded mandates.

**My assessment:** The Enablement goal is the Strategy's most honest acknowledgment of ZT's institutional challenge. "This goal identifies the 'tail' to the ZT 'tooth,' the latter being unable to achieve its mission without the former, and requires the whole of the ZT Ecosystem's attention and effort and cannot be addressed 'at a later time'" — this is the sentence every DoD Component leader needs to read. The Strategy's governance structure (ZT PfMO under DoD CIO, reporting to the DoD Cyber Council) provides clear accountability but depends on sustained senior leader attention.

---

## Claim 5: The Strategy is explicitly NOT a solution architecture — Components retain freedom to choose technologies as long as they deliver specified capability outcomes.

**DoD's claim:** "This ZT strategy does not mandate or prescribe specific technologies or potential solutions. Rather, it describes all the ZT capabilities that must be implemented to reach both the Target and Advanced Level ZT. The Components are free to select their own solutions and solution architectures, as long as they deliver the specified ZT Capability outcomes."

**Evidence presented:** The Strategy is explicitly differentiated from the DoD ZT Reference Architecture v2.0 and the DoD Cybersecurity Reference Architecture v4.2. The Capability Roadmap defines outcomes, not technologies. Components must show proof of capability achievement to their Authorizing Official and/or the ZT PfMO.

**Confidence:** HIGH. This is consistent with DoD acquisition doctrine and the Strategy's role as a strategy document rather than a technical specification.

**What's at stake:** Outcome-based rather than technology-prescriptive guidance enables innovation and Component-specific solutions. But it also creates the risk of inconsistent implementation quality — two Components could both claim a capability outcome is "achieved" with very different actual security postures. The ZT PfMO's verification role is critical.

**My assessment:** The outcome-based approach is the right one at DoD scale. Prescribing specific technologies across Components as diverse as the Army, Navy, Air Force, and Defense Agencies would be unworkable and rapidly obsolete. The risk is in verification — without standardized testing of capability outcomes, the Target Level becomes a self-certification exercise. The Strategy's mention of Red Teaming and Operational Test & Evaluation (OT&E) suggests awareness of this risk, but verification mechanisms remain under-specified.

---

## Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| 1: ZT requires cultural transformation, not just technology | HIGH | Components treating ZT as an IT project rather than DOTmLPF-P change |
| 2: Seven pillars with Data at center organize all ZT capabilities | HIGH | Pillar fragmentation if Components optimize individual pillars without integration |
| 3: Target Level by FY2027; Advanced ZT thereafter | HIGH (framework) / MEDIUM (FY2027 feasibility) | Permanent legacy system waivers undermining universal coverage |
| 4: Four strategic goals cover the full ZT lifecycle | HIGH | Goal 4 (Enablement) being under-resourced relative to Goals 2–3 |
| 5: Outcome-based, not technology-prescriptive | HIGH | Self-certification without rigorous verification of capability outcomes |

**Strongest sections:**
- **Cultural framing via DOTmLPF-P** — Unique among federal ZT documents; speaks the language of military organizational change; makes culture auditable.
- **Four-goal structure with explicit Enablement** — Honest about the institutional tail required; Goal 4 preempts the "unfunded mandate" problem.
- **Target/Advanced two-tier maturity** — Provides a clear, time-bound target while acknowledging continuous evolution beyond it.

**Weakest sections:**
- **Verification mechanisms** — How the ZT PfMO will verify that Components have achieved Target Level capability outcomes is under-specified.
- **Legacy system waiver process** — The annual waiver requirement is stated but the criteria for approval are deferred ("pre-defined set of standards"), creating ambiguity.
- **Coalition interoperability** — The Strategy mentions mission partner environments and coalition warfare but provides limited specifics on how ZT will interoperate with non-DoD partners.

**Unique contribution to OSKG-ZeroTrust:**
The DoD ZT Strategy is the only document in the federal ZT canon that:
1. **Frames ZT as a DOTmLPF-P transformation** — Making culture, doctrine, training, and personnel as central as technology.
2. **Establishes a dedicated Portfolio Management Office** — The ZT PfMO provides institutional continuity that civilian agencies lack (NSTAC's report specifically recommends CISA create an equivalent civilian office).
3. **Provides a five-year Capability Roadmap with fiscal year milestones** — More granular and time-bound than OMB's Federal ZT Strategy (which covers only FY2024).
4. **Explicitly links ZT to warfighter mission outcomes** — Including tactical environments, coalition warfare, and JADC2 — a framing absent from civilian ZT documents.

**Comparison with related notes:**
- **vs. NIST 800-207:** NIST defines the architectural principles; DoD operationalizes them at enterprise scale with a specific timeline and governance structure. NIST is abstract; DoD is institutional.
- **vs. NSTAC Report:** NSTAC recommends civilian governance structures (CISA Program Office, ZT-FISMA alignment). The DoD Strategy is a case study of what NSTAC recommends — it already has a Program Office (PfMO), a maturity model (Target/Advanced), and accountability mechanisms.
- **vs. OMB M-22-09 (Federal ZT Strategy):** OMB covers FY2022–FY2024 for civilian agencies. DoD extends to FY2027 with more comprehensive scope (all seven pillars vs. five) and deeper institutional integration (PPBE, acquisition, DOTmLPF-P).

**Open Questions:**
- Will the ZT PfMO develop robust verification mechanisms beyond Component self-reporting?
- How will the waiver process for legacy systems prevent permanent exceptions?
- How will ZT principles apply in tactical/disconnected environments where continuous cloud connectivity is unavailable?
- Will the FY2027 Target Level deadline survive the next National Defense Authorization Act cycle and potential changes in administration priorities?
