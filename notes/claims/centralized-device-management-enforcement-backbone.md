---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-device-pillar
  - topic/zt-device
  - topic/zt-implementation
  - topic/zt-identity
  - topic/zt-governance
claim_id: "nsa-device.6"
statement: "Centralized device management (UEM/MDM) is the enforcement backbone for all other capabilities"
confidence: "high"
confidence_rationale: "HIGH. Without centralized management, the other six capabilities must be implemented per-device or per-platform, which doesn't scale."
claim_type: "implementation"
source_note: "[[NSA — Device Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-device.6: Centralized device management (UEM/MDM) is the enforcement backbone for all other capabilities

**Source:** [[NSA — Device Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the Device Pillar*, 2023

## The Claim

Centralized device management "grants organizations the ability to centrally manage endpoint devices from a single location" and "provides a method for organizations to manage all devices from one central location, regardless of what platform they function in."

## Evidence

NSA cites UEM (Unified Endpoint Management for traditional IT) and MDM (Mobile Device Management for mobile) as the two tooling categories. At Advanced maturity, device integrity verification includes TPM measurements compared against SBOM (Software Bill of Materials) and RIM (Reference Integrity Manifest) — linking centralized management to supply chain integrity.

**Maturity progression:**

| Phase | State |
|-------|-------|
| **Preparation** | None at this level |
| **Basic** | Centralized management confirms compliance status for user devices; reports if a device meets minimum standards |
| **Intermediate** | UEM and MDM integrated with inventory for automated, dynamic inventory combined with compliance management; device integrity values collected from TPM and similar mechanisms |
| **Advanced** | All devices inventoried via automated management; vulnerabilities identified and patched/mitigated automatically; policy enforced through IT remote management of issued mobile devices; device integrity values compared against SBOM and RIM |

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Without centralized management, the other six capabilities must be implemented per-device or per-platform, which doesn't scale.

## Stakes

Centralized management is the enforcement point. Inventory tells you what exists; compliance checking tells you what's wrong; centralized management actually fixes it — pushes configurations, deploys patches, enforces policies, remotely wipes compromised devices. Without it, the device pillar is monitoring without remediation.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
- [[device-policy-enforcement-compliance-monitoring|Policy enforcement and compliance monitoring require centralized management (UEM/MDM) to push policies, collect complian]]
- [[device-inventory-deny-by-default|Real-time deny-by-default enrollment requires centralized management to enforce enrollment decisions and maintain the au]]

**Supports:**
- [[seven-device-capabilities-interdependent|UEM/MDM is explicitly described as 'the enforcement backbone for all other capabilities' — it operationalizes the seven-]]
  - "[[device-policy-enforcement-compliance-monitoring]]"

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The Advanced-level integration of SBOM/RIM with TPM attestation is the most ambitious requirement in the entire pillar. It means every device must not only be managed but cryptographically proven to be running only authorized firmware and software, with an auditable chain from manufacturer to operation. This is the device equivalent of Zero Trust's "verify explicitly" principle applied at the hardware root of trust.
