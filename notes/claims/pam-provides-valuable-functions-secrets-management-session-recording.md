---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-identity
  - topic/zt-access-mgmt
  - topic/zt-authentication
  - topic/zt-device
claim_id: "gc-net-access.8"
statement: "PAM provides valuable functions (secrets management, session recording) that persist under ZT, but password vaulting is premised on the non-ZT model of a too-open network — and PAM is identity-aware rather than identity-centric."
confidence: "high"
confidence_rationale: "HIGH — The PAM evaluation is nuanced, distinguishing between functions that persist (secrets management, session recording) and those premised on"
claim_type: "implementation"
source_note: "[[Garbis and Chapman — Network and Access Technologies]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-net-access.8: PAM provides valuable functions (secrets management, session recording) that persist under ZT, but password vaulting is premised on the non-ZT model of a too-open network — and PAM is identity-aware rather than identity-centric.

**Source:** [[Garbis and Chapman — Network and Access Technologies]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

The authors make a striking argument: "The entire premise of password vaulting is based on the non-Zero Trust approach of a too-open network, where every user has ongoing network access to every server, and therefore a vault with server password obfuscation and rotation is required. This premise is no longer true with Zero Trust!" They don't recommend decommissioning existing PAM vaults but advise against deploying new ones for ZT-protected environments.

## Evidence

Three core PAM functions: (1) password vaulting — secure storage and lifecycle management of privileged credentials, evolved from "checking out" passwords to automated ephemeral credential rotation; (2) secrets management — expanded beyond passwords to certificates, API keys, SSH keys, connection strings; (3) Privileged Session Management — intercepts/proxies admin access (RDP, SSH) for monitoring/recording/constraining, can enforce RBAC at the command level. Three ZT+PAM integration patterns: (1) PAM behind a PEP — simplest, most immediately valuable; (2) PDP consumes PAM policies — PAM informs ZT enforcement decisions; (3) PAM consumes PDP context — PAM uses ZT-provided identity/device attributes for better access decisions. The growing adoption of serverless/immutable infrastructure is also reducing relevance of traditional PSM and vaulting.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The PAM evaluation is nuanced, distinguishing between functions that persist (secrets management, session recording) and those premised on outdated network models (password vaulting). The three integration patterns provide actionable architecture guidance.

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

_Not addressed separately in the source note._
