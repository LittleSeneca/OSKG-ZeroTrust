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
claims_status: extracted
claims_extracted: 2026-07-24
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-threats
---

# CCCS — Zero Trust Security Model

*ITSAP.10.008* (November 2022) is the Canadian Centre for Cyber Security's awareness-level bulletin on Zero Trust. At approximately 2 pages, it's the shortest ZT publication from any national cyber agency in the OSKG corpus. Where ITSM.10.008 targets managers planning ZT adoption, ITSAP.10.008 targets anyone who needs to understand what ZT is in under ten minutes. Its primary structural contribution is presenting the CISA Zero Trust Maturity Model's five pillars as the organizing framework for ZT understanding — making it effectively a CISA ZTMM summary with Canadian government context.

## §1: Core Definition

**Claim 1 —** ZT is defined through the CISA five-pillar model rather than NIST tenets → [[zt-defined-cisa-five]]
---

## §2: The Five-Pillar Summary

**Claim 2 —** Each CISA pillar is described at the Traditional/Advanced/Optimal maturity gradient → [[cisa-pillar-described-traditional-advanced-optimal-maturity]]
---

## §3: Benefits and Challenges

**Claim 3 —** ZT provides six benefits organized around visibility, protection, and modernization → [[zt-provides-six-benefits-organized-around-visibility]]
---

**Claim 4 —** The challenges are realistic but underdeveloped → [[challenges-realistic-underdeveloped]]
---

## §4: Transition Steps

**Claim 5 —** Four concrete starting points are more actionable than abstract principles → [[four-concrete-starting-points-actionable-abstract-principles]]
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
