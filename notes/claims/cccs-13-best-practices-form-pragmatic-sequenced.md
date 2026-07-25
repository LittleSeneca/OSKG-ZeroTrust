---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cccs
  - topic/zt-architecture
  - topic/zt-implementation
claim_id: "cccs-arch.5"
statement: "CCCS's 13 best practices form a pragmatic, sequenced ZTA implementation guide"
confidence: "high"
confidence_rationale: "HIGH. These practices are consistently cited across ZT literature (Finney, Garbis & Chapman, Gilman & Barth). CCCS's contribution is the specific"
claim_type: "architectural"
source_note: "[[CCCS — ZT Approach to Security Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cccs-arch.5: CCCS's 13 best practices form a pragmatic, sequenced ZTA implementation guide

**Source:** [[CCCS — ZT Approach to Security Architecture]] — Canadian Centre for Cyber Security, *Zero Trust Approach to Security Architecture — ITSM.10.008*, 2023

## The Claim

The document lists 13 best practices "to help prioritize their efforts when implementing a zero trust architecture." These are:

1. **Authenticate all connections** — never trust the local network; at minimum authenticate user and device
2. **Implement ZT policies** — start with the six Kipling questions: Who, What, Why, Where (user), Where (endpoint), How
3. **Establish a "trust engine"** — dynamic evaluation incorporating device state, behavioral attributes, and enterprise-level security context
4. **Know your assets and network architecture** — inventory data, users, devices, applications; understand value and risk
5. **Use multi-factor authentication (MFA)** — "an essential prerequisite of ZT"
6. **Use encryption for all traffic** — reinforces the tenet that all access must be explicitly granted
7. **Enforce policy-based access** — dynamic risk-based policies; identity-based authentication replaces IP-based trust
8. **Use PAM and SAW** — privileged access management with just-in-time access; secure administrative workstations for admin tasks
9. **Implement least privilege, RBAC, and ABAC** — RBAC for role-based enforcement, ABAC for granular attribute-based rules
10. **Monitor and log devices and services access** — continuous log collection, SIEM, security analytics
11. **Manage all devices** — unique traceable identity per device, TPM, BYOD policies, device certificates
12. **Use network segmentation or micro-segmentation** — VLANs, subnets, security zones; micro-segmentation down to workload level
13. **Use software-defined perimeter (SDP)** — adaptive trust model, identity-based access, VPN alternative

## Evidence

Each practice includes specific implementation guidance. For example: PAM should use just-in-time access with dual approval (a different user must approve the privileged session). SAWs must be dedicated machines not used for email or web browsing. MFA should adjust factors based on data sensitivity. The trust engine should incorporate device state (software versions, patch levels, location), behavioral attributes (usage patterns, time-of-day), and enterprise context (heightened security states).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These practices are consistently cited across ZT literature (Finney, Garbis & Chapman, Gilman & Barth). CCCS's contribution is the specific ordering and the emphasis on non-technical practices (policies, asset inventory) preceding technical ones.

## Stakes

If organizations treat this as a sequential checklist (do #1, then #2, etc.), they'll fail. The practices are interdependent — you can't "implement ZT policies" (#2) without "knowing your assets" (#4), and you can't "establish a trust engine" (#3) without "monitoring and logging" (#10). CCCS should have made the interdependencies explicit.

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

The list is well-chosen but the ordering is debatable. Practices 1 (authenticate all connections) and 12 (micro-segmentation) are architectural prerequisites for practices 7 (policy-based access) and 13 (SDP). A better structure would group these into three phases: foundational (4, 5, 11), architectural (1, 6, 12, 13), and operational (2, 3, 7, 8, 9, 10). The Kipling Method references (practice 2) echo Finney's methodology, suggesting CCCS was influenced by the Forrester/Kindervag lineage.
