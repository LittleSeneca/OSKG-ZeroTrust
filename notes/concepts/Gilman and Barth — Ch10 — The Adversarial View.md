---
tags:
  - source/books
  - gilman-barth
  - zt-threats
  - zt-attacks
  - adversary
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
  - "[[NIST 800-207 — Ch5 — Threats]]"
  - "[[NSA — Embracing a Zero Trust Security Model]]"
  - "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
  - "[[Gilman and Barth — Ch6 — Identity, Authentication, and Authorization]]"
  - "[[Gilman and Barth — Ch5 — Trusting Devices]]"
  - "[[Books Index]]"
  - "[[Concepts Index]]"
  - topic/zt-threats
  - topic/zt-architecture
  - topic/zt-implementation
---

# Gilman & Barth — Ch10: The Adversarial View

The unique chapter in Zero Trust literature. Where every other chapter builds ZT from the inside out — architecture, components, deployment — this chapter inverts the lens and asks: "If you were trying to penetrate a zero trust network, how might you do it?" It is Gilman & Barth's security considerations section in the IETF tradition — a systematic catalog of attack vectors, honest about what ZT mitigates and what it doesn't, and the only chapter in the book that explicitly evaluates the system as an adversary.

This note covers all eight threat categories (identity theft, DDoS, endpoint enumeration, untrusted computing platform, social engineering, physical coercion, invalidation, control plane security) and cross-references the threat taxonomies in NIST 800-207 Ch5 and NSA Embracing ZT. The three documents form a progression: Gilman & Barth provide the **engineering-level adversarial analysis**, NIST provides the **architectural threat taxonomy**, NSA provides the **operational threat model** with the "assume breach" mindset.

---

**Claim 1 —** Identity theft is the first and most dangerous threat — ZT requires stealing *two* identities → [[identity-theft-is-the-first-and-most-dangerous]]

---

**Claim 2 —** DDoS is still a problem — ZT doesn't mitigate it, it reframes how you respond → [[ddos-is-still-a-problem-zt-doesnt-mitigate]]

---

**Claim 3 —** ZT guarantees confidentiality but not privacy — endpoint enumeration is a real tradeoff → [[zt-guarantees-confidentiality-but-not-privacy-endpoint-enumeration]]

---

**Claim 4 —** ZT cannot defend against a malicious computing platform — only against simpler platform attacks → [[zt-cannot-defend-against-a-malicious-computing-platform]]

---

**Claim 5 —** Social engineering and physical coercion are the threats ZT can't solve — only contain → [[social-engineering-and-physical-coercion-are-the-threats]]

---

**Claim 6 —** Invalidation is a "hard problem in computer science" — ZT addresses it through granular authorization, not push-based revocation → [[invalidation-is-a-hard-problem-in-computer-science]]

---

**Claim 7 —** Control plane compromise is the worst-case scenario — and it must be defended with the highest rigor → [[control-plane-compromise-is-the-worst-case-scenario-and]]

---

**Claim 8 —** The adversarial view reveals that ZT is a risk reduction strategy, not a risk elimination strategy → [[the-adversarial-view-reveals-that-zt-is-a]]

---

## Chapter 10 Overall Assessment

| Threat Category | ZT Mitigation Quality | Confidence | Worst-Case Remaining Risk |
|---|---|---|---|
| Identity theft | Strong — dual authentication raises the bar | HIGH | Simultaneous compromise of device + user (phishing + malware on managed device) |
| DDoS | Weak — ZT doesn't prevent volumetric attacks | MEDIUM-HIGH | Control plane DDoS makes entire ZT network unavailable |
| Endpoint enumeration | None — ZT provides confidentiality, not privacy | HIGH | Adversary builds complete network topology from observed conversations |
| Untrusted platform | None — impossible to fully defend against | HIGH | Hardware-level compromise defeats all ZT controls |
| Social engineering | Partial — behavioral detection, group auth for critical assets | MEDIUM | Willing-but-deceived insider causes damage within their authorized scope |
| Physical coercion | None — accept and limit blast radius | HIGH | Single coerced individual with access to critical systems |
| Invalidation | Good — granular auth + periodic reauthorization | HIGH | Access gap between revocation and next polling period |
| Control plane compromise | Strong — rigorous protections recommended | VERY HIGH | Complete ZT authorization collapse if policy engine is compromised |

**Strongest section:** Control plane security. The most architecturally complete treatment in the chapter — threat severity, mitigation hierarchy, and the discipline to avoid perimeterizing the control plane. The "rewriting the C compiler in C" analogy perfectly captures the bootstrapping challenge.

**Weakest section:** DDoS. Honest but thin — the policy-derived filtering idea is interesting but underdeveloped, and the real concern (control plane availability) is deferred.

**Unique contribution to OSKG-ZeroTrust:** This is the only chapter in the Zero Trust literature that evaluates the system **as an adversary would** rather than as a defender building defenses. While NIST 800-207 Ch5 catalogs threats systematically and NSA provides worked scenarios, Gilman & Barth's adversarial view is the only source that asks "how would you break this?" and answers honestly. It provides the threat model that every ZT architecture review should run against — the missing security considerations section that most vendor ZT literature omits.

**Cross-reference note:** The NIST 800-207 Ch5 note already cross-references this chapter extensively (see the synthesis table mapping threat categories across Gilman & Barth, NIST, and NSA). The three documents are complementary: Gilman & Barth (engineering-level adversarial analysis) → NIST (architectural threat taxonomy) → NSA (operational threat model). Together they form the complete threat picture for Zero Trust.

