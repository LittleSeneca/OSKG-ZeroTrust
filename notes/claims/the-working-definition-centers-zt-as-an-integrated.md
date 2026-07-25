---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-definition
  - topic/zt-architecture
  - topic/zt-implementation
  - topic/zt-network
claim_id: "gc-ch1-3.7"
statement: 'The working definition centers ZT as an "integrated security platform" — broader than network architecture.'
confidence: "high"
confidence_rationale: "HIGH. This definition is broader than NIST's (which is network-architecture-focused) and more operational than Gilman & Barth's (which is"
claim_type: "definitional"
source_note: "[[Garbis and Chapman — Ch1-3 — Introduction and Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-ch1-3.7: The working definition centers ZT as an "integrated security platform" — broader than network architecture.

**Source:** [[Garbis and Chapman — Ch1-3 — Introduction and Architecture]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"A Zero Trust system is an integrated security platform that uses contextual information from identity, security and IT Infrastructure, and risk and analytics tools to inform and enable the dynamic enforcement of security policies uniformly across the enterprise. Zero Trust shifts security from an ineffective perimeter-centric model to a resource and identity-centric model."

## Evidence

The definition is derived from the six principles and the authors' practitioner experience. It explicitly names identity, security infrastructure, IT infrastructure, risk, and analytics as input sources. It positions ZT as a platform, not a product or a single architecture.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This definition is broader than NIST's (which is network-architecture-focused) and more operational than Gilman & Barth's (which is network-engineering-focused). It captures what ZT means for the enterprise security leader, not just the network architect.

## Stakes

This definition determines what counts as a ZT initiative. Under this definition, any siloed security product — no matter how good — is not ZT because ZT requires integration. The "platform" framing also sets expectations for procurement: you're buying into an ecosystem, not a box.

## Disagreement

**Who disagrees:**

Network-centric ZT advocates might argue this definition over-extends ZT into areas (DLP, GRC, SIEM) that should remain separate disciplines. Gartner's ZTNA/ZTNS distinction is narrower. NIST's definition is more abstract and less prescriptive about platform integration.

**Alternative reading:**

"Integrated security platform" could be read as vendor-friendly — it suggests buying an integrated suite rather than assembling best-of-breed components. The authors' deliberate avoidance of vendor evaluation partially mitigates this concern.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

This is the most useful definition in the ZT literature for the enterprise security leader. NIST's definition is canonical but abstract; Gilman & Barth's is architectural but network-focused. Garbis & Chapman's definition is *operational* — it tells you what a ZT system does, what inputs it consumes, and what value it produces. The 14 platform requirements that follow make it testable: you can evaluate whether a system meets them.
