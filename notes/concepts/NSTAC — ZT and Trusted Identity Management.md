---
tags:
  - source/standards
  - nstac
  - zt-identity
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
claims_status: extracted
claims_extracted: 2026-07-24
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

**Claim 1 —** The Federal Government's current 2½-year ZT strategy is appropriately scoped for jump-starting action but insufficient for long-term transformation — absent additional institutionalization, ZT will fail. → [[federal-government-current]]
---

**Claim 2 —** Industry best practices — the Five-Step Process and the Kipling Method — should be the basis for federal ZT accountability metrics, not just technical checkbox completion. → [[industry-best-practices]]
---

**Claim 3 —** Governance is the critical gap — the Federal Government must integrate ZT into existing structures (FISMA, CDM, NIST 800-53, procurement) rather than treating it as a standalone initiative. → [[governance-critical-gap]]
---

**Claim 4 —** The Federal Government needs two dedicated ZT Program Offices — a Civilian Office (at CISA) and coordination with the existing Defense Office (at DoD) — to provide sustained institutional capacity. → [[federal-government-needs-two-dedicated-zt-program]]
---

**Claim 5 —** Internet-accessible asset discovery is a foundational prerequisite for ZT that many agencies lack — CISA should provide it as a shared service. → [[internet]]
---

**Claim 6 —** The U.S. Government must incentivize non-federal ZT adoption through grants, procurement preferences, international standards, and regulatory relief — not just lead by example. → [[government-incentivize-non]]
---

**Claim 7 —** Technology interoperability is the hidden risk — without component-level interface standards, ZT creates vendor lock-in and "a proliferation of multiple solutions [that] increases management complexity." → [[technology-interoperability-hidden-risk]]
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
