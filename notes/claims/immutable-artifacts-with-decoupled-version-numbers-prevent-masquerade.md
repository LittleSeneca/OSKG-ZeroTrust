---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-app
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
claim_id: "gb-ch7-8.4"
statement: "Immutable artifacts with decoupled version numbers prevent masquerade attacks"
confidence: "high"
confidence_rationale: "HIGH. This is standard practice in mature package ecosystems (APT, RPM, Docker registries, npm with integrity hashes). The pattern is battle-tested."
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch7-8 — Applications and Traffic]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch7-8.4: Immutable artifacts with decoupled version numbers prevent masquerade attacks

**Source:** [[Gilman and Barth — Ch7-8 — Applications and Traffic]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

Build artifacts should have Write Once Read Many semantics. The version number communicated to users should be decoupled from the immutable build identifier. A separate distribution/promotion system maps release versions to build artifacts, enabling immutable builds without sacrificing semantic versioning. Once a version is released, it cannot be changed — a new build artifact with a new version must be produced instead.

## Evidence

The Firefox release version 51.0.1 retains a separate build ID in the package name (Figure 7-4). APT repositories use a chain of signed hashes — Release file signed with private key → hash of Packages index → hashes of individual packages. The maintainer signs the Release file; consumers validate the entire chain.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is standard practice in mature package ecosystems (APT, RPM, Docker registries, npm with integrity hashes). The pattern is battle-tested.

## Stakes

Without immutable artifacts, an attacker who compromises a distribution server can replace a "good" build with a "bad" one under the same version label. Consumers pulling the latest version have no way to detect the swap.

## Disagreement

**Who disagrees:**

No one disagrees with immutability. The tension is between the authors' strict "never republish a version" stance and real-world practice where minor fixes are sometimes re-released under the same version (Docker `latest` tags, npm unpublish/republish, rolling release distros). The industry has largely moved to content-addressed artifacts (container image digests, Git commit SHAs as version identifiers) which solve the same problem differently.

**Cross-reference — NSA Device Pillar: Distribution trust.** NSA's device pillar extends distribution trust to the hardware level: firmware updates must be signed, TPM measurements compared against SBOM/RIM, and the entire update chain validated from firmware through OS to application. This is Gilman & Barth's distribution chain applied to the device foundation.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[the-build-system-is-the-most-dangerous-attack|Immutable artifacts with decoupled version numbers protect the artifact side of the unprotected build system, securing t]]
- [[the-application-pipeline-is-a-cryptographic-chain-break|Immutable artifacts with signed hashes provide the artifact-integrity link in the cryptographic chain]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The distinction between build versions and release versions is operationally critical but widely misunderstood. Most teams conflate the two. The authors provide a clean mental model: the build system produces immutable artifacts identified by build number; the release system chooses which artifact to promote. This separation of concerns is the right architecture.
