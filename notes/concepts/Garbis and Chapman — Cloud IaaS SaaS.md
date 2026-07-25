---
tags:
  - source/books
  - garbis-chapman
  - zt-cloud
  - zt-iaas
  - zt-saas
  - zt-architecture
  - oskg-zerotrust
created: 2026-07-24
confidence: high
source:
  title: "Zero Trust Security: An Enterprise Guide"
  authors: "Jason Garbis, Jerry W. Chapman"
  year: 2021
  publisher: "Apress"
  local_file: "sources/books/_txt/Zero_Trust_Security_An_Enterprise_Guide.txt"
  lines: "Ch14: 6102–6468, Ch15: 6468–6700"
related:
  - "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
  - "[[Concepts Index]]"
claims_status: extracted
claims_extracted: 2026-07-24
  - topic/zt-cloud
  - topic/zt-network
  - topic/zt-implementation
---

# Garbis & Chapman — Ch14–15: Cloud IaaS, PaaS, and SaaS

How Zero Trust applies to cloud infrastructure and SaaS applications. Garbis & Chapman argue that IaaS/PaaS platforms are highly integrable with ZT via simple source IP restrictions at the cloud boundary, while SaaS requires a lighter-touch approach since the apps are public-by-design. The chapter introduces service meshes as natural ZT microsegmentation systems and situates ZT within the converging SASE/ZTE market landscape.

---

**Claim 1 —** IaaS/PaaS security hasn't kept pace with IaaS/PaaS adoption → [[iaaspaas-security-hasnt-kept-pace-with-iaaspaas-adoption]]

---

**Claim 2 —** The PEP works best at the cloud boundary — source IP restrictions are the enabling primitive → [[the-pep-works-best-at-the-cloud-boundary]]

---

**Claim 3 —** Service meshes are self-contained Zero Trust microsegmentation systems → [[service-meshes-are-self-contained-zero-trust-microsegmentation-systems]]

---

**Claim 4 —** Zero Trust does fewer things for SaaS — but what it does is still valuable → [[zero-trust-does-fewer-things-for-saas-but]]

---

**Claim 5 —** SASE/ZTE converges networking and security, but ZTNA (ingress) is architecturally distinct → [[sasezte-converges-networking-and-security-but-ztna-ingress]]

---

**Claim 6 —** The future of ZT + SaaS is identity providers as authorization centers, not just authentication points → [[the-future-of-zt-saas-is-identity-providers]]

---

## Chapter 14–15 Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| IaaS/PaaS security hasn't kept pace with adoption | HIGH | CSP-native ZT services closing the gap since 2021 |
| PEP at cloud boundary via source IP restrictions | VERY HIGH | API-gateway or service-mesh alternatives for specific use cases |
| Service meshes as self-contained ZT microsegmentation | HIGH | All-in-one ZTNA platforms that make meshes redundant |
| ZT does fewer things for SaaS — but what it does matters | HIGH | CASB/SWG vendors arguing their approach is sufficient without ZT |
| ZTNA is architecturally distinct within SASE | HIGH | Browser-based ZTNA eliminating need for local PEPs |
| IdPs as authorization centers | MODERATE | Application-first authorization models (OPA, Zanzibar) |

**Strongest sections:**
- The PEP-at-cloud-boundary pattern (Ch14) — the most actionable guidance in either chapter, directly implementable with any CSP and any ZTNA product.
- The honest assessment of ZT's limitations for SaaS (Ch15) — prevents overclaiming and gives practitioners a clear mental model for where ZT fits in the SaaS security stack.

**Weakest sections:**
- The "fog computing" discussion is a throwaway that hasn't materialized as predicted.
- The SASE/ZTE discussion is marketing-landscape commentary rather than architectural analysis — useful context but lower information density than the rest.

**Unique contribution to OSKG-ZeroTrust:**
These chapters provide the *cloud-specific* bridge between ZT abstract architecture (NIST 800-207 Ch3–4) and practical implementation. Where NIST describes deployment *models*, Garbis & Chapman describe deployment *mechanics* — the specific integration pattern (source IP allowlisting) that makes cloud ZT work. The service mesh analysis connects ZT microsegmentation to the Kubernetes/cloud-native ecosystem, and the SaaS analysis provides an honest assessment that no other source in the corpus matches in clarity.
