---
tags:
  - source/papers
  - beyondprod
  - google
  - zt-cloud
  - zt-microservices
  - oskg-zerotrust
  - tier/3
  - security/zero-trust
  - security/cloud-native
  - security/microservices
created: 2026-07-24
confidence: high
related:
  - "[[BeyondCorp — Research Papers]]"
  - "[[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]]"
  - "[[NIST 800-207 — Ch7 — Migration]]"
  - "[[Concepts Index]]"
sources:
  - "Google_BeyondProd.txt (Google Cloud Docs, last updated May 2024)"
---

# BeyondProd — Cloud-Native Security

**Google's extension of Zero Trust principles from user-to-application access (BeyondCorp) to service-to-service communication in production microservice environments.** Where BeyondCorp answers "should this user on this device access this corporate app?", BeyondProd answers "should this microservice talk to that microservice?"

This note covers Google's published BeyondProd paper, which describes the security architecture protecting Google's production infrastructure — the same infrastructure that runs Google Search, Gmail, YouTube, and Google Cloud.

---

## The Core Analogy

> "Where Chrome Enterprise Premium [BeyondCorp] states that user trust should be dependent on characteristics like the context-aware state of devices and not the ability to connect to the corporate network, BeyondProd states that **service trust should depend on characteristics like code provenance, trusted hardware, and service identity, rather than the location in the production network, such as IP address or hostname.** "

This is the fundamental insight: the same principles that BeyondCorp applied to corporate access — eliminate trust based on network location, base decisions on verifiable attributes — apply equally to production microservice communication.

---

### Claim 1: Perimeter security breaks down for microservices because services are mobile, ephemeral, share infrastructure, and change at extreme velocity — BeyondProd replaces network-location trust with verifiable attributes (identity, code provenance, hardware integrity).

**Author's claim:** Google argues that traditional perimeter-based security fails in a cloud-native environment because: (1) microservices are deployed across heterogeneous hosts, rescheduled constantly, and lack fixed IP addresses; (2) in a monolithic app, internal components implicitly trust each other, but in microservices each service is independently developed and deployed — mutual trust must be explicitly established; (3) multiple workloads from different tenants share the same physical hosts, making network segmentation alone insufficient; (4) Borg deploys several billion containers per week, requiring security that scales at the same velocity.

**Evidence presented:** Four failure modes of perimeter security in microservice environments are enumerated. The solution is six integrated security services that together form the BeyondProd trust stack: GFE (network edge), ALTS (service-to-service auth), BAB (code provenance), Host Integrity (hardware-rooted machine trust), Service Access Management + End-User Context Tickets (policy enforcement), and gVisor (workload isolation).

**Confidence:** HIGH — This is Google's production architecture, actively operating at the scale of billions of containers per week. The problem statement is grounded in operational reality.

### Claim 2: ALTS (Application Layer Transport Security) is the workhorse of BeyondProd — binding identities to services rather than hosts is the critical design decision that enables seamless replication, load balancing, and rescheduling across machines.

**Author's claim:** Google states that ALTS provides mutual authentication and transport encryption for every service-to-service RPC call in Google's infrastructure. Identities are bound to services, not hosts — a microservice has its own ALTS identity independent of the machine it runs on.

**Evidence presented:** Machine-level ALTS credentials are provisioned using the host integrity system and can only be decrypted if secure boot was verified. Borg Prime grants microservice-level ALTS credentials based on the microservice's identity, provisioned over the machine-level secure channel. This creates a chain: Titan chip → verified boot → host integrity → machine ALTS credentials → service ALTS credentials. The design means a compromised host cannot impersonate a service, and a rescheduled service retains its identity.

**Confidence:** HIGH — ALTS is a well-documented, production-proven protocol at Google scale. The identity-to-service binding is a specific architectural decision with clear security rationale.

### Claim 3: Code provenance enforcement (Binary Authorization for Borg) closes a critical gap that most ZT frameworks overlook — ensuring that only reviewed, trusted-built code reaches production.

**Author's claim:** BAB enforces at deploy time that code changes were reviewed by a second engineer, binaries were verifiably built on dedicated trusted infrastructure, and the build process produces a signed verifiable build manifest certificate.

**Evidence presented:** The enforcement chain: developer submits change → central code repository enforces two-person review → approved change goes to central trusted build system → produces package with signed verifiable build manifest certificate → at deployment time, BAB validates the signed certificate confirming the entire review/build chain was followed. BAB rollout follows the same audit-first-then-enforce pattern as BeyondCorp: audit-only mode first, service owners identify non-compliant workflows, then switch to enforcement mode.

**Confidence:** HIGH — This is a documented Google production control. The code provenance concept maps to modern frameworks (SLSA, Sigstore/cosign) and addresses a gap in NIST 800-207 which does not explicitly address code trust.

### Claim 4: Host Integrity, rooted in the Titan security chip, creates a hardware-anchored chain of trust from firmware to user mode — ALTS machine credentials are only decryptable by hosts that pass verified boot.

**Author's claim:** Google's Host Integrity system verifies the integrity of host system software through a secure boot process backed by a hardware root of trust (Titan security chip where supported). The verification chain covers BIOS, BMC, bootloader, OS kernel, and where supported, user-mode code and peripheral firmware.

**Evidence presented:** Host Integrity ensures each host runs the intended version of these components — not just that signatures are valid. The critical integration is with ALTS: machine credentials are only decryptable by hosts that pass host integrity's verified boot. This creates a hardware-rooted chain of trust: Titan chip → verified boot chain → machine ALTS credentials → service ALTS credentials. Without passing host integrity, a machine cannot obtain credentials to participate in the BeyondProd trust fabric.

**Confidence:** HIGH — Hardware-rooted trust is a well-established security pattern. The Titan chip integration with ALTS credential provisioning is a specific architectural coupling documented in Google's paper.

### Claim 5: End-User Context Tickets solve the problem of compromised services using their legitimate service identity for lateral movement — access decisions depend on both service identity AND the originating end user's identity.

**Author's claim:** Without end-user context tickets, a compromised service could use its own legitimate service identity to access data it shouldn't. The tickets — integrity-protected, centrally-issued, forwardable credentials — attest to the identity of the end user who originated the request, breaking this attack path.

**Evidence presented:** The request flow demonstrates composition: User → GFE (TLS termination) → application frontend (authenticates user via EUA service, receives short-lived cryptographic end-user context ticket) → RPC over ALTS to storage backend, forwarding the ticket → backend service checks: frontend ALTS identity authorized to make requests AND present EUC ticket? Ticket valid? User in ticket authorized to access requested data? Every intermediary service does a service access check on inbound RPCs, and the ticket is forwarded on outbound RPCs. This is "Zero Trust at every hop" — no link inherits trust from a previous link.

**Confidence:** HIGH — The end-user context ticket mechanism addresses a specific, well-defined threat (compromised service lateral movement) with a specific, well-described solution. The "chain of backend calls" pattern demonstrates practical hop-by-hop ZT enforcement.

### Claim 6: BeyondCorp and BeyondProd together form a complete ZT model — BeyondCorp for the north-south axis (user-to-app) and BeyondProd for the east-west axis (service-to-service) — a distinction NIST 800-207 does not explicitly make.

**Author's claim:** This is a meta-claim about the architectural relationship. Google's implementation separates user-to-application access (BeyondCorp: SSO + X.509 device certificates, Access Control Engine with Trust Inferer tiers) from service-to-service access (BeyondProd: ALTS mutual auth, service access management with end-user context tickets, BAB for code provenance).

**Evidence presented:** The comparison table shows systematic mapping: BeyondCorp uses SSO + device certs for identity; BeyondProd uses ALTS + service identity. BeyondCorp authorizes via Access Control Engine + Trust Inferer; BeyondProd via Service Access Management + EUC tickets. BeyondCorp uses unprivileged VLANs + Access Proxy; BeyondProd uses all-RPC-over-ALTS + GFE edge. BeyondCorp verifies device state; BeyondProd verifies code provenance. BeyondCorp uses TPM for device certificates; BeyondProd uses Titan chip for host integrity.

**Confidence:** MEDIUM — The north-south/east-west distinction is analytically useful but somewhat simplified. Real deployments have overlapping patterns (a service can be both a BeyondCorp client and a BeyondProd server). NIST 800-207's abstract architecture accommodates both without making the distinction explicit, which can be seen as either a gap or deliberate generality.

---

## BeyondProd Benefits

| Benefit | Mechanism |
|---|---|
| **Network edge protection** | GFE shields workloads from internet-based attacks and DoS. |
| **No inherent mutual trust between services** | ALTS ensures only authenticated, authorized callers can access any service. Mutual distrust + granular access control limits blast radius. |
| **Trusted machines running code with known provenance** | BAB + Host Integrity ensure only authorized code on verified hardware. |
| **Consistent policy enforcement across services** | Service access management + end-user context tickets apply policies uniformly. |
| **Simple, automated, standardized change rollout** | Borg blue-green deployments enable fast, reviewable security patching. |
| **Isolation between co-hosted workloads** | gVisor limits blast radius when a service is compromised. |
| **Trusted hardware and attestation** | Titan chip provides hardware root of trust; host integrity verifies full boot chain. |

---

## Migration Approach: Audit-First, Then Enforce

Google's migration to BeyondProd followed the same pattern as BeyondCorp: **log before blocking.**

- **ALTS rollout:** Initially provided as a library with a single helper daemon per host, evolved into service credentials, integrated seamlessly into the core RPC library → wide adoption without burden on development teams. ALTS was a prerequisite to rolling out service access management and end-user context tickets.
- **Build/Code Review Pipeline:** Established central build process → enforced two-person review + automated testing at build/deployment time → addressed external/untrusted code via sandboxing.
- **Audit-Only Mode:** When services onboarded to BAB: audit-only mode first, identify non-compliant workflows, address issues, then switch to enforcement. Same pattern with gVisor.

---

## Mapping to Modern Tools

| BeyondProd Component | Modern Equivalent |
|---|---|
| ALTS | mTLS via Istio/Envoy, SPIFFE/SPIRE for service identity |
| BAB | SLSA framework, Sigstore/cosign for build attestation, OPA/Gatekeeper for deploy-time policy |
| Host Integrity | TPM-based measured boot, Keylime for remote attestation |
| Service Access Management | Istio AuthorizationPolicy, OPA, CEL-based policies |
| End-User Context Tickets | OAuth2 tokens with JWT claims forwarded through service mesh |
| gVisor | gVisor (open source), Kata Containers, Firecracker |
| GFE | Cloud Load Balancer, Envoy/Istio ingress gateway |
| Borg | Kubernetes |
