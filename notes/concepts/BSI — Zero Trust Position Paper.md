---
tags:
  - source/standards
  - bsi
  - zt-policy
  - germany
  - oskg-zerotrust
created: 2026-07-24
confidence: medium
source:
  title: "Positionspapier Zero Trust 2023"
  publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
  date: "June 26, 2023"
  language: "German"
  local_file: "sources/standards/_txt/BSI_Zero_Trust_Position_Paper_2023_DE.txt"
  url: "https://www.bsi.bund.de"
  contact: "zero-trust@bsi.bund.de"
related:
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[CISA ZTMM — Identity Pillar]]"
  - "[[CISA ZTMM — Device Network App Data Pillars]]"
  - "[[CCCS — ZT Approach to Security Architecture]]"
  - "[[Concepts Index]]"
note_type: standards
standard_type: position-paper
language_note: "This document was analyzed in its original German. While I have high confidence in the structural and conceptual extraction, nuanced policy language, legal terminology (particularly VS/VSA — classified information handling), and domain-specific compound nouns may carry meanings not fully captured in English translation. Key German terms are preserved in brackets. Claims with German-specific legal/regulatory context are flagged. A native German speaker should validate the §4 cross-organizational and VS-integration claims."
justification: "The BSI Zero Trust Position Paper (2023) is Germany's first comprehensive federal position on Zero Trust. It holds unique OSKG value as: (1) the only major European national cyber agency ZT publication (complementing the US-dominant NIST/CISA/NSA and UK NCSC), (2) the only ZT framework that integrates classified information (VS/Verschlusssache) handling requirements into every architectural pillar, (3) the only framework with explicit multi-organizational ZT architecture scenarios, and (4) the most detailed treatment of real-time information source integration (Shared Signals Framework, CAEP) in any government ZT publication. The five-pillar integration model (Identität/Gerät/Netz/Anwendung/Daten) with Klassisch/Fortschrittlich/Ideal maturity levels provides a European alternative to CISA's Traditional/Advanced/Optimal model."
claims_status: extracted
claims_extracted: 2026-07-24
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-identity
---

# BSI — Zero Trust Position Paper (2023)

The *Bundesamt für Sicherheit in der Informationstechnik* (BSI — Germany's Federal Office for Information Security) published its Zero Trust position paper on June 26, 2023, as its first formal statement on ZT architecture. At approximately 37 pages (plus extensive appendix with full five-pillar maturity tables), it's substantially longer and more technically detailed than Canada's CCCS publications. The document serves three functions: (1) it establishes BSI's formal ZT definition and assessment, (2) it provides a five-pillar integration model with German-specific maturity terminology, and (3) it addresses multi-organizational ZT architectures — a topic that no other national cyber agency publication covers in comparable depth.

**Language caveat:** This analysis is based on the original German text. I have high confidence in structural and conceptual extraction, but legal/regulatory terminology (particularly VS/VSA — *Verschlusssache* / classified information handling) and domain-specific compound nouns may carry meanings not fully transferred to English. Key German terms are preserved in brackets [].

---

## §1: Kernbotschaften — The Seven Core Messages

**Claim 1 —** BSI's seven core messages frame ZT as a preventive, holistic, long-term, resource-intensive, and confidentiality/integrity-focused paradigm → [[bsi-seven-core-messages-frame-zt-preventive]]
---

## §2: The BSI Definition of Zero Trust

**Claim 2 —** BSI provides a formal three-part definition that extends NIST with German regulatory context → [[bsi-provides-formal-three]]
---

## §3: The NIST Reference Architecture Adoption

**Claim 3 —** BSI adopts NIST's PDP/PEP/Control Plane/Data Plane model as its reference architecture → [[bsi-adopts-nist-pdp-pep-control-plane]]
---

## §4: The BSI Five-Pillar Integration Model

**Claim 4 —** BSI's integration model provides a German maturity framework with VS (classified information) integration → [[bsi-integration-model-provides-german-maturity-framework]]
---

## §5: Prerequisites for ZT Integration

**Claim 5 —** BSI specifies five mandatory prerequisites before ZT implementation can begin → [[bsi-specifies-five-mandatory-prerequisites-before-zt]]
---

## §6: Assessment of the ZT Paradigm

**Claim 6 —** BSI provides the most candid government assessment of ZT's limitations → [[bsi-provides-most-candid-government-assessment-zt]]
---

## §7: Real-Time Information Source Integration

**Claim 7 —** BSI is the first national agency to provide detailed guidance on integrating real-time signals into ZT access decisions → [[bsi-first-national-agency-provide-detailed-guidance]]
---

## §8: Cross-Organizational ZT — The BSI's Most Distinctive Contribution

**Claim 8 —** BSI provides the only government framework for multi-organizational ZT architectures → [[bsi-provides-only-government-framework-multi]]
---

## §9: Outlook and Next Steps

**Claim 9 —** BSI plans market surveillance, IT-Grundschutz integration, and sector-specific guidance → [[bsi-plans-market-surveillance]]
---

## §10: BSI vs. Other National Frameworks — Synthesis

| Dimension | BSI (Germany) | CCCS (Canada) | NIST (US) | CISA (US) |
|-----------|---------------|---------------|-----------|-----------|
| **Document type** | Position paper | Management guidance | Technical standard | Maturity model |
| **Length** | ~37pp + extensive appendix | 25pp | 59pp | ~30pp (v1) |
| **Definition basis** | Assume Breach + Least Privilege | NIST verbatim | Seven tenets | Five pillars |
| **Maturity model** | 5 pillars, 3 levels (Klassisch/Fortschrittlich/Ideal) | References CISA | Deployment models (Ch4) | 5 pillars, 3 levels (Traditional/Advanced/Optimal) |
| **Classified info** | Explicit VS integration in all pillars | Not addressed | Not addressed | Not addressed |
| **Multi-org** | Three explicit scenarios | Not addressed | Mentioned as deployment scenario | Not addressed |
| **Real-time signals** | Detailed Shared Signals/CAEP guidance | Not addressed | Not addressed | Not addressed |
| **Availability** | Explicitly de-prioritized | CIA balanced | CIA balanced | CIA balanced |
| **Primary audience** | German federal IT security managers | Canadian government managers | US federal architects | US federal agencies |

---

## Framework Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| 1: Seven core messages frame ZT as preventive, holistic, C/I-focused | MEDIUM | Confidentiality/integrity-over-availability position may not hold for availability-dependent sectors; legal/regulatory nuance lost in translation |
| 2: Three-part definition with verifiable trust emphasis | HIGH | "Reliable proofs" requirement may be unrealizable at scale; probabilistic trust models may be more practical |
| 3: NIST PDP/PEP adoption with Control Plane caveat | HIGH | Control Plane remaining perimeter-based is architecturally inconsistent with pure ZT; may become attack vector |
| 4: Five-pillar integration model with VS integration | MEDIUM | VS requirements may be specific to German law; non-German implementations may not map cleanly; translation uncertainty |
| 5: Five mandatory prerequisites | HIGH | Governance-first approach may delay implementation; some organizations may never clear the prerequisite phase |
| 6: Candid assessment of ZT limitations | HIGH | Centralization-as-vulnerability acknowledgment may discourage ZT adoption in risk-averse organizations |
| 7: Real-time signal integration guidance | MEDIUM | Shared Signals/CAEP standards were drafts at publication; adoption timeline uncertain |
| 8: Three multi-organizational ZT scenarios | MEDIUM | Practical viability depends on legal/organizational factors not fully assessable from text; Scenario 3 may be politically impossible outside hierarchically structured entities |
| 9: Planned market survey and IT-Grundschutz integration | LOW | Unverified as of note creation; these publications may now exist |

**Strongest sections:** §8 (Cross-organizational ZT) and §7 (Real-time signal integration) are unique contributions not found in any other national ZT framework. §6 (Candid assessment of limitations) is the most honest government ZT assessment available. The VS integration in §4 makes the BSI model the only framework applicable to classified information environments.

**Weakest section:** §1 (Kernbotschaften) is appropriately concise for a position paper but doesn't provide the depth that later sections deliver. The seven messages would benefit from expansion — particularly Message 5 (cross-organizational coordination), which is treated as a one-liner in the opening but receives an entire chapter later.

**Key structural observation:** The BSI paper is architecturally the most ambitious national ZT publication. Where NIST defines what ZT is, CISA defines how mature your ZT is, and CCCS defines which framework to use, the BSI defines where ZT is going — toward real-time cross-organizational architectures with integrated classified information handling. This forward-looking orientation makes it essential for the OSKG's "future state" modeling even though much of what it describes is not yet practically achievable.

**Outstanding questions for verification (native German speaker or updated publication):**
1. Has the BSI published the market survey results referenced in §11?
2. Have ZT principles been integrated into IT-Grundschutz as planned?
3. Do the VS-specific requirements in the appendix reflect current VSA regulations?
4. Has any German federal agency published a BSI-model-based ZT implementation case study?
5. Are the Shared Signals Framework and CAEP now ratified standards (they were drafts at publication)?

**Language quality note:** This analysis was conducted on the original German text. I have functional reading comprehension of technical German ZT terminology but cannot certify the accuracy of legal/regulatory translations. The VS-related claims in particular should be validated by a German-speaking security professional familiar with VSA. Key German terms have been preserved in brackets throughout to enable verification.
