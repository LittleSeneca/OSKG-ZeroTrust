---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-definition
  - topic/zt-access-mgmt
  - topic/zt-identity
  - topic/zt-architecture
claim_id: "gc-ch1-3.4"
statement: "Zero Trust amplifies existing security concepts (least privilege, RBAC) into a holistic, identity-centric, automated platform — this is what's new."
confidence: "high"
confidence_rationale: "HIGH. This is the most coherent answer to \"what's new about Zero Trust\" in the literature. The amplification argument — ZT doesn't invent new"
claim_type: "definitional"
source_note: "[[Garbis and Chapman — Ch1-3 — Introduction and Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-ch1-3.4: Zero Trust amplifies existing security concepts (least privilege, RBAC) into a holistic, identity-centric, automated platform — this is what's new.

**Source:** [[Garbis and Chapman — Ch1-3 — Introduction and Architecture]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"Zero Trust amplifies [existing security elements], effectively requiring that all identities and resources be segmented from one another. Zero Trust enables fine-grained, identity-and-context-sensitive access controls, driven by an automated platform."

## Evidence

The contrast between pre-ZT security (coarse-grained separation of dev/prod) and ZT (every identity and resource segmented). The integration of previously siloed security products into a single policy model.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is the most coherent answer to "what's new about Zero Trust" in the literature. The amplification argument — ZT doesn't invent new security concepts, it scales and integrates them — is both honest and compelling.

## Stakes

If ZT is just existing security done better, resistance to adoption is resistance to improvement. If ZT requires fundamentally new technologies, adoption barriers are higher. The amplification framing lowers the perceived adoption cost.

## Disagreement

**Who disagrees:**

Purists might argue that ZT requires genuinely new architectural patterns (control plane/data plane split, PDP/PEP model) that go beyond "amplification." The amplification argument is about *principles*; the architectural argument is about *implementation*.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[the-three-core-principles-secure-all-resources-regardless|Clarifies what is transformative about the three core principles: they aren't just repackaging but amplification into a]]
- [[the-working-definition-centers-zt-as-an-integrated|Explains the mechanism by which ZT becomes an integrated platform: amplifying and integrating existing concepts (least p]]

## Assessment

This is the book's most valuable intellectual contribution. "ZT amplifies existing security" is the right answer for skeptical practitioners who ask "what's new?" It's both true and reassuring. The complementary claim — that this amplification requires an integrated platform with automation — is where the architectural work happens.
