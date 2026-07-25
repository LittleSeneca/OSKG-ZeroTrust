---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-identity
  - topic/zt-device
  - topic/zt-governance
  - topic/zt-implementation
claim_id: "go-intro.5"
statement: "Identity must be contextual — WHO, WHAT device, WHERE, HOW, and WHEN all matter"
confidence: "medium"
confidence_rationale: "MEDIUM. Confidence not explicitly stated in source."
claim_type: "implementation"
source_note: "[[Green-Ortiz — Intro Ch1-2 — Foundations]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-intro.5: Identity must be contextual — WHO, WHAT device, WHERE, HOW, and WHEN all matter

**Source:** [[Green-Ortiz — Intro Ch1-2 — Foundations]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

Identity must be contextual — WHO, WHAT device, WHERE, HOW, and WHEN all matter

## Evidence

Detailed treatment of AAA (Authentication, Authorization, Accounting), certificate authorities (EAP-TLS, chain of trust), NAC (integration with all pillars), provisioning (Device, User, People, Infrastructure, Services), privileged access (least privilege, audit requirements), MFA (knowledge + possession + biometric + challenge factors), asset identity (MAC OUI, passive profiling, CMDB), and IP schemas (IPv4/IPv6 dual-stack, PI vs. PA space). The SBC Healthcare use case demonstrates how contextual identity drives policy: a surgeon in the OR gets different access than the same surgeon connecting from home over VPN.

**Green-Ortiz's claim:**

Identity is the most critical pillar because it provides the subject to which all other capabilities apply. But identity alone is not enough — full *contextual* identity is required. Contextual identity answers five questions: WHO (user/owner/manager), WHAT (device type, posture, certificate), WHERE (location, network medium), HOW (connection method: 802.1X, VPN, MAB), and WHEN (time of access, baseline behavior deviations).

**Key dynamics:**

- **MAC Authentication Bypass is a fallback, not a primary method.** MAC addresses are easily spoofed. MAB should always be combined with profiling to add confidence. Devices with lower identity confidence get more restrictive authorization.
- **802.1X with RADIUS is the preferred network authentication method.** Combined with centralized authentication databases (LDAP, Active Directory, certificate authorities), it enables dynamic policy response to identity context changes.
- **Certificate-based identity is stronger than credential-based.** EAP-TLS with user + machine certificates creates a unique contextual identity that prevents credential export and sharing. The combination of "who" and "what" enables differentiated access.
- **IoT and headless devices require special handling.** MUD (Manufacturer Usage Description) and passive profiling compensate for the inability to run supplicants. The lower confidence in IoT identity means authorization must be more restrictive.

**Cross-reference — NIST 800-207 Ch3:**

NIST's "ID Management" data source provides user identity and attributes to the PE. Green-Ortiz's contextual identity model is a superset: it adds device identity (what), location (where), connection method (how), and temporal (when) dimensions that NIST treats as separate data sources (CDM, activity logs, threat intelligence).

**Cross-reference — Gilman & Barth Ch1:**

Gilman & Barth's assertion 4 — "Every device, user, and network flow is authenticated and authorized" — is the principle. Green-Ortiz's contextual identity model is the enterprise operationalization of that principle. Gilman & Barth focus on the authentication/authorization protocols; Green-Ortiz focuses on the operational processes (provisioning, onboarding, CMDB integration) that make identity reliable at scale.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. Confidence not explicitly stated in source.

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

The contextual identity model — WHO, WHAT, WHERE, HOW, WHEN — is the most memorable framework in the book. It's immediately actionable for workshops and assessments. The treatment of IoT identity challenges is particularly valuable because it addresses the hardest ZT problem (devices that can't authenticate themselves) without hand-waving.
