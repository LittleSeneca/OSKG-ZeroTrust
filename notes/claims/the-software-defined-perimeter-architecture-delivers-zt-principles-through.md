---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-access-mgmt
  - topic/zt-network
claim_id: "gc-iam-policy.3"
statement: "The Software-Defined Perimeter architecture delivers ZT principles through two essential mechanisms — mTLS and Single-Packet Authorization"
confidence: "high"
confidence_rationale: "HIGH on the architectural alignment with ZT. MODERATE on the universal requirement for SPA — many commercial ZTNA products don't implement SPA and"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Practice IAM Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-iam-policy.3: The Software-Defined Perimeter architecture delivers ZT principles through two essential mechanisms — mTLS and Single-Packet Authorization

**Source:** [[Garbis and Chapman — Practice IAM Policy]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"SDP requires two security components that we believe should be included in every Zero Trust deployment — Mutual TLS Communications and Single-Packet Authorization." SPA makes servers "invisible to unauthorized clients" by requiring a valid HOTP (HMAC-based One-Time Password) before a TCP connection is even established.

## Evidence

SDP specification (CSA, 2014) and Architecture Guide (CSA, 2019). The SDP Controller acts as the PDP, SDP Gateways act as PEPs — "essentially identical to the enclave-based Zero Trust model." SPA uses UDP packets carrying a 64-bit HOTP; servers that don't validate drop the packet silently (no ACK, no RST). The computational cost to reject an unauthorized client is "orders of magnitude fewer server resources" than establishing a full TCP+TLS connection before failing authentication — making SPA-protected servers more DDoS-resilient.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the architectural alignment with ZT. MODERATE on the universal requirement for SPA — many commercial ZTNA products don't implement SPA and are still considered valid ZT solutions.

## Stakes

SPA fundamentally fixes the "connect before authenticate" flaw in TCP/IP. If SPA is optional, ZT implementations that skip it are still vulnerable to network-level reconnaissance and DDoS against the PEP itself. If SPA is essential, the ZT vendor market is narrower.

## Disagreement

**Who disagrees:**

Cloud-routed ZTNA solutions (Zscaler, Netskope) don't use SPA — they rely on the cloud proxy model where the PEP is always reachable but at a cloud edge. NIST 800-207 doesn't mention SPA. The BeyondCorp papers don't reference it either.

**Alternative reading:**

SPA could be read as a niche capability valuable for high-security environments (the authors note it was drawn from "classified high-side networks in the US intelligence community") but not necessary for most enterprises. The authors themselves frame it as a "first line of defense" backed by mTLS and identity authentication.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

SPA is the most underrated idea in ZT. The "connect before authenticate" problem is real — it's why VPN concentrators are attacked — and SPA elegantly solves it at the network layer. The fact that major ZTNA products don't use it doesn't make it wrong; it makes it a differentiator. The SDP case study (multinational, 14k employees) proves it works at scale.
