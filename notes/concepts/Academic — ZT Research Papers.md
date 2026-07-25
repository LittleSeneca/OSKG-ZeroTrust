---
tags:
  - source/papers
  - academic
  - zt-research
  - zt-empirical
  - oskg-zerotrust
  - type/reading-note
created: 2026-07-24
related:
  - "[[Concepts Index]]"
  - "[[../Notes Index]]"
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
  - "[[CISA ZTMM — Overview and Framework]]"
  - "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
sources:
  - title: "Zero Trust Architecture Implementation in Enterprise Networks"
    author: "Dotse, Sebuabe, Obeng, Abudu, Pappoe"
    year: 2025
    journal: "International Journal of Computer Applications (IJCA)"
    local_file: "sources/papers/_txt/ZT_Enterprise_Implementation_IJCA_2025.txt"
  - title: "Dissecting Zero Trust: Research Landscape and Its Implementation in IoT"
    author: "Liu, Tan, Wu, Feng, Jin, Zhang, Liu, Liu"
    year: 2024
    journal: "Cybersecurity (Springer Open)"
    local_file: "sources/papers/_txt/ZT_Dissecting_Research_Landscape_IoT_2024.txt"
  - title: "Automation and Orchestration of Zero Trust Architecture: Potential Solutions and Challenges"
    author: "Cao, Pokhrel, Zhu, Doss, Li"
    year: 2024
    journal: "Machine Intelligence Research (Springer)"
    local_file: "sources/papers/_txt/ZT_Automation_Orchestration_Springer_2023.txt"
claims_status: extracted
claims_extracted: 2026-07-24
---

# Academic — ZT Research Papers

Combined reading note synthesizing three academic papers that form the empirical evidence base for Zero Trust Architecture. These papers span empirical performance analysis, systematic bibliometric review of the research landscape, and AI-driven automation/orchestration of ZTA components. Together they constitute the strongest peer-reviewed evidence supporting (and qualifying) the practitioner claims found in the standards and book corpus.

---

## 1. Dotse et al. (2025) — Enterprise ZTA Implementation Effectiveness

**Source:** IJCA Vol. 187 No. 45, September 2025. University of Professional Studies / Valley View University / Wisconsin International University College, Ghana.

**Study design:** Four-phase mixed-methods analytical framework using validated synthetic data modeling across 300 enterprise instances (100 per phase × 3 phases) spanning finance (28%), technology (26%), healthcare (18%), manufacturing (16%), and other sectors (12%). Study period: 2017–2024.

**Claim 1 —** Modeled ZTA effectiveness shows very large effect sizes across all metrics — 63-79% improvements in breach reduction, financial loss, downtime, and recovery time — but all data is synthetic, not measured from real enterprise telemetry. → [[modeled-zta-effectiveness-shows-very-large-effect]]
**Claim 2 —** Executive sponsorship is the strongest predictor of ZTA implementation success (β = 0.342), and phased deployment significantly outperforms big-bang approaches — both findings converge with practitioner literature despite synthetic data limitations. → [[executive-sponsorship-strongest-predictor-zta-implementation-success]]
---

## 2. Liu et al. (2024) — ZT Research Landscape and IoT Implementation

**Source:** *Cybersecurity* (Springer Open), 2024. Institute of Information Engineering, Chinese Academy of Sciences.

**Study design:** Bibliometric analysis of 814 publications (2010–2023) from WoS and Scopus, plus manual Google Scholar review for IoT-specific threat analysis. First bibliometric/scientometric analysis of ZT literature.

**Claim 3 —** ZT research has entered a rapid growth phase (145→249→~340 publications/year from 2021–2023) with IoT and cloud computing as the two dominant application domains, and the research is geographically concentrated — US + China = 42.5% of publications, with the Asian cluster notably insular. → [[zt-research-entered-rapid-growth-phase-145]]
**Claim 4 —** The paper provides the most comprehensive existing mapping of IoT vulnerabilities → ZT solutions across the three IoT architecture layers, but all surveyed solutions are at proof-of-concept/prototype stage — none validated at production scale. → [[paper-provides-most-comprehensive-existing-mapping-iot]]
---

## 3. Cao et al. (2024) — AI for ZTA Automation and Orchestration

**Source:** *Machine Intelligence Research* (Springer), Vol. 21 No. 2, April 2024. Deakin University, Centre for Cyber Resilience and Trust, Australia.

**Study design:** Systematic review of AI techniques applicable to ZTA component automation and orchestration. Categorizes ZTA components into four automation domains and maps AI methods to each.

**Claim 5 —** ZTA cannot scale without AI-driven automation — manual access credential management, trust evaluation, and policy updates become impossible at enterprise scale, and AI is the only viable approach, but no unified automation policy exists. → [[zta-cannot-scale-without-ai]]
---

## Synthesis: What the Academic Evidence Base Tells Us

**Claim 6 —** The academic quantitative evidence for ZT effectiveness is entirely synthetic (modeled, not measured) — the actual evidentiary status of practitioner claims rests on logical argument, self-reported industry case studies, and regulatory adoption, not independently verified large-scale empirical data. → [[academic-quantitative-evidence-zt-effectiveness-entirely-synthetic]]