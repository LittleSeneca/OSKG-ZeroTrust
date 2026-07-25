---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-architecture
  - topic/zt-governance
  - topic/zt-definition
  - topic/zt-network
claim_id: "gb-ch3.5"
statement: "No standard exists for the agent format; standardization would unlock interoperability, and SNMP/MIB is a useful analogy"
confidence: "medium"
confidence_rationale: "MEDIUM. The SNMP analogy is interesting but strained — SNMP is a monitoring protocol, not an authorization data format. The chapter was written in"
claim_type: "governance"
source_note: "[[Gilman and Barth — Ch3 — Network Agents]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch3.5: No standard exists for the agent format; standardization would unlock interoperability, and SNMP/MIB is a useful analogy

**Source:** [[Gilman and Barth — Ch3 — Network Agents]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"At the time of this writing, most zero trust networks consist of systems built in-house; and while those systems have developed their own agent standards, a public standard would unlock the control plane, allowing components to be mixed and matched."

## Evidence

The chapter uses SNMP and its Management Information Base (MIB) as an extended analogy. OIDs (object identifiers) provide globally unique, hierarchical "coordinates" for data fields — analogous to IP addresses for data. The IANA Private Enterprise Number system allows organizations to register their own OID prefix for internal use. The analogy is: just as SNMP standardized how network devices expose management data in a flexible, extensible way, a future agent standard would standardize how ZT components exchange agent data. For now, the recommendation is pragmatic: "loose typing or no typing should be preferred over strong typing," use JSON blobs or custom formats, prioritize extensibility over rigor.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. The SNMP analogy is interesting but strained — SNMP is a monitoring protocol, not an authorization data format. The chapter was written in 2017, and the landscape has evolved: SPIFFE/SPIRE provides standardized workload identity, JWT claims are widely used, and Open Policy Agent (OPA) standardizes policy expression. An "agent standard" per se hasn't emerged, but the problem has been partially solved through identity and policy standards.

## Stakes

If no standard emerges, ZT control planes remain proprietary walled gardens — your policy engine, trust scorer, and device inventory must come from the same vendor or be custom-integrated. This locks organizations into vendor stacks and slows adoption.

## Disagreement

**Who disagrees:**

SPIFFE (Secure Production Identity Framework For Everyone) has effectively become the standard for workload identity representation, covering part of the agent's scope. OPA's Rego language is a de facto standard for policy expression. The chapter's vision of a single "agent standard" may have been too ambitious — the problem decomposed into smaller, separately standardized pieces.

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

This chapter's standardization discussion was prescient in identifying the problem but dated in its proposed solution (the SNMP/MIB model). The field has moved toward identity standards (SPIFFE), policy standards (OPA/Rego, Cedar), and token standards (JWT, PASETO) rather than a monolithic agent format. The real contribution is the identification that *something* needs to be standardized for ZT to become interoperable.
