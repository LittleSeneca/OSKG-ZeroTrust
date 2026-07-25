---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-user-pillar
  - topic/zt-identity
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-cloud
claim_id: "nsa-user.2"
statement: "Identity management maturity is about attribute authority, not just identity inventory"
confidence: "high"
confidence_rationale: "HIGH. This progression is the most granular in federal guidance. CISA's version (Identity Stores function) focuses more on *where* identity data"
claim_type: "implementation"
source_note: "[[NSA — User Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-user.2: Identity management maturity is about attribute authority, not just identity inventory

**Source:** [[NSA — User Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the User Pillar*, 2023

## The Claim

Identity management "begins with establishing a current and accurate inventory of all users, including person and non-person entities, ensuring those with access to critical resources are vetted and registered." But that's just preparation. Real maturity means attributes at every level — from standard to locally-defined to risk-based — all integrated directly into access control mechanisms.

## Evidence

The four-phase maturity progression for Identity Management:

| Phase | Capability | Key Shift |
|-------|-----------|-----------|
| **Preparation** | Enterprise repositories for person-entities only; NPEs managed ad-hoc locally; in-person vetting per NIST FIPS 201. | *Get everyone registered.* |
| **Basic** | Enterprise attribute standards defined; all local attributes documented; attribute claims validated during vetting or via approved remote methods; standard attributes integrated into access control. | *Standardize attributes enterprise-wide.* |
| **Intermediate** | Standardized attributes with authoritative sources identified; locally-defined attributes for highly sensitive resources; standardized issuance processes. | *Attribute authority becomes formal — you know who owns each attribute.* |
| **Advanced** | Risk-based attributes defined and standardized; risk indicators associated with entities alert resource managers; responses may be resource-specific; ALL user attributes relevant to a resource integrated directly into access mechanisms. | *Risk becomes a first-class identity attribute.* |

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This progression is the most granular in federal guidance. CISA's version (Identity Stores function) focuses more on *where* identity data lives (on-prem → cloud → integrated across partners); NSA focuses on *what attributes exist* and *how authoritative they are*. Both are necessary. NSA's emphasis on NPEs (non-person entities — services, devices, automated processes) is distinctive and reflects defense environments where service accounts and machine identities are as critical as user identities.

## Stakes

Attribute authority is the difference between *having* identity data and *trusting* it for access decisions. If your identity store says a user has clearance X but you don't know who asserted that or how it was validated, the attribute is useless for security decisions. This is why the intermediate phase's "authoritative sources identified for each attribute" is the critical inflection point.

## Disagreement

**Who disagrees:**

This is less a disagreement and more a gap. Commercial identity providers (Okta, Azure AD/Entra ID, Ping) don't natively support the "clearance" and "releasability" attributes NSA references for NSS. The commercial world models identity as HR attributes + group membership; the defense world adds classification, community-of-interest, and formal access approvals. The ABAC model (covered in Claim 4) is designed to bridge this gap.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
- [[trust-assessment-is-multi-layered-identity-posture-and-behavior|Multi-layered trust assessment needs authoritative identity attributes to evaluate the identity layer.]]
- [[access-management-permanent-to-jit-jea|JIT/JEA requires rich identity attributes to make fine-grained, automated access decisions.]]
- [[access-mgmt-abac-least-privilege|ABAC fundamentally depends on authoritative identity attributes for policy decisions.]]

**Supports:**
- [[ztmm-operationalizes-nist-seven-tenets|C8 describes identity management maturity progression within ZTMM, providing another concrete example of ZTMM operationa]]
- [[identity-must-be-contextual-who-what-device-where|Attribute authority is the prerequisite that enables contextual identity decisions across all dimensions (who, what, whe]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**
  - "[[identity-stores-integrated-not-just-federated]]"

**Extends:**
- [[icam-non-negotiable-substrate|C8 provides operational detail on the Identity Management function within the FICAM framework C3 establishes, specifying]]
- [[identity-foundational-zta-pillar|C1 claims identity maturity is essential; C8 specifies that identity management maturity means attribute authority, not]]

## Assessment

The identity management maturity model is NSA at its most practical. The progression from "ad-hoc NPE registration" to "risk-based attributes driving automated access decisions" is a realistic multi-year roadmap. The emphasis on NPEs is forward-looking — in cloud-native environments, service identities often outnumber user identities 10:1, and the same attribute-authority principles apply.
