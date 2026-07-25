---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-threats
  - topic/zt-monitoring
claim_id: "nist207-ch5.5"
statement: "The monitoring data and policy management tools that enable ZTA's contextual policies become high-value reconnaissance targets — compromising them reveals which accounts have access to which resources, enabling attackers to prioritize targets."
confidence: "high"
confidence_rationale: "HIGH. This is a well-understood risk — security data as target is a pattern recognized across frameworks, not unique to ZTA. **Cross-reference"
claim_type: "threat"
source_note: "[[NIST 800-207 — Ch5 — Threats]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch5.5: The monitoring data and policy management tools that enable ZTA's contextual policies become high-value reconnaissance targets — compromising them reveals which accounts have access to which resources, enabling attackers to prioritize targets.

**Source:** [[NIST 800-207 — Ch5 — Threats]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

The monitoring data that enables ZTA's contextual policies becomes a high-value target for attackers. (§5.5)

## Evidence

- Network traffic scans, metadata, and logs stored for forensics or analysis
- Network diagrams, configuration files, and architecture documents
- The **management tool used to encode access policies** — this reveals which accounts have access to which resources, effectively telling an attacker which accounts are most valuable to compromise

- Most restrictive access policies for security data
- Accessible only from designated/dedicated administrator accounts
- Same protections as any valuable enterprise data, but heightened because of the reconnaissance value

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is a well-understood risk — security data as target is a pattern recognized across frameworks, not unique to ZTA.

**Cross-reference — Gilman & Barth**

Gilman & Barth's "Control Plane Security" section warns that compromising a data store housing historical access data lets an attacker "artificially raise their level of trust by falsifying access patterns" — a subtler attack than compromising the policy engine but still dangerous. This maps directly to NIST's concern about the management tool and stored traffic data being recon targets.

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

## Assessment

_Not addressed separately in the source note._
