---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-user-pillar
  - topic/zt-identity
  - topic/zt-access-mgmt
  - topic/zt-implementation
claim_id: "nsa-user.4"
statement: "Access management is where least privilege becomes operational — through ABAC, JIT/JEA, PAM, and privileged access workstations"
confidence: "high"
confidence_rationale: "HIGH. The access management section is the longest and most detailed in the document, reflecting NSA's operational focus. The progression from"
claim_type: "implementation"
source_note: "[[NSA — User Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-user.4: Access management is where least privilege becomes operational — through ABAC, JIT/JEA, PAM, and privileged access workstations

**Source:** [[NSA — User Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the User Pillar*, 2023

## The Claim

Access management progresses from broad, role-based policies to fine-grained, risk-adaptive, attribute-based decisions — with specific tools and practices at each maturity level. The goal is attribute-based access control (ABAC) integrated with risk-based indicators, supported by Just-in-Time/Just-Enough Access (JIT/JEA), Privileged Access Management (PAM) tools, and dedicated privileged access workstations.

## Evidence

The document identifies five core access management capabilities and maps them across maturity phases:

### Core Capabilities

1. **Least Privilege:** "Implementing least privilege access policies minimizes the damage a malicious actor can cause." For highly privileged users: separate devices, credentials, and accounts isolated from high-risk activities (email, web browsing).

2. **Just-in-Time (JIT) / Just-Enough Access (JEA):** Privileges are granted only when needed, only at the level needed, and revoked automatically after the task. "Access to highly privileged functions are segregated both logically and chronologically."

3. **Privileged Access Management (PAM) Tools:** Centralized management for fine-grained privileges, proxying access to resources that don't support strong authenticators, enforcing workflow constraints and role separation. Critical warning: "PAM implementations should be tightly controlled and monitored, since they control the highly privileged functions that shape the environment, making them an attractive target."

4. **Privileged Access Workstations:** Dedicated physical or virtual devices for administrative functions. "It is important that administrative workstations only have access to essential applications required to perform administrative actions and do not allow high-risk activities, such as email or web browsing."

5. **Fine-grained, risk-adaptive access policies (ABAC):** Access decisions consider multiple attributes per request — user identity, device posture, resource sensitivity, data classification, risk-based indicators. "Attribute-based access control (ABAC) models provide the flexibility required to meet these goals." NIST SP 800-162 is the authoritative reference for ABAC implementation.

### Maturity Phases for Access Management

| Phase | Key Capability |
|-------|---------------|
| **Preparation** | Inventory user entitlements and access policies; remove outdated/inappropriate entitlements; identify attributes implicit in existing policies; update legacy applications to use modern methods. |
| **Basic** | Review against least privilege; implement PAM for all highly privileged users; identify authoritative sources for user attributes; implement data tagging for critical resources; ensure access logging for forensics; limit authentication assertions in time and scope. |
| **Intermediate** | Segregate highly privileged functions logically and chronologically using dedicated workstations + PAM with JIT/JEA; access policies reflect authentication strength (weaker auth = less access); differentiate access for MFA types. |
| **Advanced** | Granular access per specific resource considering user, device, application sensitivity, and data attributes; risk-based indicators from authoritative sources; user activity assessed against roles and behavior patterns (continuous authentication); risk responses triggered automatically; credential revocation interfaces with risk-based attributes. |

**The ABAC model is the architecture that makes all of this possible.** Traditional RBAC is static — a user's role determines their access, period. ABAC adds dimensions: *this* user, on *this* device, at *this* time, with *this* risk score, requesting *this* specific resource with *these* data attributes. For NSS, the attributes include classification, clearance, releasability, citizenship, community-of-interest, and need-to-know — attributes that don't exist in standard commercial IAM products but are life-or-death for defense systems.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The access management section is the longest and most detailed in the document, reflecting NSA's operational focus. The progression from "inventory your mess" (Preparation) to "risk-based automated access decisions with continuous authentication" (Advanced) is realistic and well-defined.

## Stakes

Access management is where identity credentials meet resources. The most common attacker technique — compromised credentials → lateral movement → privilege escalation — exploits gaps at every phase: no least privilege (too much access), no PAM (privileged accounts unmonitored), no JIT/JEA (standing privileges always on), no privileged workstations (admin browses web, gets phished). The four capabilities together close this kill chain.

## Disagreement

**Who disagrees:**

The practical challenge is that ABAC at NSA's Advanced level requires significant investment in attribute infrastructure, policy authoring, and enforcement mechanisms. NIST 800-162 acknowledges this: "ABAC implementations can be complex and resource-intensive to initially establish." CISA's ZTMM Access Management function sets the same destination (JIT/JEA at Optimal) but is less prescriptive about the ABAC path. Commercial ZTNA vendors (Zscaler, Palo Alto) tend to implement resource-level access controls without the full ABAC attribute framework that defense environments require.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**
  - "[[access-management-permanent-to-jit-jea]]"

**Extends:**

## Assessment

The access management section is the most practical part of the document for implementers. The five capabilities (least privilege, JIT/JEA, PAM, privileged workstations, ABAC) form a coherent strategy. The order matters: you can't do JIT/JEA without PAM, you shouldn't do PAM without privileged workstations (else the PAM console itself becomes a target), and ABAC is the long-term architecture that makes risk-adaptive decisions possible. The NSA's explicit warning that PAM itself is an attractive target is a critical operational insight that most guidance omits.
