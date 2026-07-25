---
tags:
  - source/standards
  - ncsc
  - zt-principles
  - uk
  - google-cloud
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
claims_status: extracted
claims_extracted: 2026-07-24
confidence: high
source:
  title: "Applying the NCSC Zero Trust Principles on Google Cloud"
  author: "Google Cloud"
  year: 2022
  date: "March 2022"
  local_file: "sources/standards/_txt/NCSC_ZT_Principles_on_Google_Cloud.txt"
related:
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[Concepts Index]]"
---

# NCSC — Zero Trust Principles on Google Cloud

Google Cloud's March 2022 whitepaper maps the UK National Cyber Security Centre (NCSC) Zero Trust Architecture Design Principles onto Google Cloud Platform (GCP) and Google Workspace services. It is simultaneously a compliance-mapping document (showing how GCP satisfies each NCSC principle), a product architecture guide (which Google services implement which ZT functions), and a strategic positioning document (anchoring Google's ZT credentials in BeyondCorp, their internal ZT implementation since 2009). The whitepaper is aimed at "Enterprise and Security Architects charged with developing and executing a zero trust strategy" and provides the most detailed vendor-specific ZT architecture mapping in the OSKG-ZeroTrust source corpus.

---

**Claim 1 —** The NCSC's 8 principles provide a practical, vendor-agnostic framework for ZT architecture that is complementary to NIST SP 800-207 but more operationally prescriptive. → [[ncsc-principles-provide-practical-vendor]]
---

**Claim 2 —** BeyondCorp is Google's implementation of the ZT model and provides the architectural foundation for all GCP ZT services — it is the most mature, battle-tested ZT implementation available as a cloud service. → [[beyondcorp-google-implementation-zt-model-provides-architectural]]
---

**Claim 3 —** Google's ZT architecture maps to the PDP/PEP model with IAP as the Policy Enforcement Point, Access Context Manager as the Rules Engine, and Cloud IAM/Identity as the Policy Decision Point. → [[google-zt-architecture-maps-pdp-pep-model]]
---

**Claim 4 —** Service identity (service accounts) and device identity (Verified Access via TPM) are first-class identity types in Google's ZT model — going beyond user identity. → [[service-identity-service-accounts-device-identity-verified]]
---

**Claim 5 —** Cloud-native monitoring (Security Command Center, Chronicle, Cloud Logging) enables ZT-appropriate monitoring focused on users/devices/services rather than network boundaries. → [[cloud-5]]
---

**Claim 6 —** Google's ZT architecture explicitly supports hybrid environments — on-premises applications can be secured through IAP connectors without requiring cloud migration. → [[google-zt-architecture-explicitly-supports-hybrid-environments]]
---

**Claim 7 —** The NCSC-to-GCP mapping demonstrates that ZT is achievable through cloud-native managed services with significantly reduced operational burden compared to self-built ZT infrastructure. → [[ncsc]]
---

## Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| 1: NCSC 8 principles are complementary to NIST, more operationally prescriptive | HIGH | Organizations in US-only context ignoring NCSC as irrelevant |
| 2: BeyondCorp is the most mature, battle-tested ZT implementation | HIGH | BeyondCorp's Google-specific assumptions limiting generalizability |
| 3: GCP maps cleanly to PDP/PEP model with IAP/Access Context Manager | HIGH | Edge cases where IAP/PEP model doesn't cover non-HTTP workloads |
| 4: Service and device identity are first-class identity types | HIGH | Service account key management at scale; non-ChromeOS device identity |
| 5: Cloud-native monitoring shifts focus from network to users/devices/services | HIGH | Hybrid environments creating monitoring gaps between cloud and on-prem |
| 6: Hybrid support via IAP connectors enables incremental ZT adoption | HIGH (HTTP/HTTPS) / MEDIUM (non-web apps) | Non-HTTP legacy applications still requiring alternative approaches |
| 7: Managed services reduce ZT operational burden | HIGH (exists) / MEDIUM (reduction magnitude) | Configuration complexity offsetting infrastructure simplicity |

**Strongest sections:**
- **Service identity model (Principle 2)** — Service accounts + BeyondProd principles provide the most complete treatment of non-human identity in the ZT corpus. The "no inherent mutual trust between services" principle is architecturally significant.
- **Continuous policy evaluation (Principle 4)** — The four-step flow with real-time re-evaluation within sessions demonstrates genuine ZT maturity beyond session-establishment-only models.
- **Monitoring toolchain integration (Principle 6)** — The combination of Cloud Identity Security Center (user/device behavior) + SCC (cloud workload threats) + Chronicle (long-term telemetry) + Cloud IDS (network threat detection) covers the full ZT monitoring spectrum.

**Weakest sections:**
- **Non-HTTP legacy applications** — The IAP connector model only covers HTTP/HTTPS. Industrial control systems, custom protocols, and thick-client applications are not addressed.
- **Multi-cloud interoperability** — While the whitepaper mentions "hybrid and multi-cloud environments" for Cloud Logging, the ZT architecture is inherently GCP-centric. Organizations with multi-cloud strategies may face integration challenges.
- **Quantitative evidence** — The whitepaper asserts BeyondCorp's effectiveness based on Google's internal experience but provides no quantitative metrics (breach prevention rates, incident reduction) that would allow independent evaluation.

**Unique contribution to OSKG-ZeroTrust:**
The NCSC Google Cloud whitepaper is the only document in the OSKG-ZeroTrust corpus that:
1. **Provides a complete vendor-specific ZT architecture mapping** — Every NCSC principle is mapped to a specific, available GCP service with implementation details. This makes ZT architecture tangible and procurable in a way that NIST's abstract logical components cannot.
2. **Demonstrates ZT as a cloud-native managed service** — Shifts the ZT implementation burden from "build and operate your own PDP/PEP infrastructure" to "configure and policy-manage Google's PDP/PEP infrastructure." This is a fundamentally different deployment model than on-premises ZT.
3. **Treats service identity as architecturally equal to user identity** — Service accounts, BeyondProd mutual TLS, Anthos Service Mesh, and Binary Authorization together form a service-identity framework that is more comprehensive than any other ZT document in the corpus.
4. **Provides an alternative national ZT framework (NCSC)** — Complements the US-centric NIST/CISA/DoD documents with the UK's NCSC principles, enabling cross-jurisdictional comparison.
5. **Demonstrates continuous within-session policy evaluation** — The claim that "if an element of context changes, such as geolocation, the request will be dropped or re-authenticated" represents a higher ZT maturity than most implementations, which evaluate only at session establishment.

**Comparison with related notes:**
- **vs. NIST 800-207:** NIST defines the abstract ZT architecture; Google implements it as a specific commercial product set. The NCSC-to-GCP mapping validates that NIST's PDP/PEP model can be realized in a cloud-native architecture.
- **vs. DoD ZT Strategy:** The DoD Strategy is multi-vendor, outcome-based, and technology-agnostic. Google's whitepaper is single-vendor, service-specific, and prescriptive. They represent opposite ends of the ZT implementation spectrum — the DoD can't prescribe Google, but a single enterprise can.
- **vs. Garbis & Chapman:** Garbis & Chapman's deployment models (resource-based, enclave-based, cloud-routed, microsegmentation) provide a taxonomy for evaluating vendors. Google's architecture is primarily cloud-routed (BeyondCorp Enterprise) with enclave-based elements (VPC Service Controls) and microsegmentation (Anthos Service Mesh).

**Open Questions:**
- How does the NCSC framework differ from NIST SP 800-207 in ways that matter for architecture decisions? (The whitepaper maps to NCSC but doesn't compare to NIST.)
- What is the actual operational burden of configuring Google's managed ZT services vs. self-building equivalent infrastructure? (The whitepaper asserts reduction but provides no metrics.)
- How does Google's ZT architecture handle non-ChromeOS devices (Windows, macOS, Linux) for device identity and health attestation? (Verified Access is ChromeOS-specific; Endpoint Verification covers other platforms but with weaker attestation.)
- Can organizations achieve NCSC ZT alignment using Google Cloud without becoming dependent on Google's identity platform (Cloud Identity) as the authoritative identity source?
- How does the IAP connector model perform at scale (hundreds of on-premises applications, thousands of users) vs. traditional VPN concentrators?
