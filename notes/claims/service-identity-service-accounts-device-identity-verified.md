---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/ncsc
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
claim_id: "ncsc.4"
statement: "Service identity (service accounts) and device identity (Verified Access via TPM) are first-class identity types in Google's ZT model — going beyond user identity."
confidence: "high"
confidence_rationale: "HIGH. Service identity via service accounts and device identity via TPM-backed Verified Access are genuine, production-grade capabilities. The"
claim_type: "implementation"
source_note: "[[NCSC — ZT Principles on Google Cloud]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# ncsc.4: Service identity (service accounts) and device identity (Verified Access via TPM) are first-class identity types in Google's ZT model — going beyond user identity.

**Source:** [[NCSC — ZT Principles on Google Cloud]] — NCSC, *Zero Trust Principles on Google Cloud*, 2023

## The Claim

"An identity can represent a user (a human), service (software process) or device. Each should be uniquely identifiable in a zero trust architecture. This is one of the most important factors in deciding whether someone or something should be given access to data or services."

## Evidence

- **Service identity:** Service accounts are "a special kind of account used by an application or a virtual machine (VM) instance, not a person." They use private/public RSA key-pairs (no passwords), can be impersonated by other users/service accounts, and are identified by unique email addresses. Anthos Service Mesh provides "a layer of service context-aware and request context-aware network security" with "no inherent mutual trust between services."

- **Device identity:** ChromeOS devices have TPM at every price point. Verified Access uses TPM to provide "a hardware-backed cryptographic guarantee of the identity of the device and user." The Verified Access API allows network services to "cryptographically confirm the identity and status of verified boot and enterprise policy."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Service identity via service accounts and device identity via TPM-backed Verified Access are genuine, production-grade capabilities. The combination covers the full identity spectrum (human, software, hardware).

## Stakes

NIST SP 800-207's "all data sources and computing services are considered resources" tenet implies that services themselves need identities. Google's service account model operationalizes this. Device identity via hardware root of trust (TPM) provides a stronger foundation than software-based device attestation.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[network|Demonstrates that identity primitives extend beyond user identity to services and devices, supporting the identity-over-]]
- [[alts-application-layer-transport-security-workhorse-beyondprod|Service identity as a first-class identity type aligns with ALTS's approach of binding identities to services rather tha]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The service account model is the most important identity capability for cloud-native ZT. In traditional networks, services are identified by IP address — which is spoofable and location-dependent. Service accounts provide cryptographic identity that is independent of network location. The BeyondProd principles — "no inherent mutual trust between services," "trusted machines running code with known provenance," "choke points for consistent policy enforcement" — describe a ZT architecture for microservices that extends BeyondCorp's user-focused model to the service mesh layer.
