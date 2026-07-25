---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-network
  - topic/zt-access-mgmt
  - topic/zt-definition
  - topic/zt-threats
claim_id: "gb-ch7-8.8"
statement: "The first packet problem is solved by Single Packet Authorization (SPA)"
confidence: "medium"
confidence_rationale: "MODERATE. SPA is a sound cryptographic concept but has seen limited production adoption outside niche security-focused deployments. fwknop is"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch7-8 — Applications and Traffic]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch7-8.8: The first packet problem is solved by Single Packet Authorization (SPA)

**Source:** [[Gilman and Barth — Ch7-8 — Applications and Traffic]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

Complex authentication systems like TLS have large attack surfaces. The first packet problem — how to allow only trusted connections without answering a single unauthenticated packet — is mitigated by pre-authentication: encrypting/signing a small piece of data and sending it as a UDP packet. The receiver passively listens; only upon receiving a properly encrypted pre-authentication packet does it open a tightly scoped, short-lived firewall rule for the sender.

## Evidence

fwknop is presented as the reference implementation. It supports AES (symmetric) and GnuPG (asymmetric) encryption, optionally adds HMAC to prevent ciphertext tampering, and creates firewall rules scoped to the sender's IP, destination port, and optionally source port — rules that expire after a configurable period (default 30 seconds). The seven mandatory fields in the SPA payload include random data, username, timestamp, version, message type, access request, and SHA-256 digest.

## Confidence

**Rating:** MEDIUM
**Rationale:** MODERATE. SPA is a sound cryptographic concept but has seen limited production adoption outside niche security-focused deployments. fwknop is maintained but far from ubiquitous. Modern ZTNA products achieve similar goals through different mechanisms (outbound-only connections to an access proxy that never exposes listening ports).

## Stakes

Without SPA or equivalent, every exposed TLS service is a public attack surface. Attackers can probe, fingerprint, and exploit TLS implementation vulnerabilities without ever authenticating. SPA hides the service — it's invisible until you prove you should be allowed to see it.

## Disagreement

**Who disagrees:**

Most commercial ZTNA products (Zscaler, Cloudflare Access, Google BeyondCorp) solve the same problem differently: the application is never directly exposed to the internet. Clients connect to an access proxy, which authenticates before forwarding. This proxy-based approach achieves the same "hide the service" property without SPA's protocol-level complexity.

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

SPA is elegant but has been largely superseded by architectural patterns (ZTNA access proxies, software-defined perimeter controllers). The concept — don't answer packets from untrusted sources — remains fundamental. The implementation has evolved. For a 2017 book, SPA was ahead of the curve; in 2026, the proxy model has won.
