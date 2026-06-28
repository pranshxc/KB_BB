---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-20_you-cant-stop-me-ms-teams-session-hijacking-and-bypass.md
original_filename: 2020-09-20_you-cant-stop-me-ms-teams-session-hijacking-and-bypass.md
title: You can’t stop me. MS Teams session hijacking and bypass
category: documents
detected_topics:
- supply-chain
- oauth
- sso
- sqli
- command-injection
- mfa
tags:
- imported
- documents
- supply-chain
- oauth
- sso
- sqli
- command-injection
- mfa
language: en
raw_sha256: bb0151d1ff60ed5fbed68c2176b4b53bfa409ee4acd4883147726da4c45ab964
text_sha256: d27b2b8c4767af1ea6cd675dab0400557ea2768d5e034bff0be30de850152e5c
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: true
---

# You can’t stop me. MS Teams session hijacking and bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-20_you-cant-stop-me-ms-teams-session-hijacking-and-bypass.md
- Source Type: markdown
- Detected Topics: supply-chain, oauth, sso, sqli, command-injection, mfa
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: True
- Raw SHA256: `bb0151d1ff60ed5fbed68c2176b4b53bfa409ee4acd4883147726da4c45ab964`
- Text SHA256: `d27b2b8c4767af1ea6cd675dab0400557ea2768d5e034bff0be30de850152e5c`


## Content

---
title: "You can’t stop me. MS Teams session hijacking and bypass"
page_title: "You can’t stop me. MS Teams session hijacking and bypass | Pen Test Partners"
url: "https://www.pentestpartners.com/security-blog/you-cant-stop-me-ms-teams-session-hijacking-and-bypass/"
final_url: "https://www.pentestpartners.com/security-blog/you-cant-stop-me-ms-teams-session-hijacking-and-bypass/"
authors: ["Bandit Pingu (@FlyingPhishy)"]
programs: ["Microsoft"]
bugs: ["Insecure storage of sensitive information"]
publication_date: "2020-09-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4252
---

[Home](/)

Services ▾

Test and Simulate ▾

[Penetration Testing (CHECK)](https://www.pentestpartners.com/service/penetration-testing/)

[Pen Testing as a Service (PTaaS)](https://www.pentestpartners.com/service/pen-testing-as-a-service-ptaas/)

[Artificial Intelligence Testing](https://www.pentestpartners.com/service/artificial-intelligence-testing/)

[Red Teaming (CBEST, GBEST, STAR-FS, TIBER)](https://www.pentestpartners.com/service/red-teaming-cbest-gbest-star-fs-tiber/)

[Purple Teaming](https://www.pentestpartners.com/service/purple-teaming/)

[Attack Surface Assessment](https://www.pentestpartners.com/service/attack-surface-assessment/)

[Attack Surface Management](https://www.pentestpartners.com/service/attack-surface-management-asm/)

[Cloud Testing Services](https://www.pentestpartners.com/service/cloud-testing-services/)

[Physical Security Testing](https://www.pentestpartners.com/service/physical-security-testing/)

[OT, ICS, IIot Security Testing](https://www.pentestpartners.com/service/ot-ics-iiot-security-testing/)

[Transport Systems Testing ](https://www.pentestpartners.com/service/transport-systems-testing/)

Detect and Respond ▾

[Incident Response](https://www.pentestpartners.com/service/incident-response/)

[ Incident Response Maturity Assessment](https://www.pentestpartners.com/service/incident-response-maturity-assessment/)

[Digital Forensic Investigations](https://www.pentestpartners.com/service/digital-forensic-investigations/)

[Digital Forensics Expert Witness](https://www.pentestpartners.com/service/digital-forensics-expert-witness/)

[Dark Web Annual OSINT Assessment](https://www.pentestpartners.com/service/dark-web-annual-monitoring-osint-assessment/)

[Exposure and Identity Risk Assessment](https://www.pentestpartners.com/service/exposure-and-identity-risk-assessment/)

[Managed Detection & Response](https://www.pentestpartners.com/service/managed-detection-response/)

[Compromise Assessments and Forensic Sweep](https://www.pentestpartners.com/service/compromise-assessment/)

Improve and Protect ▾

[Security Architecture](https://www.pentestpartners.com/service/security-architecture/)

[Secure Software Development (SDLC)](https://www.pentestpartners.com/service/secure-software-development-sdlc/)

[Cloud Configuration and Best Practice](https://www.pentestpartners.com/service/cloud-configuration-and-best-practice/)

[Cyber Security Gap Analysis](https://www.pentestpartners.com/service/cyber-security-gap-analysis/)

[Cyber Security Maturity Assessment (CSMA)](https://www.pentestpartners.com/service/cyber-security-maturity-assessment-csma/)

[Security Training](https://www.pentestpartners.com/service/security-training/)

[Third-party Vendors Selection and Assurance](https://www.pentestpartners.com/service/third-party-vendors-selection-and-assurance/)

[Virtual CISO](https://www.pentestpartners.com/service/virtual-ciso/)

[Proactive Advanced Password Auditor (Papa)](https://www.pentestpartners.com/service/proactive-advanced-password-auditor-papa/)

Comply ▾

[Cyber Essentials and Cyber Essentials Plus](https://www.pentestpartners.com/service/cyber-essentials-cyber-essentials-plus/)

[Formal Certification Preparation](https://www.pentestpartners.com/service/formal-certification-preparation/)

[PCI ROC Level 1 Assessment](https://www.pentestpartners.com/service/pci-roc-level-1-assessment/)

[PCI SAQ Assessment](https://www.pentestpartners.com/service/pci-saq-assessment/)

[PCI Scoping Workshop](https://www.pentestpartners.com/service/pci-scoping-workshop/)

Industries ▾

[Finance](https://www.pentestpartners.com/security-blog/industries/finance/)

[Healthcare](https://www.pentestpartners.com/security-blog/industries/healthcare/)

[Retail & Consumer](https://www.pentestpartners.com/security-blog/industries/retail-and-consumer/)

[Transport](https://www.pentestpartners.com/security-blog/industries/transport/)

About Us ▾

[About Us](https://www.pentestpartners.com/about-us/)

[In the News](https://www.pentestpartners.com/about-us/in-the-news/)

[Our Team](https://www.pentestpartners.com/about-us/meet-the-team/)

[Careers](https://www.pentestpartners.com/about-us/careers/)

[Vulnerability Disclosure Policy](https://www.pentestpartners.com/about-us/vulnerability-disclosure-policy/)

[Our Vision & Values](https://www.pentestpartners.com/our-vision-and-values/)

[Blog](/security-blog/)

[Videos](/hack-demo-videos/)

[Events](/events-and-speaking/)

[Contact Us](/contact-us/)

![You can’t stop me. MS Teams session hijacking and bypass](https://www.pentestpartners.com/wp-content/uploads/2022/09/mstshab-headline-1-1024x576.png)

  * Security Blog 
  * Vulnerabilities and Disclosures 

# You can’t stop me. MS Teams session hijacking and bypass

###  Jan Masters 

**22 Sep 2022** 5 Min Read 

  * [ ![](https://www.pentestpartners.com/wp-content/uploads/2025/05/linkedin-icon-footer.svg) ](https://www.linkedin.com/company/pen-test-partners/)
  * [ ![](https://www.pentestpartners.com/wp-content/uploads/2025/05/x-icon-footer.svg) ](https://x.com/PentestPartners)
  * [ ![](https://www.pentestpartners.com/wp-content/uploads/2025/05/youtube-icon-footer.svg) ](https://www.youtube.com/channel/UC2HCAhj6JiOsV_PcMFrjykw)

Also on this page ▾

  * Related services
  * Related blogs

How cleartext session tokens are stored in an unsecured directory that can be stolen and used to impersonate a Teams user.

### TL;DR

Microsoft Teams stores unencrypted session tokens and cached conversations in users’ roaming AppData, which can be used by an attacker to gain access to the victim’s Teams account without having to authenticate or contend with potential conditional access policies.

This is a design choice by Microsoft as the folder is located in \AppData\Roaming\, which is a folder designed to be synchronised with folder redirection and similar technologies for user convenience. Imagine the frustration IT departments would be faced with if their Citrix users had to log into Teams every single morning. You can almost hear the angry mob with torches and pitchforks.

We leveraged this on a client engagement when I compromised a central file server, which held users’ roaming AppData.

##### ![](https://www.pentestpartners.com/wp-content/uploads/2022/09/mstshab1.png)

##### **Figure 1 – Compromised file server**

Before I kick off, credit where credit is due. Vectra’s research into the [Teams cleartext auth token](https://www.vectra.ai/blogpost/undermining-microsoft-teams-security-by-mining-tokens) issue first broke via BleepingComputer, and covers the ins-and-outs of Microsoft’s ([soon to be sunsetted](https://twitter.com/TandonRish/status/1408085784016539653)) Electron framework. This blog will cover this topic from a different perspective with more of an emphasis on exploitation and it’s potential use cases.

### Introduction

Microsoft Teams stores a multitude of files within the following file path C:\Users\UserNameHere\AppData\Roaming\Microsoft\Teams, which includes configuration files, preferences, log files, application related files, and cleartext session tokens within an SQLite file.

![](https://www.pentestpartners.com/wp-content/uploads/2022/09/mstshab2.png)

##### **Figure 2 – Sample content from Cookies database**

The cookie sqlite database contains the following cookies:

**Host**| **Cookie**  
---|---  
.asm.skype.com| platformid_asm  
.asm.skype.com| skypetoken_asm  
.asyncgw.teams.microsoft.com| platformid_asm  
.asyncgw.teams.microsoft.com| skypetoken_asm  
.bing.com| MUID  
.c.bing.com| SRM_B  
.login.microsoftonline.com| CCState  
.login.microsoftonline.com| ESTSAUTHPERSISTENT  
.login.microsoftonline.com| ch  
.office.com| MUID  
.officeapps.live.com| timeZoneId  
.tasks.office.com| PlannerWebSessionId  
.teams.microsoft.com| SSOAUTHCOOKIE  
.teams.microsoft.com| authtoken ***REDACTED***| clienttype  
.teams.microsoft.com| platformid_asm  
.teams.microsoft.com| skypetoken_asm  
.teams.microsoft.com| tenantId  
.youtube.com| CONSENT  
.youtube.com| VISITOR_INFO1_LIVE  
apps.powerapps.com| PACookieRolloutBucketProd  
forms.office.com| MSFPC  
login.microsoftonline.com| SSOCOOKIEPULLED  
login.microsoftonline.com| buid  
login.microsoftonline.com| fpc  
outlook.office.com| ***REDACTED-SUSPECT-TOKEN***outlook.office.com| Micro***REDACTED-SUSPECT-TOKEN***pentestpartners.sharepoint.com| ***REDACTED-SUSPECT-TOKEN***pentestpartners.sharepoint.com| Micro***REDACTED-SUSPECT-TOKEN***s02-emea.prd.attend.teams.microsoft.com| ***REDACTED-SUSPECT-TOKEN***s02-emea.prd.attend.teams.microsoft.com| Micro***REDACTED-SUSPECT-TOKEN***s03-emea.prd.attend.teams.microsoft.com| ***REDACTED-SUSPECT-TOKEN***s03-emea.prd.attend.teams.microsoft.com| Micro***REDACTED-SUSPECT-TOKEN***shared.officeapps.live.com| DcLcid  
tasks.teams.microsoft.com| ai_user  
tasks.teams.microsoft.com| ***REDACTED-SUSPECT-TOKEN***tasks.teams.microsoft.com| Micro***REDACTED-SUSPECT-TOKEN***teams.microsoft.com| TSREGIONCOOKIE  
teams.microsoft.com| storedTheme  
teams.microsoft.com| deviceId  
teams.microsoft.com| firstTimeLaunch  
teams.microsoft.com| MUIDB  
teams.microsoft.com| clocale  
teams.microsoft.com| ringFinder  
teams.microsoft.com| minimumVersionClientUpdateTries  
ukc-excel.officeapps.live.com| DcLcid  
ukc-excel.officeapps.live.com| ***REDACTED-SUSPECT-TOKEN***ukc-excel.officeapps.live.com| PageLoadSkeletonState  
ukc-word-edit.officeapps.live.com| DcLcid  
ukc-word-edit.officeapps.live.com| ***REDACTED-SUSPECT-TOKEN***ukc-word-edit.officeapps.live.com| Micro***REDACTED-SUSPECT-TOKEN***Secure and common standards stipulate that all sensitive files, especially credentials, are encrypted to reduce the threat and likelihood of session hijacking via plaintext viewing.

Technically, using Teams with Edge or any Chromium-based browsers is a stronger choice as they encrypt cookie storage by default. However, Teams cannot encrypt its cookie database file as it needs to follow users around different devices.

### Exploitation

Exploitation is simple and does not require the use of any special tools, such as Mimikatz to extract cached credentials from memory. Copy and paste will do, which has the advantage of not alerting anti-virus software.

The following steps summarise the chain of exploitation:

  * Extract the contents of C:\Users\UserNameHere\AppData\Roaming\Microsoft\Teams. 
  * You can optimise this by only copying the necessary files: 
  * IndexDB
  * Local Storage
  * Session Storage
  * Cookies
  * Cookies-journal
  * desktop-config.json
  * json
  * Preferences
  * QuotaManager
  * QuotaManager-journal
  * json
  * json
  * json
  * TransportSecurity
  * This optimisation reduces the size from ~2 GB to 43.5 MB in my case
  * Spin up a virtual machine with Teams installed.
  * Replace your \Microsoft\Teams folder with the victim’s.
  * Open Teams.

Congratulations! You now have access to their Teams account for you to search for juicy content or you could leverage this to socially engineer staff into doing your dirty work. Why should I waste computing power attempting to capture and/or crack hashed passwords when I can review internal communications to find credentials, or I could just ask the right people as you.

The remarkable thing about session tokens is that you have already authenticated and satisfied any requirements such as multi-factor authentication, coming from a trusted geolocation or IP address; conditional access policies will not save you. Anti-virus software will not save you.

![](https://www.pentestpartners.com/wp-content/uploads/2022/09/mstshab3.png)

##### **Figure 3 – authenticated Teams session whilst PowerPoint is unauthenticated.**

### Snooping. Cached conversations

Teams also caches conversations, both direct messages and channel communications using Google’s LevelDB database structure, which stores .ldb files that can either be parsed or read as is. An attacker with access to multiple users Teams folder could leverage their access to mass parse these files to identify sensitive data such as internal communications and passwords.

Alex Bilz has researched Microsoft Teams from a forensics perspective and has developed tooling to parse these files; you can read more about his thesis work here <https://www.alexbilz.com/post/2021-09-09-forensic-artifacts-microsoft-teams/>.

![](https://www.pentestpartners.com/wp-content/uploads/2022/09/mstshab4.png)

##### **Figure 4 – Goodbye Tom!**

### Conclusion

Unfortunately you cannot mitigate this threat and I don’t believe it will be fixed by Microsoft… The only thing you can do is implement monitoring and alerting for the following file paths:

  * Windows: %AppData%\Microsoft\Teams\
  * MacOS: /Library/Application Support/Microsoft/Teams/
  * Linux: /.config/Microsoft/Microsoft Teams/

It should be noted that access logs within Azure AD do not provide any information as stolen tokens are not subjected to authentication.

### API Penetration Testing

Test your APIs for authentication, injection, and data exposure risks that could compromise your services.

[Learn more](https://www.pentestpartners.com/service/api-penetration-testing/)

[ ![Decoding Rust strings ](https://www.pentestpartners.com/wp-content/uploads/2026/06/headline-rust-strings.png) __ ](https://www.pentestpartners.com/security-blog/decoding-rust-strings/)

  * Hardware Hacking 

##### Decoding Rust strings 

7 Min Read 

Jun 23, 2026

[ ![PTP Cyber Fest 2026. Built for people to get involved ](https://www.pentestpartners.com/wp-content/uploads/2026/06/ptp-cyber-fest-blog-shameless-headline.png) __ ](https://www.pentestpartners.com/security-blog/ptp-cyber-fest-2026-built-for-people-to-get-involved/)

  * Shameless Self Promotion 

##### PTP Cyber Fest 2026. Built for people to get involved 

6 Min Read 

Jun 12, 2026

[ ![ClickFix, CrashFix and the growing family of copy and paste attacks ](https://www.pentestpartners.com/wp-content/uploads/2026/06/Clickfix-headline-joew2.png) __ ](https://www.pentestpartners.com/security-blog/clickfix-crashfix-and-the-growing-family-of-copy-and-paste-attacks/)

  * Digital Forensics and Incident Response 

##### ClickFix, CrashFix and the growing family of copy and paste attacks 

13 Min Read 

Jun 10, 2026
