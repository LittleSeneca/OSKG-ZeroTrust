---
tags:
  - source/books
  - gilman-barth
  - zt-application
  - zt-traffic
  - zt-mtls
  - zt-build
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
  lines: "L4192–6167"
related:
  - "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
  - "[[NIST 800-207 — Ch5 — Threats]]"
  - "[[CISA ZTMM — Device Network App Data Pillars]]"
  - "[[NSA — Device Pillar]]"
  - "[[NSA — Network Environment Pillar]]"
  - "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
  - "[[Concepts Index]]"
note_type: combined
justification: >
  Applications and traffic trust are operationally adjacent — apps produce traffic,
  traffic carries app data. Combining highlights the provenance-to-packet trust chain:
  from signed source code through build pipelines to mutually authenticated TLS/IPsec
  flows carrying that same application's data in production.
---

# Gilman & Barth — Ch7–8: Trusting Applications and Trusting the Traffic

These two chapters form a continuous argument: trust must flow from the developer's keyboard all the way to the network packet. Chapter 7 establishes the application provenance chain (source → build → distribution → execution). Chapter 8 secures what those applications produce — network traffic — through encryption, authentication, and filtering. Together they answer: _how do you know the application talking on your network is the one you built, and how do you know its traffic hasn't been tampered with?_

## Ch7: Trusting Applications

### Claim 1: The application pipeline is a cryptographic chain — break any link and trust is lost

**Authors' claim:** Establishing trust in code requires that the people producing it are trusted, the code was faithfully processed into a trustworthy application, trusted applications are faithfully deployed, and running applications are continuously monitored. This forms a four-phase pipeline: source code → build/compilation → distribution → execution.

**Evidence presented:** The build pipeline is compared to military supply chain security. The infamous 2007 Israeli airstrike on Syria — where Syrian radar systems failed, widely believed due to a hardware kill switch in a commercial chip — demonstrates that subversion anywhere in the chain can have catastrophic operational effects.

**Confidence:** HIGH. Every modern DevSecOps framework (SLSA, SSDF, in-toto) operationalizes this exact chain. The four phases map directly to the software supply chain security frameworks that emerged after this book's publication.

**What's at stake:** If you can't cryptographically validate every step, you're playing whack-a-mole. An attacker who compromises a CI/CD system can inject malicious code into signed binaries, and production systems would validate the signature without ever knowing the binary was poisoned. The signature becomes a false guarantee.

**Who disagrees:** No serious security framework disputes the pipeline concept. The disagreements are about _which links matter most_. NSA's device pillar emphasizes supply chain integrity artifacts (SBOM, RIM, TPM certificates) from procurement onward — extending the chain _before_ Gilman & Barth's source code phase. NIST's SSDF frames it as a software development lifecycle rather than a pipeline, adding organizational governance dimensions.

**Cross-reference — NSA Device Pillar: The procurement prequel.** NSA extends the trust chain backward: before source code reaches the build system, the _device_ that will run the build server must have verifiable supply chain provenance (TPM Platform Certificate, Reference Integrity Manifest). This adds a hardware root of trust that Gilman & Barth only hint at when they note "host security is still important."

**Cross-reference — CISA ZTMM Application Pillar: Maturity progression.** CISA operationalizes this pipeline as a maturity model. At Traditional maturity, application security testing is pre-deployment and manual. At Optimal, testing is integrated throughout the entire SDLC with automated continuous testing of deployed applications. CISA's Application pillars map the pipeline stages Gilman & Barth describe to measurable organizational capabilities.

**My assessment:** This claim is the book's most forward-looking contribution. Published in 2017 — three years before the SolarWinds attack made supply chain security a national emergency — it identified the build pipeline as the critical trust boundary. The SolarWinds attack (2020, cited by CISA's Emergency Directive 21-01) exploited exactly the gap Gilman & Barth describe: a compromised build system produced signed, trusted binaries distributed to thousands of customers. The authors were ahead of their time.

---

### Claim 2: Git's content-addressable storage provides tamper-proof history but not authenticity — signed commits bridge the gap

**Authors' claim:** Git stores source history as a Merkle tree (DAG of commits, each referencing ancestor commits by cryptographic hash). This prevents undetectable modification of history — any change to a commit changes its hash and all descendant hashes, which distributed contributors would notice. However, this guarantees _integrity_, not _authenticity_ — anyone with push access can add commits or forge author metadata. GPG-signed commits and tags solve this by cryptographically binding identity to contributions.

**Evidence presented:** A malicious committer can put whatever details they want in the author field — including impersonating Linus Torvalds on GitHub. Signed commits make impersonation impossible without stealing the developer's GPG key. Build systems can then validate the signed history before compiling, closing the authentication gap.

**Confidence:** VERY HIGH. This is the operational foundation of every modern CI/CD system. Signed commits are standard practice in mature organizations and are required by frameworks like SLSA Level 2+.

**What's at stake:** Without signed commits, build systems authenticate _nothing_ about who wrote the code. A compromised developer account or a CI misconfiguration can inject malicious code that looks identical to legitimate contributions. The chain of trust from human to machine breaks at the very first link.

**Who disagrees:** No one disagrees that signed commits are good. The disagreement is about _when_ they're necessary — some argue that for internal-only code with strong access controls, codified code review processes provide sufficient assurance. GitLab's and GitHub's protected branch + merge request workflows are often treated as a practical substitute for universal commit signing.

**My assessment:** The authors make a subtle point that's easy to miss: in a brownfield repository that transitions to signed commits, the first signed commit _endorses all prior unsigned history_. This is a powerful, pragmatic insight — you don't need to rewrite history to start signing today. It's also a liability: that first signature inherits all the unknown risk of everything that came before.

---

### Claim 3: The build system is the most dangerous attack vector — it sits between two cryptographically protected states with no protection of its own

**Authors' claim:** Source code can be signed. Build artifacts can be signed. But the build process itself — the function applied between input and output — is generally not protected cryptographically. A compromised build system can inject malicious code during compilation, producing a signed binary that downstream systems validate as trusted while containing attacker-controlled logic.

**Evidence presented:** The visual representation (Figure 7-3) shows the break in the chain: signed source → [unprotected build] → signed artifact. Without the right processes, subversion of this kind can be "difficult or impossible to detect." Reproducible builds are presented as the best available defense: if multiple parties can produce bit-for-bit identical binaries from the same source, build system compromise becomes detectable.

**Confidence:** HIGH. The SolarWinds attack (2020) proved this empirically — attackers compromised the build environment itself, and the signed Orion updates were trusted by customers. Reproducible builds remain aspirational for most organizations but are the gold standard (Debian, Bitcoin Core, Tor Browser all support them).

**What's at stake:** This is the architectural vulnerability that makes supply chain attacks so devastating. When a build system is compromised, the attack inherits all the trust of the organization's code signing infrastructure. Detection is nearly impossible at the consumer end because the artifact appears valid.

**Who disagrees:** NSA's device pillar argues that securing the build _host_ (TPM attestation, measured boot, firmware integrity) can prevent this class of attack before it reaches the reproducible build stage. Google's SLSA framework takes a complementary approach — multiple levels of build provenance requirements rather than relying solely on reproducibility.

**My assessment:** The authors correctly identify this as the weakest link, but their proposed solution (reproducible builds) is difficult to adopt at scale. The ecosystem has since evolved: SLSA, in-toto, and Sigstore provide build provenance attestations that are lighter-weight than full reproducibility while still providing meaningful guarantees. The core insight — that the build process needs its own integrity protection — remains correct and under-addressed in most organizations.

---

### Claim 4: Immutable artifacts with decoupled version numbers prevent masquerade attacks

**Authors' claim:** Build artifacts should have Write Once Read Many semantics. The version number communicated to users should be decoupled from the immutable build identifier. A separate distribution/promotion system maps release versions to build artifacts, enabling immutable builds without sacrificing semantic versioning. Once a version is released, it cannot be changed — a new build artifact with a new version must be produced instead.

**Evidence presented:** The Firefox release version 51.0.1 retains a separate build ID in the package name (Figure 7-4). APT repositories use a chain of signed hashes — Release file signed with private key → hash of Packages index → hashes of individual packages. The maintainer signs the Release file; consumers validate the entire chain.

**Confidence:** HIGH. This is standard practice in mature package ecosystems (APT, RPM, Docker registries, npm with integrity hashes). The pattern is battle-tested.

**What's at stake:** Without immutable artifacts, an attacker who compromises a distribution server can replace a "good" build with a "bad" one under the same version label. Consumers pulling the latest version have no way to detect the swap.

**Who disagrees:** No one disagrees with immutability. The tension is between the authors' strict "never republish a version" stance and real-world practice where minor fixes are sometimes re-released under the same version (Docker `latest` tags, npm unpublish/republish, rolling release distros). The industry has largely moved to content-addressed artifacts (container image digests, Git commit SHAs as version identifiers) which solve the same problem differently.

**Cross-reference — NSA Device Pillar: Distribution trust.** NSA's device pillar extends distribution trust to the hardware level: firmware updates must be signed, TPM measurements compared against SBOM/RIM, and the entire update chain validated from firmware through OS to application. This is Gilman & Barth's distribution chain applied to the device foundation.

**My assessment:** The distinction between build versions and release versions is operationally critical but widely misunderstood. Most teams conflate the two. The authors provide a clean mental model: the build system produces immutable artifacts identified by build number; the release system chooses which artifact to promote. This separation of concerns is the right architecture.

---

### Claim 5: Per-instance time-bound secrets are the mechanism for authorizing running applications

**Authors' claim:** Knowing what's running in your infrastructure requires that every running instance be individually authorized. This authorization can be implemented through per-instance secrets with defined lifetimes. By generating a unique secret for each deployed instance and attaching a lifetime, you assert that you know precisely what's running because you know how many secrets you generated, who you gave them to, and when they expire.

**Evidence presented:** HashiCorp Vault's response wrapping feature: the deployment system notifies Vault to expect a new instance, Vault provisions unique time-bound credentials, and the application retrieves them using a one-time token injected during deployment. If an instance goes rogue, its credentials expire and it can no longer operate.

**Confidence:** HIGH. This is the foundation of modern service identity (SPIFFE/SPIRE, Istio workload identity, AWS IAM roles with session tokens). The pattern has become industry standard.

**What's at stake:** Without per-instance, time-bound credentials, you can't distinguish between authorized instances and rogue ones. A compromised host could continue operating indefinitely with stolen long-lived credentials.

**Who disagrees:** The debate has moved from "should we do this" to "how should we do this." SPIFFE/SPIRE uses X.509 SVIDs with short lifetimes (typically 1 hour). Cloud IAM uses session tokens. The authors' Vault example is one implementation among many now.

**My assessment:** This claim connects the application pipeline to the traffic chapter: the secrets provisioned here (often X.509 certificates or API keys) are exactly what Chapter 8's mutually authenticated TLS and IPsec will use to authenticate network flows. The deployment system is the bridge between "this is an authorized application instance" and "this is an authorized network flow."

---

### Claim 6: Runtime security completes the trust lifecycle — isolation, secure coding, and active monitoring

**Authors' claim:** Deploying an authorized application is not enough. It must remain trustworthy throughout its lifecycle. Three defenses are required: (1) application isolation (constraining CPU, memory, network, filesystem, system calls), (2) secure coding practices (injection prevention, automated analysis, fuzzing), and (3) active monitoring (continuous scanning in production, automated response to strong signals).

**Evidence presented:** Isolation can be achieved through virtualization (stronger, more resource-intensive) or shared kernel environments/containers (lighter weight). Fuzzing and injection scanning should run continuously in production — not just pre-deployment. Active response systems should have fail-safes (e.g., "don't eject a host if the cluster is already dangerously small"). Applications can monitor peer applications for behavioral anomalies.

**Confidence:** MODERATE. Each individual practice is well-supported, but the claim that these three together _complete_ the trust lifecycle is aspirational. Real-world incident data shows that runtime attacks frequently succeed despite isolation, secure coding, and monitoring.

**What's at stake:** If runtime security is weak, the entire pipeline's investment is wasted. A perfectly built, perfectly distributed application that gets compromised at runtime is indistinguishable from a malicious application from the network's perspective — it produces valid traffic using valid credentials.

**Who disagrees:** Google's BeyondProd model argues that runtime security in a zero trust environment requires a fundamentally different architecture — service-to-service authentication at the application layer rather than host-level isolation alone. The authors acknowledge this implicitly in their discussion of application monitoring applications.

**Cross-reference — CISA ZTMM Application Pillar: Maturity in runtime.** CISA's Application pillar defines runtime security maturity: from manual pre-deployment testing (Traditional) to automated continuous testing of deployed applications (Optimal). The Advanced and Optimal levels incorporate exactly the active monitoring the authors advocate — automated application security monitoring, integration throughout the SDLC, and continuous optimization.

**My assessment:** This claim is the most aspirational in the chapter. The authors correctly identify the components, but the gap between "run a fuzzer in CI" and "applications monitor each other's behavioral health" is enormous. Most organizations are still at the Traditional/Initial CISA maturity levels for runtime application security.

---

## Ch8: Trusting the Traffic

### Claim 7: Encryption and authentication are separate concerns — zero trust requires authenticity; encryption comes "for free"

**Authors' claim:** Encryption ensures confidentiality (only the receiver can read the data). Authentication enables validation that the message was sent by the claimed sender and is unaltered (integrity). All transport protocols discussed in the book provide both, so encryption is attained "for free," leaving few good reasons to exclude it. However, encryption without authentication is dangerous — an attacker can forge messages or replay previous valid ones.

**Evidence presented:** Architecture diagrams showing encryption only at certain network boundaries (between sites but not within the datacenter) are characterized as a "direct contradiction of the zero trust architecture" because they create privileged zones. The authors argue systems that truly do not require confidentiality are rare.

**Confidence:** VERY HIGH. This is cryptographic orthodoxy — "encryption without authentication is dangerous" is a near-universal principle in modern protocol design. TLS 1.3 mandates authenticated encryption. The Noise protocol framework eliminated cipher suite negotiation entirely in favor of fixed authenticated constructions.

**What's at stake:** If you accept encryption without authentication, you get the worst of both worlds: the overhead of encryption with none of the trust guarantees. An attacker can modify ciphertext and the receiver processes it without validation.

**Who disagrees:** The "encryption comes for free" claim is slightly too strong. Encryption adds computational overhead and operational complexity (key management, packet capture blind spots, latency). Some high-frequency trading and real-time systems legitimately cannot tolerate the latency. But for the vast majority of use cases, the authors are correct.

**Cross-reference — NIST 800-207 Ch5: The DoS angle.** NIST notes that ZT policy engines can use expected traffic patterns to calculate coarse enforcement rules for upstream filtering devices. This is relevant because the encryption/authentication the authors advocate is computationally expensive — filtering out malicious traffic _before_ it reaches the authentication layer reduces the DoS attack surface.

**Cross-reference — NSA Network Pillar: Encryption requirements.** NSA specifies that API calls must be secured using encrypted protocols (TLS v1.2+, SSH v2+) with mutual authentication (client and server certificates). This aligns exactly with the authors' position: authenticity through mutual authentication, encryption as the default.

**My assessment:** This claim is deceptively important. The distinction between "we encrypted the traffic" and "we mutually authenticated the traffic" is the difference between perimeter thinking and zero trust thinking. Perimeter networks encrypt at boundaries and trust traffic within. Zero trust networks mutually authenticate every flow regardless of location.

---

### Claim 8: The first packet problem is solved by Single Packet Authorization (SPA)

**Authors' claim:** Complex authentication systems like TLS have large attack surfaces. The first packet problem — how to allow only trusted connections without answering a single unauthenticated packet — is mitigated by pre-authentication: encrypting/signing a small piece of data and sending it as a UDP packet. The receiver passively listens; only upon receiving a properly encrypted pre-authentication packet does it open a tightly scoped, short-lived firewall rule for the sender.

**Evidence presented:** fwknop is presented as the reference implementation. It supports AES (symmetric) and GnuPG (asymmetric) encryption, optionally adds HMAC to prevent ciphertext tampering, and creates firewall rules scoped to the sender's IP, destination port, and optionally source port — rules that expire after a configurable period (default 30 seconds). The seven mandatory fields in the SPA payload include random data, username, timestamp, version, message type, access request, and SHA-256 digest.

**Confidence:** MODERATE. SPA is a sound cryptographic concept but has seen limited production adoption outside niche security-focused deployments. fwknop is maintained but far from ubiquitous. Modern ZTNA products achieve similar goals through different mechanisms (outbound-only connections to an access proxy that never exposes listening ports).

**What's at stake:** Without SPA or equivalent, every exposed TLS service is a public attack surface. Attackers can probe, fingerprint, and exploit TLS implementation vulnerabilities without ever authenticating. SPA hides the service — it's invisible until you prove you should be allowed to see it.

**Who disagrees:** Most commercial ZTNA products (Zscaler, Cloudflare Access, Google BeyondCorp) solve the same problem differently: the application is never directly exposed to the internet. Clients connect to an access proxy, which authenticates before forwarding. This proxy-based approach achieves the same "hide the service" property without SPA's protocol-level complexity.

**My assessment:** SPA is elegant but has been largely superseded by architectural patterns (ZTNA access proxies, software-defined perimeter controllers). The concept — don't answer packets from untrusted sources — remains fundamental. The implementation has evolved. For a 2017 book, SPA was ahead of the curve; in 2026, the proxy model has won.

---

### Claim 9: TLS and IPsec serve different roles — mTLS for client/server, IPsec for server/server datacenter

**Authors' claim:** TLS lives at the application layer (OSI 5–6), is protocol-dependent (TCP, with DTLS for UDP), and requires applications to support client certificate presentation. IPsec lives at the internet layer (OSI 3), is implemented in the kernel, and secures _all_ IP traffic "for free" from the application's perspective. The pragmatic recommendation: mutually authenticated TLS for client/server interactions (browsers presenting client certificates to access proxies), IPsec for server/server datacenter communication.

**Evidence presented:** IPsec's advantages — kernel-level implementation, protocol-agnostic (handles TCP, UDP, ICMP, anything over IP), no application awareness needed. IPsec's disadvantages — complex configuration, network support issues (AWS blocks ESP/AH, public hotspots often block IPsec), device support variability, slow cipher suite progression. mTLS advantages — universal support, mature ecosystem, browser-native client certificates. mTLS disadvantages — protocol-dependent, requires application configuration, library fragmentation across languages.

**Confidence:** HIGH. The pragmatic split has held up remarkably well. Service meshes (Istio, Linkerd) operationalize mTLS for server-to-server in cloud-native environments, while IPsec remains the backbone of site-to-site VPNs and some government/military deployments. The authors' recommendation for Windows environments (Microsoft Server Isolation via Active Directory + Group Policy + IPsec) is exactly the path many enterprises took.

**What's at stake:** If you pick the wrong protocol for your environment, you'll either fail to deploy (IPsec in heterogeneous client environments) or fail to secure (TLS without mutual authentication in server-to-server flows). The split recommendation is operationally critical.

**Who disagrees:** The service mesh movement argues that mTLS at the application layer is sufficient and preferable for server-to-server in cloud-native environments — IPsec's kernel-level integration is less valuable when orchestrators manage the entire network stack. Google's BeyondCorp/BeyondProd model uses application-layer identity (not network-layer) for all communication.

**Cross-reference — NIST 800-207 Ch4: BeyondCorp → BeyondProd.** NIST's deployment scenarios reference Google's BeyondProd, which extends the BeyondCorp model to service-to-service communication in cloud-native environments using mutual TLS between services, workload identity rather than network identity, and continuous trust evaluation at the service boundary. This is the modern evolution of the authors' server-to-server recommendation.

**My assessment:** The authors' TLS/IPsec split was prescient but the landscape has shifted. Service meshes have made mTLS the dominant server-to-server protocol in cloud-native environments, with IPsec increasingly relegated to network infrastructure (site-to-site tunnels, government classified networks). The core insight — that you need different tools for different contexts — remains correct. The authors' recommendation for Windows shops (Microsoft Server Isolation) is still the pragmatic answer for Active Directory-centric enterprises.

---

### Claim 10: Cipher suite negotiation is an anti-pattern — newer protocols eliminate it

**Authors' claim:** TLS cipher suite negotiation, where the client presents ordered preferences and the server chooses, limits overall security to "the strongest negotiable cipher suite of the weakest client." This opens downgrade attacks. Newer protocols like Noise eliminate negotiation entirely, and the authors "look forward to widespread adoption of cryptographic protocols which lack weaknesses such as this one."

**Evidence presented:** Historical attacks against cipher suite negotiation, particularly downgrade attacks. The recommendation: servers should support only the strongest reasonable cipher suites. In datacenter deployments with strict client control, this can be limited to a few approved suites. The key exchange preference ordering: ECDHE > DHE > RSA (RSA lacks perfect forward secrecy). For authentication: RSA remains recommended despite ECDSA being technically superior, because of concerns about compromised elliptic curve constants. For bulk encryption: AES is the universal recommendation.

**Confidence:** HIGH on the weakness. MODERATE on the predictions. TLS 1.3 (finalized 2018, one year after this book) dramatically reduced negotiation surface by removing obsolete cipher suites and mandating AEAD. The Noise framework exists but is niche relative to TLS. The prediction has partially materialized — not through Noise adoption but through TLS protocol simplification.

**What's at stake:** Downgrade attacks are real and dangerous. If your server supports weak cipher suites for backward compatibility, an active attacker can force the client to use them. The authors' recommendation to curate server-side cipher suites aggressively is operationally correct.

**Who disagrees:** The practical tension is between security and compatibility. The authors acknowledge this: in true client-facing deployments, supporting only the strongest suites may block legitimate users. The balance they recommend — strict control in datacenters, pragmatic breadth for public-facing services — is sound.

**My assessment:** This claim has aged well in its diagnosis and somewhat well in its prediction. TLS 1.3 fixed the negotiation problem not by eliminating it but by constraining it to a small set of strong options. The authors' enthusiasm for Noise hasn't translated to mainstream adoption, but the spirit of the recommendation — aggressive cipher suite curation — is now standard practice.

---

### Claim 11: TLS should be separated from applications via a local daemon — not embedded in application libraries

**Authors' claim:** Historically, applications speak TLS directly by loading shared libraries. This creates fragmentation: different languages, different library versions, inconsistent configurations, and difficulty enforcing the latest cipher suites. The solution: a local TLS daemon that handles all TLS duties, brokers connections, and forwards decrypted traffic locally. This centralizes configuration and ensures all applications receive consistent TLS protection.

**Evidence presented:** The library-based approach seems more attractive initially (turnkey solution, built-in support), but in practice presents "quite a bit of hidden complexity." Applications frequently support server TLS but neglect to expose client certificate configuration required for mutual authentication. System administrators need to adjust configuration in response to vulnerabilities, and finding application-specific settings across a large fleet hampers rapid response.

**Confidence:** HIGH. This is the service mesh sidecar pattern, now dominant in cloud-native deployments. Istio's Envoy sidecar, Linkerd's proxy, and Consul Connect all implement exactly this architecture — a local daemon that handles mTLS independently of the application.

**What's at stake:** Without a local TLS daemon, every application team must implement and maintain TLS correctly. Given the complexity of TLS configuration (cipher suites, certificate rotation, mutual auth, protocol version negotiation), this is a recipe for widespread misconfiguration.

**Who disagrees:** The counter-argument is that the sidecar adds operational complexity (another process to manage, debug, and monitor) and latency (an extra hop, even if local). Some argue that TLS should be the application's responsibility because it enables finer-grained authorization decisions. The authors anticipate this: they note that the local daemon approach "looks very similar to the IPsec model, but implemented using TLS instead."

**Cross-reference — NIST 800-207 Ch4: Service mesh as ZT implementation.** NIST's BeyondProd reference documents exactly this pattern: mTLS between services, workload identity rather than network identity, continuous trust evaluation at the service boundary. The local TLS daemon is the enforcement point for service-to-service zero trust.

**My assessment:** This claim was arguably the most influential architectural recommendation in the chapter. The service mesh pattern — a local proxy handling mTLS, traffic policy, and observability — became the dominant cloud-native security architecture. The authors didn't invent sidecars, but they articulated the security rationale for separation of TLS duties from application code with clarity and foresight.

---

### Claim 12: Three types of filtering form a defense-in-depth network security architecture

**Authors' claim:** Filtering in zero trust operates at three levels: (1) **Host filtering** — every endpoint filters its own traffic via on-host firewalls (iptables, BPF, Windows Firewall). (2) **Bookended filtering** — egress filtering is applied alongside ingress, so both sender and receiver enforce policy, providing "herd immunity" against misconfiguration. (3) **Intermediary filtering** — network devices between endpoints (perimeter devices, SDN fabric) apply additional filtering, particularly for high-volume attack traffic that would overwhelm software firewalls if it reached the host.

**Evidence presented:** Host filtering: all modern OSes include firewalls (except iOS and Android, which the authors note as a gap). Bookended filtering example: a database server's ingress rules are accidentally loosened by an administrator. If application servers also have egress rules that only allow connections to the database, the misconfiguration is contained. Intermediary filtering: EC2 Security Groups implement filtering outside the VM for isolation (Figure 8-9). Project Calico demonstrates distributed host + bookended filtering at scale. UPnP is contrasted: unlike ZT-derived perimeter policies, UPnP allows _any_ application to reconfigure the perimeter without a chain of trust.

**Confidence:** HIGH. This three-tier filtering model is architecturally sound and operationally validated. Calico and similar CNI plugins implement host + bookended filtering. Cloud security groups implement intermediary filtering isolated from guest VMs.

**What's at stake:** Without all three filtering tiers, there are gaps. Host-only filtering means the network incurs cost to transport packets that are ultimately dropped, and a compromised host can disable its own firewall. Intermediary-only filtering is the perimeter model the authors spent Chapter 1 dismantling. Bookended filtering is the least common but provides the "herd immunity" property — it's the safety net for human error.

**Who disagrees:** The tension is between the authors' "start at the host and work outward" philosophy and traditional network engineering's "filter at the perimeter first" instinct. The authors explicitly address this: they don't throw out perimeter concepts, but they reorder the priority — host filtering is the foundation, intermediary filtering is an enhancement.

**Cross-reference — NSA Network Pillar: Granular traffic filtering.** NSA's Network pillar specifies microsegmentation based on application profiles and data flows, with continuous authentication of connectivity. At Advanced maturity, central management platforms provide automated visibility and security monitoring including alerting on anomalous behavior. This aligns with the authors' vision of programmable network fabric driven by application-aware policy.

**My assessment:** The three-tier model is the chapter's most durable architectural contribution. It resolves the false dichotomy between "firewalls are dead" (extreme ZT) and "just add more firewalls" (perimeter thinking). The correct answer: filtering everywhere, at every tier, with host filtering as the foundation and intermediary filtering as the optimization layer.

---

### Claim 13: Forwarding and routing authorization extends policy enforcement into the network fabric itself

**Authors' claim:** Zero trust networks leverage slowly changing details of the network to distribute enforcement. This opens the possibility of propagating enforcement into the network infrastructure: an SDN controller that only installs flow instructions based on strong authentication and authorization. A client signals the control plane with credentials, the request is authorized, and the network fabric is configured to allow only that specific flow.

**Evidence presented:** The observation that "filtering at every point" implies network devices themselves can be policy enforcement points, not just passive packet forwarders. The SDN controller model is presented as an ideal.

**Confidence:** MODERATE. The concept is sound and aligns with software-defined perimeter (SDP) architectures. However, practical deployment at scale remains limited. SDN-based security is deployed in some environments (VMware NSX, Cisco ACI with security groups) but is far from universal.

**What's at stake:** If the network fabric enforces policy, the attack surface shrinks dramatically. Malicious traffic never reaches the host — it's dropped by the first switch that knows the flow isn't authorized. This is the ultimate realization of "the network is hostile" — even the network infrastructure doesn't trust the traffic it carries.

**Who disagrees:** The debate is about where authorization logic should live. Application-layer proponents argue that authorization belongs at the application/service mesh layer because it has richer context. Network-layer proponents argue that pushing enforcement down reduces attack surface. The authors' SDN vision sits between these positions but hasn't seen widespread adoption.

**My assessment:** This is the chapter's most speculative claim. It's the logical endpoint of the filtering argument, but the operational complexity of tying SDN flow rules to application-level authorization has limited adoption. Service meshes achieve a similar goal at a different layer — the sidecar proxy is effectively a per-host SDN enforcement point. The vision is correct; the implementation layer has shifted.

---

## Synthesis: The Provenance-to-Packet Trust Chain

| Trust Stage | Ch7: Application | Ch8: Traffic | Cross-Reference |
|---|---|---|---|
| **Source** | Signed commits, code review | — | NSA Device: TPM-backed supply chain provenance |
| **Build** | Immutable artifacts, reproducible builds | — | CISA App: Integrated SDLC testing maturity |
| **Distribution** | Signed manifests, APT hash chain, promotion | — | NSA Device: Signed firmware update chains |
| **Deployment** | Per-instance time-bound secrets (Vault) | First packet: SPA hides the service | NIST Ch4: BeyondProd workload identity |
| **Execution** | Isolation, secure coding, active monitoring | mTLS/IPsec: authenticated encryption for all traffic | CISA App: Runtime monitoring maturity |
| **Network filtering** | — | Host + bookended + intermediary filtering | NSA Network: Microsegmentation, application profiles |
| **Network fabric** | — | SDN routing authorization | NIST Ch4: BeyondCorp access proxy architecture |

**Key insight:** These two chapters together describe a single continuous argument that the industry has since operationalized as distinct, complementary layers. Chapter 7 is now "software supply chain security" (SLSA, SSDF, SBOM). Chapter 8 is now "zero trust network access" (ZTNA, service mesh, SDP). The book's genius is showing that they are two halves of the same problem: _you can't trust the traffic if you can't trust the application that produced it, and you can't trust the application if it can't prove its identity on the network._ The shared dependency is X.509 certificates — they authenticate both the application instance (Chapter 7's instance authorization) and the network flow (Chapter 8's mTLS/IPsec). The certificate is the bridge between the two trust domains.

---

## Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|---|---|---|
| 1. Application pipeline as cryptographic chain | HIGH | Gap between "cryptographic chain" and "build process integrity" |
| 2. Git tamper-proof history + signed commits | VERY HIGH | Practical adoption: most orgs still don't sign commits universally |
| 3. Build system as most dangerous attack vector | HIGH | SolarWinds vindicated this — but reproducible builds remain aspirational |
| 4. Immutable artifacts + decoupled versions | HIGH | Industry moved to content-addressed artifacts (container digests) |
| 5. Per-instance time-bound secrets for authorization | HIGH | SPIFFE/SPIRE has standardized this; cloud IAM does it natively |
| 6. Runtime security completes the lifecycle | MODERATE | Gap between "run a fuzzer" and "applications monitor each other" |
| 7. Encryption vs. authentication separation | VERY HIGH | Cryptographic orthodoxy; TLS 1.3 enforces AEAD |
| 8. SPA solves the first packet problem | MODERATE | ZTNA access proxies have largely superseded SPA in practice |
| 9. mTLS for clients, IPsec for servers pragmatic split | HIGH | Service mesh mTLS has captured server-to-server; IPsec niche |
| 10. Cipher suite negotiation as anti-pattern | HIGH (diagnosis) / MODERATE (prediction) | TLS 1.3 fixed negotiation; Noise remains niche |
| 11. Local TLS daemon (sidecar) for separation of duty | HIGH | Became the service mesh pattern; dominant cloud-native architecture |
| 12. Three-tier filtering model | HIGH | Architecturally sound; Calico/cloud security groups validate |
| 13. Forwarding/routing authorization via SDN | MODERATE | Conceptually correct; operational complexity limits adoption |

**Strongest sections:** Claims 1–5 (the build pipeline) and Claim 12 (three-tier filtering). These are not just correct — they're architectural frameworks that the industry has since built products around.

**Weakest section:** Claim 8 (SPA). Correct in principle but the implementation pattern (UDP pre-authentication packets) has been overtaken by ZTNA proxy architectures that achieve the same "hide the service" property without protocol-level complexity.

**Unique contribution to OSKG-ZeroTrust:** These chapters establish the missing link between "how ZT works on the network" (Chapters 1–6) and "how you build the software that runs on it." No other ZT source — not NIST, not NSA, not CISA, not DoD — provides a comparable end-to-end treatment of the provenance-to-packet trust chain. The certificate-as-bridge insight (instance identity → flow identity) is the conceptual hinge that connects application trust to traffic trust.
