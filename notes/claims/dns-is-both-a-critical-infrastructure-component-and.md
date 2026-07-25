---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-network
  - topic/zt-monitoring
  - topic/zt-implementation
  - topic/zt-architecture
claim_id: "gc-net-access.2"
statement: 'DNS is both a critical infrastructure component and a security monitoring tool under ZT — private DNS resolution must adapt to distributed environments, and DNS monitoring for known-bad domains is "high-value and low-risk."'
confidence: "high"
confidence_rationale: "HIGH — The DoT vs. DoH recommendation reflects a specific, well-reasoned position grounded in enterprise operational requirements. The DNS monitoring"
claim_type: "implementation"
source_note: "[[Garbis and Chapman — Network and Access Technologies]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-net-access.2: DNS is both a critical infrastructure component and a security monitoring tool under ZT — private DNS resolution must adapt to distributed environments, and DNS monitoring for known-bad domains is "high-value and low-risk."

**Source:** [[Garbis and Chapman — Network and Access Technologies]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

The authors distinguish public DNS (hierarchical, unencrypted by default) from private DNS (source of complexity — only accessible from local networks, returns non-routable IPs). Two ZT models for DNS: (1) publish internal records to public DNS directing external users to cloud-facing proxies; (2) transmit client DNS requests to private DNS servers via a PEP based on search domains. DNS monitoring is described as "high-value and low-risk" and "must be part of any ZT architecture."

## Evidence

On encrypted DNS: the IETF is standardizing DNS over TLS (DoT, RFC 8310) and DNS over HTTPS (DoH, RFC 8484). The authors recommend DoT (works within enterprise DNS setups) and "strongly discourage" DoH (bypasses enterprise DNS controls). Some ZT systems tunnel DNS requests through encrypted ZT tunnels, providing encryption and enterprise monitoring simultaneously. The authors note that ZT platforms should include DNS filtering/blocking and react to malicious DNS requests by adjusting user access.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The DoT vs. DoH recommendation reflects a specific, well-reasoned position grounded in enterprise operational requirements. The DNS monitoring claim is widely supported across security frameworks.

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
