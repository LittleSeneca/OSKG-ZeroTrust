---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-implementation
claim_id: "gb-ch9.7"
statement: "The two case studies demonstrate ZT is cross-domain applicable"
confidence: "high"
confidence_rationale: "VERY HIGH. These two case studies are the most-cited ZT implementation narratives in the literature. NIST 800-207 references the BeyondCorp model"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch9.7: The two case studies demonstrate ZT is cross-domain applicable

**Source:** [[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

The case studies cover the spectrum — client-to-server (BeyondCorp) and server-to-server (PagerDuty), large enterprise and mid-size, custom-built and CM-driven. Together they show ZT principles adapt to different starting points, scales, and constraints.

## Evidence

**Cross-domain comparison:**

| Dimension | BeyondCorp (Google) | PagerDuty |
|-----------|-------------------|-----------|
| **Focus** | Client-to-server | Server-to-server |
| **Scale** | Tens of thousands of employees | Mid-size SaaS platform |
| **Resources** | Custom infrastructure from scratch | Leveraged existing Chef + open source |
| **Network** | Corporate LAN + remote | Multi-cloud public internet |
| **Enforcement** | Centralized Access Proxy | Distributed iptables per host |
| **Encryption** | LOAS (custom) + TLS | IPsec host-to-host mesh (kernel) |
| **Identity** | X.509 device certs + SSO + TPM | Role-based Chef automation |
| **Migration** | 4-year phased, netflow pipeline, simulator | Incremental log-then-enforce, per-role |
| **Key Lesson** | Data quality is the hidden bottleneck | Provider-agnostic pays off in agility |

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. These two case studies are the most-cited ZT implementation narratives in the literature. NIST 800-207 references the BeyondCorp model implicitly throughout the PEP/PDP architecture. CISA's ZTMM and DoD's ZT RA use similar migration patterns.

## Stakes

_Not addressed separately in the source note._

## Disagreement

**Who disagrees:**

_None identified._

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

_Not addressed separately in the source note._
