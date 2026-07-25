---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-governance
  - topic/zt-implementation
  - topic/zt-cloud
  - topic/zt-architecture
claim_id: "gc-ch1-3.8"
statement: "The 14 platform requirements operationalize the principles into verifiable criteria."
confidence: "high"
confidence_rationale: "HIGH. These requirements are directly derived from the principles and form a testable compliance checklist. They map well to CISA's maturity model"
claim_type: "governance"
source_note: "[[Garbis and Chapman — Ch1-3 — Introduction and Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-ch1-3.8: The 14 platform requirements operationalize the principles into verifiable criteria.

**Source:** [[Garbis and Chapman — Ch1-3 — Introduction and Architecture]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"Our goal in this section is not to simply restate the principles, but to attempt to highlight relevant aspects from a platform perspective."

## Evidence

**Key requirements (selected):**

- Data plane communications must be encrypted (Req 1)
- Enforce access controls for all resource types, driven by identity-centric and contextual policies (Req 2)
- Consistent policy for remote and on-premises users (Req 4)
- Device posture inspection prior to access and periodically thereafter (Req 5)
- Distinguish BYOD from corporate-managed devices (Req 6)
- Access to any network resource must be explicitly granted by policy — no inherent broad access (Req 7)
- Distinguish between services on the same network resource (e.g., HTTPS vs. SSH) (Req 8)
- Network traffic metadata must be logged and enriched with identity context (Req 10)
- Workloads in the cloud must have same access control policies as on-premises (Req 12)
- Automation must include identity-centric details for effective incident response (Req 13)

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These requirements are directly derived from the principles and form a testable compliance checklist. They map well to CISA's maturity model capabilities and NIST's logical components.

## Stakes

A platform that fails any of these requirements is not a ZT platform under this definition. These requirements are the bridge between principles and procurement.

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

Requirement 7 ("access to any network resource must be explicitly granted by policy") is the most transformative — it's the operational death certificate for default-allow network architectures. Requirement 8 (service-level distinction) is the most technically revealing — it exposes the weakness of IP-address-based firewall rules when multiple services share an IP.
