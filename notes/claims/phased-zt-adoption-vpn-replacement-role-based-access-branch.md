---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-migration
claim_id: "gc-iam-policy.4"
statement: "Phased ZT adoption — VPN replacement → role-based access → branch office removal — delivers incremental value and pays for itself"
confidence: "high"
confidence_rationale: "HIGH. The financial ROI ($500K/year in branch office costs alone) plus the pandemic resilience story make this the most compelling business case for"
claim_type: "migration"
source_note: "[[Garbis and Chapman — Practice IAM Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-iam-policy.4: Phased ZT adoption — VPN replacement → role-based access → branch office removal — delivers incremental value and pays for itself

**Source:** [[Garbis and Chapman — Practice IAM Policy]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

Through the SDP case study, "the organization has obtained clear and compelling benefits, both security and financial, from adopting Zero Trust through a Software-Defined Perimeter architecture." A phased approach delivered "nearly immediate value" while building toward the strategic vision.

## Evidence

A US-based multinational (14,000+ employees, 700+ retail locations, 2 data centers, 12 branch offices, IaaS cloud). Phase 1: tactical VPN replacement for 1,000 users (750 corporate + 250 developers). Phase 2: role-based access with a few basic groups (General Employee, IT, Finance, Network Admin, Database Admin). Phase 3: removed 2,000 branch office workers from the enterprise network, decommissioned branch office network hardware, replaced with commodity broadband — saving $500,000+ annually. Phase 4 (COVID response): deployed SDP client to 10,000+ part-time retail workers (mix of managed and BYOD), enabling immediate work-from-home. Phase 5 (planned): microsegmentation on Linux servers.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The financial ROI ($500K/year in branch office costs alone) plus the pandemic resilience story make this the most compelling business case for ZT in the book.

## Stakes

If phased ZT can pay for itself in under a year through infrastructure savings, the business case doesn't depend on threat reduction — it's a pure operational efficiency play. This is the strongest argument against "ZT is too expensive."

## Disagreement

**Who disagrees:**

Not a disagreement per se, but the CISA ZTMM maturity model would place this organization's phases across multiple maturity levels — some functions reached Optimal (branch office model) while others (admin access with no MFA) remained at Initial. The case study shows real-world messiness.

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

This case study is the most valuable single contribution of Ch4. It's concrete, quantified, and shows that ZT isn't a Big Bang. The pattern — start with a pain point (VPN), use wide-open policies initially to gain confidence, then progressively tighten — is the right one for virtually every organization.
