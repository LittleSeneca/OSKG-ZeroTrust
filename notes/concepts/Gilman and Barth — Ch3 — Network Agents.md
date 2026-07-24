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
---

# Gilman & Barth — Ch3: Network Agents

This chapter defines the **network agent** — the distributed component of the control plane that marries user, device, and application into a single authorization entity. It's the construct that makes holistic, context-aware policy evaluation possible in a zero trust architecture. Without the agent, ZT authorization devolves back to disjoint user and device checks, losing the multiplicative security benefit of considering them together.

## Claim 1: The network agent is the marriage of user, device, and application — the atomic unit of authorization

**Authors' claim:** "A network agent is the term given to the combination of data known about the actors in a network request, typically containing a user, application, and device. Traditionally, these entities have been authorized separately, but zero trust networks recognize that policy is best captured as a combination of all participants in a request."

**Evidence presented:** The chapter opens with the canonical ZT scenario: an organization that allows code commits from company-issued laptops but blocks source code access from phones. Here, "one factor has influenced the other — a user which might 'normally' have source code access won't enjoy such access from their mobile device." Without the agent construct, this cross-factor policy is awkward to express. With it, the policy is simply "authorize the agent" — the combined entity. The agent is formed on demand as the union of queried data at a point in time.

**Confidence:** HIGH. The agent construct is the implementation bridge between the abstract five assertions (Ch1) and concrete authorization decisions (Ch4). Every ZTNA product, service mesh sidecar, and BeyondCorp-style access proxy implements some version of this concept — even if they don't use the word "agent."

**What's at stake:** If the agent is the right atomic unit, then ZT authorization is fundamentally contextual — you can't authorize a user without knowing what device they're on, and you can't authorize a device without knowing who's using it. This invalidates any ZT implementation that does user auth and device auth as separate, sequential steps rather than as a single combined evaluation.

**Who disagrees:** Service mesh implementations (Istio, Linkerd) tend to authorize at the workload identity level without a user dimension, which is a simplified agent. Some argue that the user dimension belongs at the application layer, not the network layer. The authors' counter is that the agent includes "sparse data" by design — an autonomous system's agent might lack a user field entirely, and policy should handle that gracefully.

**Alternative reading:** The agent could be seen as nothing more than a structured claim bundle — similar to a JWT with richer claims. The innovation isn't the data structure but the architectural insistence that authorization must consume the whole bundle at once, never piecemeal.

**My assessment:** This is the chapter's most important contribution. NIST 800-207 talks about "all communication" being authenticated and authorized, but doesn't provide the granular entity model. Gilman & Barth give us the agent — the thing you actually write policy against. It's the difference between "we do ZT" and "we have an agent construct in our policy engine."

---

## Claim 2: Agents are ephemeral, request-scoped, and purely for authorization — authentication is a separate precursor

**Authors' claim:** "It's best to think of a network agent as an ephemeral entity that is formed on demand to evaluate a policy." And: "Agents serve solely as authorization components and do not play any part in authentication. In fact, authentication is a precursor to agent formation and is generally performed separately for user and device."

**Evidence presented:** The chapter draws a sharp line: authentication produces canonical identifiers (X.509 cert for device, MFA outcome for user), which are then used as lookup keys to populate agent fields (device type, user role, trust score). Authentication is session-oriented and cacheable; authorization is request-oriented and should not be cached because agent details "can change rapidly based on a number of factors." Caching an agent or authorization result is "ill advised."

**Confidence:** HIGH. This separation is operationally critical and widely adopted. It means you can authenticate once (a session token) but re-authorize every request (re-forming the agent with fresh trust scores and device state). This is exactly how Google's Access Proxy works — the session cookie authenticates, but every request hits the authorization engine.

**What's at stake:** If you conflate authentication and authorization — or cache authorization results — you lose the ability to revoke access mid-session based on changing conditions. This is the mechanism that makes "continuous verification" (NIST tenet 5) technically feasible.

**Who disagrees:** Some implementations (OAuth2/RPT-based, early ZTNA products) do cache authorization decisions for performance, accepting the security tradeoff. The authors argue agent generation should be "as lightweight as possible" so that performance pressure doesn't drive you to cache. The chapter previews that Ch4 will address performance considerations more directly.

**My assessment:** This claim is underappreciated. Everyone talks about "never trust, always verify," but the implementation insight — authentication is session-scoped, authorization is request-scoped, don't mix them — is what makes the slogan executable. The agent construct decouples these concerns cleanly.

---

## Claim 3: Revoke authorization first, credentials second

**Authors' claim:** "In the event that access must be revoked, updating authorization is more effective than changing authentication credentials. This is doubly so when considering that authentication results are typically cached and assigned to session identifier. The act of validating an authenticated session is really an authorization decision."

**Evidence presented:** This claim appears as an inset box — a standalone principle, not argued at length with multiple pieces of evidence. The logic is crisp: (1) authentication results are cached, so changing a password doesn't immediately terminate existing sessions; (2) session validation is an authorization check, not an authentication check; (3) therefore, the fastest way to cut off access is to update the authorization policy, not the credential. The chapter doesn't provide empirical data (e.g., time-to-revoke measurements) but the reasoning is sound on its face.

**Confidence:** HIGH on the logic, MEDIUM on the evidence base (it's thin). The principle is correct but the chapter could have spent more space on the operational implications — how fast does an authorization change propagate? What if the authorization engine is the bottleneck?

**What's at stake:** If you prioritize credential rotation over authorization policy updates during incident response, you leave active sessions alive. This is a common operational mistake. The principle inverts the intuitive response (change passwords!) in favor of the more effective one (update policy!).

**Who disagrees:** No one argues against the principle itself. The real debate is implementation: in a system with 10,000 policies and rapid-change trust scores, changing authorization might be just as slow as rotating credentials. The chapter doesn't address revocation latency in detail.

**My assessment:** This is a pithy, memorable principle that deserves a place in every ZT operator's mental model. It's the kind of thing you print on a poster. But it should be paired with operational detail — how fast is your authorization update propagation? What's the latency from policy change to enforcement? — that the chapter doesn't provide.

---

## Claim 4: Agent data is sensitive and should be contained to the control plane, with controlled, format-flexible exposure to the data plane

**Authors' claim:** "To adequately secure the sensitive agent details, the entirety of the agent lifecycle should be contained to trusted control plane systems, which themselves are heavily secured. These systems should be logically and physically separated from the data plane systems, have clear boundaries, and change infrequently."

**Evidence presented:** The chapter identifies two categories of sensitive agent data: (1) PII — user name, address, phone number — and (2) device details that an attacker could use for targeted attacks or physical theft patterns. The solution is a "trusted communication channel" from control plane to application, like a reverse proxy injecting agent-derived headers into requests. The proxy enforces its own authorization and exposes only a subset of agent data downstream. For pre-existing applications with their own authorization systems, the agent data format should be flexible — use whatever format the application expects.

**Confidence:** MEDIUM-HIGH. The principle is sound but the implementation details are underdeveloped. "Injecting headers into network requests that flow through a reverse proxy" is a specific implementation pattern (Google's IAP does exactly this with `X-Goog-Authenticated-User-*` headers), but the chapter doesn't discuss header spoofing risks, signed assertions, or integrity protection for the exposed agent data.

**What's at stake:** If the exposed agent data isn't integrity-protected, a compromised downstream application (or an attacker who can reach it directly) can fabricate agent claims and bypass authorization. The chapter mentions "trusted communication channel" but doesn't specify what makes it trusted — mutual TLS? Signed tokens? Network-level isolation?

**Who disagrees:** BeyondCorp-style implementations often use signed JWTs rather than plain headers to carry agent data to applications, specifically to prevent tampering. The chapter's description is closer to a reverse-proxy pattern that assumes network-level trust between proxy and application, which is less robust.

**My assessment:** This is the chapter's weakest section. The security model of exposing agent data to the data plane deserved a deeper treatment — integrity protection, least-privilege field exposure, and the risks of header injection/interception. The principle (keep agent data in the control plane) is right, but the "how" is sketched rather than specified.

---

## Claim 5: No standard exists for the agent format; standardization would unlock interoperability, and SNMP/MIB is a useful analogy

**Authors' claim:** "At the time of this writing, most zero trust networks consist of systems built in-house; and while those systems have developed their own agent standards, a public standard would unlock the control plane, allowing components to be mixed and matched."

**Evidence presented:** The chapter uses SNMP and its Management Information Base (MIB) as an extended analogy. OIDs (object identifiers) provide globally unique, hierarchical "coordinates" for data fields — analogous to IP addresses for data. The IANA Private Enterprise Number system allows organizations to register their own OID prefix for internal use. The analogy is: just as SNMP standardized how network devices expose management data in a flexible, extensible way, a future agent standard would standardize how ZT components exchange agent data. For now, the recommendation is pragmatic: "loose typing or no typing should be preferred over strong typing," use JSON blobs or custom formats, prioritize extensibility over rigor.

**Confidence:** MEDIUM. The SNMP analogy is interesting but strained — SNMP is a monitoring protocol, not an authorization data format. The chapter was written in 2017, and the landscape has evolved: SPIFFE/SPIRE provides standardized workload identity, JWT claims are widely used, and Open Policy Agent (OPA) standardizes policy expression. An "agent standard" per se hasn't emerged, but the problem has been partially solved through identity and policy standards.

**What's at stake:** If no standard emerges, ZT control planes remain proprietary walled gardens — your policy engine, trust scorer, and device inventory must come from the same vendor or be custom-integrated. This locks organizations into vendor stacks and slows adoption.

**Who disagrees:** SPIFFE (Secure Production Identity Framework For Everyone) has effectively become the standard for workload identity representation, covering part of the agent's scope. OPA's Rego language is a de facto standard for policy expression. The chapter's vision of a single "agent standard" may have been too ambitious — the problem decomposed into smaller, separately standardized pieces.

**My assessment:** This chapter's standardization discussion was prescient in identifying the problem but dated in its proposed solution (the SNMP/MIB model). The field has moved toward identity standards (SPIFFE), policy standards (OPA/Rego, Cedar), and token standards (JWT, PASETO) rather than a monolithic agent format. The real contribution is the identification that *something* needs to be standardized for ZT to become interoperable.

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
