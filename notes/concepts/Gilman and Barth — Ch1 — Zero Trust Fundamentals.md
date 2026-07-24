---
tags:
  - source/books
  - gilman-barth
  - zt-fundamentals
  - zt-architecture
  - control-plane
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
confidence: high
source:
  title: "Zero Trust Networks: Building Secure Systems in Untrusted Networks"
  authors: "Evan Gilman, Doug Barth"
  year: 2017
  publisher: "O'Reilly Media"
  local_file: "sources/books/_txt/Zero_trust_networks_building_secure_systems_in_untrusted_networks.txt"
related:
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[CISA ZTMM — Overview and Framework]]"
  - "[[Books Index]]"
  - "[[Concepts Index]]"
claims_status: "extracted"
claims_extracted_date: 2026-07-24
claims_count: 4
claims_files:
  - "[[zt-five-fundamental-assertions]]"
  - "[[zt-control-data-plane-split]]"
  - "[[zt-perimeter-historical-accident]]"
  - "[[zt-phone-home-fatal-flaw]]"
---

# Gilman & Barth — Ch1: Zero Trust Fundamentals

The most important single chapter in Zero Trust literature from an implementation perspective. This is where the control plane / data plane architecture — the dominant implementation model — is first fully articulated.

**Claim 1 —** The five fundamental assertions define ZT operationally, not abstractly → [[zt-five-fundamental-assertions]]

**Claim 2 —** The control plane / data plane split is ZT's fundamental architectural innovation → [[zt-control-data-plane-split]]

**Claim 3 —** The perimeter model's history reveals why it failed — it was an accident, not a design → [[zt-perimeter-historical-accident]]

**Claim 4 —** The phone-home attack pattern is perimeter security's fatal flaw → [[zt-phone-home-fatal-flaw]]

## Chapter 1 Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| Five fundamental assertions | HIGH | Being too network-centric for data/identity-focused ZT |
| Control plane / data plane split | VERY HIGH | Centralization as single point of failure/attack |
| Perimeter model as historical accident | HIGH | Defense that perimeter was deliberate and appropriate for its time |
| Phone-home as perimeter's fatal flaw | HIGH | Outbound filtering proponents arguing it's solvable |

**Strongest section:** The control plane / data plane architecture introduction. This is the conceptual DNA of every subsequent ZT implementation.

**Weakest section:** The historical narrative, while pedagogically effective, is longer than necessary and occasionally indulgent. The key insight (perimeter security was a side effect of NAT, not a design) could be stated in half the space.

**Unique contribution to OSKG-ZeroTrust:** This chapter provides the implementation-level architectural vocabulary (control plane, data plane, policy engine) that NIST 800-207 abstracts and that the government standards don't provide. It's the bridge between "what is ZT" (NIST) and "how do I build it" (BeyondCorp papers, Green-Ortiz case studies).