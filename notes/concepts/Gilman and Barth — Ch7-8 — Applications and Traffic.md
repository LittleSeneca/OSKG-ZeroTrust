---
tags:
  - source/books
  - gilman-barth
  - zt-application
  - zt-traffic
  - zt-mtls
  - zt-build
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
  lines: "L4192–6167"
related:
  - "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
  - "[[NIST 800-207 — Ch5 — Threats]]"
  - "[[CISA ZTMM — Device Network App Data Pillars]]"
  - "[[NSA — Device Pillar]]"
  - "[[NSA — Network Environment Pillar]]"
  - "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
  - "[[Concepts Index]]"
note_type: combined
justification: >
  Applications and traffic trust are operationally adjacent — apps produce traffic,
  traffic carries app data. Combining highlights the provenance-to-packet trust chain:
  from signed source code through build pipelines to mutually authenticated TLS/IPsec
  flows carrying that same application's data in production.
  - topic/zt-implementation
  - topic/zt-network
  - topic/zt-app
---

# Gilman & Barth — Ch7–8: Trusting Applications and Trusting the Traffic

These two chapters form a continuous argument: trust must flow from the developer's keyboard all the way to the network packet. Chapter 7 establishes the application provenance chain (source → build → distribution → execution). Chapter 8 secures what those applications produce — network traffic — through encryption, authentication, and filtering. Together they answer: _how do you know the application talking on your network is the one you built, and how do you know its traffic hasn't been tampered with?_

## Ch7: Trusting Applications

**Claim 1 —** The application pipeline is a cryptographic chain — break any link and trust is lost → [[the-application-pipeline-is-a-cryptographic-chain-break]]

---

**Claim 2 —** Git's content-addressable storage provides tamper-proof history but not authenticity — signed commits bridge the gap → [[gits-content-addressable-storage-provides-tamper-proof-history-but-not]]

---

**Claim 3 —** The build system is the most dangerous attack vector — it sits between two cryptographically protected states with no protection of its own → [[the-build-system-is-the-most-dangerous-attack]]

---

**Claim 4 —** Immutable artifacts with decoupled version numbers prevent masquerade attacks → [[immutable-artifacts-with-decoupled-version-numbers-prevent-masquerade]]

---

**Claim 5 —** Per-instance time-bound secrets are the mechanism for authorizing running applications → [[per-instance-time-bound-secrets-are-the-mechanism-for-authorizing]]

---

**Claim 6 —** Runtime security completes the trust lifecycle — isolation, secure coding, and active monitoring → [[runtime-security-completes-the-trust-lifecycle-isolation-secure]]

---

## Ch8: Trusting the Traffic

**Claim 7 —** Encryption and authentication are separate concerns — zero trust requires authenticity; encryption comes "for free" → [[encryption-and-authentication-are-separate-concerns-zero-trust]]

---

**Claim 8 —** The first packet problem is solved by Single Packet Authorization (SPA) → [[the-first-packet-problem-is-solved-by-single]]

---

**Claim 9 —** TLS and IPsec serve different roles — mTLS for client/server, IPsec for server/server datacenter → [[tls-and-ipsec-serve-different-roles-mtls-for]]

---

**Claim 10 —** Cipher suite negotiation is an anti-pattern — newer protocols eliminate it → [[cipher-suite-negotiation-is-an-anti-pattern-newer-protocols]]

---

**Claim 11 —** TLS should be separated from applications via a local daemon — not embedded in application libraries → [[tls-should-be-separated-from-applications-via-a]]

---

**Claim 12 —** Three types of filtering form a defense-in-depth network security architecture → [[three-types-of-filtering-form-a-defense-in-depth-network]]

---

**Claim 13 —** Forwarding and routing authorization extends policy enforcement into the network fabric itself → [[forwarding-and-routing-authorization-extends-policy-enforcement-into]]

---

## Synthesis: The Provenance-to-Packet Trust Chain

| Trust Stage | Ch7: Application | Ch8: Traffic | Cross-Reference |
|---|---|---|---|
| **Source** | Signed commits, code review | — | NSA Device: TPM-backed supply chain provenance |
| **Build** | Immutable artifacts, reproducible builds | — | CISA App: Integrated SDLC testing maturity |
| **Distribution** | Signed manifests, APT hash chain, promotion | — | NSA Device: Signed firmware update chains |
| **Deployment** | Per-instance time-bound secrets (Vault) | First packet: SPA hides the service | NIST Ch4: BeyondProd workload identity |
| **Execution** | Isolation, secure coding, active monitoring | mTLS/IPsec: authenticated encryption for all traffic | CISA App: Runtime monitoring maturity |
| **Network filtering** | — | Host + bookended + intermediary filtering | NSA Network: Microsegmentation, application profiles |
| **Network fabric** | — | SDN routing authorization | NIST Ch4: BeyondCorp access proxy architecture |

**Key insight:** These two chapters together describe a single continuous argument that the industry has since operationalized as distinct, complementary layers. Chapter 7 is now "software supply chain security" (SLSA, SSDF, SBOM). Chapter 8 is now "zero trust network access" (ZTNA, service mesh, SDP). The book's genius is showing that they are two halves of the same problem: _you can't trust the traffic if you can't trust the application that produced it, and you can't trust the application if it can't prove its identity on the network._ The shared dependency is X.509 certificates — they authenticate both the application instance (Chapter 7's instance authorization) and the network flow (Chapter 8's mTLS/IPsec). The certificate is the bridge between the two trust domains.

---

## Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|---|---|---|
| 1. Application pipeline as cryptographic chain | HIGH | Gap between "cryptographic chain" and "build process integrity" |
| 2. Git tamper-proof history + signed commits | VERY HIGH | Practical adoption: most orgs still don't sign commits universally |
| 3. Build system as most dangerous attack vector | HIGH | SolarWinds vindicated this — but reproducible builds remain aspirational |
| 4. Immutable artifacts + decoupled versions | HIGH | Industry moved to content-addressed artifacts (container digests) |
| 5. Per-instance time-bound secrets for authorization | HIGH | SPIFFE/SPIRE has standardized this; cloud IAM does it natively |
| 6. Runtime security completes the lifecycle | MODERATE | Gap between "run a fuzzer" and "applications monitor each other" |
| 7. Encryption vs. authentication separation | VERY HIGH | Cryptographic orthodoxy; TLS 1.3 enforces AEAD |
| 8. SPA solves the first packet problem | MODERATE | ZTNA access proxies have largely superseded SPA in practice |
| 9. mTLS for clients, IPsec for servers pragmatic split | HIGH | Service mesh mTLS has captured server-to-server; IPsec niche |
| 10. Cipher suite negotiation as anti-pattern | HIGH (diagnosis) / MODERATE (prediction) | TLS 1.3 fixed negotiation; Noise remains niche |
| 11. Local TLS daemon (sidecar) for separation of duty | HIGH | Became the service mesh pattern; dominant cloud-native architecture |
| 12. Three-tier filtering model | HIGH | Architecturally sound; Calico/cloud security groups validate |
| 13. Forwarding/routing authorization via SDN | MODERATE | Conceptually correct; operational complexity limits adoption |

**Strongest sections:** Claims 1–5 (the build pipeline) and Claim 12 (three-tier filtering). These are not just correct — they're architectural frameworks that the industry has since built products around.

**Weakest section:** Claim 8 (SPA). Correct in principle but the implementation pattern (UDP pre-authentication packets) has been overtaken by ZTNA proxy architectures that achieve the same "hide the service" property without protocol-level complexity.

**Unique contribution to OSKG-ZeroTrust:** These chapters establish the missing link between "how ZT works on the network" (Chapters 1–6) and "how you build the software that runs on it." No other ZT source — not NIST, not NSA, not CISA, not DoD — provides a comparable end-to-end treatment of the provenance-to-packet trust chain. The certificate-as-bridge insight (instance identity → flow identity) is the conceptual hinge that connects application trust to traffic trust.
