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
claim_id: "ncsc.7"
statement: "The NCSC-to-GCP mapping demonstrates that ZT is achievable through cloud-native managed services with significantly reduced operational burden compared to self-built ZT infrastructure."
confidence: "high"
confidence_rationale: 'HIGH that the services exist and map to the principles. MEDIUM on whether the "reduced operational burden" claim holds in practice — managed services'
claim_type: "implementation"
source_note: "[[NCSC — ZT Principles on Google Cloud]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# ncsc.7: The NCSC-to-GCP mapping demonstrates that ZT is achievable through cloud-native managed services with significantly reduced operational burden compared to self-built ZT infrastructure.

**Source:** [[NCSC — ZT Principles on Google Cloud]] — NCSC, *Zero Trust Principles on Google Cloud*, 2023

## The Claim

"The zero trust Infrastructure itself (including Context Aware Access and Identity Aware Proxy) are battle-tested components managed by Google on your behalf — based on BeyondCorp."

## Evidence

The whitepaper maps every NCSC principle to specific, available Google Cloud services. Key managed services include:

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

## Confidence

**Rating:** HIGH
**Rationale:** HIGH that the services exist and map to the principles. MEDIUM on whether the "reduced operational burden" claim holds in practice — managed services reduce infrastructure burden but increase configuration complexity and dependency on a single cloud provider.

## Stakes

If Google's claim is correct, organizations can achieve NCSC ZT alignment with significantly less operational overhead than self-building equivalent infrastructure. If incorrect (i.e., the managed services require extensive customization to meet real-world requirements), the operational burden shifts from infrastructure to configuration and integration.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[beyondcorp-google-implementation-zt-model-provides-architectural|The NCSC-to-GCP mapping demonstrates that Google's ZT services comprehensively address a vendor-agnostic operational fra]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[ncsc-principles-provide-practical-vendor|The NCSC-to-GCP service mapping demonstrates concretely how the 8 principles translate to available cloud-native managed]]

## Assessment

The managed-services approach is genuinely valuable for organizations without the scale to build their own BeyondCorp-equivalent. The shared responsibility model acknowledgment — "customers are required to define appropriate access policies, but are not responsible for the security of Access Context Manager itself" — is honest about where the boundary lies. The three-phase rollout guidance (Discover → Remediate → Enforce) for device policies demonstrates operational maturity and awareness of the organizational change management required.
