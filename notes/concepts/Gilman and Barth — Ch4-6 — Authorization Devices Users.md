---
tags:
  - source/books
  - gilman-barth
  - zt-authorization
  - zt-device
  - zt-user
  - zt-tpm
  - zt-mfa
  - oskg-zerotrust
created: 2026-07-24
confidence: high
source:
  title: "Zero Trust Networks: Building Secure Systems in Untrusted Networks"
  authors: "Evan Gilman, Doug Barth"
  year: 2017
  publisher: "O'Reilly Media"
  local_file: "sources/books/_txt/Zero_trust_networks_building_secure_systems_in_untrusted_networks.txt"
  chapters: "4–6 (Authorization Decisions, Trusting Devices, Trusting Users)"
  lines: 2064–4192
note_type: combined
justification: >
  Three chapters form a single unit on trust computation and the entities trusted.
  Ch4 defines how trust is computed (policy engine + trust engine + data stores).
  Ch5 and Ch6 define the entities being trusted (devices and users). Combining
  preserves the trust flow while reducing redundancy across device/user discussions.
related:
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[NIST 800-207 — Ch5 — Threats]]"
  - "[[NIST 800-207 — Ch7 — Migration]]"
  - "[[NSA — Device Pillar]]"
  - "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
  - "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
  - "[[Books Index]]"
  - "[[Concepts Index]]"
---

# Gilman & Barth — Ch4–6 — Authorization Decisions, Device Trust, and User Trust

**Chapters 4–6 form a single logical unit: trust is computed by the authorization subsystem (Ch4), then applied to the two primary entities the network must trust — devices (Ch5) and users (Ch6).** Gilman & Barth published this in 2017, when Zero Trust was still "very new" and "undergoing rapid evolution." The book is the earliest comprehensive practitioner's guide to ZT network architecture, and these three chapters define the trust path end-to-end.

---

## Part I: Authorization Architecture (Ch4, lines 2064–2483)

**Scope:** How authorization decisions are made — the four-component architecture, trust scoring, policy definition, and the flow from enforcement through policy engine to data stores.

### Claim 1: The authorization architecture has four distinct, isolated components

**Authors' claim:** "The zero trust authorization architecture comprises four main components: Enforcement, Policy Engine, Trust Engine, and Data Stores. These four components are distinct in their responsibilities... these systems represent the practical crown jewels of the zero trust security model, so special care should be taken in their maintenance and security posture."

**Evidence presented:** The authors argue from engineering principles — isolation prevents cascading compromise. The enforcement component is "in the user's data path, more exposed," so it must be process-level isolated from the policy engine. They reference Google's BeyondCorp as having "pioneered" the trust engine concept.

**Confidence:** HIGH. This four-component decomposition has become the standard reference model. NIST 800-207 formalized the same components as PEP (enforcement), PA (policy engine), and PE (with supporting data). The names differ but the functions align precisely.

**What's at stake:** If these four responsibilities are collapsed into a single system (which the authors explicitly warn against), a compromise of any one yields full authorization control. The isolation requirement is the structural security property that makes ZT authorization defendable.

**Who disagrees:** NIST 800-207 permits the PA and PE to be co-located or combined "for simple deployments" but maintains the same logical separation. Simplified vendor implementations (e.g., SDP controllers) often merge enforcement + policy engine for latency reasons, which the authors acknowledge but argue against without process-level isolation.

**Alternative reading:** The four-component model could be read as describing an ideal rather than a minimum — in practice, many "zero trust" products ship only enforcement + basic policy engine, deferring trust scoring to SIEM/SOAR. The model works better as a maturity target than a compliance gate.

**My assessment:** This is the most architecturally significant claim in Ch4. The component isolation principle is what distinguishes ZT authorization from traditional firewall rules or RBAC. Without it, ZT degenerates to perimeter-by-policy.

---

### Claim 2: The trust engine is the novel contribution of ZT — using risk scoring to catch unknown attacks

**Authors' claim:** "The trust engine is leveraged by the policy engine for risk analysis purposes. It leverages multiple data sources in order to compute a risk score, similar to a credit score. This score can be used to protect against unknown unknowns, and helps keep policy strong and robust without complicating it with edge cases and signatures."

**Evidence presented:** The trust engine pulls from inventory systems (device, user) and historical data stores. The authors describe two approaches: (a) ad hoc static rules (e.g., "a device missing latest patches has its score reduced"), sufficient for early adoption; (b) machine learning on training data derived from activity labeled as trusted/untrusted. They argue mature systems use both — ML for predictive scoring, static rules for customization.

**Confidence:** MODERATE on the ML component (the authors themselves say "the zero trust model is still very new" and "known implementations still vary wildly"). HIGH on the architectural claim that trust scoring should be separable from policy definition.

**What's at stake:** If trust scoring is wrong or gamed, the whole authorization system collapses to whatever static policy remains. Conversely, over-reliance on scoring without specific policy rules creates a "scoring monoculture" that clever attackers can optimize against.

**Who disagrees:** NIST 800-207 doesn't mandate trust scoring — it says the PE collects data and evaluates trust but doesn't prescribe a scoring function. NSA emphasizes deterministic compliance checks (patch level, config status) rather than probabilistic scoring. CISA's maturity model adds risk scoring only at Optimal maturity, not earlier.

**My assessment:** The trust engine is the ZT component with the largest gap between aspiration and implementation. In 2017, Gilman & Barth envisioned ML-driven risk scoring. In practice, most ZT deployments in 2024 still rely primarily on static rules, with scoring limited to simple aggregations (device age, last seen, patch status). The "credit score" analogy is powerful but the data quality problem is harder than the authors anticipated.

---

### Claim 3: Policy should be defined in terms of logical components, not network addressing

**Authors' claim:** "Instead of defining policy in terms of network implementation details (IP addresses and ranges), policy is best defined in terms of logical components in the network. These components will generally consist of: Network services, Device endpoint classes, User roles."

**Evidence presented:** They cite Kubernetes network policies (workload labels computing IP rules at enforcement time) as an example. Policy stored in version control enables code review, change tracking, validation. They add: "Most policy should include a trust score component." On who defines policy: distributed across teams with security review, layered with infrastructure policy that no user can override.

**Confidence:** HIGH. This is widely adopted — Kubernetes NetworkPolicy, service mesh authorization policies, and cloud IAM all define policy on logical labels. NIST 800-207's PA operates on "subject attributes" (identity-based) not network attributes. The version-control recommendation is standard practice.

**What's at stake:** If policy is defined on IP addresses, ZT loses its ability to adapt to dynamic infrastructure. Workload scheduling, auto-scaling, and failover all break static IP-based policy. The "logical component" principle is what makes ZT feasible in cloud-native environments.

**Who disagrees:** No major source disagrees. The gap is in standardization — Gilman & Barth note: "Currently, mature zero trust networks implement their own policy language/format on a case-by-case basis... such work remains an open research question." This remains true in 2024 (OPA/Rego, Cedar, various vendor-specific DSLs).

---

### Claim 4: Entities should be scored at multiple levels — network agent, device, and user

**Authors' claim:** "Taken as a whole, it seems like the right solution is to score both the network agent itself and the underlying entities that make up the agent."

**Evidence presented:** Three scenarios: (1) brute-force attack on user credentials → score the attacker's network agent, not the user account (avoids denial-of-service via lockout); (2) compromised device → all network agents on that device should be penalized; (3) malicious human user moving across kiosk devices → the user's score should follow them. Each scenario demonstrates that scoring only the agent is insufficient.

**Confidence:** HIGH on the architectural claim, MODERATE on implementation practicality. The authors acknowledge: "Presenting so many scores for consideration when writing policy, however, can make the task of crafting policy more difficult and error prone."

**My assessment:** The multi-entity scoring framework anticipates the layered trust model that later became standard. Modern ZT implementations tend to score the session (agent + device + user composite) rather than exposing individual entity scores to policy writers, which addresses the "error prone" concern.

---

### Architecture Synthesis

| Component | Responsibility | Threat if compromised | Isolation strategy |
|-----------|---------------|----------------------|-------------------|
| **Enforcement** | Carry out authorization decision; front-line in data path | Attacker bypasses all authorization | Process-level isolation from policy engine |
| **Policy Engine** | Compare request context against policy; make decision | Complete compromise of ZT authorization | Heavily isolated; separate process or host |
| **Trust Engine** | Compute numeric risk score from inventory + historical data | Attacker manipulates scores to gain access | Separate service; read-only access to data stores |
| **Data Stores** | Source of truth: inventories (current state) + historical data (past behavior) | Attacker poisons the authoritative record | Rigorous write-access control; provenance tracking |

**Cross-reference — NIST 800-207 Ch3 (Logical Components):** NIST's PEP/PA/PE model maps directly to Gilman & Barth's enforcement/policy-engine/trust-engine. The key difference: NIST atomizes the "data stores" across multiple feed sources to the PE; Gilman & Barth treat data stores as first-class components. NIST 800-207 Ch5 on threats specifically warns about policy engine compromise, citing Gilman & Barth's argument that it leads to "a complete compromise of zero trust authorization."

**Cross-reference — NIST 800-207 Ch7 (Migration):** NIST references Gilman & Barth for "constructing trust scores and policy logic for the proxy model" — acknowledging that the trust engine + policy engine interaction is the hard part of incremental ZT adoption.

---

## Part II: Trusting Devices (Ch5, lines 2480–3469)

**Scope:** How devices gain, prove, and maintain trust — from secure boot through X.509 identity, TPM-backed hardware attestation, inventory management, and trust signal decay.

### Claim 5: Device identity requires binding software credentials to hardware

**Authors' claim:** "Without a way to bind the software key to the hardware device it is attempting to identify, we cannot really call it device identity. TPMs solve this problem, providing the necessary binding."

**Evidence presented:** The chapter systematically escalates through storage methods: (1) file permissions only (weakest — attacker with root can exfiltrate the key), (2) encrypted private key with passphrase (better but impractical for servers), (3) TPM/HSM storing private key in hardware that "never leaves the security module." TPM endorsement keys (EK) provide unique hardware identity. Platform Configuration Registers (PCRs) store hashes of boot chain software, enabling attestation that the system is "in an approved configuration."

**Confidence:** VERY HIGH. This is the consensus view across all frameworks. NSA's Device Pillar mandates TPM and secure boot at Basic maturity, PCR-based attestation at Intermediate, and SBOM/RIM integration at Advanced. DoD ZT RA requires device attestation as a core capability.

**What's at stake:** If X.509 certificates (software-based identity) are used without hardware binding, device identity is trivially compromised — steal the private key, impersonate the device. The TPM is the "linchpin between software identity and physical hardware."

**Who disagrees:** No one disagrees on the principle. The disagreement is about minimum bar: Gilman & Barth say TPM "should not be considered a requirement" and that "there are much lower-hanging fruits in terms of zero trust adoption and migration." NSA sets TPM as a firm requirement. This reflects a maturity vs. accessibility trade-off.

---

### Claim 6: Certificate signing is a trust injection point that must be secured with multi-party authorization

**Authors' claim:** "By splitting these responsibilities and requiring multiple systems to assert validity, we can safely (well, as safely as is possible) remove humans from the loop."

**Evidence presented:** The authors analyze three trust sources for certificate signing: (a) humans (with TOTP — secure but doesn't scale), (b) resource managers (can assert "I turned this host on"), (c) image/device credentials (baked into image or TPM-backed). Their recommended approach: combine resource manager + image/device credentials with multiple validation points (registered TPM key, correct IP, TOTP from resource manager, expected certificate properties). They cite the DigiNotar CA breach (2011) as the cautionary tale.

**Confidence:** HIGH. The multi-party signing model is well-established. NIST 800-207 expects the PA to evaluate multiple attributes from multiple sources before granting access. Practices like SPIFFE (workload identity) implement this pattern for service-to-service authentication.

**My assessment:** This claim generalizes beyond certificate signing to all ZT trust injection. Every trust anchor needs multiple corroborating signals. The specific mechanisms (TOTP, resource manager attestation) are implementation details of a deeper principle: no single assertion is sufficient to establish trust.

---

### Claim 7: Trust degrades over time — device age is the strongest negative signal

**Authors' claim:** "The natural progression is that the longer a device is operating, the greater its chances of being compromised. This is why device age is a heavily weighted trust signal."

**Evidence presented:** Trust renewal mechanisms: reimaging (logically rotates device — removes "majority of persistent threats"), hardware rotation (tear down and rebuild cloud instances), TPM remote attestation (hardware-backed, "highly reliable" but limited to low-level software), software-based local measurement (agent reporting — "generally futile" against privileged attackers), remote vulnerability scanning (external probing — benefits from separation of duty but "relies on interrogation of the endpoint").

**Confidence:** HIGH on the principle, MODERATE on specific renewal mechanisms. Remote vulnerability scanning and local agents are both acknowledged as flawed ("it's the difference between asking someone if they robbed a bank, and watching them rob a bank").

**What's at stake:** If trust never decays, a device compromised on Day 1 retains full access indefinitely. The decay function is the security model's immune system. Getting the decay rate wrong means either too many false positives (locking out legitimate users) or false negatives (allowing compromised devices to persist).

**Cross-reference — NSA Device Pillar:** NSA's four-phase maturity model makes this explicit: Preparation phase establishes inventory; Basic mandates TPM and secure boot; Intermediate requires remote attestation and continuous monitoring; Advanced integrates SBOM/RIM with cryptographically proven firmware integrity. Gilman & Barth's 2017 guidance anticipates all four phases, though with less specificity about auditability requirements.

---

### Claim 8: Device data contextualizes and strengthens user authentication

**Authors' claim:** "When user authentication occurs, device authentication has already succeeded, and the network has knowledge of the device identity. This position can be leveraged for all kinds of useful contextual knowledge."

**Evidence presented:** Examples: (a) check whether the user is expected on that device type (engineer credentials from HR-issued device → suspicious); (b) user authentication frequency from a device — a device not seen in a year suddenly presenting credentials is suspicious; (c) lower trust score for anomalous pairings, allowing degraded access (read wiki but not financial systems). The authors call this "one of the more common lookups" and note it's "invaluable."

**Confidence:** HIGH. This is the architecture connecting Ch5 to Ch6. Device authentication first, user authentication second, each informing the other. The interaction between device and user trust signals is what makes ZT authorization richer than traditional per-entity auth.

---

### Device Trust Signals (Table)

| Signal | Mechanism | Reliability | Limitation |
|--------|-----------|------------|------------|
| **Time since image** | Record of last reimage | Strong assurance immediately, decays over time | Doesn't address firmware/hardware implants |
| **Historical access patterns** | Device seen frequency + resource access history | Good proxy for behavioral filtering | "First few" accesses always look suspicious |
| **Location** | GeoIP, office presence | Useful for sudden changes | Authors warn: "never make an absolute decision based solely on location" |
| **Network communication patterns** | Netflow, DNS queries | "Very powerful" — catches intrusions by observing behavior | Requires network instrumentation; only works on managed networks |

---

## Part III: Trusting Users (Ch6, lines 3469–4192)

**Scope:** How users establish and prove identity — authoritative vs. informal identity, bootstrapping, authentication mechanisms, trust-driven auth flow, group authorization, and user trust signals.

### Claim 9: User identity and device identity are separate trust domains — conflating them is dangerous

**Authors' claim:** "Zero trust networks identify and trust users separately from devices. Sometimes identifying a user will use the same technology that is used to identify devices, but we must be clear that these are two separate credentials."

**Evidence presented:** The authors open Ch6 with the problem: "How do we know that the intended user is actually at the keyboard? Perhaps they left their device unlocked and unattended?" They also note: user credentials copied across multiple devices increase exposure; kiosk scenarios make device-user binding impossible. The solution is layered authentication — device first, user second, each with independent trust scores that combine at authorization time.

**Confidence:** VERY HIGH. This is a foundational ZT principle echoed by every framework. NIST 800-207: "Access to individual enterprise resources is granted on a per-session basis. Trust in the requester is evaluated before access is granted." The per-session evaluation inherently combines device + user trust.

**What's at stake:** Conflating the two collapses the layered defense. A stolen device with a certificate becomes full user impersonation. A compromised user session on a compromised device has no redundant signal.

---

### Claim 10: Trust score should drive authentication requirements, not static sensitivity labels

**Authors' claim:** "Rather than selecting particular actions which require additional authentication, one should assign a required score and allow the trust score itself to drive the authentication flow and requirements."

**Evidence presented:** The traditional approach — designate sensitive actions and authenticate heavily for those — is "likened to perimeter security, in which sensitive actions must pass a particular test, after which no further protections are present." Instead: if the user's trust score is already high (recent strong auth, normal patterns), don't re-prompt. If it's low (unusual location, new device), prompt for additional factor. The system "chooses a combination of methods in order to meet the goal, possibly reducing the invasiveness by having context about the level of sensitivity."

**Confidence:** HIGH. This is the architecture behind adaptive authentication / step-up auth. It's now mainstream (Azure AD Conditional Access, Okta Adaptive MFA). In 2017 it was forward-looking.

**What's at stake:** Static auth requirements create a false sense of security (one-time gate, then trust everything) and degrade UX (users prompted for 2FA on low-risk actions). Trust-driven auth is the ZT authentication principle.

**Cross-reference — NIST 800-207 Ch3:** NIST's PE evaluates trust on a per-session basis using "as many sources as possible." The dynamic trust score driving authentication is the logical extension of NIST's continuous evaluation principle.

---

### Claim 11: The strongest user authentication binds identity to hardware tokens with additional factors

**Authors' claim:** "If we want the strongest guarantee that a particular user is who they claim to be, using a security key with additional authentication factors (e.g., a password or biometric sensor) is still strongly recommended."

**Evidence presented:** The chapter surveys the authentication landscape systematically:

| Method | Category | Strength | Weakness |
|--------|----------|----------|----------|
| Passwords | Something you know | Effective when long + unique + not reused | Users choose poor passwords; reuse across services |
| TOTP | Something you have | Good second factor | Shared secret must be protected; SMS is explicitly not recommended |
| X.509 user certificates | Something you have | Rich metadata; computer-verifiable | Private key storage is the weak point |
| Security tokens (YubiKey, smart card) | Something you have | Private key never leaves hardware | Token can be stolen; needs pairing with PIN or biometric |
| Biometrics (fingerprint, face) | Something you are | Convenient; hard to share | Cannot be rotated; can be spoofed; legal issues (Fifth Amendment) |
| U2F/UAF (FIDO) | Something you have | Replay-resistant; per-service keys; phishing-resistant | Requires ecosystem support |

The authors highlight U2F (now FIDO2) as the forward-looking standard: "Open standards like the FIDO Alliance's UAF standard use asymmetric cryptography and local device authentication systems to move trust away from a large number of services to relatively few user-controlled endpoints."

**Confidence:** HIGH on the assessment of current mechanisms. The biometric discussion is notably nuanced — the authors flag rotation impossibility, spoofing, and legal compulsion (Fifth Amendment vs. compelled fingerprint) — concerns that remain relevant in 2024.

---

### Claim 12: Out-of-band and multi-channel authentication raise the attacker's cost by requiring compromise of independent channels

**Authors' claim:** "Leveraging multiple channels is effective not because compromising a channel is hard, but because compromising many is hard."

**Evidence presented:** Separate communication channels (push notification to mobile device, confirmation call, email notification) verify that the requestor controls something independent of the primary authentication channel. The authors warn: "be sure to use a different channel than the one you are trying to authenticate/authorize in the first place." They explicitly reject SMS as a channel ("SMS system does not make sufficient guarantees to protect the random code in transit").

**Confidence:** HIGH. Multi-channel is foundational to modern auth (WebAuthn + platform authenticator, push-to-approve). The SMS warning was prescient — NIST deprecated SMS-based 2FA in 2017 (SP 800-63B).

---

### Claim 13: SSO should not remove the control plane from ongoing authorization

**Authors' claim:** "When designing authentication systems in a zero trust network, aim for as much control plane responsibility as possible, and validate authorization with the control plane as often as is reasonably possible."

**Evidence presented:** SSO provides: single authentication point, centralized credential storage, reduced credential surface area. But the common pattern of "validate token at session start, then let the application manage its own session" is "generally undesirable" because "trust variance and invalidation is a key aspect of a zero trust network." The control plane should revalidate on every request or as frequently as latency allows.

**Cross-reference — NIST 800-207 Ch7 (Migration):** This maps to the "per-session" access model. NIST's guidance on proxy/gateway migration models depends on this continuous revalidation property.

---

### Claim 14: Group authorization is the highest-trust mechanism for extremely sensitive operations

**Authors' claim:** "Nearly every system has a small set of actions or requests that must be closely guarded... it is desirable to gain the consent of multiple individuals in order to authorize a particularly sensitive action."

**Evidence presented:** Three mechanisms: (1) Shamir's Secret Sharing — split a secret into n parts, require k parts to reconstruct (cryptographically guaranteed); (2) Cloudflare's Red October — layered asymmetric encryption requiring n-of-m users; (3) DNS Root Zone Signing Ceremony — seven actors, HSMs, biometric scanners, air-gapped systems, quarterly ceremony achieving "one-in-a-million chance" of compromise (assuming 5% dishonesty rate). The authors use these to illustrate the spectrum from purely cryptographic (Shamir) to heavily procedural (DNS ceremony).

**Confidence:** HIGH on the concept, with the DNS ceremony as the gold-standard example of defense-in-depth for root trust anchors.

---

### User Trust Signals (Table)

| Signal | Mechanism | Pattern Detected |
|--------|-----------|-----------------|
| **Authentication frequency** | Rate and volume of auth attempts | Brute force (many/second), credential stuffing |
| **Application usage patterns** | Which resources accessed, how often | Access outside normal role; unusual data volume |
| **Known-bad sources** | Spamhaus, threat intel feeds | Auth attempts from malicious IPs using legitimate credentials |
| **Geolocation** | Compare current location vs. history | Impossible travel; conflicting locations across devices |

---

## Synthesis: The Trust Flow Through Ch4–6

The three chapters form a complete pipeline:

```
DATA STORES (inventories + history)
        ↓
TRUST ENGINE (risk scoring)
        ↓
POLICY ENGINE (decision)
        ↓
ENFORCEMENT (action)
        ↑
DEVICE TRUST ← device auth (X.509 + TPM) + device trust signals
USER TRUST   ← user auth (MFA/security tokens) + user trust signals
```

**Key insight:** Ch4 defines the *machinery* of trust computation (the architecture). Ch5 and Ch6 define the *inputs* to that machinery (the entities being trusted and the signals they generate). The architectural innovation is that these are decoupled — the trust engine doesn't care whether it's scoring a device or a user; it consumes inventory + historical data and produces a numeric score. The policy engine doesn't care how the score was derived; it compares score + attributes against policy. This decoupling is what makes ZT authorization scalable across new entity types (applications are added in Ch7 without changing the architecture).

| Component | Ch4 (Architecture) | Ch5 (Devices) | Ch6 (Users) |
|-----------|-------------------|---------------|-------------|
| **Identity proof** | Authentication is a prerequisite | X.509 certificates + TPM binding | Multi-factor: passwords, tokens, biometrics |
| **Trust injection** | N/A (framework) | Certificate signing (human, resource manager, or image) | In-person bootstrapping + government ID |
| **Trust signals** | Trust engine consumes them | Device age, access patterns, location, network behavior | Auth frequency, usage patterns, IP reputation, geolocation |
| **Trust decay** | Trust score is dynamic | Reimage rotation; TPM attestation renewal | Re-authentication driven by score threshold |
| **Cross-entity context** | Policy engine combines entity scores | Device data enriches user auth (Ch5 §"Using Device Data") | User/device pairing produces composite score |

### Cross-Source Alignment

| Gilman & Barth (2017) | NIST 800-207 (2020) | NSA (2021–2023) | CISA ZTMM (2021) |
|------------------------|---------------------|-----------------|------------------|
| Four-component auth architecture | PEP/PA/PE model | Policy decision/enforcement points | Five-pillar model with policy decision function |
| Trust engine with ML scoring | PE evaluates trust from multiple sources | Deterministic compliance checks (patch, config) | Risk scoring added at Optimal maturity only |
| TPM + remote attestation for device identity | Device posture assessment required | TPM mandated at Basic, attestation at Intermediate | Device hygiene as a pillar; TPM at Advanced |
| Adaptive auth driven by trust score | Continuous authentication implied | Multi-factor required across pillars | MFA as a core capability |
| Multi-entity scoring (agent + device + user) | Per-session trust evaluation | Separate pillars for User and Device | Separate pillars with cross-pillar integration |

**Gilman & Barth's unique contribution:** They connect the architecture to implementation in a way the standards documents don't. Where NIST says "evaluate trust," Gilman & Barth explain exactly how — TPM attestation, device age weighting, device-user pairing, trust-driven step-up auth. Their 2017 book remains the best practitioner-level bridge between ZT theory and ZT engineering.

---

*Note type: combined. Chapters 4–6 form a single unit on trust computation and the entities trusted. Combining preserves the trust flow (architecture → device trust → user trust → composite authorization) while eliminating redundancy across the parallel device/user trust discussions.*
