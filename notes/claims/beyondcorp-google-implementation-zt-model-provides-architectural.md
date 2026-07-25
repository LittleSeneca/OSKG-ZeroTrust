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
  - topic/zt-remote-access
claim_id: "ncsc.2"
statement: "BeyondCorp is Google's implementation of the ZT model and provides the architectural foundation for all GCP ZT services — it is the most mature, battle-tested ZT implementation available as a cloud service."
confidence: "high"
confidence_rationale: "HIGH that BeyondCorp is a genuine, production-scale ZT implementation. Google's internal deployment predates the \"Zero Trust\" branding (Kindervag's"
claim_type: "implementation"
source_note: "[[NCSC — ZT Principles on Google Cloud]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# ncsc.2: BeyondCorp is Google's implementation of the ZT model and provides the architectural foundation for all GCP ZT services — it is the most mature, battle-tested ZT implementation available as a cloud service.

**Source:** [[NCSC — ZT Principles on Google Cloud]] — NCSC, *Zero Trust Principles on Google Cloud*, 2023

## The Claim

"BeyondCorp is Google's implementation of the zero trust model. It builds upon a decade of experience at Google, combined with ideas and best practices from the community. By shifting access controls from the network perimeter to individual users, BeyondCorp enables secure work from virtually any location without the need for a traditional VPN."

## Evidence

BeyondCorp began as an internal Google initiative in 2009 and is now "used by most Googlers every day to provide user- and device-based authentication and authorization for Google's core infrastructure and corporate resources." The whitepaper describes BeyondCorp Enterprise as the commercial product that packages these capabilities. It also references BeyondProd — Google's complementary model for service-to-service ZT in cloud-native environments.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH that BeyondCorp is a genuine, production-scale ZT implementation. Google's internal deployment predates the "Zero Trust" branding (Kindervag's 2010 paper) and represents one of the earliest large-scale ZT architectures. The commercial availability of these capabilities through GCP is a validated claim.

## Stakes

If BeyondCorp is genuinely the most mature ZT implementation, organizations adopting GCP get a decade of Google's operational ZT experience embedded in the platform — not just ZT-compatible features but a ZT-native architecture. If BeyondCorp's architecture is too Google-specific, organizations with heterogeneous environments may not benefit fully.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**
- [[iaaspaas-security-hasnt-kept-pace-with-iaaspaas-adoption|iaaspaas claims CSP models are 'network/IP-centric' and 'definitely do not have the ability' to enforce ZT policies, whi]]

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[beyondcorp-beyondprod-together-form-complete-zt-model|Positions BeyondCorp as the north-south half of Google's complete ZT model and the architectural foundation for all GCP]]

## Assessment

BeyondCorp's maturity is a genuine competitive advantage for GCP in ZT. The 2009 origin date is significant — Google was operating ZT principles before the term existed. The BeyondCorp-to-BeyondProd progression (user access → service-to-service) mirrors the maturation path that enterprises need: start with user access, then extend ZT to workloads. The whitepaper's explicit acknowledgment that "the majority of business application services will have not been built explicitly as 'designed for zero trust'" and its guidance on integrating legacy services via IAP connectors shows pragmatic realism.
