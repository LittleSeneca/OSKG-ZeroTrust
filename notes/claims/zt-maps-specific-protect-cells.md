---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/yu-cdm
  - topic/zt-architecture
  - topic/zt-definition
  - topic/zt-network
  - topic/zt-governance
claim_id: "yu-cdm.4"
statement: "ZT maps to specific PROTECT cells — not the whole matrix"
confidence: "high"
confidence_rationale: "HIGH. This mapping is Yu's most significant contribution to ZT discourse — it shows exactly where ZT fits and, more importantly, what it doesn't"
claim_type: "architectural"
source_note: "[[Yu — Cyber Defense Matrix]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# yu-cdm.4: ZT maps to specific PROTECT cells — not the whole matrix

**Source:** [[Yu — Cyber Defense Matrix]] — Sounil Yu, *Cyber Defense Matrix*, 2022

## The Claim

Zero Trust is a design pattern for PROTECT, not a complete security framework. The ZT access proxy maps to three boxes: DEVICE-PROTECT, NETWORK-PROTECT, and APPLICATION-PROTECT. A DATA-PROTECT access proxy (Data Access Security Broker) is emerging. There is no USER-PROTECT access proxy because users are subjects, not resources — "a good executive assistant does the job well."

## Evidence

Yu maps the old perimeter-based model (single trust boundary at NETWORK G, implicit transitive trust to all internal assets) against the ZT model (each resource has its own trust boundary, identity assertions are verified by an access proxy before granting access to that specific resource). He shows how ZTNA (NETWORK-PROTECT), ZTAA (APPLICATION-PROTECT), and ZTDA (DEVICE-PROTECT) are distinct patterns within the same PROTECT column. Identity attributes for establishing trustworthiness come from multiple asset classes: DEVICE-IDENTIFY (certs, patch level), NETWORK-IDENTIFY (IP, identity-based IP), APPLICATION-IDENTIFY (mTLS certs, API keys), DATA-IDENTIFY (hashes, classifications), USER-IDENTIFY (passwords, tokens, 2FA, location).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This mapping is Yu's most significant contribution to ZT discourse — it shows exactly where ZT fits and, more importantly, what it doesn't cover. ZT is not IDENTIFY (though it consumes IDENTIFY outputs). ZT is not DETECT (continuous monitoring is an input to policy decisions, but the access proxy itself is a PROTECT mechanism).

## Stakes

Vendors and frameworks that claim ZT is a "comprehensive security strategy" are claiming coverage of cells they don't occupy. The Cyber Defense Matrix exposes this — if your ZT strategy doesn't address DETECT and RESPOND for each asset class, you have gaps. ZT is necessary but not sufficient.

## Disagreement

**Who disagrees:**

Forrester's ZTX framework treats ZT as spanning all seven pillars, including detect and respond functions. CISA's ZT Maturity Model includes visibility and analytics capabilities that edge into DETECT territory. Yu would argue these are consumed by ZT policies but are not themselves ZT.

**Alternative reading:**

One could argue that continuous verification (a ZT hallmark) *is* a form of DETECT — you're detecting changes in trustworthiness. Yu would counter that this is still PROTECT: you're making access decisions based on observed state, not investigating incidents.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[grid-most-parsimonious-complete-map-cybersecurity|grid-most-parsimonious-complete-map-cybersecurity]]

## Assessment

This precise mapping is the single most valuable thing the Cyber Defense Matrix contributes to OSKG-ZeroTrust. It prevents ZT scope creep while showing how ZT integrates with the rest of the security ecosystem. Every ZT note in this project should be traceable to specific cells in this matrix.
