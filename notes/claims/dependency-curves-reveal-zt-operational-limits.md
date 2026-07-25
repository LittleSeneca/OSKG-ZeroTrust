---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/yu-cdm
  - topic/zt-architecture
  - topic/zt-definition
  - topic/zt-implementation
  - topic/zt-governance
claim_id: "yu-cdm.3"
statement: "The dependency curves reveal ZT's operational limits"
confidence: "medium"
confidence_rationale: "MODERATE. The dependency curves are Yu's own synthesis and he acknowledges they are debatable. AI/ML advances in SOAR and XDR may shift the curves"
claim_type: "architectural"
source_note: "[[Yu — Cyber Defense Matrix]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# yu-cdm.3: The dependency curves reveal ZT's operational limits

**Source:** [[Yu — Cyber Defense Matrix]] — Sounil Yu, *Cyber Defense Matrix*, 2022

## The Claim

TECHNOLOGY dependency is highest in IDENTIFY and PROTECT, then diminishes as we move right toward DETECT, RESPOND, and RECOVER where PEOPLE dependency grows. PROCESS dependency remains constant across all five functions. This has profound implications for ZT investment: the most technology-intensive part (ZT access proxies) occupies the left side of the matrix, but the most people-intensive part (incident response) is on the right.

## Evidence

Yu cites research on the "ironies of automation" — the more we automate, the more critical human operators become for handling edge cases. Left-of-boom activities (inventory, vulnerability management, access control) benefit heavily from technology. Right-of-boom activities (triage, investigation, containment) still depend on human judgment, especially for novel attack patterns that evade automated detection.

## Confidence

**Rating:** MEDIUM
**Rationale:** MODERATE. The dependency curves are Yu's own synthesis and he acknowledges they are debatable. AI/ML advances in SOAR and XDR may shift the curves rightward over time.

## Stakes

Organizations that invest exclusively in ZT technology (PROTECT) without commensurate investment in SOC capabilities (DETECT/RESPOND) have a lopsided security posture. ZT reduces the attack surface but does not eliminate the need for detection and response.

## Disagreement

**Who disagrees:**

Vendors of AI-driven SOAR platforms argue that technology can increasingly handle RESPOND functions. The trend toward autonomous response (automated containment, playbook-driven remediation) challenges the steepness of Yu's PEOPLE curve on the right side.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[five-nist-csf-functions-form-strict-temporal|five-nist-csf-functions-form-strict-temporal]]

## Assessment

The dependency curves are conceptually valuable even if the exact slope is debatable. For OSKG-ZeroTrust, the key insight is that ZT frameworks (NIST 800-207, CISA ZTMM, DoD ZT RA) are heavily weighted toward IDENTIFY and PROTECT — the left side. The right side (DETECT, RESPOND, RECOVER) is under-theorized in ZT literature, creating a gap that future standards will need to address.
