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
---

# Gilman & Barth — Ch2: Managing Trust

The chapter that operationalizes trust. Ch1 defined the architecture (control plane / data plane); Ch2 defines how trust is computed, propagated, and consumed within that architecture. This is where PKI, threat models, variable trust scores, and the trust engine enter the picture — the mechanisms that make the Ch1 architecture actually work.

## Claim 1: ZT's threat model is the Internet Threat Model plus endpoint compromise

**Authors' claim:** "Zero trust networks, as a result of their control over endpoints in the network, expand upon the Internet Threat Model to consider compromises at the endpoints." The Internet Threat Model (RFC 3552) assumes attackers have "nearly complete control of the communications channel" — they can read, remove, change, or inject packets. ZT expands this to include compromised endpoints. The goal is to mitigate attacks "up to and including attacks originating from a 'trusted insider' level of access" but not all state-level actors.

**Evidence presented:** The RFC 3552 excerpt is quoted directly — the standard model assumes end-systems themselves are uncompromised, but ZT drops that assumption. The attacker categorization (opportunistic → targeted → insider → trusted insider → state-level) provides a ladder of increasing capability, and ZT draws the line below state-level actors because "an attacker with unlimited resources is essentially impossible to defend against."

**Confidence:** HIGH. RFC 3552 is a foundational IETF document and the expansion to endpoints is logically consistent with the "network is always hostile" assertion from Ch1. Every major ZT implementation (BeyondCorp, DoD ZT RA) makes the same assumption.

**What's at stake:** The threat model determines what ZT is designed to protect against — and, crucially, what it explicitly does NOT protect against. If state-level actors are out of scope, ZT is not a complete security architecture for national security systems. The authors are candid about this: "defending against these localized threats is exceedingly expensive, requiring dedicated physical hardware."

**Who disagrees:** NSA's guidance does include state-level actors in scope and treats "assume breach" as a separate organizing principle that covers endpoint compromise more comprehensively. NIST 800-207 doesn't explicitly enumerate threat actors but its continuous monitoring tenet (Tenet 5) implicitly addresses the same concern.

**Alternative reading:** The threat model could be read as a pragmatic admission by practitioners — not a theoretical limit of ZT but a statement about where the ROI of additional controls drops off. State-level mitigations exist (hardware roots of trust, air-gapped PKI) but they're deployment-specific add-ons, not core ZT requirements.

**My assessment:** This is a refreshingly honest threat model. Most security frameworks either claim universal protection (dishonest) or avoid the question (useless). Gilman & Barth draw a clear line — we defend against everything up to trusted insiders, and state-level actors require additional, specialized controls beyond the scope of this book. That clarity is valuable for resource allocation and honest risk communication.

---

## Claim 2: Private PKI is the non-negotiable bedrock of ZT identity

**Authors' claim:** "All zero trust networks rely on PKI to prove identity throughout the network. As such, it acts as the bedrock of identity authentication for the majority of operations." Private PKI is strongly preferred over public PKI for three reasons: (1) cost at scale — a ZT network has many certificates and public CAs charge per signing; (2) trust — "any one of these [public] CAs can cut certificates that your network trusts," creating a multi-jurisdictional trust problem; (3) flexibility — public CAs restrict certificate metadata, but ZT often needs site-specific metadata like roles or user IDs embedded in certificates.

**Evidence presented:** The authors enumerate the entities authenticated by PKI (devices, users, applications) and argue that the sheer number of certificates demands automation — "if humans are required in order to process certificate signing requests, the procedure will be applied sparingly, weakening the overall system." The private-vs-public analysis is practical: public PKI is "strictly better than none" but a stepping stone, not the destination.

**Confidence:** HIGH. This has been validated by every major ZT deployment. Google's BeyondCorp runs its own CA. Service mesh implementations (Istio, Linkerd) all use private PKI. The "automation or death" insight — that manual certificate processing leads to sparse issuance and weak identity — is a hard-won operational truth.

**What's at stake:** If PKI is the bedrock, PKI failures are catastrophic. The CA's private key is the skeleton key to the entire network. The authors acknowledge this — "the CA must be protected at all costs, since its subversion would be catastrophic." This makes PKI security the single most important operational concern in a ZT deployment.

**Who disagrees:** Some cloud-native approaches argue that workload identity (SPIFFE/SPIRE) can replace traditional PKI in some contexts. Managed PKI services (AWS Private CA, Azure Key Vault) argue they solve the automation problem without requiring in-house PKI expertise. But these are implementation details — the underlying principle (private, automated, cryptographically-verified identity) is universal.

**My assessment:** This chapter correctly identifies PKI as the ZT identity substrate but understates the operational complexity of running a private CA at scale. Certificate rotation, revocation, and cross-datacenter CA trust are hard problems that the book defers to Chapter 5. The "private PKI is better than public PKI" argument is correct but incomplete — the real question is whether your team has the expertise to operate a private CA securely, and the honest answer for many organizations is "no." Cloud-managed PKI may be the pragmatic middle path.

---

## Claim 3: Variable trust scores replace binary policy with continuous, dynamic authorization

**Authors' claim:** The core innovation of ZT trust management is replacing binary access decisions with a variable trust score: "Instead of defining binary policy decisions assigned to specific actors in the network, a zero trust network will continuously monitor the actions of an actor on the network to update their trust score." This score is then measured against the sensitivity of the requested resource — a calendar view needs a low score, changing system settings needs a high score. The credit agency analogy crystallizes the insight: just as credit scores let lenders make risk-based decisions without personally evaluating each borrower, trust scores let the control plane make authorization decisions without enumerating every possible access scenario.

**Evidence presented:** The credit agency analogy is the central piece of evidence. The argument is that binary policies create perverse incentives — either the policy is too rigid (creating human toil to continually adjust) or too loose (resulting in weak security). A trust score captures "a number of conditions without complicating the policy with edge cases" and allows "authorization systems to adjust to novel threats." Figure 2-3 illustrates how fewer score-based policies replace many binary policies.

**Confidence:** HIGH in principle, MODERATE in implementation. The conceptual model is sound and has been adopted by every major ZT product (Zscaler's risk score, Okta's risk-based authentication, Google's access tiers). But the chapter's treatment of HOW scores are computed is thin — that's deferred to the trust engine discussion and Chapter 3.

**What's at stake:** If trust scores are computable and reliable, ZT authorization becomes genuinely adaptive. If scores are noisy, gamed, or opaque, they create new attack surfaces and user frustration. The authors acknowledge the key concern: "Could it be possible for a persistent attacker to slowly build their credibility in a system to gain more access?" Their mitigations (requiring extended normal behavior, binding scores to device/application metadata, multi-signal authentication) are sensible but not proven.

**Who disagrees:** The NIST 800-207 model doesn't explicitly require trust scores — it requires policy decisions based on "as many sources of data as possible" (Tenet 6), which could be implemented with binary rules on top of many attributes. Some security engineers argue that trust scores create an opaque, unexplainable authorization system where users don't understand why they were denied — a legitimate usability concern the authors acknowledge but don't fully resolve.

**Alternative reading:** Variable trust can be read as an implementation detail rather than a fundamental ZT property. You can build a ZT network with complex, multi-attribute binary policies that achieve the same effect. The trust score is an aggregation mechanism, not a requirement.

**My assessment:** This is the most conceptually important claim in Ch2 and the one that most distinguishes ZT from traditional network security. Traditional security asks "is this allowed?" ZT asks "how trustworthy is this right now?" The shift from static rules to continuous evaluation is what makes ZT networks genuinely more secure, not just differently architected. The credit agency analogy is brilliant pedagogy — it makes an abstract concept immediately intuitive.

---

## Claim 4: Least privilege in ZT is dynamic, multi-attribute, and device-bound

**Authors' claim:** Least privilege in ZT goes beyond traditional user/application privilege to include the device, the temporal context, the geographic context, and the behavioral baseline. "It is the combination of user or application and the device being used that determines the privilege level granted." Privilege is temporary and contextual — "users should similarly operate in a reduced privilege mode on the network most of the time, only elevating their permissions when needed." The authors also make the subtle point that encryption itself is an application of least privilege: "Who really needs access to the packet payload?"

**Evidence presented:** Three dimensions of dynamic privilege are described: (1) temporal — access outside normal working hours is more suspicious; (2) geographical — access from an unusual location triggers additional authentication; (3) behavioral — access to resources the user doesn't normally access raises the risk score. The chapter distinguishes between low-risk elevation (re-prompt for password, second factor) and high-risk elevation (active confirmation from a peer via out-of-band request).

**Confidence:** HIGH. This multi-attribute, contextual approach to least privilege is the operational heart of ZT authorization. It's directly implemented in BeyondCorp's access tiers, in Okta's contextual access policies, and in every ZTNA product's device posture checks.

**What's at stake:** If device context binding is weak, credential theft still grants access — the device becomes just another attribute that can be spoofed. The strength of device binding (TPM, secure enclave, hardware-backed keys) is the practical limit on how much ZT least privilege actually improves security over traditional models.

**Who disagrees:** Traditional RBAC proponents would argue that multi-attribute privilege is just ABAC (Attribute-Based Access Control) and that ZT hasn't invented anything new — it's applying existing access control models in a network context. This is technically correct; the novelty is in making ABAC the default operating mode for network access decisions, not just application-level authorization.

**My assessment:** The marriage of user identity and device identity into a single authorization decision is the most underappreciated insight in this chapter. Traditional networks treat "user logged into a device" and "device on the network" as two separate problems. ZT recognizes that a compromised credential on a trusted device and a valid credential on a compromised device are different threats requiring different responses — and that you can't distinguish them without binding user and device identity together. This is the argument that Chapter 3 (Network Agents) will develop in detail.

---

## Claim 5: The control plane is the trust grantor — temporary trust and leased tokens are its operational expression

**Authors' claim:** The control plane "is the trust grantor for the entire network. Due to its far-reaching control of the network's behavior, the control plane's trustworthiness is critical." Trust granted by the control plane "should have limited real-time value. Trust should be temporary, requiring regular check-ins between the truster and trustee to ensure that the continued trust is reasonable." The interface between control plane and data plane "should resemble the user/kernel space interface, where interactions between those two systems are heavily isolated to prevent privilege escalation."

**Evidence presented:** The chapter specifies leased access tokens and short-lifetime certificates as the implementation mechanism for temporary trust. These credentials must be validated both within the data plane (agent-to-resource) and between the data plane and control plane (agent-to-controller). The isolation requirement is structural — the data plane cannot be used to gain privilege in the control plane, preventing lateral movement.

**Confidence:** HIGH. This is a direct extension of the Ch1 architecture with operational specifics. The "lease" model — credentials that expire and require renewal — is now standard in service mesh (mTLS with short-lived certificates), Kubernetes (service account tokens with expiry), and cloud IAM (temporary security credentials via STS).

**What's at stake:** If credential lifetimes are too long, the system reverts to static trust and loses its ZT properties. If they're too short, the control plane becomes a bottleneck and availability suffers. The rotation frequency trade-off — "inversely proportional to the cost of rotation" — is the key operational tension. The chapter's examples of expensive-to-rotate secrets (certificates requiring external coordination, hand-configured service accounts, database passwords requiring downtime) are still painfully relevant.

**Who disagrees:** Some architectures (e.g., SPIFFE) push toward very short-lived credentials (minutes) with automated rotation, arguing that the operational cost of rotation has been solved by modern infrastructure. Others (especially in OT/IoT contexts) argue that frequent rotation is impractical and push for hardware-backed long-lived credentials with attestation instead. Both are valid in their domains.

**My assessment:** The "trust is temporary" principle is the practical expression of "never trust, always verify" — verification isn't a one-time gate, it's a continuous process requiring regular re-authentication. The chapter's framing of the control plane as trust grantor also makes clear why the control plane is the highest-value target in the entire architecture. If you compromise the control plane, you don't need to attack individual resources — you can grant yourself access to everything.

---

## Claim 6: Trust delegation via trust chains is what makes ZT scalable

**Authors' claim:** Trust in a ZT network "always originates with the operator" but operators don't scale — so trust must be delegated. "Trust delegation is important because it allows us to build automated systems that can grow to large scale and to operate in a secure and trusted way with minimal human intervention." The mechanism is a trust chain: the operator trusts a provisioning system, the provisioning system creates and vouches for new hosts, and those hosts can be trusted because "the provisioning system can prove that the operator has granted it the ability to do so." The operator is the trust anchor at the root of the chain.

**Evidence presented:** The auto-scaling example makes the case concretely: when a new server provisions itself, how do you know it's yours and not an attacker's? Because the provisioning system — which the operator explicitly trusted — created it and can cryptographically attest to that fact. This pattern of delegated, provable trust chains is the mechanism that allows ZT to operate at scale without human approval for every access decision.

**Confidence:** HIGH. Trust delegation via chains anchored in human operators is a well-established concept in computer security (it's how PKI itself works — the root CA is the trust anchor). The ZT application of this pattern extends it from identity (who are you) to authorization (what are you allowed to do and create).

**What's at stake:** The trust chain is only as strong as its weakest link. If the provisioning system is compromised, every host it creates is compromised, and the trust chain validates the attacker's hosts as legitimate. The chapter acknowledges this implicitly through the PKI discussion — the CA must be protected at all costs — but doesn't fully explore the blast radius of a broken trust chain. This is a gap that Chapter 4 (on control plane security) partially addresses.

**Who disagrees:** Some argue that trust delegation via chains is too brittle — a single compromise anywhere in the chain cascades. Alternatives like distributed trust (threshold signatures, multi-party authorization) reduce the blast radius but add complexity. The authors' position is pragmatic: chains are simple, well-understood, and the risks can be managed through operational security of the trust anchors.

**My assessment:** Trust delegation is the least developed concept in this chapter — it gets a brief introduction at the start and then the chapter moves on. But it's foundational: without delegation, ZT doesn't scale, and without chains, delegation is unverifiable. The chapter could have made a stronger connection between trust delegation and PKI (they're the same concept at different layers — PKI is trust delegation for identity; variable trust scores are trust delegation for authorization). This connection is implicit but not explicit.

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
