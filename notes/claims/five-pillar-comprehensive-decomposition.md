---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-architecture
  - topic/zt-governance
claim_id: "cisa-ztmm-ov.6"
statement: "The five-pillar structure provides a comprehensive, independently-assessable decomposition of ZTA"
confidence: "high"
confidence_rationale: "HIGH. The pillar structure is adopted from the ACT-IAC Zero Trust Cybersecurity Current Trends report (2019), which itself derives from Forrester's"
claim_type: "architectural"
source_note: "[[CISA ZTMM — Overview and Framework]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-ov.6: The five-pillar structure provides a comprehensive, independently-assessable decomposition of ZTA

**Source:** [[CISA ZTMM — Overview and Framework]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

The ZTMM organizes zero trust into five distinct pillars: Identity, Devices, Networks, Applications and Workloads, and Data. "Each pillar can progress at its own pace and may progress more quickly than others until cross-pillar coordination is required."

## Evidence

Each pillar gets its own detailed function table with maturity-level descriptions for each function (e.g., Identity has Authentication, Identity Stores, Risk Assessment, Access Management). The pillar definitions are:

- **Identity** (5.1): "An attribute or set of attributes that uniquely describes an agency user or entity, including non-person entities." Functions: authentication, identity stores, risk assessment, access management.
- **Devices** (5.2): "Any asset (including its hardware, software, firmware, etc.) that can connect to a network." Functions: policy enforcement & compliance monitoring, asset & supply chain risk management, resource access.
- **Networks** (5.3): "An open communications medium including internal networks, wireless networks, and the Internet." Functions: network segmentation, traffic management, traffic encryption, network resilience.
- **Applications and Workloads** (5.4): "Systems, computer programs, and services that execute on-premises, on mobile devices, and in cloud environments." Functions: application access, application threat protection, accessible applications, secure application development and deployment.
- **Data** (5.5): "All structured and unstructured files and fragments... as well as associated metadata." Functions: data inventory management, data categorization, data availability, data access.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The pillar structure is adopted from the ACT-IAC Zero Trust Cybersecurity Current Trends report (2019), which itself derives from Forrester's ZTX framework. It has proven durable — OMB M-22-09 organizes its requirements by the same pillars, and DoD's ZT Strategy uses a compatible (though not identical) decomposition.

## Stakes

If the pillars are mutually independent, agencies can optimize investments per pillar. If they're tightly coupled (which the document acknowledges: "cross-pillar coordination is required"), then pillar-by-pillar optimization produces suboptimal architectures. The tension between pillar independence and cross-pillar coordination is the central design challenge of the ZTMM.

## Disagreement

**Who disagrees:**

NIST 800-207 doesn't use pillars at all — it uses logical components (PE, PA, PEP) and three approach variations. Microsoft's ZT framework uses six pillars (adding Infrastructure). Forrester ZTX uses seven. The exact pillar count is less important than the recognition that ZTA is multi-dimensional.

**Alternative reading:**

The five-pillar structure could be seen as artificially decomposing what is fundamentally a unified architecture. The "cross-cutting capabilities" section partially addresses this by providing integration mechanisms, but the pillar-by-pillar maturity tables still encourage siloed assessment.

## Edges

**Depends on:**
  - "[[ztmm-nist-800-207-definition-foundation]]"

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The pillar structure is a practical assessment tool, not an architecture specification. It works because it mirrors how federal agencies are organized (IAM team, Network team, AppDev team, etc.), making it actionable for existing organizational structures. The real risk is pillar-level optimization without cross-pillar coordination — the document warns about this but doesn't provide a strong enforcement mechanism.
