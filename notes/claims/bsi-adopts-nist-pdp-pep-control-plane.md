---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/bsi
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-identity
  - topic/zt-architecture
claim_id: "bsi-zt.3"
statement: "BSI adopts NIST's PDP/PEP/Control Plane/Data Plane model as its reference architecture"
confidence: "high"
confidence_rationale: "HIGH. This is a straightforward adoption of NIST with minor extensions."
claim_type: "definitional"
source_note: "[[BSI — Zero Trust Position Paper]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# bsi-zt.3: BSI adopts NIST's PDP/PEP/Control Plane/Data Plane model as its reference architecture

**Source:** [[BSI — Zero Trust Position Paper]] — BSI, *Zero Trust Position Paper*, 2023

## The Claim

The BSI explicitly adopts NIST SP 800-207's logical architecture as its reference model, with PDP (*Policy Decision Point*, comprising PE/Policy Engine and PA/Policy Administrator), PEP (*Policy Enforcement Point*), and Control Plane/Data Plane separation.

## Evidence

**Key architectural positions:**

- **PDP can be locally hosted or a service from a third party** (*"kann dabei ein lokaler Bestandteil des Unternehmens oder ein extern gehosteter Dienst sein"*) — a more explicit acceptance of external/cloud PDP than NIST, which is more cautious about external trust engines
- **The Control Plane (administration of IT systems) continues to rely primarily on perimeter-based security**, while ZT principles are only enforced in the Data Plane (*"Die Zero Trust-Prinzipien werden dabei nur in der 'Data Plane' wirksam umgesetzt, während die 'Control Plane' [...] weiterhin vorwiegend auf Basis eines Perimeter-Modells abgesichert wird"*)
- **No fixed requirements for which information sources the PDP must consult** — the PDP needs a "good, organizationally-specific relevant information foundation for evaluation"
- **Central components (identity management, PDP, certificate management, inventories, central detection) are critical elements requiring special protection** in all three security objectives (C, I, A)

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is a straightforward adoption of NIST with minor extensions.

## Stakes

The admission that the Control Plane remains perimeter-based is honest but creates an architectural tension: if an attacker compromises the Control Plane (through perimeter vulnerabilities), they own the ZT infrastructure even though the Data Plane is ZT-protected. This is a known limitation of all current ZT architectures — the BSI's explicit acknowledgment is valuable.

## Disagreement

**Who disagrees:**

_None identified._

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

The BSI's treatment of the Control Plane vulnerability is more candid than NIST's. By stating that the Control Plane *will* remain perimeter-based, the BSI implicitly acknowledges that current ZT architectures cannot fully eliminate perimeter thinking — they just push it to the management plane. This is a realistic assessment that other frameworks either elide or treat as a temporary condition.
