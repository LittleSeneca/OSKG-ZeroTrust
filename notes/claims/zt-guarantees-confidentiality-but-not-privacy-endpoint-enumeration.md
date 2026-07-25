---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-encryption
  - topic/zt-network
claim_id: "gb-ch10.3"
statement: "ZT guarantees confidentiality but not privacy — endpoint enumeration is a real tradeoff"
confidence: "high"
confidence_rationale: "HIGH. This is a clear, honest tradeoff. ZT trades network topology privacy for scalability, availability, and the elimination of gateway bottlenecks"
claim_type: "definitional"
source_note: "[[Gilman and Barth — Ch10 — The Adversarial View]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch10.3: ZT guarantees confidentiality but not privacy — endpoint enumeration is a real tradeoff

**Source:** [[Gilman and Barth — Ch10 — The Adversarial View]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"The zero trust model guarantees network confidentiality, but not privacy. That is, ongoing conversations can be observed and asserted to exist; however, the contents of the conversation are protected." An adversary observing a perimeterless ZT network can "build a system diagram by observing which systems talk to which endpoints."

## Evidence

The distinction between confidentiality (contents protected) and privacy (conversation existence hidden) is well-drawn. VPN architectures obscure which specific hosts communicate by hiding them behind a gateway — this advantage is lost in ZT's peer-to-peer model. The authors note that site-to-site tunnels can provide limited privacy but warn that this "undermines the zero trust model itself, as hiding information in one part of the network and not another suggests that one is more trusted than the other."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is a clear, honest tradeoff. ZT trades network topology privacy for scalability, availability, and the elimination of gateway bottlenecks. Tor provides network privacy but is "a wholly different problem space" considered out of scope.

## Stakes

In military or intelligence environments, revealing which endpoints communicate can be as damaging as revealing what they say. This is why the DoD ZT RA retains VPN-like constructs for classified environments. For most enterprises, the confidentiality/privacy distinction is academic — content protection is sufficient, and the scalability gains of eliminating VPNs outweigh topology privacy concerns.

## Disagreement

**Who disagrees:**

NIST 800-207 §5.4 discusses visibility on the network from the defender's perspective (encrypted traffic is opaque to Layer 3 analysis). The authors discuss it from the attacker's perspective (conversation existence is observable). Both are correct — encryption is a double-edged sword.

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

This is the most philosophically nuanced section of the chapter. The willingness to admit a genuine tradeoff — rather than claiming ZT is superior in every dimension — is a mark of engineering honesty that distinguishes Gilman & Barth from vendor literature. The practical advice is sound: if topology privacy matters, use tunnels, but understand you're reintroducing trust distinctions.
