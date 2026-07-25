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
claims_status: extracted
claims_extracted: 2026-07-24
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-governance
---

# BeyondProd — Cloud-Native Security

**Google's extension of Zero Trust principles from user-to-application access (BeyondCorp) to service-to-service communication in production microservice environments.** Where BeyondCorp answers "should this user on this device access this corporate app?", BeyondProd answers "should this microservice talk to that microservice?"

This note covers Google's published BeyondProd paper, which describes the security architecture protecting Google's production infrastructure — the same infrastructure that runs Google Search, Gmail, YouTube, and Google Cloud.

---

## The Core Analogy

> "Where Chrome Enterprise Premium [BeyondCorp] states that user trust should be dependent on characteristics like the context-aware state of devices and not the ability to connect to the corporate network, BeyondProd states that **service trust should depend on characteristics like code provenance, trusted hardware, and service identity, rather than the location in the production network, such as IP address or hostname.** "

This is the fundamental insight: the same principles that BeyondCorp applied to corporate access — eliminate trust based on network location, base decisions on verifiable attributes — apply equally to production microservice communication.

---

**Claim 1 —** Perimeter security breaks down for microservices because services are mobile, ephemeral, share infrastructure, and change at extreme velocity — BeyondProd replaces network-location trust with verifiable attributes (identity, code provenance, hardware integrity). → [[perimeter-security-breaks-down-microservices-because-services]]
**Claim 2 —** ALTS (Application Layer Transport Security) is the workhorse of BeyondProd — binding identities to services rather than hosts is the critical design decision that enables seamless replication, load balancing, and rescheduling across machines. → [[alts-application-layer-transport-security-workhorse-beyondprod]]
**Claim 3 —** Code provenance enforcement (Binary Authorization for Borg) closes a critical gap that most ZT frameworks overlook — ensuring that only reviewed, trusted-built code reaches production. → [[code-provenance-enforcement-binary-authorization-borg-closes]]
**Claim 4 —** Host Integrity, rooted in the Titan security chip, creates a hardware-anchored chain of trust from firmware to user mode — ALTS machine credentials are only decryptable by hosts that pass verified boot. → [[host-integrity-rooted-titan-security-chip-creates]]
**Claim 5 —** End-User Context Tickets solve the problem of compromised services using their legitimate service identity for lateral movement — access decisions depend on both service identity AND the originating end user's identity. → [[end]]
**Claim 6 —** BeyondCorp and BeyondProd together form a complete ZT model — BeyondCorp for the north-south axis (user-to-app) and BeyondProd for the east-west axis (service-to-service) — a distinction NIST 800-207 does not explicitly make. → [[beyondcorp-beyondprod-together-form-complete-zt-model]]
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
