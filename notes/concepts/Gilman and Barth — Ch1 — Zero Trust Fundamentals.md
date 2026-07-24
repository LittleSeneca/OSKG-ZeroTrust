---
tags:
  - source/books
  - gilman-barth
  - zt-fundamentals
  - zt-architecture
  - control-plane
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
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[CISA ZTMM — Overview and Framework]]"
  - "[[Books Index]]"
  - "[[Concepts Index]]"
---

# Gilman & Barth — Ch1: Zero Trust Fundamentals

The most important single chapter in Zero Trust literature from an implementation perspective. This is where the control plane / data plane architecture — the dominant implementation model — is first fully articulated.

## Claim 1: The five fundamental assertions define ZT operationally, not abstractly

**Authors' claim:** "A zero trust network is built upon five fundamental assertions: (1) The network is always assumed to be hostile. (2) External and internal threats exist on the network at all times. (3) Network locality is not sufficient for deciding trust. (4) Every device, user, and network flow is authenticated and authorized. (5) Policies must be dynamic and calculated from as many sources of data as possible."

**Evidence presented:** These five assertions are derived from engineering practice at Netflix and PagerDuty, not from theoretical analysis. The book is written by practitioners who built ZT systems. Each assertion maps to a specific engineering decision: assertion 1 → always encrypt, assertion 4 → no unauthenticated traffic anywhere, assertion 5 → policy engines fed by multiple data sources.

**Confidence:** HIGH. These assertions have held up as the pragmatic, engineering-level complement to NIST's seven abstract tenets. They're more operational than NIST and less threat-focused than NSA.

**What's at stake:** If the assertions are the right decomposition, ZT is fundamentally about network architecture. If they're too narrowly focused on network-level concerns, they miss organizational, identity, and data-centric dimensions. CISA's five-pillar model explicitly expands beyond network concerns.

**Who disagrees:** NIST 800-207's seven tenets are broader — they include resource definition, continuous monitoring, and data collection (Tenets 1, 5, 7) that Gilman & Barth's assertions don't directly address. NSA adds "assume breach" as a separate organizing principle. CISA adds cross-cutting capabilities (Visibility, Automation, Governance) that span all five assertions.

**Alternative reading:** The five assertions could be read as a network engineer's manifesto — they're about what happens on the wire. A data-centric ZT approach would start with "all data is classified" rather than "the network is hostile." Both are correct; they're different entry points to the same architecture.

**My assessment:** These five assertions are the most readable, most actionable expression of Zero Trust principles in the field. They're what you put on a whiteboard. NIST's seven tenets are what you put in an RFP. Both needed.

---

## Claim 2: The control plane / data plane split is ZT's fundamental architectural innovation

**Authors' claim:** "The supporting system is known as the control plane, while most everything else is referred to as the data plane... Requests for access to protected resources are first made through the control plane, where both the device and user must be authenticated and authorized. Once the control plane has decided that the request will be allowed, it dynamically configures the data plane to accept traffic from that client."

**Evidence presented:** The control plane is authoritative — it authenticates, authorizes, and coordinates access in real time. The data plane accepts configuration from the control plane and enforces it. This architecture is directly inspired by software-defined networking (SDN) and Google's BeyondCorp. It's validated by every major ZT implementation: Google Access Proxy, ZTNA products, service mesh.

**Confidence:** VERY HIGH. Every subsequent ZT architecture document — NIST 800-207, DoD ZT RA, CISA maturity model — implicitly or explicitly uses this split. NIST's PDP/PEP model is a more abstract version of the same concept.

**What's at stake:** If the control plane is centralized, it's a single point of failure and attack. If it's distributed, consistency becomes hard. The tension between centralized policy and distributed enforcement is THE architectural tension in ZT.

**Who disagrees:** Sounil Yu's Cyber Defense Matrix situates ZT control differently depending on the asset class (devices vs. networks vs. applications vs. data). Service mesh architectures distribute control plane functions across sidecars rather than centralizing them.

**My assessment:** This chapter's description of the control plane / data plane model is the single most influential piece of ZT architectural writing. Every implementation in the BeyondCorp papers, every vendor ZTNA product, and every deployment in Green-Ortiz's case studies follows this pattern. Gilman & Barth didn't invent the concept (SDN did), but they established it as the canonical ZT architecture.

---

## Claim 3: The perimeter model's history reveals why it failed — it was an accident, not a design

**Authors' claim:** The perimeter model is a historical accident driven by three events: (1) RFC 1597 creating private address space that was "fundamentally incapable of joining other networks," (2) the DMZ emerging as a side effect of connecting mail servers to the internet, (3) NAT inadvertently providing firewall-like properties that made perimeter enforcement feel "secure."

**Evidence presented:** A detailed historical narrative from Joe Postel's IP registry (1982) through RFC 1597 (1994), RFC 1631 NAT (1994), to the modern perimeter firewall. The key insight: "Private networks were more secure, because they were fundamentally incapable of joining other networks." Security was a side effect of isolation, not a designed property.

**Confidence:** HIGH. The history is well-documented and matches the IETF RFC record. The interpretative claim — that perimeter security was accidental — is stronger than the evidence strictly supports, but it's a productive lens.

**What's at stake:** If perimeter security was accidental, adding more firewalls doesn't fix the underlying problem. You can't accidentally arrive at good security architecture. This history lesson makes ZT feel inevitable rather than radical.

**Who disagrees:** No one disputes the history. Some argue that the perimeter model WAS a deliberate engineering response to real threats at the time and that its failure reflects changing conditions, not a design flaw. Kindervag's original ZT argument (2010) made this point differently — the perimeter model was "always wrong," not "wrong now."

**My assessment:** The historical narrative is the chapter's best pedagogical device. It transforms ZT from "new security trend" to "correction of a historical accident." This framing makes ZT adoption feel like inevitability rather than fad — and that's a much better argument to leadership than technical details.

---

## Claim 4: The phone-home attack pattern is perimeter security's fatal flaw

**Authors' claim:** The critical flaw in perimeter security is that "security policies are defined by network zones, enforced only at zone boundaries, using nothing more than the source and destination details." The phone-home pattern — malware initiates an outbound connection, receives commands, and the attacker bypasses inbound firewall rules entirely — exploits this flaw systematically.

**Evidence presented:** The attack chain: exploit user's browser → dialer payload phones home → real malware downloads → attacker gets interactive session on internal host → lateral movement. This pattern "very effectively undermines the perimeter security model" because outbound traffic is generally allowed.

**Confidence:** HIGH. This is the standard attack pattern described in every incident response report. It's empirically validated by decades of breaches.

**What's at stake:** If the phone-home pattern is the norm, every enterprise with NAT-based outbound internet access is vulnerable regardless of how well their inbound firewall is configured. This makes perimeter security indefensible — not just insufficient, but structurally incapable of addressing the primary attack vector.

**Who disagrees:** Outbound proxy/filtering solutions (Zscaler, Netskope) argue that tight outbound controls can mitigate this. NIST's TIC 3.0 program explicitly addresses this. But Gilman & Barth's argument is that filtering outbound connections is an arms race you can't win — the ZT solution is to make the internal network hostile so that even if malware phones home, it can't move laterally.

**My assessment:** This argument is the operational death certificate for perimeter-based security. It's not that firewalls are useless — they're still useful for coarse filtering. It's that they can't be the organizing principle of security architecture because the attack pattern they're designed to prevent (inbound connections from the internet) is no longer the primary threat vector.

---

## Chapter 1 Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| Five fundamental assertions | HIGH | Being too network-centric for data/identity-focused ZT |
| Control plane / data plane split | VERY HIGH | Centralization as single point of failure/attack |
| Perimeter model as historical accident | HIGH | Defense that perimeter was deliberate and appropriate for its time |
| Phone-home as perimeter's fatal flaw | HIGH | Outbound filtering proponents arguing it's solvable |

**Strongest section:** The control plane / data plane architecture introduction. This is the conceptual DNA of every subsequent ZT implementation.

**Weakest section:** The historical narrative, while pedagogically effective, is longer than necessary and occasionally indulgent. The key insight (perimeter security was a side effect of NAT, not a design) could be stated in half the space.

**Unique contribution to OSKG-ZeroTrust:** This chapter provides the implementation-level architectural vocabulary (control plane, data plane, policy engine) that NIST 800-207 abstracts and that the government standards don't provide. It's the bridge between "what is ZT" (NIST) and "how do I build it" (BeyondCorp papers, Green-Ortiz case studies).
