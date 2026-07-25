---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/ncsc
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-migration
claim_id: "ncsc.6"
statement: "Google's ZT architecture explicitly supports hybrid environments — on-premises applications can be secured through IAP connectors without requiring cloud migration."
confidence: "high"
confidence_rationale: "HIGH. The IAP connector for on-premises applications is a documented, available feature. It addresses the most common ZT deployment challenge: legacy"
claim_type: "implementation"
source_note: "[[NCSC — ZT Principles on Google Cloud]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# ncsc.6: Google's ZT architecture explicitly supports hybrid environments — on-premises applications can be secured through IAP connectors without requiring cloud migration.

**Source:** [[NCSC — ZT Principles on Google Cloud]] — NCSC, *Zero Trust Principles on Google Cloud*, 2023

## The Claim

"BeyondCorp Enterprise customers can secure HTTP or HTTPS based on-premises applications (outside of Google Cloud) with Identity-Aware Proxy (IAP) by deploying a connector. When a request is made for an on-premises app, IAP authenticates and authorizes the user request and then routes the request to the connector."

## Evidence

The connector model allows organizations to apply ZT controls (identity-aware proxy, context-aware access, continuous evaluation) to on-premises applications without migrating them to GCP. Google's "Open Cloud" approach emphasizes partner ecosystem integration rather than lock-in.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The IAP connector for on-premises applications is a documented, available feature. It addresses the most common ZT deployment challenge: legacy applications that can't be immediately migrated.

## Stakes

The hybrid support claim is critical for enterprise adoption. Organizations with significant on-premises investment can't adopt GCP ZT if it requires full cloud migration first. The connector model enables incremental adoption: secure on-premises apps with ZT today, migrate at your own pace.

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

The hybrid connector model is strategically important — it positions GCP ZT as an overlay that can secure existing infrastructure, not just cloud-native workloads. However, the limitation to "HTTP or HTTPS based" applications is significant. Non-web legacy applications (thick clients, custom protocols, industrial control systems) still require alternative ZT approaches. Google's Professional Services offerings (Zero Trust Foundations, Cloud Deploy: Zero Trust) suggest that the connector model is a starting point, not a complete solution for all legacy applications.
