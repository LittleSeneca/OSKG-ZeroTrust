---
tags:
  - source/standards
  - oskg-zerotrust
  - nist
  - zt-definition
  - zt-history
created: 2026-07-24
updated: 2026-07-24
confidence: high
source:
  title: "NIST SP 800-207 — Zero Trust Architecture"
  authors: "Scott Rose, Oliver Borchert, Stu Mitchell, Sean Connelly"
  year: 2020
  publisher: "National Institute of Standards and Technology"
  local_file: "sources/standards/_txt/NIST_SP_800-207_Zero_Trust_Architecture.txt"
  chapter_lines: "335–456"
related:
  - "[[NIST 800-207 Index]]"
  - "[[Concepts Index]]"
  - "[[History Index]]"
  - "[[Notes Index]]"
  - "[[Standards Index]]"
claims_status: extracted
claims_extracted_date: 2026-07-24
claims_count: 8
claims_files:
  - "[[perimeter-security-obsolete]]"
  - "[[zt-no-implicit-trust-continuous-eval]]"
  - "[[zta-prevent-breach-limit-lateral-movement]]"
  - "[[zt-not-a-product-hybrid-journey]]"
  - "[[zt-predates-term-disa-jericho]]"
  - "[[kindervag-coined-zero-trust]]"
  - "[[federal-programs-building-toward-zt]]"
  - "[[nist-document-structure-framework]]"
---

# NIST SP 800-207 — Ch 1: Introduction

The Introduction chapter establishes why Zero Trust exists (perimeter-based security has failed), defines ZT and ZTA in NIST's authoritative voice, traces the concept's intellectual lineage from DISA and Jericho Forum through Kindervag, and previews the document structure. It is the orienting chapter for the U.S. federal government's formal adoption of Zero Trust as a cybersecurity paradigm.

---

## §1.0: Opening Definition and Motivation (Lines 337–387)

**Claim 1 —** Perimeter-based network security has been rendered obsolete by enterprise complexity. → [[perimeter-security-obsolete]]

---

**Claim 2 —** Zero Trust assumes breach and eliminates implicit trust — every access request must be continuously authenticated, authorized, and risk-evaluated. → [[zt-no-implicit-trust-continuous-eval]]

---

**Claim 3 —** ZTA is an enterprise cybersecurity architecture designed specifically to prevent data breaches and limit internal lateral movement. → [[zta-prevent-breach-limit-lateral-movement]]

---

**Claim 4 —** ZT is an architectural paradigm, not a product — adoption is a journey of risk evaluation, incremental, and most enterprises will operate in hybrid mode. → [[zt-not-a-product-hybrid-journey]]

---

## §1.1: History of Zero Trust Efforts Related to Federal Agencies (Lines 388–413)

**Claim 5 —** The concept of zero trust predates the term — DISA "black core" and the Jericho Forum were conceptual predecessors focused on per-transaction security and de-perimeterization. → [[zt-predates-term-disa-jericho]]

---

**Claim 6 —** John Kindervag at Forrester coined the term "zero trust," which then became the dominant term for security solutions that evaluate trust per-transaction rather than by network location. → [[kindervag-coined-zero-trust]]

---

**Claim 7 —** Federal agencies have been building toward ZT for over a decade through foundational programs (FISMA, RMF, FICAM, TIC, CDM) that were initially limited by technology but are now maturing toward dynamic, granular access control. → [[federal-programs-building-toward-zt]]

---

## §1.2: Structure of This Document (Lines 414–446)

**Claim 8 —** The document's organization — definitions → components → use cases → threats → federal guidance → migration roadmap — represents the essential framework for understanding and implementing ZTA. → [[nist-document-structure-framework]]

---

## Chapter 1 Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| 1: Perimeter security obsolete | HIGH | Empirical counter-examples of effective perimeter-only architectures |
| 2: ZT = assume breach, no implicit trust, continuous evaluation | HIGH (definitional) / MEDIUM (efficacy) | Operational evidence that "assume breach" is infeasible |
| 3: ZTA designed to prevent breaches and limit lateral movement | MEDIUM | Lack of breach-prevention evidence at scale; policy-engine-as-single-point-of-failure |
| 4: ZT is principles, not product; adoption is incremental journey | HIGH | Platform vendors demonstrating "ZT in a box" works at scale |
| 5: ZT predates the term — DISA black core + Jericho Forum as precursors | HIGH | Disputing the conceptual continuity between these programs and modern ZT |
| 6: Kindervag coined "zero trust" at Forrester | HIGH | Earlier documented uses of the term (none known) |
| 7: Federal programs (FISMA, RMF, FICAM, TIC, CDM) built toward ZT | MEDIUM-LOW | Evidence that these programs were conceived independently and only retroactively aligned with ZT |
| 8: Document structure represents essential ZTA framework | LOW (as optimal) / HIGH (as descriptive) | Alternative organizations proving more effective for adoption or understanding |

**Strongest section:** §1.1 (History) — the intellectual lineage from DISA black core through Jericho Forum to Kindervag is well-sourced, properly hedged, and establishes federal legitimacy for ZT without erasing the contributions of industry and DoD. The chronology is accurate and the citations ([BCORE], [JERICHO]) point to verifiable primary sources.

**Weakest section:** §1.0's Claim 7 (federal program alignment) — the characterization of FISMA, RMF, FICAM, TIC, and CDM as building toward ZT is the most vulnerable to challenge. TIC in particular represents the antithesis of ZT principles (centralized choke-point enforcement), and retroactively claiming it as a ZT precursor strains credibility. The technology-maturation argument rescues the claim partially but doesn't address the fundamental architectural tension.

**Cross-cutting observations:**
- NIST writes for a federal audience; the chapter's emphasis on federal programs and DoD heritage reflects this institutional positioning. Non-federal readers may find the history parochial — missing Google's BeyondCorp, the Cloud Security Alliance's contributions, and international ZT efforts.
- The chapter performs significant *legitimation work* — establishing ZT as having military roots, as the natural culmination of existing federal investment, and as principles-based rather than vendor-driven. This is strategically important but analytically selective.
- The tension between absolutist language ("no implicit trust," "assume breach") and pragmatic guidance ("hybrid mode," "incremental," "by use case") runs throughout the chapter and is never resolved. This tension persists through the entire document and through subsequent ZT guidance.
- Claims 4 and 7 together produce an interesting paradox: if federal agencies have been building toward ZT for a decade, why is wholesale technology replacement not needed? The answer — because ZT is principles, not technology — is definitionally true but may understate the architectural changes required.

**Open questions for subsequent chapters:**
- Does Section 2's formal ZT definition resolve the absolutist/pragmatic tension?
- Does Section 5's threat model address the "policy engine as single point of failure" critique?
- Does Section 7's migration roadmap reconcile with the claim that existing federal programs are ZT-enabling?
- How does NIST's definition compare with concurrent definitions from CISA, DoD, and international standards bodies? (See [[Questions Index]])
