---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-tenets
  - topic/zt-threats
  - topic/zt-definition
  - topic/zt-implementation
claim_id: "dod-ra-ov.4"
statement: "DoD's five tenets are threat-operational, NIST's seven tenets are architectural"
confidence: "high"
confidence_rationale: "VERY HIGH. The difference in framing is consistent and intentional. DoD's tenets 1 and 2 (\"Assume Hostile Environment,\" \"Presume Breach\") have no"
claim_type: "definitional"
source_note: "[[DoD ZT Reference Architecture — Overview and Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-ov.4: DoD's five tenets are threat-operational, NIST's seven tenets are architectural

**Source:** [[DoD ZT Reference Architecture — Overview and Strategy]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

ZT has five major tenets that "represent the foundational elements and influence all aspects within ZT":

1. **Assume a Hostile Environment.** "There are malicious personas both inside and outside the environment. All users, devices, applications, environments, and all other NPEs are treated as untrusted."

2. **Presume Breach.** "Consciously operate and defend resources with the assumption that an adversary has presence within your environment. Enhanced scrutiny of access and authorization decisions to improve response outcomes."

3. **Never Trust, Always Verify.** "Deny access by default. Every device, user, application/workload, and data flow are authenticated and explicitly authorized using least privilege, multiple attributes, and dynamic cybersecurity policies."

4. **Scrutinize Explicitly.** "All resources are consistently accessed in a secure manner using multiple attributes (dynamic and static) to derive confidence levels for contextual access to resources."

5. **Apply Unified Analytics.** "Apply unified analytics for Data, Applications, Assets, Services (DAAS) to include behavioristics, and log each transaction."

## Evidence

Compare to NIST's seven tenets (see [[NIST 800-207 — Ch2 — Zero Trust Basics]]). NIST's tenets describe what a ZT architecture *does* — consider all data sources as resources, secure all communication, grant per-session access, use dynamic policy, monitor all assets, enforce strict authentication, collect telemetry. DoD's tenets describe what a ZT operator *assumes and does* — assume the environment is hostile, presume you're already breached, never trust, scrutinize everything, apply analytics.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. The difference in framing is consistent and intentional. DoD's tenets 1 and 2 ("Assume Hostile Environment," "Presume Breach") have no NIST equivalent. DoD's tenet 5 ("Apply Unified Analytics") has no direct NIST equivalent (NIST's tenet 7 is about collecting information, not applying analytics). The overlap is in tenets 3 and 4, which map to NIST's tenets 2-6.

## Stakes

If ZT is defined by NIST's architectural tenets, the focus is on building a policy engine. If defined by DoD's operational tenets, the focus is on threat hunting and continuous monitoring. Both are necessary, but the emphasis determines resource allocation.

## Disagreement

**Who disagrees:**

NSA's three guiding principles ("Never Trust, Always Verify"; "Assume Breach"; "Verify Explicitly") align more closely with DoD's tenets — unsurprising, as NSA co-authored both documents. CISA's maturity model is tenet-agnostic — it measures capabilities, not adherence to any specific tenet set.

**Alternative reading:**

The DoD's five tenets could be seen as a *subset* of NIST's seven, repackaged for operational audiences. But tenets 1 and 2 ("Assume Hostile Environment," "Presume Breach") add an adversarial framing that NIST deliberately avoids — NIST's "minimize uncertainty" is risk-management language, not threat-operational language.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The DoD's five tenets are better for briefing commanders. NIST's seven tenets are better for briefing architects. Both sets are correct; they describe the same thing from different perspectives. The CISA maturity model synthesizes both by measuring capability maturity against a threat-informed baseline.
