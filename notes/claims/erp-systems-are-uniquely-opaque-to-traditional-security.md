---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-app
  - topic/zt-monitoring
  - topic/zt-implementation
  - topic/zt-access-mgmt
claim_id: "finney-ch4-7.2"
statement: "ERP systems are uniquely opaque to traditional security tools and require specialized solutions — but process changes matter more than technology purchases."
confidence: "high"
confidence_rationale: "HIGH. These findings map directly to real-world ERP security assessments and are consistent with industry reports. The five gaps enumerated in the"
claim_type: "implementation"
source_note: "[[Finney — Ch4-7 — Building the ZT Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch4-7.2: ERP systems are uniquely opaque to traditional security tools and require specialized solutions — but process changes matter more than technology purchases.

**Source:** [[Finney — Ch4-7 — Building the ZT Strategy]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"The internals of an ERP system are usually a blind spot for security teams."

## Evidence

Peng's assessment reveals five specific gaps:
1. **Specialized programming languages** (e.g., ABAP for SAP) are not supported by most security code review tools — vulnerabilities go undetected.
2. **ERP change control is manual** and not built into the ERP itself — separation of duties exists on paper but can be bypassed in code.
3. **Traditional vulnerability scanners** don't scan applications or code within ERP systems.
4. **Compliance management** (password standards, configurations, access controls) isn't native to ERP systems.
5. **Application logs** are not digestible by most SIEMs — SOC teams are blind to ERP activity.

Additionally: the ERP hadn't been patched in five years, real customer data was used in dev/test environments, superuser accounts proliferated, hard-coded passwords existed in the code, and a former developer's finance report was still being emailed to his personal Gmail account.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These findings map directly to real-world ERP security assessments and are consistent with industry reports. The five gaps enumerated in the chapter are specific enough to serve as an assessment checklist.

## Stakes

If these gaps aren't addressed, the ERP becomes an attacker's paradise — financial fraud, data exfiltration, and supply chain attacks (shipping treadmills to wrong addresses) are all possible without detection. The ERP is where "more ways to lose money than make it" exist.

## Disagreement

**Who disagrees:**

ERP vendors emphasize their built-in security features. The counterargument is that those features exist but require expertise to configure and maintain — expertise most organizations don't retain in-house.

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

The chapter's genius is in showing that Dylan doesn't just buy a tool and call it done. Aaron specifies a specialized ERP security solution but *also* requires process changes: weekly maintenance windows for patching (negotiated with finance), role cleanup, removal of hard-coded credentials, data masking in dev/test. The tool enables visibility; the process changes prevent recurrence. This is "process before technology" in action — Donna's line, which Finney has her explicitly praise.
