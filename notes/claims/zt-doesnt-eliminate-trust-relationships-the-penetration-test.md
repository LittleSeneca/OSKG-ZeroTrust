---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-implementation
  - topic/zt-trust
  - topic/zt-architecture
  - topic/zt-network
claim_id: "finney-ch8-11.9"
statement: "ZT doesn't eliminate trust relationships — the penetration test exposed two that remained"
confidence: "high"
confidence_rationale: "HIGH. These are not theoretical — they're common penetration testing findings. The scanner-as-attack-vector is particularly important because it's a"
claim_type: "implementation"
source_note: "[[Finney — Ch8-11 — Execution and Sustainability]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch8-11.9: ZT doesn't eliminate trust relationships — the penetration test exposed two that remained

**Source:** [[Finney — Ch8-11 — Execution and Sustainability]] — George Finney, *Project Zero Trust*, 2022

## The Claim

Even after the full ZT implementation, two trust relationships were exploitable: (1) **IoT devices** (treadmills) were implicitly trusted by the internal update server, and (2) the **vulnerability scanning server** was trusted to communicate with nearly every device in the organization. Trust relationships in your own security tools are among the most dangerous.

## Evidence

- **IoT vector:** The treadmill's firmware update mechanism allowed the attacker to pivot from an IoT device to an internal server. Peter recommended memory-safe languages (Rust) for IoT firmware and device-to-device isolation.
- **Scanner vector:** The vulnerability scanner had broad network access because uncredentialed scans need open ports. Peter recommended: credentialed scans (fewer ports needed), time-limited firewall rules (only open during scan windows), and locking down what printers and other IoT devices can reach.
- **Physical exfiltration:** LED data exfiltration at ~4Kbps (<100 feet), memory bus as antenna at ~1Kbps (100+ feet), burner cell phones. These are real techniques, not hypothetical.
- **Protocol downgrade:** Attacker could force TLS downgrade to SSL 3.0 on vulnerable servers — disable everything below TLS 1.2.

**Cross-reference — Gilman & Barth Ch10:**

Gilman & Barth's adversarial view chapter catalogs similar trust exploitation vectors (identity theft, control plane compromise, endpoint enumeration). Finney operationalizes these as tabletop injects rather than theoretical threat categories. The scanner compromise maps to Gilman & Barth's "invalidation" category — using a trusted component to undermine the system.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These are not theoretical — they're common penetration testing findings. The scanner-as-attack-vector is particularly important because it's a trust relationship that security teams create themselves.

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

The scanner trust relationship is the most important finding in the exercise. It's a form of "eating your own dog food" — security tools must themselves be secured with ZT principles. A vulnerability scanner that can talk to everything is a vulnerability scanner that, if compromised, gives an attacker a map and keys to every door.
