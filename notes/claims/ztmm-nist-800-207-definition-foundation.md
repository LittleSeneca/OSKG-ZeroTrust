---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-identity
  - topic/zt-implementation
claim_id: "cisa-ztmm-ov.3"
statement: "The ZTMM is built on NIST SP 800-207's operative definition — zero trust minimizes uncertainty, not risk"
confidence: "high"
confidence_rationale: "VERY HIGH. This is a direct quote from the authoritative source. The ZTMM doesn't innovate on the definition — it inherits it and builds the"
claim_type: "definitional"
source_note: "[[CISA ZTMM — Overview and Framework]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-ov.3: The ZTMM is built on NIST SP 800-207's operative definition — zero trust minimizes uncertainty, not risk

**Source:** [[CISA ZTMM — Overview and Framework]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

The document reproduces NIST SP 800-207's definition verbatim: "Zero trust provides a collection of concepts and ideas designed to minimize uncertainty in enforcing accurate, least privilege per-request access decisions... in the face of a network viewed as compromised." It also cites the NSTAC description: "a cybersecurity strategy premised on the idea that no user or asset is to be implicitly trusted."

## Evidence

The definition is quoted directly with the exact NIST SP 800-207 citation. The document synthesizes both NIST's formal definition and NSTAC's operational description, establishing a dual foundation: NIST provides the conceptual framework, NSTAC provides the operational framing ("assume breach, continual verification").

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This is a direct quote from the authoritative source. The ZTMM doesn't innovate on the definition — it inherits it and builds the assessment framework on top.

## Stakes

The ZTMM's legitimacy depends on its fidelity to NIST 800-207. If it diverges, agencies face conflicting guidance. If it faithfully extends NIST, it benefits from NIST's authority. The document's extensive NIST citations signal that CISA sees itself as an implementer, not a reinventor.

## Disagreement

**Who disagrees:**

ForgeRock's ZTX framework (2018, Cunningham) defines ZT across seven pillars including Automation & Orchestration as a separate dimension. The NSTAC report (2022) emphasizes identity management more heavily than NIST 800-207. These are differences in emphasis, not contradiction.

**Alternative reading:**

The document could be read as cherry-picking from NIST — using the definition but not NIST's full component model (Policy Engine, Policy Administrator, Policy Enforcement Point). The ZTMM's pillar-based structure is closer to ZTX than to NIST 800-207's logical component architecture. This is a structural choice, not a fidelity violation — the pillars are an assessment framework, not an architecture specification.

## Edges

**Depends on:**

**Supports:**
- [[location-centric-to-identity-data-centric-shift|The NIST definition of minimizing uncertainty rather than trusting location provides the conceptual basis for the locati]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The ZTMM sits between NIST 800-207 (architecture) and ZTX (assessment) — it uses NIST's definition but ZTX's pillar structure. This is a practical synthesis that serves its purpose: giving agencies measurable capabilities to assess. The NIST component model appears in the background as the target architecture, but the ZTMM doesn't require agencies to implement specific components.
