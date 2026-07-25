---
tags:
  - source/standards
  - nist
  - zt-threats
  - denial-of-service
  - insider-threat
  - oskg-zerotrust
created: 2026-07-24
source: "[[NIST SP 800-207 Zero Trust Architecture]]"
related:
  - "[[NSA Embracing Zero Trust]]"
  - "[[Zero Trust Networks (Gilman & Barth)]]"
  - "[[Concepts Index]]"
claims_status: extracted
claims_extracted_date: 2026-07-24
claims_count: 8
claims_files:
  - "[[pe-pa-compromise-highest-impact-threat]]"
  - "[[dos-against-pa-pep-unique-pathology]]"
  - "[[stolen-credentials-zta-constrains-blast-radius]]"
  - "[[encrypted-traffic-visibility-gap]]"
  - "[[monitoring-data-reconnaissance-target]]"
  - "[[proprietary-lock-in-amplified-zta]]"
  - "[[npe-authentication-unresolved-risk]]"
  - "[[three-threat-frameworks-progression]]"
---

# NIST 800-207 — Chapter 5 — Threats Associated with Zero Trust Architecture

## Overview

Chapter 5 of NIST SP 800-207 catalogs the threats that **persist or take unique forms** under a Zero Trust Architecture. The chapter's framing is realistic: "No enterprise can eliminate cybersecurity risk." ZTA reduces overall risk, but certain threats have distinctive features when the policy engine (PE) and policy administrator (PA) become the critical control points for all resource access. This note covers all seven threat categories (Sections 5.1–5.7) and cross-references the threat models presented in NSA's *Embracing a Zero Trust Security Model* (2021) and Gilman & Barth's *Zero Trust Networks* (Chapter 10, "The Adversarial View").

---

**Claim 1 —** Subversion of the ZTA decision process (PE/PA compromise) is the highest-impact threat because the PE and PA are the linchpins of all resource access — their compromise collapses the entire access control fabric. → [[pe-pa-compromise-highest-impact-threat]]

---

**Claim 2 —** DoS and network disruption against the PA/PEP are a unique ZTA pathology — even if access is authorized, the PA may be unable to configure the communication path, making resources unreachable despite valid authorization. → [[dos-against-pa-pep-unique-pathology]]

---

**Claim 3 —** Stolen credentials remain a threat under ZTA, but ZTA's "no implicit trust" principle constrains the blast radius — compromised accounts cannot move laterally to resources outside their authorized scope, and contextual trust algorithms detect anomalous access patterns faster. → [[stolen-credentials-zta-constrains-blast-radius]]

---

**Claim 4 —** Encrypted traffic under ZTA creates a visibility gap — all traffic is inspected but much of it is opaque to Layer 3 analysis, requiring alternative assessment methods like metadata analysis and ML-based traffic categorization. → [[encrypted-traffic-visibility-gap]]

---

**Claim 5 —** The monitoring data and policy management tools that enable ZTA's contextual policies become high-value reconnaissance targets — compromising them reveals which accounts have access to which resources, enabling attackers to prioritize targets. → [[monitoring-data-reconnaissance-target]]

---

**Claim 6 —** Proprietary data formats and vendor-specific solutions create lock-in that is amplified under ZTA — interoperability gaps can lock an enterprise into a subset of providers, and migration costs are extreme if a provider has a security issue because ZTA is heavily dependent on dynamic information access. → [[proprietary-lock-in-amplified-zta]]

---

**Claim 7 —** Non-Person Entities (NPEs) — AI agents and software-based automation managing ZTA security components — introduce unresolved authentication and decision-quality risks, and NIST flags NPE authentication as an "open issue." → [[npe-authentication-unresolved-risk]]

---

**Claim 8 —** The three major ZT threat frameworks — NIST 800-207, NSA Embracing ZT, and Gilman & Barth — form a progression from architectural taxonomy through operational threat model to engineering-level adversarial analysis, and together cover threats from implementation detail through architecture to operational philosophy. → [[three-threat-frameworks-progression]]

