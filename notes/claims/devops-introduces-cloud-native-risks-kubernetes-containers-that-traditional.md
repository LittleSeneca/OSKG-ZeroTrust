---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-cloud
  - topic/zt-app
claim_id: "finney-ch4-7.8"
statement: "DevOps introduces cloud-native risks (Kubernetes, containers) that traditional perimeter security cannot address — ZT provides the model for securing them."
confidence: "high"
confidence_rationale: "HIGH. Kubernetes default insecurity is well-documented. The specific controls mentioned (network segmentation, RBAC, runtime security, image"
claim_type: "implementation"
source_note: "[[Finney — Ch4-7 — Building the ZT Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch4-7.8: DevOps introduces cloud-native risks (Kubernetes, containers) that traditional perimeter security cannot address — ZT provides the model for securing them.

**Source:** [[Finney — Ch4-7 — Building the ZT Strategy]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"Kubernetes isn't secure at all by default. So we've done a lot already to make sure it's secure."

## Evidence

Boris enumerates Kubernetes security controls: network segmentation between clusters and workloads, isolation of control plane from data plane traffic, firewalls between control and data planes. Dylan adds: RBAC enabled and integrated with the (now-separated) identity system. They also discuss:
- **Runtime security**: detecting privileged containers, monitoring file access, audit trails of all commands/sessions
- **Container image integrity**: preventing compromised images from being deployed
- **Web Application Firewall (WAF)**: described as "a Band-Aid" — useful for blocking OWASP attacks and credential stuffing while vulnerabilities are being fixed, but not a substitute for secure code
- **Secrets management**: millions of API keys leaked annually via hard-coding; secret managers eliminate sharing over Slack/Teams/email

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Kubernetes default insecurity is well-documented. The specific controls mentioned (network segmentation, RBAC, runtime security, image scanning) align with the CNCF's security best practices and CIS benchmarks.

## Stakes

Cloud-native workloads are the fastest-growing attack surface. Organizations that apply perimeter-model thinking to cloud (firewall at the edge, trust everything inside) are structurally vulnerable. ZT's inside-out approach — treating each container and service as its own protect surface — is the correct model.

## Disagreement

**Who disagrees:**

Some argue that cloud providers' shared responsibility model shifts enough security to the provider that organizations don't need to implement Kubernetes-level controls themselves. The chapter implicitly rejects this: Boris and Dylan discuss controls at the Kubernetes layer, not relying on cloud provider defaults.

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

The DevOps chapter is where the ZT strategy starts to demonstrate compound returns. Because identity is now clean (separate domains, SSO, MFA, PAM), the DevOps pipeline can consume identity for every control decision. Because the ERP taught the team about protect surfaces, they can model the DevOps pipeline the same way. Each protect surface makes the next one easier — this is the ZT flywheel that Finney is quietly demonstrating across chapters.
