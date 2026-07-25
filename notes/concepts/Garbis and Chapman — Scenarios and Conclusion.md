---
tags:
  - source/books
  - garbis-chapman
  - zt-scenarios
  - zt-organizational
  - zt-implementation
  - vpn-replacement
  - devops
  - mergers-and-acquisitions
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
  lines: "8294–9961"
  chapters: "18–21"
related:
  - "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
  - "[[NIST 800-207 — Ch7 — Migration]]"
  - "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
  - "[[CISA ZTMM — Overview and Framework]]"
  - "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
  - "[[Concepts Index]]"
  - topic/zt-governance
  - topic/zt-implementation
  - topic/zt-architecture
---

# Garbis & Chapman — Ch18–21: Scenarios, Success Factors, and Conclusion

These four closing chapters pivot from architecture and technology (Ch 1–17) to the practical and organizational dimensions of Zero Trust: what to use it for (Ch 18), how to make it succeed (Ch 19), and what it all means (Ch 20–21 with Christopher Steffen's afterword). Together they form the "how to actually do this" conclusion of the book — the bridge from understanding ZT to deploying it.

**Claim 1 —** Seven ZT scenarios provide a practical, non-exhaustive framework for identifying and prioritizing projects → [[seven-zt-scenarios-provide-a-practical-non-exhaustive-framework]]

---

**Claim 2 —** ZT success requires deliberately blending top-down strategic vision with bottom-up tactical execution → [[zt-success-requires-deliberately-blending-top-down-strategic-vision]]

---

**Claim 3 —** Five business value drivers — not security alone — justify ZT investment → [[five-business-value-drivers-not-security-alone-justify]]

---

**Claim 4 —** Common roadblocks — IAM immaturity, political resistance, regulatory constraints, resource visibility gaps, and analysis paralysis — are predictable, documented, and surmountable → [[common-roadblocks-iam-immaturity-political-resistance-regulatory-constraints]]

---

**Claim 5 —** ZT is a journey, not a destination — success comes from starting small, planning thoroughly, navigating politics, leveraging digital transformation, and aligning budget across stakeholders → [[zt-is-a-journey-not-a-destination-success]]

---

## Chapters 18–21 Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| Seven scenarios as practical project framework | HIGH | Emerging use cases (IoT/OT, AI workloads) not covered |
| Blending top-down strategic + bottom-up tactical | HIGH | Organizations without either executive sponsorship or receptive architecture teams |
| Five business value drivers for ZT justification | HIGH | Security-only budgeting cultures that can't access cross-departmental funding |
| Five roadblocks as predictable and surmountable | HIGH | Deeply entrenched political resistance in dysfunctional orgs |
| ZT as journey — start small, plan thoroughly | VERY HIGH | Vendor marketing promising one-product ZT |

**Strongest sections:**

1. **The seven-scenario framework (Ch 18)** — the most detailed, actionable use-case taxonomy in the ZT literature. Every scenario includes concrete Considerations and Recommendations. The VPN replacement and third-party access scenarios in particular provide immediately usable project evaluation criteria.

2. **The five-value-driver model (Ch 19)** — addresses the real-world problem of cross-stakeholder justification. The radar chart visualization is a communication tool that should be standard practice for ZT project proposals.

3. **The roadblock taxonomy (Ch 19)** — specific, honest, and practical. The IAM immaturity counter ("ZT as catalyst, not consumer") and the analysis paralysis counter ("run in parallel, don't wait for perfect visibility") remove the two most common excuses for delaying ZT adoption.

4. **The tactical project sample timeline (Ch 19)** — provides a realistic ~3-month project template with clear gates, stakeholder checkpoints, and the deliberate choice to involve enterprise architecture early. This is directly usable as a project plan template.

**Weakest sections:**

1. **DevOps scenario (Ch 18)** — the most abstract scenario, offering less actionable detail than the others. The authors acknowledge that application security (static analysis, fuzzing, vulnerability management) sits "outside the scope of Zero Trust," which limits the scenario's completeness.

2. **Strategic initiative sample (Ch 19)** — relies on a crisis catalyst (near-miss ransomware) that not every organization will have. The transition from "lucky break" to "board demands action" is not a reproducible strategy.

3. **Afterword (Ch 21)** — adds external validation but no new analysis. Functions as an executive summary of themes already covered.

**Unique contributions to OSKG-ZeroTrust:**

1. **The seven-scenario framework** provides a practitioner-level complement to NIST 800-207's deployment scenarios (Ch 4). While NIST answers "where should the architecture components live?", Garbis & Chapman answer "what business problems should I solve and in what order?" — both are needed.

2. **The business value driver model** fills a gap in the ZT literature. NIST, CISA, DoD, and Forrester all address *what* ZT is and *how* to deploy it, but none provide a framework for *justifying* it to non-security stakeholders. The five-driver model (with radar chart visualization) is a distinct contribution.

3. **The roadblock taxonomy with specific countermeasures** is the most honest treatment of ZT organizational challenges in the literature. NIST 800-207 is silent on organizational barriers; CISA's ZTMM implies them but doesn't provide countermeasures; DoD addresses them through the acquisition lens only. Garbis & Chapman's practitioner voice — "perfection is an unattainable goal, but dramatic improvements are attainable and realistic" — is the right tone.

4. **The blended top-down/bottom-up approach** resolves a false dichotomy present in much ZT discourse. Strategic ZT programs need tactical first projects; tactical ZT projects need strategic scaffolding to scale. The deliberate blending of both perspectives is a more nuanced and realistic model than either extreme.

**Cross-source synthesis:**

| Garbis & Chapman Topic | NIST 800-207 | CISA ZTMM | DoD ZT RA | Forrester ZTX |
|------------------------|-------------|-----------|-----------|---------------|
| Seven ZT scenarios | Ch 4: Five deployment scenarios (topology-driven) | Maturity progression across pillars | Use cases mapped to pillars | Capability areas across pillars |
| Value drivers | Not addressed | Implicit in maturity improvement | Mission assurance drivers | Business outcome focus |
| Roadblocks | Not addressed | Implicit organizational challenges | Acquisition/funding barriers | Adoption challenges |
| Blended approach | Ch 7: Migration guidance (capability-level) | Maturity model (phased progression) | Strategy & Roadmap (phased capability) | Ecosystem approach |
| Incrementalism | "Incrementally implement" (Ch 7) | Maturity levels (Traditional → Optimal) | Target-Level ZT (phased) | Journey framing |

**Bottom line:** These four chapters are the most practically useful conclusion to a ZT book in the literature. They don't introduce new architectural concepts — they answer the question every practitioner asks after understanding ZT: "How do I actually do this in my organization?" The scenario framework, value driver model, roadblock taxonomy, and sample deployment timelines together form an immediately usable ZT project planning toolkit.
