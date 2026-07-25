---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/bsi
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-implementation
  - topic/zt-network
claim_id: "bsi-zt.2"
statement: "BSI provides a formal three-part definition that extends NIST with German regulatory context"
confidence: "high"
confidence_rationale: "HIGH for the structural elements. The three operational implications are consistent with NIST's tenets but with German-specific terminology and"
claim_type: "definitional"
source_note: "[[BSI — Zero Trust Position Paper]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# bsi-zt.2: BSI provides a formal three-part definition that extends NIST with German regulatory context

**Source:** [[BSI — Zero Trust Position Paper]] — BSI, *Zero Trust Position Paper*, 2023

## The Claim

"Der Begriff 'Zero Trust' beschreibt ein aus dem 'Assume Breach'-Ansatz entwickeltes Architekturdesign-Paradigma, welches im Kern auf dem Prinzip der minimalen Rechte (engl. 'Least Privileges') aller Entitäten (Nutzer, Geräte, Systeme, ...) in der Gesamtinfrastruktur (auf allen Ebenen) basiert. Das heißt, es existiert kein implizites Vertrauen zwischen allen Entitäten."

The definition has three operational implications:

1. **No implicit trust → mandatory authentication and authorization** for every entity accessing resources. Strong authentication (*starke Authentifizierung*) plays a decisive role.
2. **Least privilege → resources divided into smallest possible units, permissions granted with maximum granularity.** The smaller radius limits uncontrolled data exfiltration, manipulation, and lateral movement in case of malicious access.
3. **No differentiation between inside/outside the network** — the internal network is always considered untrusted. Trust is never permanently granted. Dynamic access policies, continuous monitoring, and risk analyses continually reassess trust, with each access decision made anew.

## Evidence

The definition explicitly derives from the "Assume Breach" approach, tracing its lineage through Marsh (1994), Jericho Forum (2003), Kindervag/Forrester (2010), Google BeyondCorp (2014), and NIST SP 800-207 (2019). The BSI positions its definition as synthesizing this lineage while adding German-specific emphasis on *Nachweise* (verifiable evidence/proofs) for trust establishment.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH for the structural elements. The three operational implications are consistent with NIST's tenets but with German-specific terminology and emphasis on formal verifiability.

## Stakes

The BSI's emphasis on *verlässliche Nachweise* (reliable proofs) for trust establishment is more formal than the Anglo-American frameworks' "trust signals" or "risk-based evaluation." This may reflect German regulatory culture's preference for auditable, evidence-based decisions over probabilistic risk assessments.

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

The BSI definition is rigorous and well-sourced. It's more compact than NIST's seven tenets while capturing the same essential principles. The emphasis on *verifiable* trust (rather than *calculated* trust) is a genuine contribution — it suggests that German ZT implementations may require different audit and compliance structures than US implementations, even when using the same underlying technologies.
