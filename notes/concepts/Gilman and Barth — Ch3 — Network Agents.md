---
tags:
  - source/books
  - gilman-barth
  - zt-agent
  - zt-authorization
  - zero-trust
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
claims_status: extracted
claims_extracted: 2026-07-24
confidence: high
source:
  title: "Zero Trust Networks: Building Secure Systems in Untrusted Networks"
  authors: "Evan Gilman, Doug Barth"
  year: 2017
  publisher: "O'Reilly Media"
  local_file: "sources/books/_txt/Zero_trust_networks_building_secure_systems_in_untrusted_networks.txt"
related:
  - "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
  - "[[Gilman and Barth — Ch4 — Authorizing the Request]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[Books Index]]"
  - "[[Concepts Index]]"
  - topic/zt-definition
  - topic/zt-network
  - topic/zt-architecture
---

# Gilman & Barth — Ch3: Network Agents

This chapter defines the **network agent** — the distributed component of the control plane that marries user, device, and application into a single authorization entity. It's the construct that makes holistic, context-aware policy evaluation possible in a zero trust architecture. Without the agent, ZT authorization devolves back to disjoint user and device checks, losing the multiplicative security benefit of considering them together.

**Claim 1 —** The network agent is the marriage of user, device, and application — the atomic unit of authorization → [[the-network-agent-is-the-marriage-of-user]]

---

**Claim 2 —** Agents are ephemeral, request-scoped, and purely for authorization — authentication is a separate precursor → [[agents-are-ephemeral-request-scoped-and-purely-for-authorization]]

---

**Claim 3 —** Revoke authorization first, credentials second → [[revoke-authorization-first-credentials-second]]

---

**Claim 4 —** Agent data is sensitive and should be contained to the control plane, with controlled, format-flexible exposure to the data plane → [[agent-data-is-sensitive-and-should-be-contained]]

---

**Claim 5 —** No standard exists for the agent format; standardization would unlock interoperability, and SNMP/MIB is a useful analogy → [[no-standard-exists-for-the-agent-format-standardization]]

---

## Chapter 3 Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| Agent as the atomic unit of authorization | HIGH | Workload-only auth approaches that omit user dimension |
| Agents are ephemeral, authorization-only | HIGH | Performance pressure driving auth result caching |
| Revoke authorization first, credentials second | HIGH (logic) / MEDIUM (evidence) | Slow authorization propagation in large systems |
| Agent data containment in control plane | MEDIUM-HIGH | Weak integrity protection for exposed agent data |
| Standardization desirable, SNMP as analogy | MEDIUM | SPIFFE/JWT/OPA solving pieces without a unified agent standard |

**Strongest section:** The agent definition and its role as the atomic unit of authorization (Claim 1). This is the conceptual innovation that the rest of the ZT architecture depends on. Without it, every subsequent chapter's discussion of policy engines, trust scoring, and authorization is operating on an undefined entity.

**Weakest section:** The "How to Expose an Agent?" discussion. The security implications of pushing agent data into the data plane deserved more rigor — integrity protection, least-privilege field selection, and the risk of header spoofing are all mentioned only obliquely or not at all.

**Unique contribution to OSKG-ZeroTrust:** This chapter provides the agent construct — the entity model that NIST 800-207 abstracts into "all communication must be authenticated and authorized" without specifying what "all communication" has as its subject. Gilman & Barth give us the *who* and *what* that the policy engine evaluates. The agent is the bridge between the architectural concepts (Ch1's control/data plane split) and the operational mechanisms (Ch4's authorization engine). It's the "noun" of the ZT vocabulary.
