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

## Claim 1: The NCSC's 8 principles provide a practical, vendor-agnostic framework for ZT architecture that is complementary to NIST SP 800-207 but more operationally prescriptive.

**Context:** The NCSC Zero Trust Architecture Design Principles are the UK government's equivalent of NIST SP 800-207. The 8 principles are:

1. **Know your architecture** — including users, devices, services, and data
2. **Know your User, Service and Device identities** — each uniquely identifiable
3. **Assess your user behaviour, devices and services health** — continuous health evaluation as signals for policy engines
4. **Use policies to authorize requests** — each request authorized against policy
5. **Authenticate & Authorise everywhere** — multiple signals; assume hostile network
6. **Focus your monitoring on users, devices and services** — not just network boundaries
7. **Don't trust any network, including your own** — secure transport; traditional network-based protections must shift
8. **Choose services designed for zero trust** — prefer standards-based, ZT-native services; legacy services require additional integration

**Google's mapping:** The whitepaper maps each principle to specific Google Cloud services. For example: Principle 1 maps to Cloud Asset Inventory, Data Catalog, and Professional Services migration planning; Principle 2 maps to Cloud Identity, IAM, service accounts, and Verified Access (device identity via TPM on ChromeOS); Principle 4 maps to Identity-Aware Proxy (IAP) as the PEP, Access Context Manager as the Rules Engine, and VPC Service Controls for network-layer enforcement.

**Confidence:** HIGH on the NCSC principles being a valid ZT framework. They are more operationally prescriptive than NIST's seven tenets — Principle 7 ("don't trust any network, including your own") is a stronger, more directive statement than NIST's "all communication is secured regardless of network location." The NCSC framework is designed for UK government adoption but is jurisdiction-agnostic in its technical content.

**What's at stake:** The NCSC principles represent an alternative ZT articulation to NIST. For organizations operating in both US and UK contexts (or multinationals), understanding the mapping between the two frameworks is essential. Google's whitepaper implicitly claims GCP satisfies both.

**My assessment:** The NCSC principles are a valuable complement to NIST. They are more concrete — Principle 1 ("know your architecture") is an action, not an abstraction. Principle 3 ("assess user behaviour, devices and services health") operationalizes continuous monitoring more explicitly than NIST's tenet 5. The 8-principle structure maps cleanly to an implementation sequence (know → identify → assess → authorize → authenticate → monitor → secure transport → choose services), making it a more natural project plan than NIST's seven tenets.

---

## Claim 2: BeyondCorp is Google's implementation of the ZT model and provides the architectural foundation for all GCP ZT services — it is the most mature, battle-tested ZT implementation available as a cloud service.

**Google's claim:** "BeyondCorp is Google's implementation of the zero trust model. It builds upon a decade of experience at Google, combined with ideas and best practices from the community. By shifting access controls from the network perimeter to individual users, BeyondCorp enables secure work from virtually any location without the need for a traditional VPN."

**Evidence presented:** BeyondCorp began as an internal Google initiative in 2009 and is now "used by most Googlers every day to provide user- and device-based authentication and authorization for Google's core infrastructure and corporate resources." The whitepaper describes BeyondCorp Enterprise as the commercial product that packages these capabilities. It also references BeyondProd — Google's complementary model for service-to-service ZT in cloud-native environments.

**Confidence:** HIGH that BeyondCorp is a genuine, production-scale ZT implementation. Google's internal deployment predates the "Zero Trust" branding (Kindervag's 2010 paper) and represents one of the earliest large-scale ZT architectures. The commercial availability of these capabilities through GCP is a validated claim.

**What's at stake:** If BeyondCorp is genuinely the most mature ZT implementation, organizations adopting GCP get a decade of Google's operational ZT experience embedded in the platform — not just ZT-compatible features but a ZT-native architecture. If BeyondCorp's architecture is too Google-specific, organizations with heterogeneous environments may not benefit fully.

**My assessment:** BeyondCorp's maturity is a genuine competitive advantage for GCP in ZT. The 2009 origin date is significant — Google was operating ZT principles before the term existed. The BeyondCorp-to-BeyondProd progression (user access → service-to-service) mirrors the maturation path that enterprises need: start with user access, then extend ZT to workloads. The whitepaper's explicit acknowledgment that "the majority of business application services will have not been built explicitly as 'designed for zero trust'" and its guidance on integrating legacy services via IAP connectors shows pragmatic realism.

---

## Claim 3: Google's ZT architecture maps to the PDP/PEP model with IAP as the Policy Enforcement Point, Access Context Manager as the Rules Engine, and Cloud IAM/Identity as the Policy Decision Point.

**Google's claim:** The whitepaper describes a four-step policy enforcement flow that directly implements the PDP/PEP model:

1. **PEP:** Identity-Aware Proxy (IAP), IAM, Cloud Identity, or VPC Service Controls — depending on request type
2. **Rules Engine:** Access Context Manager
3. **Enforcement:** Requests not matching policy are dropped by the Enforcement Point
4. **Continuous Evaluation:** Each request in a session is evaluated by the Rules Engine in real time; if context changes (e.g., geolocation), the request is dropped or requires re-authentication

**Evidence presented:** Access Context Manager uses multiple signals for access decisions — user and device posture, IP address, geolocation, session age, time of day, and credential strength (e.g., hardware second factor). Access levels can be tiered (e.g., "High_Trust" vs. "Medium_Trust") and applied to different resources.

**Confidence:** HIGH. This architecture cleanly maps to the NIST logical component model: IAP/IAM = PEP, Access Context Manager = Policy Engine/Policy Administrator (combined PDP function), multiple signal sources = feed into the Policy Engine. The continuous evaluation within a session (Principle 4, point 4) is a sophisticated implementation of NIST's "access is granted on a per-session basis" tenet.

**What's at stake:** If the PDP/PEP model is the correct ZT architecture (as NIST asserts), Google's implementation validates that the model is commercially viable at scale. The tiered access levels ("High_Trust" / "Medium_Trust") demonstrate how ZT moves beyond binary allow/deny to risk-adaptive authorization.

**My assessment:** The continuous evaluation capability — "if an element of context changes, such as geolocation, the request will be dropped or re-authenticated" — is the most architecturally significant feature described. Most ZT implementations evaluate context at session establishment but don't continuously re-evaluate within a session. This is genuine ZT maturity. The tiered access levels capability enables risk-based policies that balance security and usability.

---

## Claim 4: Service identity (service accounts) and device identity (Verified Access via TPM) are first-class identity types in Google's ZT model — going beyond user identity.

**Google's claim:** "An identity can represent a user (a human), service (software process) or device. Each should be uniquely identifiable in a zero trust architecture. This is one of the most important factors in deciding whether someone or something should be given access to data or services."

**Evidence presented:**

- **Service identity:** Service accounts are "a special kind of account used by an application or a virtual machine (VM) instance, not a person." They use private/public RSA key-pairs (no passwords), can be impersonated by other users/service accounts, and are identified by unique email addresses. Anthos Service Mesh provides "a layer of service context-aware and request context-aware network security" with "no inherent mutual trust between services."

- **Device identity:** ChromeOS devices have TPM at every price point. Verified Access uses TPM to provide "a hardware-backed cryptographic guarantee of the identity of the device and user." The Verified Access API allows network services to "cryptographically confirm the identity and status of verified boot and enterprise policy."

**Confidence:** HIGH. Service identity via service accounts and device identity via TPM-backed Verified Access are genuine, production-grade capabilities. The combination covers the full identity spectrum (human, software, hardware).

**What's at stake:** NIST SP 800-207's "all data sources and computing services are considered resources" tenet implies that services themselves need identities. Google's service account model operationalizes this. Device identity via hardware root of trust (TPM) provides a stronger foundation than software-based device attestation.

**My assessment:** The service account model is the most important identity capability for cloud-native ZT. In traditional networks, services are identified by IP address — which is spoofable and location-dependent. Service accounts provide cryptographic identity that is independent of network location. The BeyondProd principles — "no inherent mutual trust between services," "trusted machines running code with known provenance," "choke points for consistent policy enforcement" — describe a ZT architecture for microservices that extends BeyondCorp's user-focused model to the service mesh layer.

---

## Claim 5: Cloud-native monitoring (Security Command Center, Chronicle, Cloud Logging) enables ZT-appropriate monitoring focused on users/devices/services rather than network boundaries.

**Google's claim:** "Cloud native monitoring solutions provide a richer set of protective monitoring capabilities than traditional network boundary logging — e.g. at a VPN chokepoint. Comprehensive protective monitoring in a zero trust environment will likely involve a range of teams — from those who are supporting users and devices through to service and product owners."

**Evidence presented:** Google provides two primary monitoring locations:
- **Cloud Identity Security Center:** Device and user configurations and behavior; login attempt reports; suspicious sign-in activity alerts; device security health events
- **Security Command Center (SCC):** Asset discovery/inventory; threat prevention (web app vulnerabilities, misconfigurations); threat detection (container attacks, suspicious binaries, reverse shells); integrates with Chronicle for long-term security telemetry analysis

Additional monitoring capabilities include VPC Flow Logs, Packet Mirroring, Cloud IDS (built with Palo Alto Networks threat detection), and the Network Forensics & Telemetry blueprint (Packet Mirroring → Zeek → Pub/Sub → datalake → Chronicle).

**Confidence:** HIGH. The monitoring toolchain is comprehensive and cloud-native. Chronicle's ability to ingest on-premise telemetry via forwarders and third-party integrations (Office 365, Azure AD) addresses hybrid environments.

**What's at stake:** ZT monitoring must shift from "what's happening at the network perimeter?" to "what are users, devices, and services doing, and does it match policy?" Google's monitoring architecture enables this shift. The integration of device health signals (rooted/jailbroken detection, account registration changes) into policy enforcement (device management rules that can automatically block/wiped devices) closes the monitoring-to-enforcement loop.

**My assessment:** The monitoring section reveals Google's architectural advantage: because the platform owns both the enforcement (IAP, IAM) and the monitoring (SCC, Chronicle, Cloud Logging), telemetry is natively integrated rather than bolted on. The device management rules — "block a device when the account registration state changes" — demonstrate automated response, not just detection. The BYOD/guest device handling via work profiles (Android) and Context-Aware access levels is pragmatic and recognizes that not all devices can be fully managed.

---

## Claim 6: Google's ZT architecture explicitly supports hybrid environments — on-premises applications can be secured through IAP connectors without requiring cloud migration.

**Google's claim:** "BeyondCorp Enterprise customers can secure HTTP or HTTPS based on-premises applications (outside of Google Cloud) with Identity-Aware Proxy (IAP) by deploying a connector. When a request is made for an on-premises app, IAP authenticates and authorizes the user request and then routes the request to the connector."

**Evidence presented:** The connector model allows organizations to apply ZT controls (identity-aware proxy, context-aware access, continuous evaluation) to on-premises applications without migrating them to GCP. Google's "Open Cloud" approach emphasizes partner ecosystem integration rather than lock-in.

**Confidence:** HIGH. The IAP connector for on-premises applications is a documented, available feature. It addresses the most common ZT deployment challenge: legacy applications that can't be immediately migrated.

**What's at stake:** The hybrid support claim is critical for enterprise adoption. Organizations with significant on-premises investment can't adopt GCP ZT if it requires full cloud migration first. The connector model enables incremental adoption: secure on-premises apps with ZT today, migrate at your own pace.

**My assessment:** The hybrid connector model is strategically important — it positions GCP ZT as an overlay that can secure existing infrastructure, not just cloud-native workloads. However, the limitation to "HTTP or HTTPS based" applications is significant. Non-web legacy applications (thick clients, custom protocols, industrial control systems) still require alternative ZT approaches. Google's Professional Services offerings (Zero Trust Foundations, Cloud Deploy: Zero Trust) suggest that the connector model is a starting point, not a complete solution for all legacy applications.

---

## Claim 7: The NCSC-to-GCP mapping demonstrates that ZT is achievable through cloud-native managed services with significantly reduced operational burden compared to self-built ZT infrastructure.

**Google's claim:** "The zero trust Infrastructure itself (including Context Aware Access and Identity Aware Proxy) are battle-tested components managed by Google on your behalf — based on BeyondCorp."

**Evidence presented:** The whitepaper maps every NCSC principle to specific, available Google Cloud services. Key managed services include:

| NCSC Principle | Google Managed Service | Customer Responsibility |
|---------------|----------------------|------------------------|
| Know your architecture | Cloud Asset Inventory, Data Catalog | Define scope, maintain inventory |
| Know identities | Cloud Identity, IAM, Service Accounts | Configure identity lifecycle, least privilege |
| Assess health | Security Center, SCC, Chronicle | Define health policies, respond to alerts |
| Authorize requests | IAP, Access Context Manager, IAM | Define access policies and trust levels |
| Authenticate everywhere | Cloud Identity 2SV, Security Keys, Context-Aware | Enforce MFA, choose second factors |
| Monitor users/devices/services | Security Center, SCC, VPC Flow Logs, Cloud IDS | Configure monitoring scope, respond |
| Don't trust any network | Encryption in transit, Safe Browsing, HSTS, DNS-over-HTTPS | Configure browser policies |
| Choose ZT-designed services | BeyondCorp Enterprise, BeyondProd, Anthos Service Mesh | Select services, integrate legacy apps |

**Confidence:** HIGH that the services exist and map to the principles. MEDIUM on whether the "reduced operational burden" claim holds in practice — managed services reduce infrastructure burden but increase configuration complexity and dependency on a single cloud provider.

**What's at stake:** If Google's claim is correct, organizations can achieve NCSC ZT alignment with significantly less operational overhead than self-building equivalent infrastructure. If incorrect (i.e., the managed services require extensive customization to meet real-world requirements), the operational burden shifts from infrastructure to configuration and integration.

**My assessment:** The managed-services approach is genuinely valuable for organizations without the scale to build their own BeyondCorp-equivalent. The shared responsibility model acknowledgment — "customers are required to define appropriate access policies, but are not responsible for the security of Access Context Manager itself" — is honest about where the boundary lies. The three-phase rollout guidance (Discover → Remediate → Enforce) for device policies demonstrates operational maturity and awareness of the organizational change management required.

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
