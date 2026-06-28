---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-02_technical-advisory-multiple-vulnerabilities-in-pandorafms-enterprise.md
original_filename: 2024-01-02_technical-advisory-multiple-vulnerabilities-in-pandorafms-enterprise.md
title: Technical Advisory – Multiple Vulnerabilities in PandoraFMS Enterprise
category: documents
detected_topics:
- xss
- idor
- access-control
- command-injection
- file-upload
- path-traversal
tags:
- imported
- documents
- xss
- idor
- access-control
- command-injection
- file-upload
- path-traversal
language: en
raw_sha256: 2eb04ed93ce16f0a6ba75ad38e95a8370a0095116946c4a0f7dee9ca3efe1c5b
text_sha256: 878a4838401b53213925145759f7b5a93cf7eb744ddd42ceaa7baac9da624a07
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Technical Advisory – Multiple Vulnerabilities in PandoraFMS Enterprise

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-02_technical-advisory-multiple-vulnerabilities-in-pandorafms-enterprise.md
- Source Type: markdown
- Detected Topics: xss, idor, access-control, command-injection, file-upload, path-traversal
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `2eb04ed93ce16f0a6ba75ad38e95a8370a0095116946c4a0f7dee9ca3efe1c5b`
- Text SHA256: `878a4838401b53213925145759f7b5a93cf7eb744ddd42ceaa7baac9da624a07`


## Content

---
title: "Technical Advisory – Multiple Vulnerabilities in PandoraFMS Enterprise"
page_title: "Cyber Security Research | NCC Group"
url: "https://research.nccgroup.com/2024/01/02/technical-advisory-multiple-vulnerabilities-in-pandorafms-enterprise/"
final_url: "https://www.nccgroup.com/research/"
authors: ["Oliver Brooks"]
programs: ["PandoraFMS"]
bugs: ["Account takeover", "Information disclosure", "RCE", "Unrestricted file upload", "Stored XSS", "Arbitrary file read", "Local Privilege Escalation", "Path traversal", "DoS", "IDOR", "Hardcoded credentials"]
publication_date: "2024-01-02"
added_date: "2024-01-08"
source: "pentester.land/writeups.json"
original_index: 588
---

# Research

Powering the future of cyber security through  
breakthrough research and practical innovation

[Articles](/research/research-articles/)

**|Research Articles | Research Activities | Key Contacts |**

**2025 Annual**  
**Research Report**

[ Download Report ](/research/annual-cyber-security-research-report-2025/)

**Past reports**

  * [2024](/media/5r2lj233/2024-ncc-group-annual-research-report.pdf "2024 NCC Group Annual Research Report")
  * [2022 & 2023](/media/qzpjwdjj/2023-ncc-group-annual-research-report.pdf "2023 NCC Group Annual Research Report")
  * [2021](/media/yz0cte3u/2021-ncc-group-annual-research-report.pdf "2021 NCC Group Annual Research Report")
  * [2020](/media/3uchuovw/2020-ncc-group-annual-research-report.pdf "2020 NCC Group Annual Research Report")

At NCC Group, our Research advances cyber security by discovering vulnerabilities, building open‑source tools, and translating insights into practical guidance for customers and the wider community.

Our projects span vulnerability research and exploitation, network and system security, malware and ransomware analysis/DFIR, applied cryptography, hardware & embedded systems/IoT, and software/AI security – with a track record of publishing reports and tooling that strengthen real‑world cyber resilience. 

For over 25 years, NCC Group researchers have contributed deep technical insight across industry and academia, presenting at global conferences and collaborating with partners worldwide. 

## 2000+

person-days of security research annually

## 280

Open-source tools & datasets authored by NCC authors on our public Github

## 150+

CVEs found since 2020

* * *

## Research Articles

Research

### Time as an Attack Surface

[Read more](/research/time-as-an-attack-surface/)

Research

### Dissecting Android Malware - Post 2: Mamont Variant - Advanced Dropper Logic and Encrypted Payload

[Read more](/research/dissecting-android-malware-post-2-mamont-variant-advanced-dropper-logic-and-encrypted-payload/)

Research

### Auto-Pentester LLM Research

[Read more](/research/auto-pentester-llm-research/)

Research

### An Introduction to AI Coding Agent Security

[Read more](/research/an-introduction-to-ai-coding-agent-security/)

Research

### BLS (Boneh-Lynn-Shacham) Signatures Implementation Review

[Read more](/research/bls-boneh-lynn-shacham-signatures-implementation-review/)

Research

### The Symmetry Problem: Why AI Attackers and AI Defenders Share the Same Blind Spots

[Read more](/research/the-symmetry-problem-why-ai-attackers-and-ai-defenders-share-the-same-blind-spots/)

Research

### Postcards from Hardwear.io

[Read more](/research/postcards-from-hardweario/)

Research

### Async PICOs and Custom Beacon Wakeups in Cobalt Strike

[Read more](/research/async-picos-and-custom-beacon-wakeups-in-cobalt-strike/)

Research

### Tool Release - Ghidra MediaTek Modem Image Loader

[Read more](/research/tool-release-ghidra-mediatek-modem-image-loader/)

Research

### Postcards from Berlin - OffensiveCon 2026

[Read more](/research/postcards-from-berlin-offensivecon-2026/)

Research

### So, what even is Threat Modelling? A security practitioner's guide

[Read more](/research/so-what-even-is-threat-modelling-a-security-practitioners-guide/)

Research

### Teaching the Mapmakers: How AI Training Data Shapes (and Distorts) Security Coverage

[Read more](/research/teaching-the-mapmakers-how-ai-training-data-shapes-and-distorts-security-coverage/)

Previous slide Next slide

## Research Activities

![Commerical Research](/media/rzydrxvu/commerical-research.jpg?quality=80)

### Security Research Services

Our Security Research Services help organisations answer complex, high‑risk cyber security questions that lie beyond standard consulting. 

This work: 

  * Is funded by customers
  * Often requires exploration of previously untested hypotheses
  * Draws on expertise across cryptography, hardware, AI, vulnerability research, secure systems engineering and more
  * Has delivered major projects for the UK public sector and North American technology companies, with ongoing expansion into new geographies 

These services can range from feasibility research and prototype development to deep technical investigations that improve resilience, reduce uncertainty, or validate future defensive approaches. 

### Exploit Development Group (EDG)

The Exploit Development Group is NCC Group’s cutting-edge exploitation team. 

They:

  * Deliver high‑impact research with global recognition
  * Present at top‑tier conferences worldwide
  * Compete in events such as Pwn2Own on behalf of NCC Group
  * Provide bespoke exploit development support to our consultants
  * Offer secondment opportunities that develop elite exploitation skills within our technical teams 

EDG ensures NCC Group remains an industry leader in vulnerability discovery, exploitation, and advanced security research. 

![EDG](/media/d3zhmz5y/edg.jpg?quality=80)

![Academic V2](/media/ademijie/academic-v2.jpg?quality=80)

### Academic Partnerships

Our academic partnerships extend NCC Group’s mission by collaborating with universities and research institutions to: 

  * Support PhD and Masters-level research programmes
  * Shape undergraduate teaching through challenges, curriculum contributions and student projects
  * Deliver STEM outreach and careers engagement
  * Build awareness of NCC Group as a destination for future cyber security professionals 

These collaborations provide access to new technologies and early theoretical developments, while enabling the next generation of talent to gain hands‑on experience with real-world security problems. 

## Key Contacts

![Andydavis](/media/5jfhc0ik/andydavis.png?quality=80)

### Andy Davis

**Global Research Director**

➤ [andy.davis@nccgroup.com](mailto:andy.davis@nccgroup.com)

![Ristinrivera](/media/nreohloq/ristinrivera.png?quality=80)

### Ristin Rivera

**Research Manager**

➤[ristin.rivera@nccgroup.com](mailto:ristin.rivera@nccgroup.com)

## Commercial research enquiries

![Jonrenshaw](/media/nj0hzpor/jonrenshaw.png?quality=80)

### Jon Renshaw

**Director, Commercial Research**

➤[jon.renshaw@nccgroup.com](mailto:jon.renshaw@nccgroup.com)
