---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-device-pillar
  - topic/zt-device
  - topic/zt-inventory
  - topic/zt-identity
  - topic/zt-architecture
claim_id: "nsa-device.2"
statement: "Device Inventory progresses from manual lists to real-time, deny-by-default enrollment"
confidence: "high"
confidence_rationale: "HIGH. Inventory as the foundation of device trust is universally accepted across ZT standards (NIST 800-207 Tenet 5, CISA ZTMM v2 Device pillar"
claim_type: "implementation"
source_note: "[[NSA — Device Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-device.2: Device Inventory progresses from manual lists to real-time, deny-by-default enrollment

**Source:** [[NSA — Device Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the Device Pillar*, 2023

## The Claim

"Knowing what is in an organization's environment is a foundation to establishing trust." A complete inventory of registered devices that are allowed to access enterprise resources enables a "deny all" by default environment.

## Evidence

NSA emphasizes that devices present cybersecurity risks differently — user devices leveraging session access protocols vs. resource devices hosting applications vs. embedded service devices. The inventory solution must distinguish device types and roles.

**Maturity progression:**

| Phase | State |
|-------|-------|
| **Preparation** | Manual inventory; may be based on multiple partial inventories from disparate systems |
| **Basic** | Complete list in separate inventories; planning for NPE (Non-Person Entity) PKI certificates started; specific capabilities identified for new acquisitions |
| **Intermediate** | Standardized device attributes and version information; NPE certificate authentication mostly implemented with "deny all, allow by exception"; specific make/model/revisions eligible for acquisition; automation begins to unify disparate inventories |
| **Advanced** | Complete inventory updated in real time via NPE certificates; only approved devices allowed, all others denied by default; acceptance process checks all new devices; deprovisioning process sanitizes retired devices |

**Key procurement implications:**

NSA specifies that inventory governance must cover the full lifecycle: procurement criteria (TPM certificates, firmware configuration, component revisions), acceptance testing (SBOM, Reference Integrity Manifest, TPM Platform Certificate for auditable supply chain chain of custody, per NIST SP 800-161), and deprovisioning (secure erase storage, factory reset firmware, erase TPM NVRAM, reset BMC, remove UEFI Secure Boot modifications).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Inventory as the foundation of device trust is universally accepted across ZT standards (NIST 800-207 Tenet 5, CISA ZTMM v2 Device pillar function 1).

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

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
  - "[[asset-supply-chain-risk-management]]"

## Assessment

The advanced-level emphasis on real-time updates and full lifecycle governance (procure → accept → operate → deprovision) is NSA's most distinctive contribution here. Most organizations stop at "we have a CMDB." NSA says: real-time, NPE-certificate-backed, with supply chain integrity artifacts at acquisition and forensic sanitization at retirement. This is an exceptionally high bar.
