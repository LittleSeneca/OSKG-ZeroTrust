---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-definition
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-access-mgmt
claim_id: "finney-ch4-7.11"
statement: "Incident response must follow ZT principles, and the NIST Cybersecurity Framework provides a timeline-based structure that maps cleanly to ZT protect surfaces."
confidence: "high"
confidence_rationale: "HIGH. The NIST CSF mapping is standard. The novel contribution is treating the IR process itself through a ZT lens — scoping access, removing"
claim_type: "definitional"
source_note: "[[Finney — Ch4-7 — Building the ZT Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch4-7.11: Incident response must follow ZT principles, and the NIST Cybersecurity Framework provides a timeline-based structure that maps cleanly to ZT protect surfaces.

**Source:** [[Finney — Ch4-7 — Building the ZT Strategy]] — George Finney, *Project Zero Trust*, 2022

## The Claim

The NIST CSF five functions (Identify, Protect, Detect, Respond, Recover) map to a pre-incident/post-incident timeline. ZT applies across the entire timeline — not just to the pre-incident phases.

## Evidence

The chapter presents both the NIST CSF and NIST SP 800-61 (Incident Handling Guide) as frameworks. When Dylan asks whether a compromised computer should be powered off or monitored ("Do we monitor the compromised computer to see what other devices it may be connecting to?"), Luis walks through the Containment/Eradication/Recovery considerations: potential damage, data theft risk, evidence preservation, impact on critical services, resource availability, and the permanence risk of emergency workarounds.

Aaron's final phone call adds: "You need to incorporate Zero Trust into the incident response process itself." The implication: every step of IR — who is authorized to declare an incident, who can isolate systems, who can access forensic data, who approves recovery — requires ZT policies. The CSIRT team interacts with the SOC as a protect surface.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The NIST CSF mapping is standard. The novel contribution is treating the IR process itself through a ZT lens — scoping access, removing implicit trust from IR workflows, applying the five-step methodology to incident response as its own protect surface.

## Stakes

IR processes that operate with implicit trust (any CSIRT member can isolate any system, forensic data is shared without access controls, recovery procedures bypass normal change control) create opportunities for attackers who've compromised IR credentials or for insider threats. And yet almost no organizations apply ZT to their IR process.

## Disagreement

**Who disagrees:**

Incident responders often argue that speed is paramount and that ZT-style access controls introduce friction during time-critical responses. The ZT response: access can be pre-provisioned, scoped to specific systems, and triggered by incident declaration — it doesn't require manual approval during an active incident.

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

The IR-as-protect-surface insight is Finney's most forward-looking contribution in this section. It's underdeveloped in the chapter (Aaron raises it in a brief phone call and it's not fully explored), but the seed is planted: every process that touches a ZT environment must itself be subject to ZT principles, including the processes designed to respond to ZT failures.
