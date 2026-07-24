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

## The Problem: Perimeter Security Breaks Down for Microservices

Traditional perimeter-based security (firewalls protecting a production network) fails in a cloud-native environment because:

1. **Microservices are mobile and ephemeral**: They're deployed across heterogeneous hosts, rescheduled constantly, and operate at varying levels of trust and sensitivity. Fixed IP addresses don't exist; hostnames are transient.
2. **No inherent trust between services**: In a monolithic app, internal components implicitly trust each other. In microservices, each service is independently developed, deployed, and scaled — mutual trust must be explicitly established.
3. **Shared infrastructure**: Multiple workloads from different tenants share the same physical hosts. Network segmentation alone cannot provide sufficient isolation.
4. **Rapid change**: Borg (Google's container orchestration system, the inspiration for Kubernetes) deploys **several billion containers per week**. Security must scale at the same velocity.

---

## BeyondProd Security Services

Google built six core security services that work together to implement Zero Trust principles for production workloads:

### 1. Google Front End (GFE) — Network Edge Protection

**Function**: The first point of entry for any user connecting to Google infrastructure. Terminates TLS, enforces TLS best practices, provides DoS protection, load balances, and routes traffic to the correct microservice.

**ZT role**: While GFE is a perimeter component (the network edge), it's not the security model — it's a **first filter**. All traffic behind GFE is still subject to the full BeyondProd trust stack. The perimeter is a best-practice defense-in-depth layer, not the primary security control.

**Google Cloud variant**: Customer VMs register with **Cloud Front End** (a GFE configuration using Compute Engine networking) rather than GFE directly.

### 2. Application Layer Transport Security (ALTS) — Trust Between Services

**Function**: Mutual authentication and transport encryption for RPC between services. This is the **workhorse of BeyondProd** — every service-to-service call in Google's infrastructure uses ALTS.

**Key design decisions:**
- **Identities are bound to services, not hosts**: A microservice has its own ALTS identity, independent of the machine it runs on. This enables seamless replication, load balancing, and rescheduling across hosts.
- **Machine-level ALTS credentials** are provisioned using the host integrity system and can only be decrypted if secure boot was verified.
- **Borg Prime** grants microservice-level ALTS credentials to workloads based on the microservice's identity. These are provisioned over the machine-level secure channel.

**ZT role**: ALTS is the "no inherent mutual trust between services" enforcement mechanism. Only authenticated, trusted, and specifically authorized callers can access any service.

### 3. Binary Authorization for Borg (BAB) — Code Provenance

**Function**: Deploy-time enforcement check that ensures code meets internal security requirements before deployment. This is Google's implementation of **code provenance verification**.

**What BAB enforces:**
- Code changes must be **reviewed by a second engineer** before submission.
- Binaries must be **verifiably built on dedicated (trusted) infrastructure**.
- The build process produces a **signed, verifiable build manifest certificate**.
- At deployment time, BAB validates the signed certificate from the build pipeline.

**ZT role**: Service identities are constrained to use only authorized code and configurations, running only in authorized, verified environments. This prevents attackers from deploying unauthorized code or using untrusted code to access services.

### 4. Host Integrity — Machine Trust

**Function**: Verifies the integrity of the host system software through a secure boot process, backed by a **hardware root of trust** (Titan security chip where supported).

**Verification chain:**
- Digital signatures on BIOS.
- Baseboard management controller (BMC).
- Bootloader.
- OS kernel.
- Where supported: user-mode code and peripheral firmware (NICs).

Host integrity also ensures each host is running the **intended version** of these components — not just that signatures are valid.

**ZT role**: Only known and authorized code (from firmware to user mode) is running before any workloads are scheduled. ALTS machine credentials are only decryptable by hosts that pass host integrity's verified boot. This creates a hardware-rooted chain of trust.

### 5. Service Access Management and End-User Context Tickets — Policy Enforcement

**Two complementary mechanisms for consistent, fine-grained access control:**

**Service Access Management:**
- Defines authorization and auditing policies for RPCs between services.
- Limits how data is accessed between services.
- Grants the **minimal level of access** needed.
- Specifies how access can be audited.
- Allows for **global analyses of access controls** across the entire infrastructure.

**End-User Context Tickets:**
- Issued by a central end-user authentication service.
- Provide services with a **user identity separate from their service identity**.
- Integrity-protected, centrally-issued, forwardable credentials.
- Attest to the identity of the end user who originated the request.

Without end-user context tickets, a compromised service could use its own (legitimate) service identity to access data it shouldn't. The tickets break this attack path: peer identities via ALTS alone are insufficient; access decisions also depend on the end user's identity.

**ZT role**: Consistent policy enforcement across services — access decisions are dependable regardless of which service is making the request. No service can bypass authorization by exploiting trust relationships.

### 6. gVisor — Workload Isolation

**Function**: A user-space kernel that intercepts and handles syscalls, reducing interaction with the host kernel and limiting the attack surface. Provides isolation between workloads sharing an OS.

**ZT role**: If a service is compromised, it cannot affect the security of another workload running on the same host. This limits blast radius. Less trusted workloads (e.g., those sourced externally) are deployed with stronger isolation layers.

### Supporting Infrastructure: Borg Tooling

**Blue-green deployments**: Borg tooling gradually moves traffic from an existing job to a new one, enabling microservice updates with no downtime and without user impact. This is used for both feature updates and critical security patches. For infrastructure-level changes, live migration of customer VMs ensures workloads are not impacted.

**ZT role**: Simple, automated, and standardized change rollout means security patches can be applied rapidly with minimal production impact. Infrastructure changes are easily reviewed for security implications.

---

## BeyondProd Benefits

| Benefit | Mechanism |
|---------|-----------|
| **Network edge protection** | GFE shields workloads from internet-based attacks and DoS. |
| **No inherent mutual trust between services** | ALTS ensures only authenticated, authorized callers can access any service. Mutual distrust + granular access control limits blast radius. |
| **Trusted machines running code with known provenance** | BAB + Host Integrity ensure only authorized code on verified hardware. |
| **Consistent policy enforcement across services** | Service access management + end-user context tickets apply policies uniformly. |
| **Simple, automated, standardized change rollout** | Borg blue-green deployments enable fast, reviewable security patching. |
| **Isolation between co-hosted workloads** | gVisor limits blast radius when a service is compromised. |
| **Trusted hardware and attestation** | Titan chip provides hardware root of trust; host integrity verifies full boot chain. |

---

## End-to-End Walkthroughs

### Accessing User Data

The request flow demonstrates how BeyondProd services compose:

1. User sends request → **GFE** terminates TLS, forwards via **ALTS** to application frontend.
2. Application frontend authenticates user via central **end-user authentication (EUA) service** → receives short-lived, cryptographic **end-user context ticket**.
3. Application frontend makes **RPC over ALTS** to storage backend, forwarding the ticket.
4. Backend service uses **service access management** to check:
   - Frontend authenticated with valid, unrevoked certificate? (Implies running on trusted host, BAB checks passed.)
   - Frontend's ALTS identity authorized to make requests to this backend AND present an EUC ticket?
   - End-user context ticket valid?
   - User in ticket authorized to access requested data?
5. Any check fails → denied. All pass → data returned, served to authorized user.

**Critical detail**: In many cases, there is a **chain of backend calls**. Every intermediary service does a service access check on inbound RPCs, and the ticket is forwarded on outbound RPCs. This is "Zero Trust at every hop" — no link in the chain inherits trust from a previous link.

### Making a Code Change

The deployment security flow:

1. Developer submits change to **central code repository** → enforces code review (two-person review requirement).
2. Approved change → **central, trusted build system** → produces package with **signed verifiable build manifest certificate**.
3. At deployment time → **BAB** validates the signed certificate — confirms the entire review/build chain was followed.
4. **Borg** handles workload updates via blue-green deployment — no service interruption.
5. **GFE** moves traffic to new deployment via load balancing.

**Workload isolation by trust level**: If workload source code originates from outside Google (less trusted) → deployed with stronger isolation (gVisor-protected environment). This contains adversaries who manage to compromise an application.

---

## Migration Approach: Audit-First, Then Enforce

Google's migration to BeyondProd followed the same pattern as BeyondCorp: **log before blocking.**

**ALTS rollout:**
- Initially provided as a library with a single helper daemon on each host.
- Evolved into a library using service credentials.
- Integrated seamlessly into the core RPC library → wide adoption without burden on individual development teams.
- ALTS rollout was a **prerequisite** to rolling out service access management and end-user context tickets.

**Build/Code Review Pipeline:**
- Established a central build process → began enforcing two-person review + automated testing at build and deployment time.
- After basics established → addressed external/untrusted code via sandboxing (ptrace first, then gVisor).

**Audit-Only Mode (repeated pattern):**
- When a service is onboarded to BAB: **audit-only mode first**.
- Service owners identify code/workflows that don't meet requirements.
- Address issues flagged by audit-only → then switch to **enforcement mode**.
- Same pattern with gVisor: sandbox workloads even with compatibility gaps → address gaps systematically.

> "It was easier if a service started out by logging policy violations rather than blocking violations."

---

## Cloud-Native Security Implications: Traditional vs. Cloud-Native

The paper systematically compares traditional and cloud-native security models:

| Dimension | Traditional | Cloud-Native (BeyondProd) |
|-----------|------------|---------------------------|
| **Application architecture** | Monolithic, three-tier, deployed to private data centers with peak capacity. Fixed IP addresses. | Microservices in containers, portable across environments, immutable (rebuilt/redeployed frequently). |
| **Network trusts** | Internal network trusted; firewall at perimeter. | No inherent trust between services; IAM at microservice level. Zero-trust security model. |
| **Service mesh** | Applications responsible for their own security (identity, TLS, data access). Inconsistent implementations. | Shared fabric (service mesh) enveloping all microservices. Security managed separately from development. |
| **Rollouts** | Infrequent, large, hard to coordinate. Long-lived applications with infrequent patching. | Frequent, standardized. Blue-green deployments enable rapid security patching. "Shift left" — security early in development lifecycle. |
| **Choke points** | Limited shared services; code often duplicated. | Choke points enable consistent policy enforcement across all services. Different policies enforced by different services. |

### The Service Mesh Concept

> "By building shared and securely designed infrastructure that all developers use, the burden on developers to know and implement common security requirements is minimized. Security functionality should require little to no integration into each application, and is instead provided as a fabric enveloping and connecting all microservices."

This is the **service mesh** — a shared infrastructure layer that controls traffic, applies policies, and provides centralized monitoring for all service-to-service communication. Developers get security "for free" by operating within the mesh, rather than implementing it per-application.

---

## BeyondCorp vs. BeyondProd: The Full Google ZT Model

| Dimension | BeyondCorp | BeyondProd |
|-----------|------------|------------|
| **Domain** | User → Corporate Application | Service → Service (production) |
| **Identity type** | User identity + Device identity | Service identity + (optionally) End-user identity |
| **Authentication mechanism** | SSO + X.509 device certificates | ALTS mutual auth (service identity); EUA (end-user context) |
| **Authorization** | Access Control Engine with Trust Inferer tiers | Service access management with end-user context tickets |
| **Network model** | Unprivileged network; access proxy for all apps | All RPC over ALTS; GFE for edge |
| **Code trust** | Device state verification (OS patches, encryption, AV) | Code provenance (BAB — review + trusted build + signed manifest) |
| **Hardware trust** | TPM for device certificate storage | Titan chip for host integrity verified boot |
| **Isolation** | VLAN segmentation via RADIUS/802.1x | gVisor sandboxing between co-hosted workloads |
| **Key paper** | 6-paper series (2014-2018) | Single paper (updated 2024) |

Together, they form a **complete ZT model**: BeyondCorp for the north-south axis (user-to-app) and BeyondProd for the east-west axis (service-to-service). The NIST 800-207 abstract architecture doesn't explicitly distinguish these two dimensions, but Google's implementation makes the separation clear and operational.

---

## Assessment

**Strengths:**
- Extends ZT to the hardest problem in cloud-native security: service-to-service trust at scale (billions of containers/week).
- The ALTS design — binding identity to service rather than host — is elegant and essential for dynamic microservice environments.
- Code provenance (BAB) closes a critical gap that most ZT frameworks overlook: how do you know the code running IS the code that was reviewed?
- The end-user context ticket mechanism elegantly solves the problem of compromised services using their legitimate service identity for lateral movement.
- The hardware root of trust (Titan) provides a foundation for the entire chain — from verified boot through ALTS credential provisioning.
- Consistent audit-first migration pattern: ALTS, BAB, gVisor all follow the same "log then enforce" approach.

**Weaknesses:**
- The paper is a high-level architectural overview with limited operational detail compared to the BeyondCorp series (no metrics, no failure modes, no cost data).
- gVisor and workload isolation are mentioned but not deeply detailed.
- No discussion of multi-cloud or hybrid deployment — the architecture assumes Google's own infrastructure.
- The paper doesn't address what happens when a service's ALTS identity is compromised, or the revocation mechanisms.

**Confidence: HIGH** — This is a primary-source paper from Google Cloud documentation, maintained and updated through May 2024.

**What's at stake for ZT implementation**: BeyondProd demonstrates that network-based trust elimination applies to production infrastructure as well as corporate access. Organizations adopting microservices and Kubernetes should view BeyondProd as the reference model for service mesh security. The ALTS/BAB/Host Integrity triad — mutual auth via service identity, code provenance enforcement, and hardware-rooted machine trust — is the core pattern that maps to any cloud-native environment.

**Who would disagree**: Organizations that haven't fully adopted containers/microservices may find the architecture overwhelming. The paper assumes a level of infrastructure control (container orchestration, service mesh, hardware security chips) that many organizations lack. However, the principles — service identity over IP, code provenance verification, mutual authentication at every hop — are universally applicable even if the specific implementations differ.

---

## Mapping to Modern Tools

While BeyondProd describes Google's internal infrastructure, the patterns map to modern open-source and cloud-native tools:

| BeyondProd Component | Modern Equivalent |
|----------------------|-------------------|
| ALTS | mTLS via Istio/Envoy, SPIFFE/SPIRE for service identity |
| BAB | SLSA framework, Sigstore/cosign for build attestation, OPA/Gatekeeper for deploy-time policy |
| Host Integrity | TPM-based measured boot, Keylime for remote attestation |
| Service Access Management | Istio AuthorizationPolicy, OPA, CEL-based policies |
| End-User Context Tickets | OAuth2 tokens with JWT claims forwarded through service mesh |
| gVisor | gVisor (open source), Kata Containers, Firecracker |
| GFE | Cloud Load Balancer, Envoy/Istio ingress gateway |
| Borg | Kubernetes |
