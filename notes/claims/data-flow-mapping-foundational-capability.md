---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-network-pillar
  - topic/zt-network
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-migration
claim_id: "nsa-network.2"
statement: "Data flow mapping is the foundational capability — you can't segment what you don't understand"
confidence: "high"
confidence_rationale: "HIGH. This claim is logically sound and practically validated — data flow mapping is a prerequisite for any network segmentation effort. The maturity"
claim_type: "implementation"
source_note: "[[NSA — Network Environment Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-network.2: Data flow mapping is the foundational capability — you can't segment what you don't understand

**Source:** [[NSA — Network Environment Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the Network and Environment Pillar*, 2024

## The Claim

"Data flow mapping identifies the route data travels within an organization and describes how that data transforms from one location or application to another." It is "foundational for other network activities, such as macro and micro segmentation," and "aids in efficiently identifying anomalous traffic behavior via analytics."

## Evidence

Four-phase maturity progression:

| Phase | Capability |
|-------|-----------|
| **Preparation** | Identify locations where data is stored and processed, and in which state the data components are stored. |
| **Basic** | Begin mapping physical and logical data flows. Mapping is primarily manual. Transition unencrypted flows to encrypted flows or within encrypted tunnels/protocols. |
| **Intermediate** | Complete list of applications; critical data flows identified. Some automation maintains mapping accuracy. Anomalous data flows isolated or eliminated. |
| **Advanced** | Complete inventory of all data flows. Automation monitors for controls and mitigates all current, new, or anomalous data flows. |

**Cross-reference to CISA:**

CISA's Network pillar does not explicitly separate "data flow mapping" as a standalone function — it's embedded within the Network Segmentation function's maturity progression. NSA's treatment is more granular. CISA's cross-cutting Visibility & Analytics capability covers the monitoring dimension that NSA ties directly to data flow mapping: at the Optimal level, CISA calls for "visibility into communication across all agency networks and environments."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This claim is logically sound and practically validated — data flow mapping is a prerequisite for any network segmentation effort. The maturity model correctly identifies the manual-to-automated trajectory and the critical Intermediate milestone of identifying anomalous flows.

## Stakes

If data flow mapping is incomplete, segmentation boundaries will be wrong — either too permissive (leaving lateral movement paths open) or too restrictive (breaking legitimate workflows). The NSA's emphasis on encryption discovery during mapping is particularly important: flows that aren't encrypted in transit represent a compounding risk (data exposed + lateral movement path available).

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
- [[sequential-network-maturity-journey|The maturity journey explicitly builds on data flow mapping as its foundation: 'you cannot segment without understanding]]
  - "[[network-segmentation-micro-perimeters]]"

**Supports:**
- [[macro-segmentation-cross-function|'You can't segment what you don't understand' — data flow mapping is the prerequisite that enables effective macro segme]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

This is the most underappreciated capability in the document. Every organization that has attempted network segmentation has discovered that their data flow documentation is incomplete — and that discovering actual flows (vs. documented flows) reveals shadow IT, legacy interconnections, and forgotten VPN tunnels. NSA's placement of data flow mapping as Capability #1, before any discussion of segmentation, is architecturally correct.
