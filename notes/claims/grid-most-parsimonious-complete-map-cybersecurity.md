---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/yu-cdm
  - topic/zt-architecture
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-policy
claim_id: "yu-cdm.1"
statement: "The 5×5 grid is the most parsimonious complete map of cybersecurity"
confidence: "high"
confidence_rationale: "HIGH. The framework has been widely adopted in the practitioner community and maps cleanly to every major ZT standard. The NIST CSF functions are the"
claim_type: "architectural"
source_note: "[[Yu — Cyber Defense Matrix]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# yu-cdm.1: The 5×5 grid is the most parsimonious complete map of cybersecurity

**Source:** [[Yu — Cyber Defense Matrix]] — Sounil Yu, *Cyber Defense Matrix*, 2022

## The Claim

The Cyber Defense Matrix is a MECE representation — every security capability maps to exactly one cell, and the 25 cells collectively cover the entire defensive landscape. The five NIST CSF functions (IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) × five asset classes (DEVICES, NETWORKS, APPLICATIONS, DATA, USERS) = 25 boxes, and "every defensive function against every kind of asset that needs defending" lands in one of them.

## Evidence

The matrix emerged from Yu's practical need as Chief Security Scientist at Bank of America — evaluating hundreds of security startups against a complex enterprise portfolio with no common framework. The grid's simplicity is its strength: it forces practitioners to answer two questions about every capability — *what does it do?* (the function) and *to what?* (the asset class). The internal consistency rules (e.g., IDENTIFY is always left-of-boom, DETECT is always right-of-boom) prevent definitional drift.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The framework has been widely adopted in the practitioner community and maps cleanly to every major ZT standard. The NIST CSF functions are the closest thing cybersecurity has to a universal taxonomy.

## Stakes

Without a MECE framework, organizations can't systematically assess coverage gaps. Vendors exploit the ambiguity — a product that "detects" threats against devices vs. networks vs. data may overlap in ways that look like defense-in-depth but are actually redundant spending on one cell while leaving others empty.

## Disagreement

**Who disagrees:**

MITRE ATT&CK maps the *offensive* landscape (tactics × techniques) rather than the defensive one — complementary, not competing. Forrester's ZTX framework defines seven pillars but doesn't enforce mutual exclusivity. Gartner's CARTA focuses on dynamic risk assessment rather than capability mapping. The Cyber Defense Matrix is unique in its MECE rigor.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The matrix earns its place as a Tier 4 OSKG-ZeroTrust source precisely because it situates ZT within the full landscape. ZT is not the whole answer — it's one design pattern occupying specific cells. Understanding which cells those are (and which are not) is essential for avoiding ZT scope creep.
