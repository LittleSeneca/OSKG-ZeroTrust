---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-device
  - topic/zt-encryption
  - topic/zt-identity
  - topic/zt-trust
claim_id: "gb-ch4-6.5"
statement: "Device identity requires binding software credentials to hardware"
confidence: "high"
confidence_rationale: "VERY HIGH. This is the consensus view across all frameworks. NSA's Device Pillar mandates TPM and secure boot at Basic maturity, PCR-based"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch4-6 — Authorization Devices Users]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch4-6.5: Device identity requires binding software credentials to hardware

**Source:** [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"Without a way to bind the software key to the hardware device it is attempting to identify, we cannot really call it device identity. TPMs solve this problem, providing the necessary binding."

## Evidence

The chapter systematically escalates through storage methods: (1) file permissions only (weakest — attacker with root can exfiltrate the key), (2) encrypted private key with passphrase (better but impractical for servers), (3) TPM/HSM storing private key in hardware that "never leaves the security module." TPM endorsement keys (EK) provide unique hardware identity. Platform Configuration Registers (PCRs) store hashes of boot chain software, enabling attestation that the system is "in an approved configuration."

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This is the consensus view across all frameworks. NSA's Device Pillar mandates TPM and secure boot at Basic maturity, PCR-based attestation at Intermediate, and SBOM/RIM integration at Advanced. DoD ZT RA requires device attestation as a core capability.

## Stakes

If X.509 certificates (software-based identity) are used without hardware binding, device identity is trivially compromised — steal the private key, impersonate the device. The TPM is the "linchpin between software identity and physical hardware."

## Disagreement

**Who disagrees:**

No one disagrees on the principle. The disagreement is about minimum bar: Gilman & Barth say TPM "should not be considered a requirement" and that "there are much lower-hanging fruits in terms of zero trust adoption and migration." NSA sets TPM as a firm requirement. This reflects a maturity vs. accessibility trade-off.

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

_Not addressed separately in the source note._
