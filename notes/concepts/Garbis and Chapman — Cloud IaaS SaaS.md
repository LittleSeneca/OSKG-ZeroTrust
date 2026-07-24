---
tags:
  - source/books
  - garbis-chapman
  - zt-cloud
  - zt-iaas
  - zt-saas
  - zt-architecture
  - oskg-zerotrust
created: 2026-07-24
confidence: high
source:
  title: "Zero Trust Security: An Enterprise Guide"
  authors: "Jason Garbis, Jerry W. Chapman"
  year: 2021
  publisher: "Apress"
  local_file: "sources/books/_txt/Zero_Trust_Security_An_Enterprise_Guide.txt"
  lines: "Ch14: 6102–6468, Ch15: 6468–6700"
related:
  - "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
  - "[[Concepts Index]]"
---

# Garbis & Chapman — Ch14–15: Cloud IaaS, PaaS, and SaaS

How Zero Trust applies to cloud infrastructure and SaaS applications. Garbis & Chapman argue that IaaS/PaaS platforms are highly integrable with ZT via simple source IP restrictions at the cloud boundary, while SaaS requires a lighter-touch approach since the apps are public-by-design. The chapter introduces service meshes as natural ZT microsegmentation systems and situates ZT within the converging SASE/ZTE market landscape.

---

## Claim 1: IaaS/PaaS security hasn't kept pace with IaaS/PaaS adoption

**Authors' claim:** Cloud platforms "have transformed the way that much of our software is built, deployed, and accessed" but "don't believe that these platforms have yet had a similarly broad and significant impact on security." CSP security models are designed to protect services *within* their cloud environments, not to serve as broad enterprise security solutions across heterogeneous environments. Microsoft is the exception — leveraging identity, desktop OS, and cloud computing together.

**Evidence presented:** Google pioneered ZT internally and now offers Identity-Aware Proxy, but it's GCP-scoped. AWS and Azure have sophisticated IAM and network security groups, but they're cloud-native, not enterprise-wide. The CSPs' access control models are powerful but network/IP-centric rather than identity-centric — they "definitely do not have the ability to define and enforce the types of Zero Trust policies that we need, across our heterogeneous and diverse enterprise environments."

**Confidence:** HIGH. This matches NIST 800-207's analysis (Ch4 deployment scenarios, multi-cloud/cross-boundary access) and the DoD ZT RA's emphasis on cross-pillar integration. The CSPs themselves have acknowledged this gap with products like AWS Verified Access and Azure Global Secure Access, which emerged after this book's publication.

**What's at stake:** If CSP-native security is treated as sufficient, enterprises build siloed, cloud-specific security models that don't interoperate. If it's treated as worthless, enterprises miss the genuinely useful metadata, service identity, and IAM capabilities that CSPs provide.

**Who disagrees:** Cloud-native security advocates argue that CSP IAM + service mesh + Policy-as-Code (OPA, Cedar) *can* provide enterprise-grade ZT without an external platform. The BeyondCorp papers show Google doing exactly this with internal tooling. The tension is between "buy an external ZT platform" and "build ZT from cloud-native primitives."

**My assessment:** Garbis & Chapman's framing is a product of its time (2021), when ZTNA vendors were positioning against CSP-native tooling. In 2026, the line has blurred significantly — CSPs now offer ZTNA-like services and ZTNA vendors offer cloud-native deployment. The enduring insight is that *someone* needs to provide cross-boundary, identity-centric policy — whether that's a third-party platform or a well-architected CSP-native stack.

---

## Claim 2: The PEP works best at the cloud boundary — source IP restrictions are the enabling primitive

**Authors' claim:** "The PEP works most effectively as an access control point across the cloud boundary (at the ingress point into the cloud environment)." The foundational enabling capability is CSPs' ability to restrict source IP addresses for accessing resources. "This capability, although basic, is all that's necessary for us to achieve our goal: our Zero Trust system (enforced via the PEP) is how we're applying dynamic and identity-centric policies."

**Evidence presented:** Two topologies are presented:

1. **Co-located PEP** (Figure 14-1): PEP runs inside the CSP. IaaS resources assigned private IPs, PaaS resources accessed via public URLs with private prefixes (e.g., `https://abc123def.execute-api.us-east-1.amazonaws.com`). The CSP access gateway is configured so only traffic originating from the PEP can reach the resources. The PEP can make local API calls to retrieve cloud metadata tags for dynamic policy evaluation and auto-detect newly created service instances.

2. **Remote PEP** (Figure 14-2): PEP runs in an arbitrary environment (on-premises, another cloud). Resources need public IPs. The same source IP restriction is enforced, but this topology only works for encrypted protocols (the native app protocol goes PEP → gateway → resource).

**Confidence:** VERY HIGH. This pattern — ZTNA gateway with source IP allowlisting — is exactly how every major ZTNA product (Zscaler, Cloudflare, Netskope) integrates with cloud resources. NIST 800-207's enclave-based and cloud-routed models describe the same pattern at a higher level of abstraction. The BeyondCorp Access Proxy operates identically.

**What's at stake:** If source IP restrictions are treated as a security control on their own (without the ZT PEP in front), they're trivially bypassed. If they're treated as unnecessary because "ZT handles it," cloud resources are left exposed. The correct posture is IP restrictions as the *enforcement mechanism* and the ZT PEP as the *policy mechanism* — two layers that must both be present.

**Who disagrees:** API-gateway-based approaches (API keys, signed requests, OAuth tokens) argue that IP-layer restrictions are too coarse. Service mesh advocates argue that mTLS + SPIFFE identities are superior. Both are correct for their domains — API gateways for application-layer access, service meshes for east-west traffic — but neither replaces the need for a boundary PEP for user-to-resource access.

**My assessment:** This is the most practically useful section of both chapters. The "source IP allowlisting → PEP is the policy gate" pattern is the simplest, most universal integration model for cloud ZT. It works with every CSP, requires no agent on the resource, and maps cleanly to NIST's PDP/PEP architecture. The recommendation to "keep things simple, and externalize the dynamic and identity-centric access controls to your Zero Trust platform" is battle-tested advice.

---

## Claim 3: Service meshes are self-contained Zero Trust microsegmentation systems

**Authors' claim:** "Service meshes are in some ways essentially a self-contained Zero Trust microsegmentation model and system." Istio and Linkerd provide control plane / data plane separation with distributed proxies (PEPs) enforcing mTLS, service identity management, and declarative authorization policies. They have "enough of their own 'center of gravity' to warrant continued enterprise use of them, even within a broader Zero Trust program."

**Evidence presented:** Istio's architecture maps cleanly to ZT: istiod services = PDP (certificate authority, service identity, authorization policies), sidecar proxies = PEPs, mTLS for confidentiality + mutual authentication. Authorization is based on requestor attributes, target service attributes, and request metadata — services are addressed by identifiers, not IP addresses.

The mesh defines a clear boundary — its edge — and "can very easily and effectively utilize a surrounding Zero Trust platform enforcement of ingress and egress policies." From the ZT system's perspective, the mesh becomes the implicit trust zone.

**Confidence:** HIGH. The service-mesh-as-ZT-microsegmentation framing is now widely accepted. NIST 800-207's microsegmentation deployment model, the DoD ZT RA's application workload pillar, and CISA ZTMM's Application Workload function all describe the same pattern. Istio's own documentation positions the platform as a ZT implementation.

**What's at stake:** If service meshes are treated as *replacing* enterprise ZT, the east-west security is excellent but the north-south (user-to-app) boundary is unprotected. If they're treated as *irrelevant to ZT*, enterprises miss the opportunity to leverage mesh-native identity and policy for east-west traffic. The correct posture is the one Garbis & Chapman describe: arm's-length integration where the ZT platform handles ingress/egress and the mesh handles internal service-to-service.

**Who disagrees:** Pure-ZTNA advocates might argue that if every service call goes through a ZT PEP, service meshes are redundant. This is technically true but operationally impractical — the latency and complexity of routing every microservice call through an external PEP is prohibitive. Cloud-native advocates might argue that service mesh + OPA + external secrets is a complete ZT solution without an enterprise ZT platform. This is viable for cloud-native-only organizations but breaks down when legacy on-premises apps are in scope.

**My assessment:** The service mesh section is forward-looking for 2021 — it correctly identifies the mesh edge as the integration point and anticipates the need for ZT context propagation into the mesh (via HTTP headers, which is now standard practice). The vision of "a Zero Trust solution in which the PEP is able to render policies based on workload attributes within the container environment" has largely arrived with products like Tetrate, Solo.io, and CSP-native offerings.

---

## Claim 4: Zero Trust does fewer things for SaaS — but what it does is still valuable

**Authors' claim:** "Using Zero Trust to manage and control access to SaaS applications does provide value, even though we do acknowledge that Zero Trust does fewer things for SaaS resources compared with private resources." SaaS apps are publicly accessible by design (no resource hiding needed) and use HTTPS (no encryption needed from the PEP). But ZT can still enforce "identity-centric and context-sensitive access policies" using group membership, identity attributes, device posture, and enterprise system state.

**Evidence presented:** Two native SaaS access control mechanisms exist: (1) source IP address restrictions — the SaaS platform permits access only from a designated IP (the PEP's egress IP), applied per-customer tenancy; (2) federated identity management via SAML/OIDC — the SaaS app delegates authentication to the enterprise IdP. These can be combined: "federated identity system for authentication combined with a Zero Trust network solution to perform deep device posture checks."

However, most SaaS apps "do not currently have mechanisms to consume external contextual information and make authorization decisions based on this" — they rely on internal role-based authorization models. This is the gap ZT can partially fill.

**Confidence:** HIGH. The observation that SaaS apps are public-by-design and HTTPS-native means ZT can't provide network hiding or encryption — the two functions that are most valuable for private resources. What remains is identity-centric policy enforcement, which is genuinely useful but narrower in scope. This is consistent with NIST 800-207's SaaS scenarios (Ch4) and CISA ZTMM's SaaS guidance.

**What's at stake:** If ZT is sold as a complete SaaS security solution, enterprises get a false sense of security — ZT doesn't address SaaS data security, configuration management, or insider threats within the SaaS app. If ZT is dismissed as irrelevant to SaaS, enterprises miss the opportunity to enforce device posture, session risk scoring, and just-in-time access for SaaS apps.

**Who disagrees:** CASB vendors argue that their approach (API-based, inline proxy, or both) provides more value for SaaS than ZTNA alone because they address data-at-rest, DLP, and configuration assessment. SWG vendors argue that their web filtering and threat protection are necessary companions to ZT for SaaS access. Both are correct — ZT + CASB + SWG is the realistic enterprise posture, which Garbis & Chapman acknowledge.

**My assessment:** The honest assessment — "ZT does fewer things for SaaS" — is the most valuable sentence in this chapter. It prevents overclaiming and helps practitioners understand where ZT fits in their broader SaaS security stack. The gap Garbis & Chapman identify — SaaS apps not consuming external authorization context — remains largely unfilled in 2026, though standards like CAEP (Continuous Access Evaluation Protocol) and products like Microsoft's Conditional Access for SaaS are beginning to address it.

---

## Claim 5: SASE/ZTE converges networking and security, but ZTNA (ingress) is architecturally distinct

**Authors' claim:** SASE (Gartner) and ZTE (Forrester) describe converged cloud-based platforms combining three groups of functions: (1) network connectivity (SD-WAN, WAN optimization), (2) security for Internet access/egress (SWG, CASB, DNS filtering), and (3) access to private resources/ingress (ZTNA). ZTNA is *architecturally different* from the other components: it "will continue to require that elements (PEPs) be deployed into enterprise-controlled environments, including on-premises enterprise networks, data centers, and public cloud-based IaaS and PaaS environments."

**Evidence presented:** Two reasons: (1) TCP/IP networks require a local node to terminate the encrypted tunnel and proxy connections to private resources on the private network; (2) the local PEP is needed to obtain and use local context/attributes as policy inputs. Gartner makes the same distinction between "ingress SASE" and "egress SASE" with different requirements.

Additionally, enterprises "still have on-premises users and on-premises resources" and "need to control on-premises server-to-server access, which cloud-based services often struggle to manage." The ZT principle of enforcing policy "for all identities' access to all resources, regardless of the location of the identity or resource" means ZTNA can't be purely cloud-delivered.

**Confidence:** HIGH. The ingress/egress distinction is now standard industry terminology. The requirement for on-premises or cloud-local PEPs is validated by every major ZTNA deployment — even "cloud-delivered" ZTNA products deploy connectors, app connectors, or agents into enterprise environments. The BeyondCorp Access Proxy model also requires infrastructure on the enterprise side (the proxy itself).

**What's at stake:** If ZTNA is treated as just another SASE feature, enterprises underestimate the deployment complexity of on-premises connectors and the policy integration work. If ZTNA is treated as completely separate from SASE, enterprises end up with disjointed security stacks that don't share context.

**Who disagrees:** Pure cloud-delivery advocates might argue that with enough cloud connectivity (SD-WAN everywhere, direct cloud interconnects), on-premises PEPs become unnecessary. This works for greenfield, cloud-native organizations but not for enterprises with legacy data centers. Browser-based ZTNA approaches argue that the browser itself can act as the PEP, eliminating the need for a local network node — this is valid for web apps but not for SSH, RDP, or non-HTTP protocols.

**My assessment:** This is prescient for 2021. The SASE market has consolidated significantly since then (Netskope, Zscaler, Cloudflare, Palo Alto all now offer integrated SASE + ZTNA), but the architectural distinction Garbis & Chapman draw remains true. The local PEP requirement is the reason every ZTNA product ships some form of connector/app connector — it's not a temporary limitation, it's an architectural necessity.

---

## Claim 6: The future of ZT + SaaS is identity providers as authorization centers, not just authentication points

**Authors' claim:** "We believe that identity providers will not just serve as authoritative directories and authentication points but as 'centers of gravity' for user access to web apps, and for access control models." The future includes: JIT access provisioning via SCIM, a standard for communicating authenticated identity context to SaaS applications, and SaaS apps that are "Zero Trust-aware" — consuming external authorization signals.

**Evidence presented:** The authors acknowledge this is forward-looking. Current IdP access portals provide only authentication + launchpad, not authorization. SCIM is the first step toward JIT provisioning. XACML failed to achieve adoption because "applications will never fully externalize their authorization." The opportunity is narrower: a commonly accepted way to communicate *trusted identity context* (authentication strength, device posture, session risk) to SaaS apps for consumption in their internal authorization models.

**Confidence:** MODERATE. This is a prediction, not an evidence-based claim. Some elements have materialized: Microsoft's Continuous Access Evaluation (CAE) and Entra ID Conditional Access, Okta's Risk-Based Authentication, and the emerging CAEP standard. But full authorization context propagation remains aspirational. SCIM adoption for JIT is growing but not ubiquitous.

**What's at stake:** If IdPs remain authentication-only, ZT for SaaS is limited to access control at the network layer (IP allowlisting) and the gap between authentication and authorization stays unfilled. If IdPs become authorization hubs, the identity provider becomes the single most critical security component in the enterprise — a concentration of risk that demands extraordinary protection.

**Who disagrees:** The "authorization belongs in the application" school argues that only the application knows its data model and business logic well enough to make authorization decisions. The "authorization as code" school (OPA, Cedar, Google Zanzibar) argues that authorization logic should be externalized but owned by application teams, not centralized in the IdP. Both are partly correct — the likely future is a distribution of authorization logic across IdP (coarse access), policy engine (context evaluation), and application (fine-grained, data-level decisions).

**My assessment:** This is a thoughtful prediction that has aged well. The trend toward identity-centered security architecture has accelerated, with Okta, Microsoft, and Ping all positioning themselves as more than authentication providers. The specific mechanism (SCIM + some authorization standard) is less important than the architectural direction: IdPs are becoming the control plane for access decisions, even if enforcement remains distributed.

---

## Chapter 14–15 Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| IaaS/PaaS security hasn't kept pace with adoption | HIGH | CSP-native ZT services closing the gap since 2021 |
| PEP at cloud boundary via source IP restrictions | VERY HIGH | API-gateway or service-mesh alternatives for specific use cases |
| Service meshes as self-contained ZT microsegmentation | HIGH | All-in-one ZTNA platforms that make meshes redundant |
| ZT does fewer things for SaaS — but what it does matters | HIGH | CASB/SWG vendors arguing their approach is sufficient without ZT |
| ZTNA is architecturally distinct within SASE | HIGH | Browser-based ZTNA eliminating need for local PEPs |
| IdPs as authorization centers | MODERATE | Application-first authorization models (OPA, Zanzibar) |

**Strongest sections:**
- The PEP-at-cloud-boundary pattern (Ch14) — the most actionable guidance in either chapter, directly implementable with any CSP and any ZTNA product.
- The honest assessment of ZT's limitations for SaaS (Ch15) — prevents overclaiming and gives practitioners a clear mental model for where ZT fits in the SaaS security stack.

**Weakest sections:**
- The "fog computing" discussion is a throwaway that hasn't materialized as predicted.
- The SASE/ZTE discussion is marketing-landscape commentary rather than architectural analysis — useful context but lower information density than the rest.

**Unique contribution to OSKG-ZeroTrust:**
These chapters provide the *cloud-specific* bridge between ZT abstract architecture (NIST 800-207 Ch3–4) and practical implementation. Where NIST describes deployment *models*, Garbis & Chapman describe deployment *mechanics* — the specific integration pattern (source IP allowlisting) that makes cloud ZT work. The service mesh analysis connects ZT microsegmentation to the Kubernetes/cloud-native ecosystem, and the SaaS analysis provides an honest assessment that no other source in the corpus matches in clarity.
