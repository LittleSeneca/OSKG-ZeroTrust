---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/practitioner
  - source/gilman-barth
  - topic/zt-network
  - topic/zt-definition
  - topic/zt-implementation
  - topic/zt-architecture
claim_id: "gilmanbarth-ch1.3"
statement: "The perimeter model's history reveals why it failed — it was an accident, not a design"
confidence: "high"
confidence_rationale: "HIGH. The history is well-documented and matches the IETF RFC record. The interpretative claim — that perimeter security was accidental — is stronger "
claim_type: "definitional"
source_note: "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---

# gilmanbarth-ch1.3: The perimeter model's history reveals why it failed — it was an accident, not a design

**Source:** [[Gilman and Barth — Ch1 — Zero Trust Fundamentals]] — Evan Gilman, Doug Barth, *Zero Trust Networks: Building Secure Systems in Untrusted Networks*, 2017

## The Claim

The perimeter model is a historical accident driven by three events: (1) RFC 1597 creating private address space that was "fundamentally incapable of joining other networks," (2) the DMZ emerging as a side effect of connecting mail servers to the internet, (3) NAT inadvertently providing firewall-like properties that made perimeter enforcement feel "secure."

## Evidence

A detailed historical narrative from Joe Postel's IP registry (1982) through RFC 1597 (1994), RFC 1631 NAT (1994), to the modern perimeter firewall. The key insight: "Private networks were more secure, because they were fundamentally incapable of joining other networks." Security was a side effect of isolation, not a designed property.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The history is well-documented and matches the IETF RFC record. The interpretative claim — that perimeter security was accidental — is stronger 

## Stakes

If perimeter security was accidental, adding more firewalls doesn't fix the underlying problem. You can't accidentally arrive at good security architecture. This history lesson makes ZT feel inevitable rather than radical.

## Disagreement

**Who disagrees:**

No one disputes the history. Some argue that the perimeter model WAS a deliberate engineering response to real threats at the time and that its failure reflects changing conditions, not a design flaw. Kindervag's original ZT argument (2010) made this point differently — the perimeter model was "always wrong," not "wrong now."

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
<!-- Claims this one requires to be true -->

**Supports:**
- [[perimeter-security-obsolete|The historical narrative that perimeter security was an accident of NAT/IP isolation, not a designed property, explains]]
- [[zt-phone-home-fatal-flaw]]

**Contradicts:**
<!-- Claims that cannot be true if this one is -->

**Challenged by:**
<!-- Evidence or arguments that weaken this claim -->

**Operationalizes:**
<!-- Standards/implementations that put this claim into practice -->

**Extends:**
- [[zt-network-assumptions]]

## Assessment

The historical narrative is the chapter's best pedagogical device. It transforms ZT from "new security trend" to "correction of a historical accident." This framing makes ZT adoption feel like inevitability rather than fad — and that's a much better argument to leadership than technical details.

## Zero Trust Taxonomy

### Topic tags
`topic/zt-network` `topic/zt-definition`

### Evidence tags
`evidence/practitioner`
