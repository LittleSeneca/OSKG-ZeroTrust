---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/bsi
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-identity
  - topic/zt-threats
claim_id: "bsi-zt.1"
statement: "BSI's seven core messages frame ZT as a preventive, holistic, long-term, resource-intensive, and confidentiality/integrity-focused paradigm"
confidence: "high"
confidence_rationale: "HIGH for structural extraction. MEDIUM for Message 3's implications — the confidentiality/integrity-over-availability hierarchy may reflect German"
claim_type: "definitional"
source_note: "[[BSI — Zero Trust Position Paper]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# bsi-zt.1: BSI's seven core messages frame ZT as a preventive, holistic, long-term, resource-intensive, and confidentiality/integrity-focused paradigm

**Source:** [[BSI — Zero Trust Position Paper]] — BSI, *Zero Trust Position Paper*, 2023

## The Claim

The document opens with seven *Kernbotschaften* (core messages) that define the BSI's official position:

1. ZT approaches improve preventive security for application access and reduce damage scope from attacks (*"Anwendungszugriffe besser präventiv abgesichert werden und insbesondere das Schadensausmaß von Angriffen weiter reduziert werden"*)
2. ZT unifies known security measures and best practices into a holistic approach — these measures are becoming increasingly important due to the heightened threat landscape
3. **ZT's protective effect focuses primarily on integrity (*Integrität*) and confidentiality (*Vertraulichkeit*), not availability (*Verfügbarkeit*)** — this is a distinctive BSI position
4. Holistic, effective ZT implementation is a long-term undertaking requiring sustained high financial and personnel resources
5. Cross-organizational networking requires ZT concepts to be coordinated across organizations — potentially with binding agreements
6. **Product interoperability is essential for successful ZT implementation and remains a major challenge due to lack of standardization** (*"Die Interoperabilität von Produktfunktionalitäten ist für eine erfolgreiche Zero Trust-Umsetzung elementar und stellt heute, u.a. aufgrund fehlender Standardisierungen, noch eine große Herausforderung dar"*)

## Evidence

_No evidence separable from the claim statement in the source note._

## Confidence

**Rating:** HIGH
**Rationale:** HIGH for structural extraction. MEDIUM for Message 3's implications — the confidentiality/integrity-over-availability hierarchy may reflect German legal frameworks that I cannot fully assess.

## Stakes

Message 3 is the BSI's most distinctive claim relative to other national frameworks. NIST, CISA, and CCCS all treat CIA as a balanced triad. The BSI explicitly de-prioritizes availability, noting that ZT principles "do not prevent Denial of Service (DoS) attacks on devices or applications or associated Policy Enforcement Points (PEPs)" and that "long-term, even in the ideal state, central defense [against DoS] will remain necessary." This has architectural implications: it means BSI-endorsed ZT architectures can accept availability tradeoffs in exchange for confidentiality/integrity gains — a position that would be controversial in availability-dependent sectors.

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

The de-prioritization of availability is intellectually honest and technically accurate — ZT's continuous verification and microsegmentation can introduce latency and single points of failure (PDP, identity provider) that reduce availability. However, this framing may limit ZT adoption in German critical infrastructure (KRITIS) sectors where availability is the primary security objective. The BSI is essentially saying: "ZT protects data; use other mechanisms for availability" — which is a cleaner separation of concerns than most frameworks offer.
