---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-migration
  - topic/zt-device
claim_id: "nist207-ch7.6"
statement: "The enterprise must identify, catalog, and continuously monitor all assets — hardware, digital artifacts, virtual infrastructure, and shadow IT — because device posture assessment is integral to access decisions and incomplete inventory causes access denials."
confidence: "high"
confidence_rationale: "HIGH. Asset inventory as prerequisite is consistent across NIST, CISA, and DoD frameworks."
claim_type: "migration"
source_note: "[[NIST 800-207 — Ch7 — Migration]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch7.6: The enterprise must identify, catalog, and continuously monitor all assets — hardware, digital artifacts, virtual infrastructure, and shadow IT — because device posture assessment is integral to access decisions and incomplete inventory causes access denials.

**Source:** [[NIST 800-207 — Ch7 — Migration]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

ZTA requires the ability to **identify and manage devices** — both enterprise-owned and non-enterprise-owned (BYOD, collaborator assets) that access enterprise resources. (§7.3.2)

## Evidence

| Category | Examples |
|----------|----------|
| **Hardware** | Laptops, phones, IoT devices, servers |
| **Digital artifacts** | User accounts, applications, digital certificates, virtual assets, containers |
| **Physical location** | As best estimated |
| **Network location** | Observed and tracked |

- Beyond cataloging, the enterprise must have **configuration management and monitoring** — the ability to observe the current state of an asset.
- **Shadow IT** presents a special problem: certain ZTA approaches (mainly network-based) may cause shadow IT components to become **unusable** because they are not known and included in network access policies.
- **Federal context:** Agencies with CDM program capabilities (HWAM, SWAM) already have a rich data set. High Value Assets (HVA) identified under [[OMB M-19-03]] provide ZTA candidate lists.

**Cross-reference:**

Gilman & Barth's [[Zero Trust Networks]] emphasizes that device identity and trust are co-equal to user identity. Green-Ortiz et al.'s [[Zero Trust Architecture]] adds the cloud-native dimension: asset inventory now includes containers, serverless functions, and ephemeral compute that may exist for minutes.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Asset inventory as prerequisite is consistent across NIST, CISA, and DoD frameworks.

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
  - [[cdm-visibility-prerequisite-zta]]

## Assessment

_Not addressed separately in the source note._
