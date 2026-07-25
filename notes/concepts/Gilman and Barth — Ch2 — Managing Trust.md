---
tags:
  - source/books
  - gilman-barth
  - zt-trust
  - zt-pki
  - trust-engine
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
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[Books Index]]"
  - "[[Concepts Index]]"
  - topic/zt-implementation
  - topic/zt-definition
  - topic/zt-architecture
---

# Gilman & Barth — Ch2: Managing Trust

The chapter that operationalizes trust. Ch1 defined the architecture (control plane / data plane); Ch2 defines how trust is computed, propagated, and consumed within that architecture. This is where PKI, threat models, variable trust scores, and the trust engine enter the picture — the mechanisms that make the Ch1 architecture actually work.

**Claim 1 —** ZT's threat model is the Internet Threat Model plus endpoint compromise → [[zts-threat-model-is-the-internet-threat-model]]

---

**Claim 2 —** Private PKI is the non-negotiable bedrock of ZT identity → [[private-pki-is-the-non-negotiable-bedrock-of-zt]]

---

**Claim 3 —** Variable trust scores replace binary policy with continuous, dynamic authorization → [[variable-trust-scores-replace-binary-policy-with-continuous]]

---

**Claim 4 —** Least privilege in ZT is dynamic, multi-attribute, and device-bound → [[least-privilege-in-zt-is-dynamic-multi-attribute-and]]

---

**Claim 5 —** The control plane is the trust grantor — temporary trust and leased tokens are its operational expression → [[the-control-plane-is-the-trust-grantor-temporary]]

---

**Claim 6 —** Trust delegation via trust chains is what makes ZT scalable → [[trust-delegation-via-trust-chains-is-what-makes]]

---

## Chapter 2 Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| Internet Threat Model + endpoint expansion | HIGH | NSA-level critics arguing state-level must be in scope |
| Private PKI as ZT bedrock | HIGH | Cloud-managed PKI advocates arguing in-house PKI is unnecessary risk |
| Variable trust scores replace binary policy | HIGH (principle), MODERATE (implementation) | Score gaming by persistent attackers; opaque decisions frustrating users |
| Dynamic, multi-attribute, device-bound least privilege | HIGH | Weak device binding reducing to just-another-attribute |
| Control plane as trust grantor / temporary trust | HIGH | Availability bottlenecks from too-short credential lifetimes |
| Trust delegation via chains | HIGH | Single compromised link cascading through the entire chain |

**Strongest section:** The variable trust / trust engine discussion (Claim 3). The credit agency analogy is the best pedagogical device in the chapter, and the shift from binary to continuous trust is the idea that most distinguishes ZT from traditional security. This section is what you put in a slide deck for executives.

**Weakest section:** The threat modeling methodology discussion (STRIDE, DREAD, PASTA, Trike, VAST). It's a catalogue of acronyms with no analysis of how they apply to ZT specifically. The value is in the ZT-specific threat model (Internet Threat Model + endpoints), not in the survey of general threat modeling frameworks.

**Unique contribution to OSKG-ZeroTrust:** This chapter provides the trust computation layer that NIST 800-207's PDP/PEP model requires but doesn't specify. NIST says "the PDP makes an authorization decision based on policy and input data." Gilman & Barth say "here's HOW: variable trust scores computed by a trust engine from continuously monitored attributes, bound to PKI-verified identity, enforced through temporary leased credentials." It's the difference between "what should happen" and "how to build it."

**What's missing:** The trust engine itself — the component that computes the trust score — is mentioned (Figure 2-4) but never detailed. How are scores initialized? How do they decay? What's the algorithm? The chapter defers this to Chapter 3 (Network Agents), but even there the treatment is more about agent architecture than score computation. This is a gap in the book as a whole, and one that real ZT implementations fill with their own (often proprietary) scoring models.
