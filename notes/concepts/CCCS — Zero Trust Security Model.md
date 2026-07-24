---
tags:
  - source/standards
  - cccs
  - zt-model
  - canada
  - oskg-zerotrust
created: 2026-07-24
confidence: high
source:
  title: "Zero Trust Security Model"
  number: "ITSAP.10.008"
  publisher: "Canadian Centre for Cyber Security (CCCS)"
  date: "November 2022"
  classification: "UNCLASSIFIED"
  local_file: "sources/standards/_txt/CCCS_Zero_Trust_Security_Model_ITSAP10008.txt"
  url: "https://www.cyber.gc.ca"
related:
  - "[[CCCS — ZT Approach to Security Architecture]]"
  - "[[CISA ZTMM — Identity Pillar]]"
  - "[[CISA ZTMM — Device Network App Data Pillars]]"
  - "[[Concepts Index]]"
note_type: standards
standard_type: awareness-bulletin
justification: "CCCS ITSAP.10.008 is a compact 2-page awareness bulletin that introduces Zero Trust to a Canadian government audience at the introductory level. At ~9KB it's the shortest formal ZT publication in the OSKG corpus. It distills ZT into: a one-sentence definition, the CISA five-pillar model (with full pillar descriptions), benefits, challenges, and four transition steps. Unlike ITSM.10.008 (management guidance) or NIST 800-207 (technical architecture), ITSAP.10.008 is the 'ZT in two pages' document — designed to be read by non-technical stakeholders in under ten minutes. Its value to the OSKG is as the most condensed authoritative ZT summary available from a national cyber agency."
---

# CCCS — Zero Trust Security Model

*ITSAP.10.008* (November 2022) is the Canadian Centre for Cyber Security's awareness-level bulletin on Zero Trust. At approximately 2 pages, it's the shortest ZT publication from any national cyber agency in the OSKG corpus. Where ITSM.10.008 targets managers planning ZT adoption, ITSAP.10.008 targets anyone who needs to understand what ZT is in under ten minutes. Its primary structural contribution is presenting the CISA Zero Trust Maturity Model's five pillars as the organizing framework for ZT understanding — making it effectively a CISA ZTMM summary with Canadian government context.

## §1: Core Definition

### Claim 1: ZT is defined through the CISA five-pillar model rather than NIST tenets

**CCCS's claim:** "The term 'Zero Trust' (ZT) does not apply to a single product, technology, or architecture layer. Rather, it represents a security framework for protecting infrastructure and data. ZT's central tenet is that no subject (application, user, or device) in an information system is trusted by default. Trust must be re-assessed and verified every time a subject requests access to a new resource."

**Evidence presented:** Unlike ITSM.10.008 (which uses NIST's seven tenets), ITSAP.10.008 organizes ZT understanding around CISA's five pillars — Identity, Device, Network/Environment, Application Workload, and Data — plus three cross-cutting capabilities (Visibility & Analytics, Automation & Orchestration, Governance). Each pillar is given a single-paragraph description at the Traditional-to-Optimal maturity spectrum.

**Confidence:** HIGH. The CISA model is the most cited ZT framework for maturity progression, and using it simplifies ZT communication to non-technical audiences. The choice of CISA over NIST reflects the document's awareness purpose — CISA's pillar model is more visually intuitive and easier to remember than NIST's seven tenets.

**What's at stake:** If readers take the five pillars as *the* definition of ZT rather than one framework among several, they may treat ZT as a checklist of five technology domains rather than an architectural philosophy.

**My assessment:** This is a defensible editorial choice for an awareness document. The five pillars are concrete domains that non-technical readers can map to their organization (Identity = HR/IT, Device = endpoint management, Network = infrastructure, Application = development, Data = information management). NIST's tenets ("all data sources and computing services are considered a resource") are conceptually deeper but harder to operationalize for a general audience.

---

## §2: The Five-Pillar Summary

### Claim 2: Each CISA pillar is described at the Traditional/Advanced/Optimal maturity gradient

**CCCS's claim:** The document describes each pillar with specific practices at each maturity level (the table in the original is reproduced and annotated below):

| Pillar | Traditional | Advanced | Optimal |
|--------|-------------|----------|---------|
| **Identity** | Password or MFA; limited risk assessment | MFA; identity federation with cloud/on-prem; compliance enforcement | Continuous validation; real-time ML analysis |
| **Device** | Limited visibility into compliance; simple inventory | Compliance enforcement employed; data access depends on device posture | Constant device security monitor/validation; data access depends on real-time risk analytics |
| **Network/Environment** | Large macro-segmentation; minimal traffic encryption | Defined by ingress/egress micro-perimeters; basic analytics | Fully distributed ingress/egress micro-perimeters; ML-based threat protection; all traffic encrypted |
| **Application Workload** | Access based on local authorization; minimal integration with workflow | Access based on centralized authentication; basic integration into application workflow | Access authorized continuously; strong integration into application workflow |
| **Data** | Not well inventoried; static control; unencrypted | Least privilege controls; data stored in cloud/remote encrypted at rest | Dynamic support; all data encrypted |

**Confidence:** HIGH. This is a faithful summary of CISA's ZTMM v1 (June 2021 draft). Note that CISA published v2 in 2023 with refined pillars and additional maturity stages — this document reflects v1, which is consistent with its November 2022 publication date.

**What's at stake:** The v1→v2 evolution of CISA ZTMM means this summary may be slightly outdated. The v2 model restructured pillars (splitting "Network/Environment" into "Network" and "Environment" as separate considerations, for example).

**My assessment:** The maturity gradient is presented without the governance framing that CISA intended — Traditional/Advanced/Optimal are not just technical states but organizational maturity states requiring different governance structures. This flattening is appropriate for a 2-page document but loses the critical insight that ZT maturity is primarily an organizational journey, not a technology procurement journey.

---

## §3: Benefits and Challenges

### Claim 3: ZT provides six benefits organized around visibility, protection, and modernization

**CCCS's claim:** The document identifies six benefits:

1. **Continuous compliance** — improved visibility of who/what/where enables policy verification
2. **Improved visibility, detection and response** — automatic logging and monitoring with real-time environmental view
3. **Modernization of the workforce** — secure connection of users/devices/applications over any network using identity-based validation
4. **Increased network security** — every digital interaction verified and authorized continuously
5. **Reduced impact from data breach** — smaller trust zones require re-authentication at each security boundary, limiting lateral movement
6. **Improved data protection** — strong encryption, VPNs, and data loss prevention for data at rest and in motion

**Confidence:** HIGH. These align with the benefit frameworks in ITSM.10.008 and the broader ZT literature. The emphasis on "modernization of the workforce" (#3) is notable — it frames ZT not just as a security improvement but as an enabler of modern work practices (remote/hybrid, cloud, BYOD).

**My assessment:** The order of benefits (compliance → visibility → modernization → network security → breach impact → data protection) is unusual. Most frameworks lead with security benefits. The compliance-first ordering may reflect the document's government audience — compliance and audit are front-of-mind for federal IT leaders, and positioning ZT as a compliance enabler may be more persuasive than positioning it as a security control.

---

### Claim 4: The challenges are realistic but underdeveloped

**CCCS's claim:** Three challenges are identified:

1. **Increased time and effort** — strong authentication for every user/device, significant technical/administrative work to define detailed attributes
2. **Increased organizational focus and commitment over multiple years** — ZT affects multiple levels of infrastructure/operations requiring tight coordination
3. **Vendor lock-in risk** — "Organizations with multi-cloud solutions may encounter such challenges since ZT is a framework and not an industry standard"

**Confidence:** MEDIUM. The first two challenges are universally applicable. The third — vendor lock-in — is under-explored. The document notes that "partnership with commercial cloud providers is key to properly understand the organization's business and security objectives" but doesn't provide guidance on how to evaluate or negotiate such partnerships.

**What's at stake:** The vendor lock-in warning is critical but buried. Government organizations with multi-cloud strategies are exactly the audience most vulnerable to vendor ZT platforms that work within a single cloud but fail across clouds.

**My assessment:** The three challenges are too few and too brief. ITSM.10.008 (published four months later) expands to seven challenges with more specific guidance. The brevity may be intentional — an awareness document shouldn't overwhelm readers — but the vendor lock-in warning deserves more prominence given its strategic importance to government procurement.

---

## §4: Transition Steps

### Claim 5: Four concrete starting points are more actionable than abstract principles

**CCCS's claim:** "To improve your organization's cyber security posture consider implementing the following steps as a starting point in your transition towards ZT":

1. **Use dedicated devices (PAW/SAW)** — separate sensitive tasks and accounts from non-administrative computer uses (email, web browsing)
2. **Employ JIT/JEA risk-based adaptive policies** — implement least privilege access through just-in-time and just-enough access
3. **Enforce strong MFA** — aim for Level of Assurance (LoA) 3, referencing ITSP.30.031 v3
4. **Grant access based on user/device information, not logical location** — use multiple data points (identity, location, device health, resource, data classification, anomalies)

**Confidence:** HIGH. These four steps are specific, actionable, and achievable for most organizations. They don't require architectural transformation — they're incremental improvements that any organization can start today. PAW/SAW (step 1) is the lowest-hanging fruit; MFA (step 3) is the highest-impact.

**What's at stake:** If organizations treat these four steps as sufficient for ZT, they'll stop here and never implement microsegmentation, continuous monitoring, or dynamic policy — the architectural elements that make ZT transformative rather than just better authentication.

**My assessment:** The four steps are well-chosen for an awareness document. They're the "ZT on-ramp" — things every organization should do regardless of whether they pursue full ZT. Steps 1 and 3 (PAW + MFA) are security hygiene; steps 2 and 4 (JIT/JEA + identity-based access) are the mindset shift. The document wisely references specific CCCS technical guidance (ITSP.30.031 for authentication, ITSG-33 for risk management) — this creates a documented trail for auditors and demonstrates that ZT is supported by existing Canadian government security standards.

---

## §5: References

The document references five external frameworks:
- NIST SP 800-207: Zero Trust Architecture
- NIST SP 1800-35: Implementing a Zero Trust Architecture (Preliminary Draft)
- CISA's Zero Trust Maturity Model
- NCSC-UK: Zero trust architecture design principles
- Australian Cyber Security Centre: Essential Eight Maturity Model

**Notable:** The inclusion of the Australian Essential Eight is unique to this document — neither ITSM.10.008 nor most non-Australian ZT publications reference it. This suggests CCCS is monitoring the Five Eyes ZT landscape holistically.

---

## Framework Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| 1: ZT defined through CISA five-pillar model | HIGH | Readers treating pillars as definition rather than one framework; CISA ZTMM v2 superseding the v1 summarized here |
| 2: Pillar maturity gradient describes Traditional→Optimal | HIGH | CISA v2 maturity restructuring changing Traditional/Advanced/Optimal to Initial/Advanced/Optimal with additional stages |
| 3: Six benefits organized around visibility/protection/modernization | HIGH | Benefits are qualitative, not quantitative; compliance-first ordering may mislead about ZT's primary purpose |
| 4: Three challenges (effort, commitment, vendor lock-in) | MEDIUM | Underdeveloped vendor lock-in warning; insufficient for organizations making procurement decisions |
| 5: Four transition steps are actionable on-ramp | HIGH | Organizations may treat four steps as sufficient, never progressing to architectural ZT |

**Strongest section:** The five-pillar summary table (§2). It's the most compact, accurate CISA ZTMM summary in any government publication — useful as a quick reference for anyone who needs to understand the pillars without reading the full 30+ page CISA document.

**Weakest section:** The challenges (§3, Claim 4). Three bullet points with no mitigation guidance underserves readers who will encounter far more challenges than described.

**Key structural observation:** ITSAP.10.008 is an *awareness* document, not a *guidance* document. It says "here's what ZT is and here's where to start" — not "here's how to implement ZT." Its OSKG value is as the most condensed authoritative ZT summary available. It should be the first ZT document shown to any stakeholder who asks "what is Zero Trust?" and needs an answer in 5 minutes or less.

**Relationship to ITSM.10.008:** ITSAP.10.008 (November 2022) predates ITSM.10.008 (March 2023) by four months. The awareness bulletin was likely a precursor — testing messaging and framework selection before the more comprehensive management guidance was published. The two documents are complementary: ITSAP for introduction, ITSM for planning. This two-tier approach (awareness → management guidance → technical implementation guidance, presumably forthcoming) reflects a mature communications strategy for national cyber guidance.
