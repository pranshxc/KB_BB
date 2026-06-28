---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-13_undermining-microsoft-teams-security-by-mining-tokens.md
original_filename: 2022-09-13_undermining-microsoft-teams-security-by-mining-tokens.md
title: Undermining Microsoft Teams Security by Mining Tokens
category: documents
detected_topics:
- cloud-security
- supply-chain
- automation-abuse
- csrf
- oauth
- sso
tags:
- imported
- documents
- cloud-security
- supply-chain
- automation-abuse
- csrf
- oauth
- sso
language: en
raw_sha256: 7ed48cc91c70d90cb1b5d752e4476dd5b08feb9e4c7d1f78bf6546a68f0637f3
text_sha256: 565868c9a5279980718ba21a7b401baff1b0a54b8d9cc1a2dc951e34bae11e50
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Undermining Microsoft Teams Security by Mining Tokens

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-13_undermining-microsoft-teams-security-by-mining-tokens.md
- Source Type: markdown
- Detected Topics: cloud-security, supply-chain, automation-abuse, csrf, oauth, sso
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `7ed48cc91c70d90cb1b5d752e4476dd5b08feb9e4c7d1f78bf6546a68f0637f3`
- Text SHA256: `565868c9a5279980718ba21a7b401baff1b0a54b8d9cc1a2dc951e34bae11e50`


## Content

---
title: "Undermining Microsoft Teams Security by Mining Tokens"
page_title: "Vectra AI Cybersecurity Blog"
url: "https://www.vectra.ai/blogpost/undermining-microsoft-teams-security-by-mining-tokens"
final_url: "https://www.vectra.ai/blog"
authors: ["Vectra Protect team (@Vectra_AI)"]
programs: ["Microsoft"]
bugs: ["Insecure storage of sensitive information"]
publication_date: "2022-09-13"
added_date: "2022-09-20"
source: "pentester.land/writeups.json"
original_index: 2175
---

# Welcome to the Vectra Blog

Insights into how detection holds up in real environments and how changing attacker tactics impact your team’s response capabilities.

June 25, 2026

6/25/2026

—

Aakash Gupta

and 

Zoey Chu

Why Cloud Security Remains Difficult in Multi-Cloud Environments

Cloud security challenges aren't caused by lack of visibility. Learn why correlating identity, control-plane, and network activity across AWS, Azure, GCP, and OCI is critical for detecting modern cloud attacks.

[Read more](/blog/why-cloud-security-remains-difficult-in-multi-cloud-environments)

June 24, 2026

6/24/2026

—

Fabien Guillot

and 

AI Agents in the SOC: Moving from AI Hype to Operational Reality

Learn how security teams are using AI agents, MCP, and AI-assisted investigations to improve SOC operations, reduce analyst workload, and accelerate threat response.

[Read more](/blog/ai-agents-in-the-soc-moving-from-ai-hype-to-operational-reality)

June 23, 2026

6/23/2026

—

Lucie Cardiet

and 

A Valid Microsoft Signature Does Not Mean a Driver Is Safe

Four signed drivers. Three had documented CVEs. None on the blocklist. How DragonForce used the kernel signing pipeline to disable security tools.

[Read more](/blog/a-valid-microsoft-signature-does-not-mean-a-driver-is-safe)

Blog Posts

Filter

Account takeover

Agentic AI Security

AI Governance Tools

AI Phishing

AI Red Teaming

AI scams

AI Security

AI Security Posture Management 

AI threat detection

Alert Fatigue

APT (Advanced Persistent Threat)

Attacker Behavior

Attack surface

Attack surface management

Attack surface monitoring

AWS Threat Detection

Backdoor

Behavioral Analytics

Behavioral Threat Detection

Botnet

CDR (Cloud Detection and Response)

Cloud security

Cobalt Strike

Command and control

Compliance

Credential theft

Cross-site request forgery (CSRF)

CTEM

CVE

Cyberattack

Cyber attack detection

Cyberattack techniques

Cyber resilience

Cybersecurity automation

Cybersecurity Metrics

Cybersecurity monitoring

Cybersecurity solutions

Cybersecurity threat

Data breach

Detection engineering

Diamond Model of intrusion analysis

Double extortion ransomware

EDR

EDR evasion

EDR tools

EDR vs XDR

Enterprise cybersecurity

Exfiltration

Exploit

Extended Detection and Response (XDR)

Fileless malware

Financial Services Cybersecurity

GDPR compliance

GenAI Security

Healthcare cybersecurity

Hybrid cloud security

Hybrid cloud threat detection

Identity Analytics

Identity threat detection and response (ITDR)

Incident response

Incident Response Automation

Indicator of Compromise

Infostealers

Insider risk management

Insider threat

Intrusion Detection and Prevention System - IDS/IDPS

IoT Security

Kerberoasting

Kill chain

Kubernetes Security

Lateral movement

Living Off the Land

Malware

Managed IT security services

MDR (Managed Detection and Response)

Metadata

Metasploit

Mimikatz

Mishing

MITRE ATLAS

MITRE ATT&CK

MITRE D3FEND

Modern Network

Multi-cloud security

Multi factor authentication (MFA)

NDR Tools

NDR vs EDR

NDR vs XDR

Network anomaly detection

Network Detection and Response (NDR)

Network security

Network Traffic Analysis

Network visibility

OPSEC (Operations Security)

Phishing

Privilege Escalation

Proactive threat detection

Prompt injection

Pyramid of Pain

Ransomware

Clear

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)June 25, 20266/25/2026Aakash Guptaand Zoey ChuWhy Cloud Security Remains Difficult in Multi-Cloud EnvironmentsCloud security challenges aren't caused by lack of visibility. Learn why correlating identity, control-plane, and network activity across AWS, Azure, GCP, and OCI is critical for detecting modern cloud attacks.Read more](/blog/why-cloud-security-remains-difficult-in-multi-cloud-environments)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)June 24, 20266/24/2026Fabien Guillotand AI Agents in the SOC: Moving from AI Hype to Operational RealityLearn how security teams are using AI agents, MCP, and AI-assisted investigations to improve SOC operations, reduce analyst workload, and accelerate threat response.Read more](/blog/ai-agents-in-the-soc-moving-from-ai-hype-to-operational-reality)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)June 23, 20266/23/2026Lucie Cardietand A Valid Microsoft Signature Does Not Mean a Driver Is SafeFour signed drivers. Three had documented CVEs. None on the blocklist. How DragonForce used the kernel signing pipeline to disable security tools.Read more](/blog/a-valid-microsoft-signature-does-not-mean-a-driver-is-safe)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)June 18, 20266/18/2026Lucie Cardietand What Anthropic's Attacker-AI Data Means for DetectionA year of AI-enabled attacker activity, what it tells us about where attacks are headed, and where detection holds up.Read more](/blog/what-anthropics-attacker-ai-data-means-for-detection)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)June 17, 20266/17/2026Mark Wojtasiakand In the AI Era, Insider Threats Are Not Just Human. They’re Artificial.AI agents, service accounts, and automation are the new insider threat. Learn how artificial insiders create risk at machine speed.Read more](/blog/in-the-ai-era-insider-threats-are-not-just-human-theyre-artificial)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)June 12, 20266/12/2026Martin Roeschand The Security Event Horizon: Rethinking Cybersecurity Beyond Prevention The Security Event Horizon explains where prevention ends and detection, context, and response become critical to stopping attacks.Read more](/blog/the-security-event-horizon-rethinking-cybersecurity-beyond-prevention)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)June 11, 20266/11/2026John Manciniand Exposure management is broken. Here’s why and what needs to change.Security teams aren’t short on exposure management tools. There are asset inventories, vulnerability scanners, EDR, cloud security platforms, identity systems, attack surface management (ASM) platforms, and SIEMs. Each one provides a piece of insight into the environment. Read more](/blog/exposure-management-is-broken-heres-why-and-what-needs-to-change)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)June 8, 20266/8/2026John Manciniand Why Modern C2 Detection Requires Behavioral Modeling, Not DecryptionModern attackers evade decryption, reputation checks, and beacon detection. Learn how Vectra AI uses behavioral AI to detect hidden command-and-control activity.Read more](/blog/why-modern-c2-detection-requires-behavioral-modeling-not-decryption)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)June 4, 20266/4/2026Mark Wojtasiakand 5 Takeaways from the Gartner Security & Risk Management Summit 2026Explore five key Gartner SRM 2026 trends shaping cybersecurity, from AI-driven defense and identity security to cyber resilience.Read more](/blog/5-takeaways-from-the-gartner-security-risk-management-summit-2026)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)June 2, 20266/2/2026Lucie Cardietand From Conti to The Gentlemen: tooling evolved, gaps didn't.Conti to The Gentlemen: four ransomware leaks, four years. The operators evolved. The gaps stayed exactly where they were. What CISOs should do next.Read more](/blog/from-conti-to-the-gentlemen-tooling-evolved-gaps-didnt)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)June 2, 20266/2/2026Brad Woodbergand Closing Modern Attack Gaps: How Vectra AI + Zscaler Deliver Modern Network Protection Discover how Zscaler and Vectra AI deliver modern network protection with Zero Trust, AI-driven detection, and unified visibility.Read more](/blog/closing-modern-attack-gaps-how-vectra-ai-zscaler-deliver-modern-network-protection)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)June 1, 20266/1/2026Kat Traxlerand Azure’s Hidden Operators: A Threat Model for Platform-Level Managed IdentitiesAzure’s Hidden Operators: A Threat Model for Platform-Level Managed IdentitiesRead more](/blog/azures-hidden-operators-a-threat-model-for-platform-level-managed-identities)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)June 1, 20266/1/2026Tommy Jenkinsand We Were AI Before AI Became a Checkbox AI isn't new to Vectra AI. Discover why we're making it more visible now and what it means for modern cybersecurity.Read more](/blog/we-were-ai-before-ai-became-a-checkbox)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)May 21, 20265/21/2026Hitesh Shethand AI-Driven Network Detection and Response: Insights from a 2026 Gartner® Magic Quadrant™ Leader A Vectra AI CEO perspective on the 2026 Gartner Magic Quadrant for NDR, and what it reveals about the future of AI-driven network security.Read more](/blog/ai-driven-network-detection-and-response-insights-from-a-2026-gartner-magic-quadrant-leader)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)May 18, 20265/18/2026Aakash Guptaand Securing AI Adoption Starts with VisibilityAI adoption is no longer a future planning exercise. It's happening inside the AI Enterprise.Read more](/blog/securing-ai-adoption-starts-with-visibility)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)May 18, 20265/18/2026Dale O’Gradyand The Missing Data Layer Behind SIEM and SOARLearn how Vectra AI’s Investigate API delivers security telemetry and evidence into SIEM and SOAR workflows for faster investigations. Read more](/blog/security-telemetry-siem-soar)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)May 14, 20265/14/2026Dale O’Gradyand Why Most SIEM/SOAR Integrations Break — and How to Fix ThemLearn why SIEM and SOAR integrations fail and how Vectra AI improves security automation with context-rich alerts and reliable workflows. Read more](/blog/fixing-siem-soar-integrations)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)May 13, 20265/13/2026Lucie Cardietand Shai-Hulud Part 2: When the Worm Forged Its Own Security CertificateTeamPCP open-sourced Shai-Hulud today. The OIDC token extraction technique that made the TanStack attack different from every previous campaign is now a public toolkit.Read more](/blog/shai-hulud-part-2-when-the-worm-forged-its-own-security-certificate)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)May 11, 20265/11/2026Gearóid Ó Fearghaíland Improve SIEM and SOAR Workflows with Better Security SignalLearn how Vectra AI improves SIEM and SOAR workflows with behavior-driven signal, investigation-ready telemetry, and better security orchestration.Read more](/blog/improve-siem-soar-workflows)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)May 6, 20265/6/2026Lucie Cardietand Aakash GuptaShinyHunters isn’t a group. It’s a pattern.ShinyHunters isn't a single group. It's a pattern of attacks where authentication succeeds. Here's how to detect them before the data warehouse. Read more](/blog/shinyhunters-isnt-a-group-its-a-pattern)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)May 5, 20265/5/2026Aakash Guptaand How Vectra AI Secures the AI EnterpriseLearn how Vectra AI uses AI to secure the AI enterprise—reducing risk, accelerating detection, and enabling faster, more confident response.Read more](/blog/how-vectra-ai-secures-the-ai-enterprise)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)May 4, 20265/4/2026Tiffany Nipand AI agents: the new workforce — and attack surface.AI agents are becoming the new workforce, and a new attack surface. Learn the risks they introduce and how to maintain visibility and control at AI speed.Read more](/blog/ai-agents-the-new-workforce-and-attack-surface)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 29, 20264/29/2026John Manciniand How Vectra AI Scoring Helps Security Teams Focus on What Matters First Why Modern Threat Scoring Must Reflect Attacker Progression Read more](/blog/how-vectra-ai-scoring-helps-security-teams-focus-on-what-matters-first)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 28, 20264/28/2026Oliver Tavakoliand What’s Next for the Enterprise After Two GenAI Tidal Waves? Claude Mythos and GenAI are reshaping security — discover why faster exploits, endless patching, and resilient detection now define defense.Read more](/blog/whats-next-for-the-enterprise-after-two-genai-tidal-waves)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 22, 20264/22/2026Zoey Chuand If An Identity was Compromised, Would We Know?Identity-based attacks are increasing across hybrid environments. Learn how to detect compromised identities before attackers move laterally.Read more](/blog/if-an-identity-was-compromised-would-we-know)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 21, 20264/21/2026Mark Wojtasiakand Help Over Hype: Claude Mythos, Project Glasswing and the Real Questions CISOs Want AnsweredClaude Mythos accelerates risk—not just hype. Learn what CISOs must focus on now: visibility, speed, and understanding attacks as they unfold.Read more](/blog/help-over-hype-claude-mythos-project-glasswing-and-the-real-questions-cisos-want-answered)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 20, 20264/20/2026Alex Groyzand Zack AbzugAzure Logging just Changed - Your Detections May be Missing it This blog explains how Microsoft's shift from the legacy Azure Diagnostics Agent to the Azure Monitor Agent fundamentally changes how VM logging is controlled and highlights how this redesign can introduce detection blind spots if security teams don't update their monitoring approach.Read more](/blog/azure-logging-just-changed-your-detections-may-be-missing-it)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 20, 20264/20/2026Justin Howeand When the Defender Becomes the Door: BlueHammer, RedSun, and UnDefend in the WildThree leaked Windows Defender exploits are now hitting real enterprise targets. Here is what the attack chain looks like, why endpoint tools alone cannot contain it, and where the Vectra AI Platform with RUX surfaces it before the damage is done. Read more](/blog/when-the-defender-becomes-the-door-bluehammer-redsun-and-undefend-in-the-wild)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 20, 20264/20/2026Tiffany Nipand Gearóid Ó FearghaílAI-Assisted Search: Clarity at the Speed of a QuestionAI-assisted search lets analysts ask investigative or hunting questions in plain language.Read more](/blog/introducing-ai-assisted-search-clarity-at-the-speed-of-a-question)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 20, 20264/20/2026Jesse Kimbreland 4 Ways to Improve SOC Efficiency with AIDiscover four key ways AI can enhance SOC efficiency by improving alert accuracy, optimizing investigations, automating threat hunting, and prioritizing high-risk threats.Read more](/blog/4-ways-to-give-your-soc-valuable-time-back-with-ai)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 17, 20264/17/2026Brad Woodbergand Why triage alerts - when AI can do it for you?If you ask security analysts to describe the biggest pain points in their role, you will no doubt get a diverse set of answers. One thing that they will almost certainly have in common is the challenge of dealing with alert fatigue.Read more](/blog/why-triage-alerts-when-ai-can-do-it-for-you)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 16, 20264/16/2026Tiffany Nipand The Two Control Points That Will Define the Future of Cybersecurity – Network and Identity Identity and network are the new control points in cybersecurity. Learn why securing them is critical for visibility, detection, and resilient defense. Read more](/blog/the-two-control-points-that-will-define-the-future-of-cybersecurity-network-and-identity)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 16, 20264/16/2026Lucie Cardietand Attackers Don’t Hack In — They Log In: The MFA Blind SpotAttackers bypass MFA using non-interactive sign-ins. Learn how to detect and stop credential-based threats before they escalate.Read more](/blog/attackers-dont-hack-in-they-log-in-the-mfa-blind-spot)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 14, 20264/14/2026Lucie Cardietand Supply chain-driven data theft in SaaS: ShinyHunters, Anodot, and the pattern that's repeating.Another supply-chain breach hit SaaS in April 2026 — Anodot tokens used to access Snowflake. Why the same ShinyHunters-branded pattern keeps repeating, and what makes the MO hard to detect.Read more](/blog/the-rise-of-supply-chain-driven-data-theft-in-saas-environments)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 13, 20264/13/2026Zoey Chuand What We Learned from Analyzing Millions of AlertsWe took a deep dive into millions of detections across MDR/MXDR and Respond UX deployments with the goal of getting a clearer picture of where the real threats are so that we can get a better understanding how security teams can work smarter, not harder. Read more](/blog/what-we-learned-from-analyzing-millions-of-alerts)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 9, 20264/9/2026Mark Wojtasiakand EDR Isn’t Enough: Why Forward-Thinking CISOs Are Turning to Network + Identity EDR alone can’t stop modern breaches. Learn why CISOs are uniting network and identity signals to outpace attackers and build resilience.Read more](/blog/edr-isnt-enough-why-forward-thinking-cisos-are-turning-to-network-identity)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 8, 20264/8/2026Lucie Cardietand FortiClient EMS Zero-Day: When the Control Plane Becomes Initial AccessCompromise of endpoint management systems changes the attack path entirely. Learn how control-plane attacks bypass early detection and why behavior across identity, network, and endpoints is the only reliable signal.Read more](/blog/forticlient-ems-zero-day-when-the-control-plane-becomes-initial-access)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 3, 20264/3/2026Yusri Mohd Yusopand Detecting Compromise After the Axios Supply Chain Attack.The axios supply chain compromise shows why risk begins after execution. Learn how to detect post-compromise behavior across CI/CD pipelines, identity systems, and network activity. Read more](/blog/the-axios-breach-a-wake-up-call-for-software-supply-chain-security)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 2, 20264/2/2026Mark Wojtasiakand Who’s Doing What on Your Network?Can you confidently answer who is doing what on your network? Learn why visibility into user activity is key to security, risk, and compliance.Read more](/blog/whos-doing-what-on-your-network)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)April 1, 20264/1/2026Lucie Cardietand Breaking down the axios supply chain incidentA compromised npm package is only the entry point. The axios incident shows how quickly attackers pivot from code execution to credential abuse, identity misuse, and cloud access.Read more](/blog/breaking-down-the-axios-supply-chain-incident)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)March 23, 20263/23/2026Lucie Cardietand Detecting Sliver C2: When Advanced Beaconing Tries to Hide in Plain SightDetect how Sliver C2 evades traditional beacon detection and how behavioral AI identifies command-and-control activity hidden in encrypted traffic.Read more](/blog/detecting-sliver-c2-when-advanced-beaconing-tries-to-hide-in-plain-sight)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)March 19, 20263/19/2026Lucie Cardietand Mauro ParedesPrompt Control: How Context Becomes the Command-and-Control Layer for AI AgentsPrompt control turns AI agents into command-and-control systems by manipulating context, memory, and inputs—enabling persistent, stealthy attacker control through normal agent behavior.Read more](/blog/prompt-control-how-context-becomes-the-command-and-control-layer-for-ai-agents)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)March 17, 20263/17/2026Lucie Cardietand How Attackers Move Through Hybrid Networks After the Initial BreachLearn how attackers move laterally across hybrid networks, abusing identity, credentials, and legitimate tools to reach critical systems before launching ransomware or stealing data.Read more](/blog/how-attackers-move-through-hybrid-networks-after-the-initial-breach)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)March 16, 20263/16/2026Lucie Cardietand How Attackers Establish Persistence in Hybrid EnvironmentsLearn how attackers maintain hidden access inside hybrid networks and how SOC teams can detect persistence before it leads to data theft or ransomware.Read more](/blog/how-attackers-establish-persistence-in-hybrid-environments)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)March 13, 20263/13/2026Lucie Cardietand What the Stryker Incident Reveals About Handala’s Attack PlaybookInside the Stryker incident: how Handala likely moved from identity access to disruption, and the identity, scripting, and data transfer signals SOC teams should watch.Read more](/blog/what-the-stryker-incident-reveals-about-handalas-attack-playbook)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)March 13, 20263/13/2026Jesse Kimbreland Why Cyber Resilience is Lagging in the AI Era Cyber resilience is lagging as defenders face alert overload, visibility gaps, and AI-speed attacks. Learn what SOC teams must change to stay resilient.Read more](/blog/why-cyber-resilience-is-lagging-in-the-ai-era)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)March 6, 20263/6/2026Lucie Cardietand 5-Minute Hunt: Six Queries to Detect Iranian APT ActivityDetect Iranian APT activity across identity and network telemetry with six practical threat hunts. Run ready-to-use queries in the Vectra AI Platform to uncover credential abuse, C2 infrastructure, and early compromise signals.Read more](/blog/5-minute-hunt-six-queries-to-detect-iranian-apt-activity)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)February 27, 20262/27/2026John Manciniand AI-Powered Attacks Are Here, But So Is AI-Powered NDR to Stop ThemAI-powered attacks are accelerating with agentic AI, but network behaviors remain visible. Learn why AI-powered NDR detects and stops these threats.Read more](/blog/ai-powered-attacks-are-here-but-so-is-ai-powered-ndr-to-stop-them)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)February 20, 20262/20/2026Anna Baron Garciaand What is hiding in AI trafficAI traffic now hides autonomous, agentic attacks. Learn how MCP-enabled swarms blur legitimate AI activity and command and control, reshaping detection and defense.Read more](/blog/what-is-hiding-in-ai-traffic)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)February 10, 20262/10/2026Alex Groyzand AWS Compromised by AI Agents in MinutesAn AI-driven AWS attack reached admin access in minutes using valid credentials. Learn how identity abuse and automation compress cloud attack timelines.Read more](/blog/aws-compromised-by-ai-agents-in-minutes)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)February 4, 20262/4/2026Padraig Mannionand The UX of Cybersecurity AI: Designing for Behavior at Machine Speed UX teams must translate attacker behavior—not alerts—to help SOC teams act on AI-driven threats that move at machine speed. Read more](/blog/the-ux-of-cybersecurity-ai-designing-for-behavior-at-machine-speed)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)February 4, 20262/4/2026Lucie Cardietand Molt Road and the Automation of Underground MarketplacesMolt Road reveals how attacker marketplaces could evolve when autonomous agents trade services, coordinate attacks, and remove humans from the loop.Read more](/blog/molt-road-and-the-automation-of-underground-marketplaces)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)February 3, 20262/3/2026Lucie Cardietand Moltbook and the Illusion of “Harmless” AI-Agent CommunitiesMoltbook exposes how autonomous AI agents turn trust and interaction into attack paths, enabling prompt injection, lateral movement, and covert command and control.Read more](/blog/moltbook-and-the-illusion-of-harmless-ai-agent-communities)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)February 2, 20262/2/2026Mark Wojtasiakand From Network Detections to Understanding Risk: The Vectra AI Take on Gartner’s Redefinition of NDRGartner redefines NDR—and Vectra AI agrees. Learn why true resilience starts with understanding risk, not just detecting anomalies.Read more](/blog/gartner-redefinition-of-ndr-network-detection-and-response)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)January 30, 20261/30/2026Lucie Cardietand From Clawdbot to OpenClaw: When Automation Becomes a Digital BackdoorClawdbot – now Moltbot – shows how autonomous AI agents become shadow superusers, enabling initial access, lateral movement, and ransomware when trust is abused.Read more](/blog/clawdbot-to-moltbot-to-openclaw-when-automation-becomes-a-digital-backdoor)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)January 21, 20261/21/2026Hitesh Shethand Securing the AI Enterprise: How I’m Thinking About It as a CEO AI moves fast—leaders must move smarter. Vectra AI’s CEO shares how to balance innovation with resilience in today’s machine-speed enterprise.Read more](/blog/securing-the-ai-enterprise-how-im-thinking-about-it-as-a-ceo)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)January 16, 20261/16/2026Fabien Guillotand Cybersecurity Predictions 2026: AI, Agents, and SOC DefenseAI agents are accelerating the kill chain faster than defenders can respond. See what changes in 2026 and where SOCs fall behind.Read more](/blog/security-predictions-for-2026-when-ai-scales-the-offense-defense-must-evolve)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)January 9, 20261/9/2026Lucie Cardietand OPSEC Failures: How Threat Actor Mistakes Help DefendersThreat actors try to stay invisible, but OPSEC mistakes keep exposing them. A look at real-world failures and what they reveal about human error and AI-driven attacks.Read more](/blog/opsec-failures-how-threat-actor-mistakes-help-defenders)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)January 5, 20261/5/2026Mauro Paredesand How Threat Actors Turned AI Into a WeaponAI is no longer assisting attackers, it is running the operation. A deep look at how threat actors moved from experimentation to autonomous, AI-driven cyberattacks.Read more](/blog/how-threat-actors-turned-ai-into-a-weapon)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)December 29, 202512/29/2025Fabien Guillotand CVE-2025-14847 MongoBleed in the Wild: Identifying MongoDB Exposure and Exploitation with Network MetadataCVE-2025-14847 ‘MongoBleed’ exposes critical memory leaks—learn how Vectra AI detects vulnerable MongoDB instances across your network.Read more](/blog/cve-2025-14847-mongobleed-in-the-wild-identifying-mongodb-exposure-and-exploitation-with-network-metadata)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)December 17, 202512/17/2025Lucie Cardietand Pro-Russia Hacktivists Are Targeting Critical InfrastructurePro-Russia hacktivists are disrupting critical infrastructure by abusing legitimate access. Learn how these OT attacks work and why traditional tools miss them.Read more](/blog/pro-russia-hacktivists-are-targeting-critical-infrastructure)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)December 11, 202512/11/2025Dale O’Gradyand How Vectra AI Connects Network Detections to Endpoint Processes AutomaticallyVectra AI instantly connects network detections to endpoint processes—no pivots, no delay, just complete attack context in one view.Read more](/blog/how-vectra-ai-connects-network-detections-to-endpoint-processes-automatically)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)December 10, 202512/10/2025Tiffany Nipand How Vectra AI and CrowdStrike Deliver Complete Context Across Endpoint and NetworkSee how Vectra AI and CrowdStrike unite EDR and NDR to deliver full attack context, faster investigations, and clearer, more decisive threat response.Read more](/blog/how-vectra-ai-and-crowdstrike-deliver-complete-context-across-endpoint-and-network)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)December 10, 202512/10/2025Kat Traxlerand You are the Blackboard - AI Agent Assisted Bug HuntingYou are the Blackboard - AI Agent Assisted Bug HuntingRead more](/blog/ai-agent-assisted-bug-hunting)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)December 2, 202512/2/2025Tom Bilenand TCP Reset Does Not Stop Modern Attacks – Here's Why TCP resets don’t stop modern attackers. Learn why they fail—and how Vectra AI’s 360 Response delivers true, enforced containment across identity, device, and traffic.Read more](/blog/tcp-reset-does-not-stop-modern-attacks---heres-why)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)November 26, 202511/26/2025Lucie Cardietand Shai-Hulud: When a Supply-Chain Incident Turns Into a WormHow the Shai-Hulud worm hijacked trusted development tools and why defenders need behavioral visibility to catch the attack after the first package is installed.Read more](/blog/shai-hulud-when-a-supply-chain-incident-turns-into-a-worm)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)November 20, 202511/20/2025Lucie Cardietand How Typhoon APTs Infiltrate Infrastructure Without Leaving a TraceChinese state-backed Typhoon APTs infiltrate networks using trusted tools. Learn how the Vectra AI Platform detects their stealthy, persistent behavior.Read more](/blog/how-typhoon-apts-infiltrate-infrastructure-without-leaving-a-trace)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)November 19, 202511/19/2025Tiffany Nipand Think Your Microsoft Environment Is Resilient to Attacks? Think Again Microsoft prevention isn’t enough. Learn how attackers exploit gaps across Azure, M365, and Entra ID—and how Vectra AI delivers the visibility to stop them.Read more](/blog/think-your-microsoft-environment-is-resilient-to-attacks-think-again)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)November 14, 202511/14/2025Lucie Cardietand Europol Operation ENDGAME: Takedown of Initial Access BrokersEuropol seized 1,000+ servers and €21M across three phases targeting initial access brokers. Criminal groups rebuilt within days — static defenses cannot keep up.Read more](/blog/operation-endgame-and-the-battle-for-initial-access)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)November 14, 202511/14/2025Nicole Drakeand What 400+ NDR Power Users Taught Us About Network VisibilityDiscover insights from 400+ NDR power users on how network visibility closes security gaps, boosts SOC efficiency, and speeds threat response.Read more](/blog/what-400-ndr-power-users-taught-us-about-network-visibility)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)November 12, 202511/12/2025Lucie Cardietand How Attackers Gain Initial Access in Hybrid EnvironmentsLearn how attackers gain initial access to your hybrid network, and how to stop intrusions before they turn into breaches.Read more](/blog/how-attackers-gain-initial-access-in-hybrid-environments)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)November 4, 202511/4/2025Fabien Guillotand Can Your SOC's AI Actually Think? Evaluating LLMs with the Vectra AI MCP ServerVectra AI tests how LLMs like GPT and Claude perform in real SOCs—revealing which AI agents truly think, act, and reason in cybersecurity.Read more](/blog/can-your-socs-ai-actually-think-evaluating-llms-with-the-vectra-ai-mcp-server)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)October 30, 202510/30/2025Tiffany Nipand How Vectra AI Hybrid NDR Enables Proactive Threat Hunting and Outcome-Driven DefenseTransform SOC efficiency with AI-driven threat hunting. Detect stealthy attacks earlier, cut MTTR, and operationalize Gartner’s 2025 recommendations.Read more](/blog/how-vectra-ai-hybrid-ndr-enables-proactive-threat-hunting-and-outcome-driven-defense)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)October 27, 202510/27/2025Fabien Guillotand Introducing the Vectra AI MCP Server for On-Premises (QUX) Introducing the Vectra AI MCP Server for QUX—bringing AI-powered SOC automation and MCP innovation to on-premises security environments.Read more](/blog/introducing-the-vectra-ai-mcp-server-for-on-premises-qux)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)October 17, 202510/17/2025Lucie Cardietand From Conti to Black Basta to DevMan: The Endless Ransomware RebrandFrom Conti to Black Basta to DevMan, ransomware code keeps resurfacing. See how behavioral AI detects the attacker behaviors that rebrands cannot hide.Read more](/blog/from-conti-to-black-basta-to-devman-the-endless-ransomware-rebrand)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)October 16, 202510/16/2025Lucie Cardietand How the F5 Breach Exposed Critical Edge Security GapsThe F5 compromise shows how attackers abuse trusted edge systems. Behavioral detection spots hidden persistence where perimeter tools fail.Read more](/blog/could-the-f5-breach-expose-a-new-edge-security-gap)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)October 15, 202510/15/2025Lucie Cardietand Qilin’s 2025 Playbook, and the Security Gap it ExposesQilin’s 2025 variants use MFA bombing, SIM swapping, and AES-256-CTR encryption to evade detection. Discover how the Vectra AI Platform exposes their behavior before encryption starts.Read more](/blog/qilins-2025-playbook-and-the-security-gap-it-exposes)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)October 14, 202510/14/2025Mark Wojtasiakand Vectra Fusion: Extending the Vectra AI Platform to Build Resilience Both Pre and Post CompromiseVectra Fusion unifies observability and detection to build SOC resilience before and after compromise across hybrid environments.Read more](/blog/vectra-fusion-extending-the-vectra-ai-platform-to-build-resilience-both-pre-and-post-compromise)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)October 9, 202510/9/2025Lucie Cardietand Seeing Beneath the Surface: What Crimson Collective Reveals About Cloud Detection DepthCrimson Collective says defenders only “map the coastline.” See how Vectra AI dives deeper, turning cloud and identity telemetry into real-time detection of hidden threats.Read more](/blog/seeing-beneath-the-surface-what-crimson-collective-reveals-about-cloud-detection-depth)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)October 7, 202510/7/2025Lucie Cardietand Cl0p Is Back, Exploiting Supply Chains Again.The Cl0p ransomware group’s link to the Oracle EBS exploit sparks debate. Learn how supply chain attacks evolve and what defenders must do next.Read more](/blog/cl0p-is-back-exploiting-supply-chains-again)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)October 7, 202510/7/2025Mark Wojtasiakand How to Choose the Best NDR for Hybrid EnvironmentsNot all NDR tools cover hybrid networks equally. Identify capabilities that matter for detection and control.Read more](/blog/best-ndr-for-hybrid-environments-visibility-control-and-threat-response)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)October 3, 202510/3/2025Lucie Cardietand Red Hat GitLab Breach Shows Why Consulting Data is a Goldmine for AttackersThe Crimson Collective claims to have stolen Red Hat consulting data, exposing customer engagement reports. Learn why consulting artifacts are prime attacker targets and how Vectra AI helps close the gap.Read more](/blog/red-hat-gitlab-breach-shows-why-consulting-data-is-a-goldmine-for-attackers)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)October 2, 202510/2/2025Lucie Cardietand Why the GoAnywhere vulnerability exposed the limits of patchingPatching stops entry, but not attacker behavior. See how detection closes the post-exploitation gapRead more](/blog/when-goanywhere-lets-attackers-go-everywhere)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)October 2, 202510/2/2025Hitesh Shethand Martin RoeschVectra AI with Netography Redefining the SOC Platform around Modern Attack Resilience Vectra AI and Netography deliver the first converged SOC platform, uniting prevention and response for resilience across hybrid enterprises.Read more](/blog/vectra-ai-with-netography-redefining-the-soc-platform-around-modern-attack-resilience)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)October 1, 202510/1/2025Lucie Cardietand Beyond Endpoints: How BRICKSTORM Exposed Security Blind SpotsDiscover how BRICKSTORM hid for 400 days in enterprise blind spots and learn how Vectra AI closes detection gaps across network, identity, and cloud.Read more](/blog/beyond-endpoints-how-brickstorm-exposed-security-blind-spots)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)September 22, 20259/22/2025Mark Wojtasiakand What Modern SOCs Should Know About NDR Alternatives EDR stops at endpoints. SIEM reconstructs after the fact. See why NDR fills the detection gap where attackers operateRead more](/blog/evaluating-ndr-alternatives-why-every-modern-soc-needs-network-detection-and-response)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)September 17, 20259/17/2025Lucie Cardietand Scattered Lapsus$ Hunters Announce They Are Going Dark but the Threat RemainsScattered Lapsus$ Hunters may claim they’re gone, but The Com endures. Cybercrime has moved beyond ransomware into an era where extortion is the goal.Read more](/blog/scattered-lapsus-hunters-announce-they-are-going-dark-but-the-threat-remains)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)September 12, 20259/12/2025Lucie Cardietand LockBit is Back: What’s New in Version 5.0LockBit is back with version 5.0. Discover its new features, TTPs, and how SOC teams can detect attacks where prevention alone falls short.Read more](/blog/lockbit-is-back-whats-new-in-version-5-0)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)September 11, 20259/11/2025Lucie Cardietand The Npm Exploit Is The Entry Point, What Follows Is Just As Critical.Poisoned npm packages are just the entry point. Discover how attackers move next and why SOC teams must detect behaviors beyond the initial exploit.Read more](/blog/the-npm-exploit-is-the-entry-point-what-follows-is-just-as-critical)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)September 10, 20259/10/2025Lucie Cardietand How AI is Fueling Cybercrime and Why Security Gaps Are GrowingAI is accelerating cybercrime — from ransomware kits to insider fraud. Learn how attackers exploit security gaps and how Vectra AI helps you detect what others miss.Read more](/blog/how-ai-is-fueling-cybercrime-and-why-security-gaps-are-growing)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)September 9, 20259/9/2025Lucie Cardietand 5-Minute Hunt: Detecting Risky Multi-Tenant Apps in Microsoft 365Hunt for risky multi-tenant apps in Microsoft 365. Learn how attackers exploit consent-based access and how to detect misconfigurations in minutes.Read more](/blog/5-minute-hunt-detecting-risky-multi-tenant-apps-in-microsoft-365)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)September 8, 20259/8/2025Lucie Cardietand GLOBAL RaaS: Dissecting a Modern Ransomware FranchiseDiscover how GLOBAL RaaS empowers affiliates with enterprise-scale ransomware features, and how Vectra AI detects threats others miss.Read more](/blog/global-raas-dissecting-a-modern-ransomware-franchise)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)August 28, 20258/28/2025Lucie Cardietand What the CISA Advisory Reveals About Nation-State AttacksNation-state campaigns bypass prevention controls. Learn why post-compromise detection is now criticalRead more](/blog/cisas-august-advisory-why-you-need-post-compromise-detection)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)August 27, 20258/27/2025Strahinja Janjusevicand New Technologies bring new risks: MCP-Powered Swarm C2Explore how MCP-powered agent swarms evade detection, bypass EDR, and exploit LLMs for stealthy attacks. A new era of autonomous C2 is here.Read more](/blog/new-technologies-bring-new-risks-mcp-powered-swarm-c2)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)August 21, 20258/21/2025Lucie Cardietand 4 Real-World Attacks That Show Why SOCs Need NDRDiscover how Scattered Spider, Volt Typhoon, Mango Sandstorm, and UNC3886 evaded defenses - and why SOC teams need NDR to stop them in time.Read more](/blog/4-real-world-attacks-that-show-why-socs-need-ndr)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)August 21, 20258/21/2025Tiffany Nipand Why insider threats go undetected by security toolsDLP and EDR miss insider misuse. Learn behavioral indicators and how detection identifies risk before damageRead more](/blog/insider-threats-how-security-tools-miss-them-and-why-behavioral-ai-closes-the-gap)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)August 19, 20258/19/2025Nicole Drakeand Black Hat USA 2025: What Security Teams Asked Us in Las Vegas What different stakeholders looking for an NDR asked the Vectra AI team at BlackHat 2025.Read more](/blog/black-hat-usa-2025-what-security-teams-asked-us-in-las-vegas)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)August 18, 20258/18/2025Zoey Chuand Vectra AI and Google Security Operations: Breaking Down Security Silos Vectra AI and Google Security Operations unite to break security silos, streamline workflows, and strengthen threat detection and response.Read more](/blog/vectra-ai-and-google-security-operations-breaking-down-security-silos)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)August 15, 20258/15/2025Lucie Cardietand Black Hat Takeaway: Everyone Talks Prevention, But Who Detects Compromise?Modern attacks often begin with valid credentials and evade detection. Learn what questions to ask vendors about post-compromise visibility.Read more](/blog/black-hat-takeaway-everyone-talks-prevention-but-who-detects-compromise)

[Security Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)AI Research![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)Threat Briefings![](https://cdn.prod.website-files.com/64e36a72d57403710ee5415d/67997019bca251d01ced691b_security-research-icon-background.svg)August 14, 20258/14/2025Mark Wojtasiakand Black Hat USA 2025: What It Told Me About Protecting the Modern Network from Modern Attacks Key takeaways from Black Hat USA 2025 on defending modern networks from AI-driven threats, identity attacks, and converged risks.Read more](/blog/black-hat-usa-2025-what-it-told-me-about-protecting-the-modern-network-from-modern-attacks)

[Next](?f321d0b1_page=2)

Previous

1

Next
