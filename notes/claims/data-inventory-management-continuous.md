---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-data
  - topic/zt-inventory
  - topic/zt-maturity
  - topic/zt-governance
claim_id: "cisa-ztmm-dnad.17"
statement: "Data Inventory Management — maturity progresses from manual identification and inventory of some agency data to continuous inventory of all applicable agency data with robust data loss prevention strategies that dynamically block suspected data exfiltration."
confidence: "high"
confidence_rationale: "HIGH. Direct from the source document."
claim_type: "implementation"
source_note: "[[CISA ZTMM — Device Network App Data Pillars]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-dnad.17: Data Inventory Management — maturity progresses from manual identification and inventory of some agency data to continuous inventory of all applicable agency data with robust data loss prevention strategies that dynamically block suspected data exfiltration.

**Source:** [[CISA ZTMM — Device Network App Data Pillars]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

Data inventory is foundational — you can't protect what you don't know exists. (§5.5)

## Evidence

| Stage | Description |
|-------|-------------|
| **Traditional** | Manually identifies and inventories some agency data (e.g., mission-critical data). |
| **Initial** | Begins automating data inventory processes for on-premises and cloud environments, covering most agency data; begins incorporating protections against data loss. |
| **Advanced** | Automates data inventory and tracking enterprise-wide, covering all applicable agency data; data loss prevention strategies based on static attributes and/or labels. |
| **Optimal** | Continuously inventories all applicable agency data; robust data loss prevention strategies that dynamically block suspected data exfiltration. |

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Direct from the source document.

## Stakes

_Not addressed separately in the source note._

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[data-centric-security-abac-protection|DLP (Data Loss Prevention), one of the four ABAC protection mechanisms, monitors for data exfiltration. Continuous inven]]
- [[data-categorization-automated-labeling|You must know what data exists before you can categorize it. Continuous data inventory is the foundational discovery lay]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
