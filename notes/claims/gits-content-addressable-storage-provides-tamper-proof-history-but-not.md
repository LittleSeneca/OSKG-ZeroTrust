---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-app
  - topic/zt-encryption
  - topic/zt-implementation
  - topic/zt-governance
claim_id: "gb-ch7-8.2"
statement: "Git's content-addressable storage provides tamper-proof history but not authenticity — signed commits bridge the gap"
confidence: "high"
confidence_rationale: "VERY HIGH. This is the operational foundation of every modern CI/CD system. Signed commits are standard practice in mature organizations and are"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch7-8 — Applications and Traffic]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch7-8.2: Git's content-addressable storage provides tamper-proof history but not authenticity — signed commits bridge the gap

**Source:** [[Gilman and Barth — Ch7-8 — Applications and Traffic]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

Git stores source history as a Merkle tree (DAG of commits, each referencing ancestor commits by cryptographic hash). This prevents undetectable modification of history — any change to a commit changes its hash and all descendant hashes, which distributed contributors would notice. However, this guarantees _integrity_, not _authenticity_ — anyone with push access can add commits or forge author metadata. GPG-signed commits and tags solve this by cryptographically binding identity to contributions.

## Evidence

A malicious committer can put whatever details they want in the author field — including impersonating Linus Torvalds on GitHub. Signed commits make impersonation impossible without stealing the developer's GPG key. Build systems can then validate the signed history before compiling, closing the authentication gap.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This is the operational foundation of every modern CI/CD system. Signed commits are standard practice in mature organizations and are required by frameworks like SLSA Level 2+.

## Stakes

Without signed commits, build systems authenticate _nothing_ about who wrote the code. A compromised developer account or a CI misconfiguration can inject malicious code that looks identical to legitimate contributions. The chain of trust from human to machine breaks at the very first link.

## Disagreement

**Who disagrees:**

No one disagrees that signed commits are good. The disagreement is about _when_ they're necessary — some argue that for internal-only code with strong access controls, codified code review processes provide sufficient assurance. GitLab's and GitHub's protected branch + merge request workflows are often treated as a practical substitute for universal commit signing.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[the-build-system-is-the-most-dangerous-attack|Signed commits protect the source side of the unprotected build system, securing one flank of the build gap]]
- [[the-application-pipeline-is-a-cryptographic-chain-break|Git's content-addressable storage and signed commits provide the source-integrity link in the application pipeline crypt]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The authors make a subtle point that's easy to miss: in a brownfield repository that transitions to signed commits, the first signed commit _endorses all prior unsigned history_. This is a powerful, pragmatic insight — you don't need to rewrite history to start signing today. It's also a liability: that first signature inherits all the unknown risk of everything that came before.
