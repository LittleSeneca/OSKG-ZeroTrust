---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-network
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-definition
claim_id: "gc-cloud.5"
statement: "SASE/ZTE converges networking and security, but ZTNA (ingress) is architecturally distinct"
confidence: "high"
confidence_rationale: "HIGH. The ingress/egress distinction is now standard industry terminology. The requirement for on-premises or cloud-local PEPs is validated by every"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Cloud IaaS SaaS]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-cloud.5: SASE/ZTE converges networking and security, but ZTNA (ingress) is architecturally distinct

**Source:** [[Garbis and Chapman — Cloud IaaS SaaS]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

SASE (Gartner) and ZTE (Forrester) describe converged cloud-based platforms combining three groups of functions: (1) network connectivity (SD-WAN, WAN optimization), (2) security for Internet access/egress (SWG, CASB, DNS filtering), and (3) access to private resources/ingress (ZTNA). ZTNA is *architecturally different* from the other components: it "will continue to require that elements (PEPs) be deployed into enterprise-controlled environments, including on-premises enterprise networks, data centers, and public cloud-based IaaS and PaaS environments."

## Evidence

Two reasons: (1) TCP/IP networks require a local node to terminate the encrypted tunnel and proxy connections to private resources on the private network; (2) the local PEP is needed to obtain and use local context/attributes as policy inputs. Gartner makes the same distinction between "ingress SASE" and "egress SASE" with different requirements.

Additionally, enterprises "still have on-premises users and on-premises resources" and "need to control on-premises server-to-server access, which cloud-based services often struggle to manage." The ZT principle of enforcing policy "for all identities' access to all resources, regardless of the location of the identity or resource" means ZTNA can't be purely cloud-delivered.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The ingress/egress distinction is now standard industry terminology. The requirement for on-premises or cloud-local PEPs is validated by every major ZTNA deployment — even "cloud-delivered" ZTNA products deploy connectors, app connectors, or agents into enterprise environments. The BeyondCorp Access Proxy model also requires infrastructure on the enterprise side (the proxy itself).

## Stakes

If ZTNA is treated as just another SASE feature, enterprises underestimate the deployment complexity of on-premises connectors and the policy integration work. If ZTNA is treated as completely separate from SASE, enterprises end up with disjointed security stacks that don't share context.

## Disagreement

**Who disagrees:**

Pure cloud-delivery advocates might argue that with enough cloud connectivity (SD-WAN everywhere, direct cloud interconnects), on-premises PEPs become unnecessary. This works for greenfield, cloud-native organizations but not for enterprises with legacy data centers. Browser-based ZTNA approaches argue that the browser itself can act as the PEP, eliminating the need for a local network node — this is valid for web apps but not for SSH, RDP, or non-HTTP protocols.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

This is prescient for 2021. The SASE market has consolidated significantly since then (Netskope, Zscaler, Cloudflare, Palo Alto all now offer integrated SASE + ZTNA), but the architectural distinction Garbis & Chapman draw remains true. The local PEP requirement is the reason every ZTNA product ships some form of connector/app connector — it's not a temporary limitation, it's an architectural necessity.
