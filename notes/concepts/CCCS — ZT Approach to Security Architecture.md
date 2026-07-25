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
claims_status: extracted
claims_extracted: 2026-07-24
  - topic/zt-architecture
  - topic/zt-implementation
  - topic/zt-cloud
---

# CCCS — ZT Approach to Security Architecture

The Canadian Centre for Cyber Security's *ITSM.10.008* (March 2023) is the Government of Canada's management-level guidance on Zero Trust security architecture. It distills NIST SP 800-207, CISA's ZT Maturity Model, and the UK NCSC's eight design principles into accessible guidance for Canadian federal departments and agencies. The document is explicitly a bridge: it doesn't define new ZT principles but rather teaches organizations which frameworks exist, how to choose among them, and what best practices to follow. At 25 pages, it's one of the shortest formal government ZT publications, optimized for leaders and decision-makers rather than architects.

## §1: Core Position on Zero Trust

**Claim 1 —** ZT is a comprehensive security architecture strategy, not a product or technology → [[zt-comprehensive-security-architecture-strategy-product-technology]]
---

**Claim 2 —** The GC is developing its own ZT framework aligned with CISA and NIST pillars → [[gc-developing-own-zt-framework-aligned-cisa]]
---

**Claim 3 —** Preventing lateral movement is the *primary* goal of ZT → [[preventing-lateral-movement-primary-goal-zt]]
---

## §2: The Three-Framework Synthesis

**Claim 4 —** Organizations should choose among NIST, CISA, and NCSC frameworks — not invent their own → [[organizations-choose-among-nist-cisa-ncsc-frameworks]]
---

## §3: The 13 Best Practices

**Claim 5 —** CCCS's 13 best practices form a pragmatic, sequenced ZTA implementation guide → [[cccs-13-best-practices-form-pragmatic-sequenced]]
---

## §4: Benefits, Challenges, and Organizational Realities

**Claim 6 —** ZT improves security across seven dimensions → [[zt-improves-security-across-seven-dimensions]]
---

**Claim 7 —** ZT implementation faces significant organizational and technical challenges → [[zt-implementation-faces-significant-organizational-technical-challenges]]
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
