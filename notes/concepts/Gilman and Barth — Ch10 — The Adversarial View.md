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
---

# Gilman & Barth — Ch10: The Adversarial View

The unique chapter in Zero Trust literature. Where every other chapter builds ZT from the inside out — architecture, components, deployment — this chapter inverts the lens and asks: "If you were trying to penetrate a zero trust network, how might you do it?" It is Gilman & Barth's security considerations section in the IETF tradition — a systematic catalog of attack vectors, honest about what ZT mitigates and what it doesn't, and the only chapter in the book that explicitly evaluates the system as an adversary.

This note covers all eight threat categories (identity theft, DDoS, endpoint enumeration, untrusted computing platform, social engineering, physical coercion, invalidation, control plane security) and cross-references the threat taxonomies in NIST 800-207 Ch5 and NSA Embracing ZT. The three documents form a progression: Gilman & Barth provide the **engineering-level adversarial analysis**, NIST provides the **architectural threat taxonomy**, NSA provides the **operational threat model** with the "assume breach" mindset.

---

## Claim 1: Identity theft is the first and most dangerous threat — ZT requires stealing *two* identities

**Authors' claim:** "Practically all of the decisions and operations performed within a zero trust network are made on the basis of authenticated identity." Since ZT authenticates both device AND user/application, "it is necessary for an attacker to steal at least two identities in order to gain access to resources within it, raising the bar when compared to traditional approaches."

**Evidence presented:** The argument is structural, not empirical. ZT's dual authentication requirement (device + user) means credential theft alone is insufficient — the attacker also needs a trusted device identity. Trust engine behavioral analysis provides additional mitigation. The authors are careful to note that identity theft is an "industry-wide concern and is not specific to zero trust" but that ZT "naturally mitigates" the threat without claiming elimination.

**Confidence:** HIGH. The dual-identity requirement is a genuine architectural advantage. However, this claim is weakened if device identity is poorly protected — a stolen laptop with cached credentials defeats both checks simultaneously.

**What's at stake:** The single most important claim for ZT's defensive advantage. If attackers can routinely compromise both identities (e.g., via phishing + malware on a managed device), ZT's advantage collapses to behavioral detection, which is probabilistic, not preventive.

**Who disagrees:** NIST 800-207 Ch5 (§5.3) agrees but adds MFA and contextual trust algorithms as additional mitigations. NSA Embracing ZT provides worked examples showing the attack chain failing at device authentication. Google BeyondCorp papers emphasize device health attestation as the critical second factor — an unpatched device should fail even with valid user credentials.

**My assessment:** The dual-identity requirement is real but fragile. It's only as strong as the weaker of the two authentication systems. If device identity is bound to a TPM and user identity to a hardware token, the combination is genuinely hard to defeat. If both are software-based secrets on the same machine, one malware infection compromises both. This is why device attestation (Ch5) and hardware roots of trust matter — they're the difference between "two identities" and "two secrets stored on the same compromised machine."

---

## Claim 2: DDoS is still a problem — ZT doesn't mitigate it, it reframes how you respond

**Authors' claim:** "While the architecture strives to authenticate and authorize just about everything on the network, it does not provide good mitigation against denial-of-service (DoS) attacks on its own. Distributed DoS (DDoS) attacks that are volumetric in nature can be particularly troublesome."

**Evidence presented:** The authors acknowledge that "darkening" internet-facing endpoints via pre-authentication protocols (deny-all rules, narrow exceptions based on signaling) helps obscure addresses but "does not fundamentally mitigate DDoS attacks." Their key innovation: **policy-derived upstream filtering** — use ZT policy information about expected traffic patterns to calculate coarse, stateless enforcement rules for upstream devices. This has two advantages: fully automated configuration, and stateless operation that "obviates the need for expensive hardware and complicated state replication schemes."

**Confidence:** MEDIUM-HIGH. The policy-derived filtering approach is clever and genuinely novel — converting ZT's detailed knowledge of expected communication patterns into upstream scrubber rules. But it only works for large networks that control their own upstream infrastructure. Cloud-native deployments are told to "leverage an online DDoS-prevention service" — which is the same advice for non-ZT networks.

**What's at stake:** If the control plane itself is DDoS'd, the entire ZT network becomes unavailable — because nothing happens without the PE/PA. This is the ZT-specific DoS vulnerability that the authors don't address directly (NIST 800-207 §5.2 does).

**Who disagrees:** NIST 800-207 §5.2 identifies the PE/PA as DDoS targets specifically — a vulnerability the authors mention only implicitly through their control plane security discussion. NSA Embracing ZT subsumes availability under "assume breach" — the expectation is rapid recovery rather than prevention.

**My assessment:** This is one of the chapter's weakest sections — honest but thin. The policy-derived filtering idea is interesting but underdeveloped. The real concern (control plane availability) is deferred to the control plane security section. In practice, cloud-hosted ZT implementations (Zscaler, Cloudflare One) solve this through provider-scale DDoS protection, which the authors correctly identify as the pragmatic answer for most deployments.

---

## Claim 3: ZT guarantees confidentiality but not privacy — endpoint enumeration is a real tradeoff

**Authors' claim:** "The zero trust model guarantees network confidentiality, but not privacy. That is, ongoing conversations can be observed and asserted to exist; however, the contents of the conversation are protected." An adversary observing a perimeterless ZT network can "build a system diagram by observing which systems talk to which endpoints."

**Evidence presented:** The distinction between confidentiality (contents protected) and privacy (conversation existence hidden) is well-drawn. VPN architectures obscure which specific hosts communicate by hiding them behind a gateway — this advantage is lost in ZT's peer-to-peer model. The authors note that site-to-site tunnels can provide limited privacy but warn that this "undermines the zero trust model itself, as hiding information in one part of the network and not another suggests that one is more trusted than the other."

**Confidence:** HIGH. This is a clear, honest tradeoff. ZT trades network topology privacy for scalability, availability, and the elimination of gateway bottlenecks. Tor provides network privacy but is "a wholly different problem space" considered out of scope.

**What's at stake:** In military or intelligence environments, revealing which endpoints communicate can be as damaging as revealing what they say. This is why the DoD ZT RA retains VPN-like constructs for classified environments. For most enterprises, the confidentiality/privacy distinction is academic — content protection is sufficient, and the scalability gains of eliminating VPNs outweigh topology privacy concerns.

**Who disagrees:** NIST 800-207 §5.4 discusses visibility on the network from the defender's perspective (encrypted traffic is opaque to Layer 3 analysis). The authors discuss it from the attacker's perspective (conversation existence is observable). Both are correct — encryption is a double-edged sword.

**My assessment:** This is the most philosophically nuanced section of the chapter. The willingness to admit a genuine tradeoff — rather than claiming ZT is superior in every dimension — is a mark of engineering honesty that distinguishes Gilman & Barth from vendor literature. The practical advice is sound: if topology privacy matters, use tunnels, but understand you're reintroducing trust distinctions.

---

## Claim 4: ZT cannot defend against a malicious computing platform — only against simpler platform attacks

**Authors' claim:** "Totally defending against untrustworthy computing platforms is practically impossible." If hardware purposefully generates weak random numbers, even detecting the attack may be impossible if the attacker hides the capability most of the time. However, ZT can guard against "simpler attacks against the platform" through encryption of persistent data and swapped-out memory pages.

**Evidence presented:** The distinction between the "computing platform" (cloud hardware, hypervisor) and the "device" is carefully maintained — attacks against each differ because of privilege levels. The authors recommend encrypting data at rest and swapped memory as a mitigation against malicious peers on the platform, acknowledging it removes "some small amount of trust in the platform's operators."

**Confidence:** HIGH. This is the honest answer — no security model survives a compromised foundation. It echoes Ken Thompson's "Reflections on Trusting Trust" (1984): you can't trust code you didn't totally create yourself.

**What's at stake:** This is the argument for hardware roots of trust (TPM, secure enclaves) and supply chain security. If you can't trust the platform, the entire ZT architecture — which depends on device identity and attestation — is built on sand. This is why NSA's device pillar emphasizes firmware integrity and supply chain provenance so heavily.

**Who disagrees:** No one disputes the impossibility claim. The disagreement is about what "simpler attacks" means. Modern confidential computing (AMD SEV, Intel SGX) pushes the trusted boundary further down the stack but doesn't eliminate the problem. The authors' 2017 framing predates widespread confidential computing availability.

**My assessment:** Short section, correct conclusion. The more interesting question — which the authors don't explore — is whether ZT increases or decreases the attack surface of the platform. By requiring device attestation and identity, ZT gives the platform more responsibilities, making platform compromise more consequential. This is the double-edged sword again.

---

## Claim 5: Social engineering and physical coercion are the threats ZT can't solve — only contain

**Authors' claim:** For social engineering: "A zero trust network can only do so much to defend against attacks enabled by an unwitting participant." For physical coercion: "Defending against these types of compromises is ill-advised. No security professional would ever tell someone in this situation to risk their physical well-being to protect the information that they have access to."

**Evidence presented:** The social engineering discussion covers phishing and face-to-face communication (customer service attacks). Mitigations: behavioral analysis for less-sensitive resources, group authentication/authorization (Shamir's Secret Sharing) for critical assets. The physical coercion section includes the famous XKCD #538 reference ("someone with a blunt instrument can force even the most honest individuals to aid them") and recommends group authorization for high-value targets, with credential/device cycling and scanning for subtler physical attacks (USB insertion, unattended device tampering).

**Confidence:** HIGH on the framing — these are genuinely threats ZT doesn't eliminate. MEDIUM on the mitigations — behavioral analysis detects anomalies but doesn't prevent willing-but-deceived actions.

**What's at stake:** These two sections together acknowledge that the human element remains the irreducible vulnerability. Every technical control in ZT is mediated by humans who can be tricked, coerced, or compromised. The best defense is limiting the blast radius of any single human's compromise.

**Who disagrees:** NSA Embracing ZT's threat scenarios (compromised credentials, insider threat) directly parallel these concerns but frame them as ZT's raison d'être — the scenarios that prove ZT's value. Gilman & Barth are more cautious: ZT improves containment but doesn't prevent the initial compromise.

**My assessment:** The XKCD reference is the right frame. Physical coercion is a solved problem in the only way it can be solved: accept it and limit blast radius. The social engineering discussion is thinner than it should be — Ch6 has more detail on mechanisms (Shamir's Secret Sharing) but this section serves more as a catalog entry than a deep analysis. The group authentication recommendation is repeated across both sections, which is correct — it's the only reliable mitigation for single-human compromise of critical systems.

---

## Claim 6: Invalidation is a "hard problem in computer science" — ZT addresses it through granular authorization, not push-based revocation

**Authors' claim:** "Invalidation is a hard problem in computer science. In the context of a zero trust network, invalidation applies chiefly to long-running actions that were previously authorized but are no longer."

**Evidence presented:** Three approaches are presented in increasing sophistication: (1) more granular authorizations on short-lived actions (application-level requests instead of TCP sessions), (2) periodic session resets enforcing maximum lifetimes, (3) the best approach — enforcement components track ongoing actions and periodically reauthorize by querying the policy engine, forcibly resetting sessions if authorization is revoked. The authors note this is still a "pull" model — sessions can only be invalidated as fast as the longest polling period — but acknowledge push/event-based models "come with additional complexities and challenges which perhaps outweigh the benefits."

**Confidence:** HIGH. The pull-model limitation is real and honest. The progression from option 1 to 3 is a clear engineering tradeoff analysis.

**What's at stake:** If your polling period is 5 minutes and credential revocation happens at t=0, the attacker retains access until t=5. The question is whether that gap is acceptable. For most enterprises, yes. For high-security environments (defense, critical infrastructure), no — which is why push-based revocation is an active research area.

**Who disagrees:** NIST 800-207 §5.7 addresses a related concern with NPEs (non-person entities) — if autonomous agents make authorization decisions at machine speed, the invalidation gap becomes more dangerous. Gilman & Barth don't address NPEs (their 2017 framing predates widespread AI-agent deployment in security operations). Google BeyondCorp's Access Proxy model uses short-lived tokens with continuous revalidation, which is effectively approach 3 with a very short polling period.

**My assessment:** This is one of the chapter's strongest sections — clearly framed, honestly bounded, with a practical solution progression. The willingness to admit that push-based models "perhaps outweigh the benefits" is characteristic of the authors' engineering pragmatism. The open question — which the authors don't address — is whether authorization granularity should be driven by risk (higher-risk resources get per-request authorization, lower-risk get per-session) or uniformly applied. The implicit answer is risk-driven, which is the right one.

---

## Claim 7: Control plane compromise is the worst-case scenario — and it must be defended with the highest rigor

**Authors' claim:** "It is possible to completely undermine the zero trust architecture if a control plane compromise is pervasive enough. As such, it is absolutely critical to ensure the security of these systems."

**Evidence presented:** The control plane comprises multiple services (policy engine, inventory tracking, data stores). Not all are equal: compromising historical access data "is strictly less useful to an attacker than compromising the policy engine" — the former allows falsifying access patterns to artificially raise trust scores, the latter leads to "complete compromise of zero trust authorization." Mitigations: group authentication/authorization for policy engine changes, broadly visible alerts (no change goes unnoticed), administrative isolation (dedicated cloud account, rigorous access control) while keeping systems logically integrated, and eventually "zero trust enforcement can be slowly applied to the control plane systems themselves. Kind of like rewriting the C compiler in C."

**Evidence presented:** The approach of "backing zero trust enforcement into the control plane" — making the control plane itself a consumer of ZT policies — is the most architecturally sophisticated recommendation. It eliminates special cases and ensures homogeneous security enforcement. The authors warn against the temptation to put control plane systems in a perimeter network: "The alternative would leave these systems the least protected of all, and is generally unacceptable in the context of a zero trust network."

**Confidence:** VERY HIGH. This is the best section of the chapter — comprehensive, practical, and architecturally honest. Every major ZT framework (NIST, DoD, CISA) treats control plane security as the critical architectural concern.

**What's at stake:** The control plane is the single point of failure in ZT architecture. If you can't protect it, you can't have Zero Trust. The "rewriting the C compiler in C" analogy is apt: you're using ZT to protect ZT, creating a chicken-and-egg problem that requires careful bootstrapping.

**Who disagrees:** NIST 800-207 §5.1 (Subversion of ZTA Decision Process) covers the same ground with a slightly different emphasis — NIST focuses on configuration abuse and compromised PA specifically, while Gilman & Barth emphasize the architectural isolation approach. NSA Embracing ZT's "assume breach" principle implies that control plane compromise should be planned for (detection, recovery) rather than assumed impossible to prevent. DoD ZT RA's multi-decision-point architecture distributes control plane functions across five decision points, reducing blast radius compared to a single PDP — this is a structural mitigation Gilman & Barth don't explore.

**My assessment:** The progression from "protect the control plane traditionally" → "administer isolately" → "subject the control plane to ZT itself" is the correct maturity path. The warning against perimeterizing the control plane is the most important sentence in this section — it's the architectural discipline that distinguishes ZT from perimeter-plus-ZT-window-dressing. The group authentication recommendation for policy engine changes is underappreciated: it's the only mechanism that prevents a single compromised administrator from destroying the entire ZT fabric. Every production ZT deployment should implement this.

---

## Claim 8: The adversarial view reveals that ZT is a risk reduction strategy, not a risk elimination strategy

**Authors' claim:** "Even a zero trust network can be compromised by a determined adversary, as the inconvenience of defending against any theoretical attack is simply too high a price to pay in the day-to-day operation of such a network." And: "When faced with the most advanced attacks, the best we can hope for is efficient and accurate detection. Starting from the assertion that a system has been compromised and working our way backward toward limiting the damage is sage advice."

**Evidence presented:** This is the summary's thesis — the chapter catalogs attack vectors not to show ZT's invulnerability but to identify what ZT mitigates, what it detects, and what it can only contain. The honest acknowledgment that "every system is susceptible to an attacker with sufficient resources" is the chapter's meta-claim.

**Confidence:** HIGH. This framing anticipates NSA's "assume breach" principle by four years and is more nuanced — Gilman & Barth distinguish between threats ZT prevents (unauthorized access), detects (behavioral anomalies), and contains (blast radius of compromised identities).

**What's at stake:** The entire credibility of the Zero Trust literature depends on this honesty. If Gilman & Barth claimed ZT eliminates all threats, the book would be vendor marketing. By cataloging what ZT doesn't solve, they establish the engineering credibility that makes the rest of the book's architectural recommendations trustworthy.

**Who disagrees:** Vendor ZT literature routinely overclaims. Gilman & Barth's chapter is the antidote. NIST 800-207 Ch5 takes the same honest approach — "No enterprise can eliminate cybersecurity risk" — but with a formal taxonomy. NSA takes a different rhetorical approach: the threats are the *reason* for ZT, so the emphasis is on what ZT *prevents* rather than what it doesn't.

**My assessment:** This chapter, more than any other, makes Gilman & Barth's book the most intellectually honest work in the Zero Trust canon. The willingness to say "here's what we can't protect against" — and to mean it, not as rhetorical setup for a solution — establishes trust with the reader that the rest of the book's claims have been similarly scrutinized. Every ZT implementation team should read this chapter as a threat model checklist during architecture review.

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

