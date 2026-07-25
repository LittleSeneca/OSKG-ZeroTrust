---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-authentication
  - topic/zt-encryption
  - topic/zt-identity
  - topic/zt-threats
claim_id: "gb-ch7-8.7"
statement: 'Encryption and authentication are separate concerns — zero trust requires authenticity; encryption comes "for free"'
confidence: "high"
confidence_rationale: 'VERY HIGH. This is cryptographic orthodoxy — "encryption without authentication is dangerous" is a near-universal principle in modern protocol'
claim_type: "definitional"
source_note: "[[Gilman and Barth — Ch7-8 — Applications and Traffic]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch7-8.7: Encryption and authentication are separate concerns — zero trust requires authenticity; encryption comes "for free"

**Source:** [[Gilman and Barth — Ch7-8 — Applications and Traffic]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

Encryption ensures confidentiality (only the receiver can read the data). Authentication enables validation that the message was sent by the claimed sender and is unaltered (integrity). All transport protocols discussed in the book provide both, so encryption is attained "for free," leaving few good reasons to exclude it. However, encryption without authentication is dangerous — an attacker can forge messages or replay previous valid ones.

## Evidence

Architecture diagrams showing encryption only at certain network boundaries (between sites but not within the datacenter) are characterized as a "direct contradiction of the zero trust architecture" because they create privileged zones. The authors argue systems that truly do not require confidentiality are rare.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This is cryptographic orthodoxy — "encryption without authentication is dangerous" is a near-universal principle in modern protocol design. TLS 1.3 mandates authenticated encryption. The Noise protocol framework eliminated cipher suite negotiation entirely in favor of fixed authenticated constructions.

## Stakes

If you accept encryption without authentication, you get the worst of both worlds: the overhead of encryption with none of the trust guarantees. An attacker can modify ciphertext and the receiver processes it without validation.

## Disagreement

**Who disagrees:**

The "encryption comes for free" claim is slightly too strong. Encryption adds computational overhead and operational complexity (key management, packet capture blind spots, latency). Some high-frequency trading and real-time systems legitimately cannot tolerate the latency. But for the vast majority of use cases, the authors are correct.

**Cross-reference — NIST 800-207 Ch5: The DoS angle.** NIST notes that ZT policy engines can use expected traffic patterns to calculate coarse enforcement rules for upstream filtering devices. This is relevant because the encryption/authentication the authors advocate is computationally expensive — filtering out malicious traffic _before_ it reaches the authentication layer reduces the DoS attack surface.

**Cross-reference — NSA Network Pillar: Encryption requirements.** NSA specifies that API calls must be secured using encrypted protocols (TLS v1.2+, SSH v2+) with mutual authentication (client and server certificates). This aligns exactly with the authors' position: authenticity through mutual authentication, encryption as the default.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[agents-are-ephemeral-request-scoped-and-purely-for-authorization|Both articulate separation-of-concerns in zero trust: Claim 1 separates authentication from authorization; Claim 3 exten]]

## Assessment

This claim is deceptively important. The distinction between "we encrypted the traffic" and "we mutually authenticated the traffic" is the difference between perimeter thinking and zero trust thinking. Perimeter networks encrypt at boundaries and trust traffic within. Zero trust networks mutually authenticate every flow regardless of location.
