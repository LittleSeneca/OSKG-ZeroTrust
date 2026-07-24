---
tags:
  - source/standards
  - cccs
  - zt-architecture
  - canada
  - oskg-zerotrust
created: 2026-07-24
confidence: high
source:
  title: "A Zero Trust Approach to Security Architecture"
  number: "ITSM.10.008"
  publisher: "Canadian Centre for Cyber Security (CCCS)"
  date: "March 15, 2023"
  classification: "UNCLASSIFIED / TLP:CLEAR"
  local_file: "sources/standards/_txt/CCCS_Zero_Trust_Approach_ITSM10008.txt"
  url: "https://www.cyber.gc.ca"
related:
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[CISA ZTMM — Overview and Framework]]"
  - "[[CCCS — Zero Trust Security Model]]"
  - "[[Concepts Index]]"
note_type: standards
standard_type: management-guidance
justification: "CCCS ITSM.10.008 is the Canadian government's management-level guidance on ZT security architecture. It synthesizes NIST, CISA, and NCSC frameworks for a Canadian federal audience and provides 13 actionable best practices for ZTA implementation. Unlike NIST 800-207 (technical architecture) or CISA ZTMM (maturity model), ITSM.10.008 is the bridge document: it explains what ZT is in plain language, why it matters to organizations, and which frameworks to adopt. It functions as the 'onboarding' document for Canadian agencies beginning their ZT journey."
---

# CCCS — ZT Approach to Security Architecture

The Canadian Centre for Cyber Security's *ITSM.10.008* (March 2023) is the Government of Canada's management-level guidance on Zero Trust security architecture. It distills NIST SP 800-207, CISA's ZT Maturity Model, and the UK NCSC's eight design principles into accessible guidance for Canadian federal departments and agencies. The document is explicitly a bridge: it doesn't define new ZT principles but rather teaches organizations which frameworks exist, how to choose among them, and what best practices to follow. At 25 pages, it's one of the shortest formal government ZT publications, optimized for leaders and decision-makers rather than architects.

## §1: Core Position on Zero Trust

### Claim 1: ZT is a comprehensive security architecture strategy, not a product or technology

**CCCS's claim:** "A ZTA is an enterprise approach to a system design whose security perspective is based on ZT principles. Its core principle is that inherent trust is never granted by default to any subject." The document repeatedly emphasizes that "ZT is more than just a technical solution, it requires a fundamental shift in how security is managed" and warns: "Some vendors will claim that their products are the answer to adopting a full ZT security model. Be wary of these vendors. The reality is that there's not a single ZT vendor or solution that can offer all the answers."

**Evidence presented:** The document defines ZT through NIST's operative definition verbatim, frames it as an *enterprise cybersecurity plan* (not a product suite), and structures its entire guidance around organizational change (mindset shift, executive commitment, phased implementation) rather than technology procurement. The 13 best practices include only 4 that are directly technology-oriented (MFA, encryption, SDP, segmentation); the other 9 are organizational, procedural, and strategic.

**Confidence:** HIGH. This is the consensus position across all major ZT frameworks. CCCS's contribution is making it explicit and actionable for a government audience that will face vendor pressure to "buy ZT in a box."

**What's at stake:** If ZT were reducible to products, procurement-driven organizations could solve it with purchasing — the most dangerous misunderstanding in this domain.

**My assessment:** CCCS correctly positions this as the first and most important message for its audience. Government procurement cycles are designed around buying products; ZT requires buying *integration, process change, and ongoing operations*. The vendor warning is sharper here than in NIST or CISA documents — likely reflecting the Canadian government's experience with vendor-driven security transformations.

---

### Claim 2: The GC is developing its own ZT framework aligned with CISA and NIST pillars

**CCCS's claim:** "The Government of Canada (GC) is developing a ZT security framework that will help GC departments and agencies improve their overall security posture. The GC ZT security framework will align with the pillars in the CISA and NIST references." Until that framework is published, organizations should use NIST, CISA, or NCSC guidance.

**Evidence presented:** The document lists the GC's seven goals for the ZT shift: resilient digital ecosystem, seamless user experience, secure platform for data/systems, end-to-end protection of information/applications/devices/networks, mature security processes/governance/standards, and CIA assurance for IT infrastructure and critical business data.

**Confidence:** MEDIUM. As of this note's creation (July 2026), I have not independently confirmed whether the GC ZT framework has been published. The document was published in March 2023 and the framework was described as "developing." This claim should be verified against current CCCS publications.

**What's at stake:** If the GC framework has been published since this document, it should be analyzed as a primary source. If not, Canadian agencies are operating under interim guidance with no domestic ZT standard.

**My assessment:** The seven goals are notably user-experience-forward ("seamless and enhanced user experience") compared to NIST's more technically-oriented tenets. This suggests the GC framework may prioritize usability alongside security — a pragmatic concession to the political reality of federal IT (where user resistance to security controls is a major implementation barrier).

---

### Claim 3: Preventing lateral movement is the *primary* goal of ZT

**CCCS's claim:** "It's important to note that preventing lateral movement is the primary goal of ZT, not the elimination of the legacy boundary defence or bring your own device (BYOD). These are things that may be enabled by ZT but should not be seen as primary reason for doing ZT."

**Evidence presented:** The document anchors its threat model in the lateral movement attack pattern: "We often hear of attacks that involve a compromised user account or device being used as an entry point... Once in, the attacker will then progress laterally in the network to gain access to credentials or other sensitive information."

**Confidence:** HIGH. This aligns with NIST's threat model and the Jericho Forum's original "de-perimeterization" thesis. CCCS's emphasis on lateral movement as *primary* goal (rather than continuous verification or least privilege) is a usefully concrete framing for organizations trying to measure ZT success: "Does this change reduce lateral movement?" is a more actionable metric than "Does this improve trust?"

**What's at stake:** If lateral movement prevention is the primary goal, then ZT investments should be evaluated against that criterion. Technologies that improve authentication but don't constrain lateral movement (e.g., MFA at the perimeter only) are insufficient.

**My assessment:** This is the most operationally useful framing in the document. It gives organizations a clear success metric: can a compromised workload reach other workloads? It also explains why ZT is more than just strong authentication — authentication without microsegmentation still allows lateral movement from authenticated positions.

---

## §2: The Three-Framework Synthesis

### Claim 4: Organizations should choose among NIST, CISA, and NCSC frameworks — not invent their own

**CCCS's claim:** The document provides an overview of "three commonly cited and trusted ZT frameworks/guidelines" and recommends organizations "choose which framework or set of guidelines aligns best with their business requirements and network infrastructure." The three are:

1. **NIST SP 800-207** (August 2020): Seven basic tenets, abstract logical architecture, technology-agnostic. "Helps agencies reduce implicit trust zones and better understand their network infrastructure."
2. **CISA ZTMM** (June 2021): Five pillars (Identity, Device, Network, Application Workload, Data) plus three cross-cutting capabilities, three maturity stages (Traditional → Advanced → Optimal). "One of many roadmaps to support the transition to ZT."
3. **NCSC** (UK, July 2021): Eight design principles for architecture review. "Most ZT approaches can be linked to these eight core principles."

**Evidence presented:** The document provides detailed summaries of all three frameworks: the full seven NIST tenets, the five CISA pillars with maturity stage descriptions, and all eight NCSC principles. The level of detail for each is sufficient for a reader to make an informed choice without consulting the original documents.

**Confidence:** HIGH. These are the three most-cited ZT frameworks globally, and the summaries are accurate.

**What's at stake:** By curating the frameworks rather than creating a fourth, CCCS avoids fragmenting the ZT standards landscape while providing Canadian-specific context. This is the responsible approach for a national cyber agency.

**My assessment:** This section is the document's primary value-add for the OSKG. It provides a single reference point that maps all three frameworks, including cross-cutting observations: NIST provides the *tenets* (what to believe), CISA provides the *maturity path* (how to progress), and NCSC provides the *design principles* (how to build). Organizations should use all three in combination, not pick one.

---

## §3: The 13 Best Practices

### Claim 5: CCCS's 13 best practices form a pragmatic, sequenced ZTA implementation guide

**CCCS's claim:** The document lists 13 best practices "to help prioritize their efforts when implementing a zero trust architecture." These are:

1. **Authenticate all connections** — never trust the local network; at minimum authenticate user and device
2. **Implement ZT policies** — start with the six Kipling questions: Who, What, Why, Where (user), Where (endpoint), How
3. **Establish a "trust engine"** — dynamic evaluation incorporating device state, behavioral attributes, and enterprise-level security context
4. **Know your assets and network architecture** — inventory data, users, devices, applications; understand value and risk
5. **Use multi-factor authentication (MFA)** — "an essential prerequisite of ZT"
6. **Use encryption for all traffic** — reinforces the tenet that all access must be explicitly granted
7. **Enforce policy-based access** — dynamic risk-based policies; identity-based authentication replaces IP-based trust
8. **Use PAM and SAW** — privileged access management with just-in-time access; secure administrative workstations for admin tasks
9. **Implement least privilege, RBAC, and ABAC** — RBAC for role-based enforcement, ABAC for granular attribute-based rules
10. **Monitor and log devices and services access** — continuous log collection, SIEM, security analytics
11. **Manage all devices** — unique traceable identity per device, TPM, BYOD policies, device certificates
12. **Use network segmentation or micro-segmentation** — VLANs, subnets, security zones; micro-segmentation down to workload level
13. **Use software-defined perimeter (SDP)** — adaptive trust model, identity-based access, VPN alternative

**Evidence presented:** Each practice includes specific implementation guidance. For example: PAM should use just-in-time access with dual approval (a different user must approve the privileged session). SAWs must be dedicated machines not used for email or web browsing. MFA should adjust factors based on data sensitivity. The trust engine should incorporate device state (software versions, patch levels, location), behavioral attributes (usage patterns, time-of-day), and enterprise context (heightened security states).

**Confidence:** HIGH. These practices are consistently cited across ZT literature (Finney, Garbis & Chapman, Gilman & Barth). CCCS's contribution is the specific ordering and the emphasis on non-technical practices (policies, asset inventory) preceding technical ones.

**What's at stake:** If organizations treat this as a sequential checklist (do #1, then #2, etc.), they'll fail. The practices are interdependent — you can't "implement ZT policies" (#2) without "knowing your assets" (#4), and you can't "establish a trust engine" (#3) without "monitoring and logging" (#10). CCCS should have made the interdependencies explicit.

**My assessment:** The list is well-chosen but the ordering is debatable. Practices 1 (authenticate all connections) and 12 (micro-segmentation) are architectural prerequisites for practices 7 (policy-based access) and 13 (SDP). A better structure would group these into three phases: foundational (4, 5, 11), architectural (1, 6, 12, 13), and operational (2, 3, 7, 8, 9, 10). The Kipling Method references (practice 2) echo Finney's methodology, suggesting CCCS was influenced by the Forrester/Kindervag lineage.

---

## §4: Benefits, Challenges, and Organizational Realities

### Claim 6: ZT improves security across seven dimensions

**CCCS's claim:** The document identifies seven benefits, each tied to a specific ZT mechanism:

| # | Benefit | Mechanism |
|---|---------|-----------|
| 1 | Greater network and lateral movement protection | All communication authenticated before access; every action subject to policy decision |
| 2 | Greater visibility and improved monitoring | Register and monitor all devices; stringent authentication provides access visibility |
| 3 | Improved incident detection and response | Detailed information links incidents to specific entities, applications, and data |
| 4 | Improved access control over cloud | Asset classification enables appropriate protection in shared-responsibility models |
| 5 | Improved data protection | Least privilege + continuous reassessment reduces data breach impact |
| 6 | Continuous compliance and auditing | Every access request evaluated and logged; complete audit trail |
| 7 | Secures the remote workforce | Micro-perimeters with stringent identification for distributed workers |

**Confidence:** HIGH. These benefits are well-documented in ZT literature and consistent with NIST, CISA, and vendor research (e.g., Forrester TEI studies).

**My assessment:** Benefits 4 (cloud) and 7 (remote workforce) are the most contextually relevant for 2023-2026, as hybrid work and cloud migration are the primary drivers of ZT adoption in government. Benefits 1 (lateral movement) and 5 (data protection) are the security fundamentals; the others are operational advantages. The benefit list implicitly prioritizes: preventing breaches (1, 5) > detecting breaches (2, 3) > enabling modernization (4, 7) > satisfying regulators (6). This is the right hierarchy for a security agency.

---

### Claim 7: ZT implementation faces significant organizational and technical challenges

**CCCS's claim:** "Migration to a ZTA can get messy." Challenges include:
- Granular attribute definition for every user and resource requires increased technical/administrative effort
- User frustration with repeated MFA and authentication
- Cost and time for hardware tokens and device rollout
- Legacy firewall incompatibility with dynamic ZT functionality
- Scarce technical resources for implementation
- Multi-year timeline — "it can take years to move to a full ZTA"
- The transition period where some systems are ZT-compatible and others are not
- "A permanent shift in mindset must be adopted and embraced fully"

**Confidence:** HIGH. These are realistic challenges documented across implementations (see Garbis & Chapman on the difficulty of brownfield ZT).

**What's at stake:** If organizations underestimate these challenges, they risk abandoned ZT programs (the "pilot purgatory" problem). CCCS's candor about the multi-year timeline and organizational resistance is valuable for setting realistic expectations.

**My assessment:** The challenge around legacy firewalls is understated — many government networks run on equipment that fundamentally cannot support dynamic, identity-aware policies. The document recommends "phased plans for introducing new equipment" but doesn't address the budget reality: replacing firewalls is a capital expense that competes with the ZT program itself. This is the hidden cost most ZT frameworks ignore.

---

## §5: Framework Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| 1: ZT is strategy, not product | HIGH | Vendor platform claims of "complete ZT in a box" eroding organizational commitment to process change |
| 2: GC developing own ZT framework | MEDIUM | Framework may have been published (unverified as of note creation); if published, this claim is superseded |
| 3: Lateral movement prevention is primary ZT goal | HIGH | Alternative framing (e.g., data protection as primary goal) may better serve data-centric organizations |
| 4: Choose among NIST/CISA/NCSC | HIGH | Emergence of a fourth framework (e.g., EU's proposed ZT standard) that CCCS hasn't evaluated |
| 5: 13 best practices form pragmatic guide | HIGH | Interdependencies between practices not addressed; sequential implementation will fail |
| 6: Seven benefit dimensions | HIGH | Benefits are qualitative; no quantitative evidence or case studies provided |
| 7: Significant organizational/technical challenges | HIGH | Understated cost of legacy equipment replacement; doesn't quantify multi-year total cost of ownership |

**Strongest section:** §2 (Three-Framework Synthesis). The NIST/CISA/NCSC comparison provides genuine value — no other single document maps all three frameworks with this level of detail and accessibility. For OSKG purposes, this section alone justifies the note.

**Weakest section:** §4 (Challenges). The challenges are listed but not prioritized or addressed with mitigations. "It can take years" and "it can get messy" are true but not actionable. A risk matrix mapping challenges to the 13 best practices would be more useful.

**Key structural observation:** ITSM.10.008 is designed as a *decision-support document*, not an *implementation guide*. It tells you what to think about, which frameworks to use, and what practices to follow — but not how to execute any specific practice in a Canadian government context. For implementation detail, readers must go to NIST, CISA, or NCSC. This is the correct scope for a national cyber agency's management publication, but it means the document's OSKG value is primarily in framework synthesis and benefit/challenge enumeration, not in actionable implementation patterns.

**Relationship to OSKG:** This document is the primary Canadian government ZT source. It confirms that Canada's approach is derivative of NIST and CISA rather than novel, which simplifies the OSKG's standards mapping: Canadian ZT = NIST tenets + CISA maturity model + NCSC design principles, contextualized for Canadian federal IT. The GC's forthcoming framework (if published) would supersede this as the primary Canadian source.
