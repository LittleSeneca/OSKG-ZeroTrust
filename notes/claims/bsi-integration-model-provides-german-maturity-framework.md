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
claim_id: "bsi-zt.4"
statement: "BSI's integration model provides a German maturity framework with VS (classified information) integration"
confidence: "high"
confidence_rationale: "HIGH for structural elements. MEDIUM for VS-specific maturity descriptions — German classified information handling law (*VSA /"
claim_type: "definitional"
source_note: "[[BSI — Zero Trust Position Paper]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# bsi-zt.4: BSI's integration model provides a German maturity framework with VS (classified information) integration

**Source:** [[BSI — Zero Trust Position Paper]] — BSI, *Zero Trust Position Paper*, 2023

## The Claim

The BSI proposes a five-pillar integration model (*Integrationsmodell*) structured around:

| Pillar (German) | Pillar (English) | Description |
|-----------------|------------------|-------------|
| Identität | Identity | Users and their logical/technical identities; authentication, authorization, identity provider, identity lifecycle |
| Gerät | Device | Physical or virtualized hardware connecting to networks; compliance, inventory, security posture |
| Netz | Network | Communication channels to be controlled, segmented, and protected |
| Anwendung | Application | Systems, programs, services executed on-premises and in cloud; access decisions, threat protection integration |
| Daten | Data | Protection across devices, networks, applications, cloud; inventory, categorization, encryption |

## Evidence

**Two cross-cutting functions:**

*Detektion & Reaktion* (Detection & Response) spans Identity, Device, Network, and Application. *Anforderungen an VS* (Requirements for Classified Information) spans **all five pillars** — this is unique to the BSI model.

**Three maturity levels:**

| Level (German) | Level (English) | Description |
|----------------|-----------------|-------------|
| Klassisch (KL) | Classical/Traditional | Manual configurations, static policies, pillar-level solutions, coarse dependencies, limited visibility |
| Fortschrittlich (FO) | Advanced | Cross-pillar coordination, centralized visibility, centralized identity control, cross-pillar policy enforcement, pre-defined mitigations |
| Ideal (ID) | Ideal/Optimal | Fully automated attribute assignment, dynamic policies based on automated triggers, open standards for cross-pillar interoperability, centralized visibility with historian functionality |

## Confidence

**Rating:** HIGH
**Rationale:** HIGH for structural elements. MEDIUM for VS-specific maturity descriptions — German classified information handling law (*VSA / Verschlusssachenanweisung*) has specific requirements that I cannot fully assess in English translation.

## Stakes

The VS integration makes this the only national ZT framework that explicitly addresses classified information handling. For German government agencies handling VS-NfD (*Verschlusssache — Nur für den Dienstgebrauch*, roughly equivalent to "For Official Use Only") or higher classifications, this may be the *only* applicable ZT framework — NIST and CISA don't address US classified information handling in their ZT publications.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[bsi-provides-only-government-framework-multi|The VS (classified information) integration in bsi-zt.4 implies multi-organizational scope across government and contrac]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The VS integration is the BSI model's most distinctive feature. The appendix provides detailed maturity tables where every pillar function includes an "Anforderungen an VS" row specifying classified information requirements at each maturity level. For example, in the Identity pillar: at Klassisch level, perimeter-based VS control; at Fortschrittlich, ZT identities used to enforce need-to-know; at Ideal, products with BSI approval (*Zulassungsaussage des BSI*) handle VS access, with access rights initially granted only to the creator and explicitly extended. This is genuinely novel and has no equivalent in any other national ZT framework.
