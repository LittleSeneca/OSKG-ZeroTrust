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
claims_status: extracted
claims_extracted: 2026-07-24
---

# Gilman & Barth — Ch4–6 — Authorization Decisions, Device Trust, and User Trust

**Chapters 4–6 form a single logical unit: trust is computed by the authorization subsystem (Ch4), then applied to the two primary entities the network must trust — devices (Ch5) and users (Ch6).** Gilman & Barth published this in 2017, when Zero Trust was still "very new" and "undergoing rapid evolution." The book is the earliest comprehensive practitioner's guide to ZT network architecture, and these three chapters define the trust path end-to-end.

---

## Part I: Authorization Architecture (Ch4, lines 2064–2483)

**Scope:** How authorization decisions are made — the four-component architecture, trust scoring, policy definition, and the flow from enforcement through policy engine to data stores.

**Claim 1 —** The authorization architecture has four distinct, isolated components → [[the-authorization-architecture-has-four-distinct-isolated-components]]

---

**Claim 2 —** The trust engine is the novel contribution of ZT — using risk scoring to catch unknown attacks → [[the-trust-engine-is-the-novel-contribution-of]]

---

**Claim 3 —** Policy should be defined in terms of logical components, not network addressing → [[policy-should-be-defined-in-terms-of-logical]]

---

**Claim 4 —** Entities should be scored at multiple levels — network agent, device, and user → [[entities-should-be-scored-at-multiple-levels-network]]

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

**Claim 5 —** Device identity requires binding software credentials to hardware → [[device-identity-requires-binding-software-credentials-to-hardware]]

---

**Claim 6 —** Certificate signing is a trust injection point that must be secured with multi-party authorization → [[certificate-signing-is-a-trust-injection-point-that]]

---

**Claim 7 —** Trust degrades over time — device age is the strongest negative signal → [[trust-degrades-over-time-device-age-is-the]]

---

**Claim 8 —** Device data contextualizes and strengthens user authentication → [[device-data-contextualizes-and-strengthens-user-authentication]]

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

**Claim 9 —** User identity and device identity are separate trust domains — conflating them is dangerous → [[user-identity-and-device-identity-are-separate-trust]]

---

**Claim 10 —** Trust score should drive authentication requirements, not static sensitivity labels → [[trust-score-should-drive-authentication-requirements-not-static]]

---

**Claim 11 —** The strongest user authentication binds identity to hardware tokens with additional factors → [[the-strongest-user-authentication-binds-identity-to-hardware]]

---

**Claim 12 —** Out-of-band and multi-channel authentication raise the attacker's cost by requiring compromise of independent channels → [[out-of-band-and-multi-channel-authentication-raise-the-attackers-cost]]

---

**Claim 13 —** SSO should not remove the control plane from ongoing authorization → [[sso-should-not-remove-the-control-plane-from]]

---

**Claim 14 —** Group authorization is the highest-trust mechanism for extremely sensitive operations → [[group-authorization-is-the-highest-trust-mechanism-for-extremely]]

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
