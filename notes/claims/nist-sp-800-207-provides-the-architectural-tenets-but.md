---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-definition
  - topic/zt-architecture
  - topic/zt-implementation
  - topic/zt-network
claim_id: "finney-ch4-7.3"
statement: "NIST SP 800-207 provides the architectural tenets, but Kindervag's design principles and five-step methodology provide the actionable strategy."
confidence: "high"
confidence_rationale: "HIGH. This tension between architecture (NIST) and strategy/methodology (Kindervag) is real and underappreciated. NIST tells you *what* to build"
claim_type: "definitional"
source_note: "[[Finney — Ch4-7 — Building the ZT Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch4-7.3: NIST SP 800-207 provides the architectural tenets, but Kindervag's design principles and five-step methodology provide the actionable strategy.

**Source:** [[Finney — Ch4-7 — Building the ZT Strategy]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"NIST 800-207 is focused on architecture, which is important. But there's not much guidance for what to do or where to start if you're going to do the work of maturing your information security program to embrace the strategy of Zero Trust... The design principles and methodology were developed by John Kindervag over a decade of actually doing the work."

## Evidence

Aaron displays the NIST Zero Trust Basic Tenets (all seven) and the NIST network assumptions (all six), but he's explicitly critical: "I get frustrated with the NIST Zero Trust architecture because there's nothing in it about aligning with the business. Remember, Zero Trust is the strategy for preventing a security breach at your unique organization." He warns that NIST recommendations, if implemented literally, "would make it harder for employees to do their work or for consumers to use your products."

The chapter presents both frameworks side by side:
- **NIST 800-207**: seven basic tenets (all resources, secure all communication, per-session access, dynamic policy, monitor integrity, dynamic auth, collect information) + six network assumptions (no implicit trust zone, devices may not be yours, no inherent trust, resources outside enterprise infra, remote networks untrusted, consistent policy across boundaries)
- **Kindervag methodology**: four design principles (focus on business, inside-out, determine access, inspect/log) + five-step methodology (define protect surface → map transaction flows → architect → create policies → monitor/maintain)

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This tension between architecture (NIST) and strategy/methodology (Kindervag) is real and underappreciated. NIST tells you *what* to build; Kindervag tells you *how* to do it. Both are necessary.

## Stakes

Organizations that follow only NIST risk building technically correct ZT architecture that alienates the business and fails to be adopted. Organizations that follow only Kindervag's methodology without NIST's architectural rigor risk building controls that don't meet compliance or interoperability standards.

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

Finney's synthesis is pragmatic and correct. The book doesn't reject NIST — it layers NIST's tenets onto Kindervag's methodology. The architectural tenets become the criteria for evaluating solutions at each step of the methodology. This is the most balanced treatment of the NIST-vs-Kindervag tension in the ZT literature.
