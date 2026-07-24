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
---

# Garbis & Chapman — Ch18–21: Scenarios, Success Factors, and Conclusion

These four closing chapters pivot from architecture and technology (Ch 1–17) to the practical and organizational dimensions of Zero Trust: what to use it for (Ch 18), how to make it succeed (Ch 19), and what it all means (Ch 20–21 with Christopher Steffen's afterword). Together they form the "how to actually do this" conclusion of the book — the bridge from understanding ZT to deploying it.

## Claim 1: Seven ZT scenarios provide a practical, non-exhaustive framework for identifying and prioritizing projects

**Authors' claim:** The seven scenarios — VPN Replacement, Third-Party Access, Cloud Migration, Service-to-Service Access, DevOps, Mergers & Acquisitions/Divestiture, and Full Zero Trust Network/Network Transformation — "cover most of the major scenarios" and arm readers with "an understanding of how and when these different scenarios would be applicable in your environment, and to provide you with relevant recommendations for how to approach them."

**Evidence presented:** Each scenario is analyzed through a consistent lens: Considerations (examining Resources, Users/User Experience, Identity Providers, and Networking/Architecture angles) followed by Recommendations. The analysis across all seven yields several recurring patterns:

1. **VPN Replacement** (Ch 18, scenario 1): The most common first ZT project. VPNs perpetuate perimeter-based models, create identity silos, struggle with distributed resources, and impose WAN costs. ZT provides multiple secure connections to distributed PEPs, better IdP integration, fine-grained policies, and can be deployed incrementally — group by group or application by application. Key recommendation: be aware of "webs of interdependent tools" built around legacy VPNs that may complicate incremental rollout.

2. **Third-Party Access** (Ch 18, scenario 2): Non-employees with a legal relationship to the enterprise, using unmanaged devices. The enterprise "cannot impose internal policies on external actors" (quoting NIST) but "may be able to implement some Zero Trust-based policies on nonenterprise users who have a special relationship with the organization." Key recommendations: use the third party's IdP for authentication if confidence in their maturity exists; enforce MFA under your control; consider tying access to business processes (e.g., service desk ticket state); agentless access is often required.

3. **Cloud Migration** (Ch 18, scenario 3): Four migration categories — Forklift, Refactor, Rewrite, Adopt SaaS — each presenting different ZT integration opportunities. ZT's dynamic and context-sensitive nature "can take advantage of the rich set of APIs presented by cloud platforms." Key recommendation: "be proactive and collaborate with your application owner colleagues. Exposing them to your Zero Trust platform architecture and roadmap can in fact be a catalyst for accelerating cloud migration projects."

4. **Service-to-Service Access** (Ch 18, scenario 4): Legitimate and important, but typically lower priority than user-to-service because servers are more controlled environments. The key value: Zero Trust enforces least privilege, provides "top-down visibility and control of service-to-service communications," and serves as "a form of referential integrity for the network" — unexpected communications are blocked, improving deployment maturity. Three architectural approaches: microsegmentation (all servers are identities), asymmetric service-to-service (one authenticated identity, one target behind a PEP), and IoT-style (neither authenticated — not recommended).

5. **DevOps** (Ch 18, scenario 5): ZT and DevOps are "both modern and effective approaches" that should be integrated. ZT applies across all DevOps phases — Plan/Code (educate developers on platform capabilities), Build/Test (automated policies granting access based on workload attributes), Release/Deploy (policies controlling production access via change windows), Operate/Monitor (identity-enriched logs). A ZT system "can be connected to an organization's DevOps platforms, and automatically adjust access as workloads flow through the full application lifecycle."

6. **M&A and Divestiture** (Ch 18, scenario 6): ZT provides a "unifying or normalizing layer on top of heterogeneous resources and networks" — near-immediate cross-domain access, IP address conflict mitigation, and avoidance of WAN deployment costs. For divestiture, ZT manages transitional access during the months-long technical unwinding.

7. **Full Zero Trust Network/Network Transformation** (Ch 18, scenario 7): The composite end-state — all users off the enterprise network, most private services behind PEPs (enclave-based model), some microsegmentation, some implicit trust zones. The key mindset shift: "the problem to be solved isn't 'remote access' — it's just 'access.'" "Be sure to define limits and have a realistic vision for your end state in mind."

**Confidence:** HIGH. These seven scenarios reflect real enterprise patterns seen across the industry, and the consistent analytical framework (Considerations → Recommendations) makes them actionable.

**What's at stake:** If these seven scenarios are framed as an exhaustive taxonomy (which the authors explicitly deny), organizations may miss emerging use cases (IoT, OT, AI/ML workloads). If they're treated as independent silos, organizations miss the compounding value of a unified ZT platform. The authors acknowledge the scenarios are connected — "each of the previous six use cases is a microcosm of the ideas, approaches, and challenges of the full Zero Trust network scenario."

**Who disagrees:** NIST 800-207's five deployment scenarios (Ch 4) overlap substantially but differ in framing — NIST is topology-driven (satellite facilities, multi-cloud, contractors, cross-enterprise, public-facing), while Garbis & Chapman are use-case-driven (VPN replacement, third-party, cloud migration, etc.). Both are correct; they're different organizing principles. Green-Ortiz (Cisco Press) adds IoT/OT scenarios that Garbis & Chapman only address in Ch 16. Forrester's ZTX model organizes around pillars (data, networks, people, workloads, devices, visibility/automation) rather than scenarios.

**My assessment:** The seven-scenario framework is the most useful practitioner-oriented ZT taxonomy in the literature. NIST's deployment scenarios answer "where should the PE/PA live?" while Garbis & Chapman answer "what business problem am I solving?" — and the second question is what actually gets projects funded. The consistent structure (considerations by Resources, Users, Identity Providers, Networking, and Architecture; followed by recommendations) makes this chapter directly usable as a project evaluation template.

---

## Claim 2: ZT success requires deliberately blending top-down strategic vision with bottom-up tactical execution

**Authors' claim:** "Take a focused and incremental approach while still keeping sight of (and planning for) your larger Zero Trust initiative, and consciously taking the time to build bridges and lines of communication with your peers across the organization." The top-down/bottom-up distinction is "an artificial distinction" — "every Zero Trust project and initiative will combine elements of both." "Deliberately including strategic aspects within a tactical first Zero Trust project is an excellent way to set yourself up for approved and supported second and third projects."

**Evidence presented:** Two detailed sample deployments illustrate the blended approach:

*Tactical Project (transportation services org):* Third-party financial analysts accessing on-prem systems via VPN. Audit findings (MFA requirement, zombie account cleanup) create the catalyst. The 7-step project timeline spans ~3 months: Define Problem → Research Solutions → Review Architecture → POC Two Platforms → Present Results → Production Pilot (1 month) → Full Rollout. The security team deliberately involves the enterprise architecture team at multiple checkpoints, "knowing that they intend to grow the scope and maturity of their Zero Trust initiative over time." Key structural choices: parallel VPN/ZT access during pilot so users can switch back, formal "go/no-go" gate before production, promotion of success to generate momentum.

*Strategic Initiative (pharmaceutical company):* A near-miss ransomware incident creates board-level demand for change. The CISO structures a two-phase program: Phase 1 (immediate) secures highest-value assets with MFA, device posture checks, network segmentation; Phase 2 (longer-term) moves all users "off net," migrates to cloud-based IDaaS, and incorporates IaaS/PaaS. The first project is deliberately focused — addressing the most immediate weaknesses — while establishing the platform for broader rollout. The organization uses five value drivers (Security, Audit/Compliance, Agility, Customer/Partner Integrations, Technology Modernization) on a radar chart to quantify each project's impact. Formal Architecture and Change Management boards are strengthened; a Governance board is deemed unnecessary because the Architecture board already incorporates risk and compliance.

**Confidence:** HIGH. The sample deployments are idealized but structurally realistic. The emphasis on *deliberately* blending strategic and tactical perspectives is the chapter's most important organizational insight.

**What's at stake:** Organizations that go purely tactical risk building a brittle, one-off solution that can't scale. Organizations that go purely strategic risk "analysis paralysis" — years of planning without production deployment. The blended approach is harder to execute but more likely to deliver sustained value.

**Who disagrees:** Forrester's ZTX framework is inherently strategic — it assumes an organization-wide transformation program. Google's BeyondCorp was essentially a top-down initiative (though incremental in rollout). The Software-Defined Perimeter case study from Ch 4 was purely tactical. The tension between "strategic ZT program" and "tactical ZT project" is real, and different organizations in different circumstances will favor one pole. Garbis & Chapman's contribution is acknowledging that the best outcomes come from deliberately mixing both.

**My assessment:** The blended approach is correct but under-specified. The authors don't provide criteria for *when* to emphasize strategic vs. tactical, or *how much* strategic scaffolding a tactical first project needs. The pharmaceutical company example leans heavily on a crisis catalyst — without it, would the same approach work? The transportation example is more broadly applicable but assumes a receptive enterprise architecture team, which many organizations lack. This gap is where the NIST 800-207 migration chapter (Ch 7) provides complementary guidance at the capability level.

---

## Claim 3: Five business value drivers — not security alone — justify ZT investment

**Authors' claim:** "While the implementation of Zero Trust is usually technology focused, business goals will ultimately be the impetus behind these projects." Five value drivers apply: Security, Audit and Compliance, Agility/New Business Initiatives, Customer/Partner Integrations, and Technology Modernization.

**Evidence presented:**

- **Security**: The obvious driver — "as simple as incorporating MFA into the user experience or as complex as deploying an enterprise-wide Zero Trust network." But the authors note that security may not be the primary focus for every ZT project — a customer integration project on an already-deployed ZT platform may primarily serve the Customer/Partner Integration driver.
- **Audit and Compliance**: ZT's identity-centric logging provides "improved audit results and better compliance attainment." "Zero Trust projects often reduce audit costs and cycle times, due to providing easily accessible and easily understandable access logs."
- **Agility/New Business Initiatives**: ZT provides "guardrails and direction" for Cloud First strategies and rapid business innovation through automated, context-based access controls.
- **Customer/Partner Integrations**: ZT enables "new types of system, data, and process integrations with customers and partners" — "as simple as enabling secure customer access to a normally private web application or as complex as real-time data exchange across enterprises."
- **Technology Modernization**: "Upgrades of outdated security or IT infrastructure, decommissioning of now-ineffective systems, and transitions to modern replacements."

The authors recommend visualizing these drivers on a radar chart to "more objectively evaluate, compare, and prioritize candidate projects through the life of your initiative."

**Confidence:** HIGH. This value-driver framework is widely applicable and addresses the real-world problem that ZT projects need multi-stakeholder justification.

**What's at stake:** If security is the only value driver, ZT competes with every other security investment for the same limited budget. The multi-driver framework allows ZT to draw funding from operations (Technology Modernization), compliance (Audit), business development (Customer Integrations), and innovation (Agility) budgets — not just security. This is the financial argument for cross-organizational ZT adoption.

**Who disagrees:** NIST 800-207 doesn't address business justification — it's a technical architecture document. DoD's ZT Strategy addresses value through the lens of mission assurance and cybersecurity readiness, which are security-specific drivers. CISA's ZT Maturity Model implies value through maturity improvement but doesn't provide a business justification framework. Garbis & Chapman's value driver model is unique in the ZT literature and fills a genuine gap.

**My assessment:** The five-driver model is one of the most practically useful contributions in the book. The radar chart visualization is effective for stakeholder communication — it transforms "we should do ZT because security" into "here's how this project advances five organizational priorities." The specific recommendation to reduce audit costs (a tangible, budget-visible benefit) is especially sharp — it gives CFOs and compliance officers a concrete reason to support ZT.

---

## Claim 4: Common roadblocks — IAM immaturity, political resistance, regulatory constraints, resource visibility gaps, and analysis paralysis — are predictable, documented, and surmountable

**Authors' claim:** "Enterprise IT and security is hard and complex, and some Zero Trust projects will fail. This is unfortunate, but true. The good news is that most will be a success." The five roadblocks can be mitigated with specific countermeasures.

**Evidence presented:**

- **IAM Immaturity**: The "our directory is a mess" problem. Counter: Zero Trust doesn't require perfect IAM — it can be a "catalyst for improved maturity and data integrity in your IAM system, even if it's just for a narrow slice." ZT systems consume IAM attributes; you control how many attributes inform policy. Start narrow.

- **Political Resistance**: "People who impose barriers to change, despite the clear benefits." Four counterstrategies: (1) education on concrete benefits, (2) strong executive sponsorship breaking down barriers, (3) line-of-business champions whose projects demonstrate revenue or cost benefits, (4) finding allies within opposing organizations — "Zero Trust systems are inherently integratable, there may be some creative ways to tie into and augment the existing infrastructure, avoiding the perception that you're going to be 'ripping and replacing.'"

- **Regulatory/Compliance Constraints**: Regulations lag behind technology. Counter: "be proactive about engaging with your third-party/external auditor... collaborate with them and educate them, to ensure that they understand your trajectory."

- **Discovery and Visibility of Resources**: "I don't know who is accessing what, how can I control them?" Two valid approaches: (1) the BeyondCorp/PagerDuty observational approach — deploy broadly, collect network data, ensure no productivity interruption, (2) the SDP incremental approach — onboard users and groups incrementally, start with coarser policies, tighten over time. "Don't fall into the trap of assuming that you need perfect visibility of every connection and every data flow before you can begin."

- **Analysis Paralysis**: "Attempting to fully understand, identify risks, and scope out any new technology or approach... has a too-common downside of indefinitely delaying any decision or action." Counter: "collaborate with all relevant stakeholders, and approach their initiative from the perspective of how they can get Zero Trust into pilot or production as quickly as possible, even if it's initially limited in scope." Run ZT in parallel with existing access methods until confidence is high; only then decommission the old approach.

**Confidence:** HIGH. These roadblocks are empirically validated by practitioner experience and match patterns observed in other large-scale security transformations (cloud migration, IAM modernization, SDN adoption).

**What's at stake:** If these roadblocks are treated as insurmountable, organizations never start. If they're dismissed as trivial, projects fail on non-technical grounds. The authors' approach — naming the roadblocks, providing specific countermeasures, and acknowledging that "perfection is an unattainable goal, but dramatic improvements in security and efficiency are attainable and realistic" — is the right balance.

**Who disagrees:** NIST 800-207 doesn't address organizational roadblocks (it's a technical architecture). CISA's ZTMM acknowledges that maturity progression faces organizational challenges but doesn't provide specific countermeasures. The DoD ZT Strategy addresses acquisition and funding challenges specific to the defense ecosystem. Garbis & Chapman's roadblock taxonomy is provider-agnostic and broadly applicable.

**My assessment:** The roadblock section is where the authors' practitioner experience most clearly shows. The guidance is specific ("run ZT in parallel with existing access methods") rather than abstract ("manage change carefully"). The IAM immaturity counter — ZT as catalyst rather than consumer of perfect IAM — is particularly important because it removes the most common excuse for not starting. The political resistance section is refreshingly honest about organizational reality in a way most technical ZT literature avoids.

---

## Claim 5: ZT is a journey, not a destination — success comes from starting small, planning thoroughly, navigating politics, leveraging digital transformation, and aligning budget across stakeholders

**Authors' claim (Conclusion, Ch 20):** "It's neither possible nor appropriate to force-fit your Zero Trust system into every part of your environment. In fact, deliberately excluding certain components of your IT infrastructure will help with your focus, velocity, and success." The book's ZT definition (from Ch 2) "should serve as baseline principles for your organization's overall Zero Trust program, and inform your decision-making and priorities throughout your journey."

**Steffen's claim (Afterword, Ch 21):** ZT implementation is not "one and done." Five summary themes:

1. **Plan Thoroughly**: "So many Zero Trust implementations fail because of incomplete planning... not a lack of planning, since most organizations have some kind of game plan." The failure mode is *incomplete* planning, not absent planning.

2. **Navigate Politics**: "Because of the scope of most Zero Trust projects, it has a lot of stakeholders. Getting all of those stakeholders to agree on anything can be a massive challenge." Executive sponsorship sets the tone; line-of-business support carries weight up the chain.

3. **Dream Big, Start Small**: "Zero Trust does not have to be implemented all at once. In fact, it should not be." Start with a specific test group — "once you establish a proof of concept and the value of Zero Trust, the political problems decrease and support increases."

4. **Align Budgets**: "Make certain to align your goals with [operations, DevOps, compliance] and maybe — just maybe — you can get some of the valuable budget dollars from those departments."

5. **Leverage Digital Transformation**: "Incorporate your Zero Trust framework as part of the digital transformation process... You were going to have to update the security controls for those digital transformation projects anyway, so take the opportunity to align them with your Zero Trust vision."

**Evidence presented:** The conclusion emphasizes the book's definition (integrated security platform, contextual information, dynamic enforcement, resource/identity-centric model) as the organizing principle. The Afterword provides high-level synthesis from an industry analyst perspective (Steffen is Research Director at EMA) — less technical detail, more strategic framing.

**Confidence:** HIGH. These concluding themes are consistent with the rest of the book and with broader industry consensus. The "journey" framing is universal across ZT literature (NIST, CISA, DoD, Forrester all use it).

**What's at stake:** Treating ZT as a product purchase rather than an organizational journey leads to shelfware — solutions bought and never fully deployed. The journey framing correctly positions ZT as an ongoing transformation rather than a one-time project.

**Who disagrees:** No one disagrees with the journey framing, but vendor marketing often implies the opposite — "buy our ZTNA product and you're Zero Trust." This tension between marketing simplicity and implementation complexity is a recurring challenge that Garbis & Chapman navigate with unusual honesty.

**My assessment:** The book's conclusion is modest rather than grandiose — "you now have armaments, magic spells, potions, and provisions. Assemble your team, build alliances, and go forth to slay monsters." This tone is appropriate. Steffen's afterword provides useful external validation but doesn't add new technical content; it functions as an executive-summary-level reinforcement of the book's main themes. The most important practical takeaway across these closing chapters is the consistent advocacy for *incrementalism with strategic intent* — start focused, learn, build momentum, scale deliberately.

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
