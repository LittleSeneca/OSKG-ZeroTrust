---
tags:
  - type/index
  - oskg-zerotrust
  - notes
  - concepts
created: 2026-07-24
related:
  - "[[../Notes Index]]"
---

# Concepts Index

Core Zero Trust concepts, definitions, and principles. These notes define the vocabulary of the knowledge graph.

## Core Concepts (to be developed)

- Zero Trust definition and tenets (NIST SP 800-207)
- Never trust, always verify
- Assume breach
- Least privilege access
- Microsegmentation
- Identity-centric security
- Policy engine / policy administrator / policy enforcement point
- Control plane / data plane separation
- Software-Defined Perimeter (SDP)
- Zero Trust Network Access (ZTNA)
- Zero Trust eXtended (ZTX) framework
- Continuous verification
- Dynamic policy
- Trust zones
- Implicit trust zone elimination
- Lateral movement prevention

## Concept Categories

| Category | Key Concepts |
|----------|-------------|
| **Identity** | Authentication, authorization, MFA, continuous validation, identity fabric |
| **Device** | Device trust, posture assessment, endpoint compliance, BYOD |
| **Network** | Microsegmentation, SDP, ZTNA, VPN replacement, SD-WAN integration |
| **Application** | Application-level access, API security, workload identity |
| **Data** | Data classification, encryption, DLP, data-centric security |

## Reading Notes

Chapter-by-chapter conceptual analysis of each book in the Book Guide. These notes capture definitions, principles, and conceptual frameworks from each source before they are decomposed into claims.

- [[NIST 800-207 — Ch3 — Logical Components]] — The canonical ZTA component model: PE, PA, PEP; three approach variations; four deployment models; trust algorithm; control plane / data plane separation. **Load-bearing chapter for the entire ZT standards ecosystem.**
- [[NIST 800-207 — Ch7 — Migration]] — Migration to ZTA: pure vs. hybrid brownfield, the 7-step deployment cycle (actors → assets → processes → policies → solutions → deploy/monitor → expand).

---

*Concepts will be populated as source texts are read. Each concept note links to the claims that depend on it.*
