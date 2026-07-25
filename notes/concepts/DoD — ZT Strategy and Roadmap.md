---
tags:
  - source/standards
  - dod
  - zt-strategy
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
claims_status: extracted
claims_extracted: 2026-07-24
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
  - topic/zt-governance
  - topic/zt-migration
  - topic/zt-architecture
---

# DoD — Zero Trust Strategy and Roadmap

The Department of Defense's first enterprise-wide Zero Trust strategy, issued October 2022, defines the Department's vision for achieving ZT across the DoD Information Enterprise by FY2027. Distinct from the DoD Zero Trust Reference Architecture (which specifies technical design tenets), the Strategy addresses the full spectrum of Doctrine, Organization, Training, Materiel, Leadership and Education, Personnel, Facilities, and Policy (DOTmLPF-P) — recognizing that ZT is a cultural transformation as much as a technical one. The Strategy is orchestrated by the ZT Portfolio Management Office (PfMO), established January 2022 under DoD CIO, and provides the framework for Component-level execution plans, resource prioritization, and accountability.

---

**Claim 1 —** Zero Trust is not an IT solution or product — it requires cultural transformation across the entire Department, not just the cybersecurity workforce. → [[zero-trust-solution-product]]
---

**Claim 2 —** The seven DoD ZT Pillars (User, Device, Applications/Workloads, Data, Network/Environment, Automation/Orchestration, Visibility/Analytics) provide the organizing construct for all ZT capabilities, with Data at the center. → [[seven-dod-zt-pillars-user-device-applications]]
---

**Claim 3 —** Target Level ZT must be achieved by end of FY2027 as the minimum security baseline; Advanced ZT represents the next-generation adaptive security state. → [[target-level-zt-achieved-end-fy2027-minimum]]
---

**Claim 4 —** The four strategic goals (Cultural Adoption, Systems Secured/Defended, Technology Acceleration, Zero Trust Enablement) address the full lifecycle of ZT transformation from mindset to sustainment. → [[four-strategic-goals-cultural-adoption-systems-secured]]
---

**Claim 5 —** The Strategy is explicitly NOT a solution architecture — Components retain freedom to choose technologies as long as they deliver specified capability outcomes. → [[strategy-explicitly-solution-architecture]]
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
