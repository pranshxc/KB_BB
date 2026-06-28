---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-26_f5-networks-endpoint-inspector-browser-to-rce.md
original_filename: 2019-06-26_f5-networks-endpoint-inspector-browser-to-rce.md
title: F5 Networks Endpoint Inspector – Browser-to-RCE?
category: documents
detected_topics:
- supply-chain
- access-control
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- supply-chain
- access-control
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 3a79c4867cb11316db9a1fbd125fcccad7be96bcc76b2fbc54f213ccf23f3ba3
text_sha256: f93376ab813880a9a0ef1cbcd2c7fe90ee6b5d0a804f6fe252121b3c29a15c29
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# F5 Networks Endpoint Inspector – Browser-to-RCE?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-26_f5-networks-endpoint-inspector-browser-to-rce.md
- Source Type: markdown
- Detected Topics: supply-chain, access-control, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `3a79c4867cb11316db9a1fbd125fcccad7be96bcc76b2fbc54f213ccf23f3ba3`
- Text SHA256: `f93376ab813880a9a0ef1cbcd2c7fe90ee6b5d0a804f6fe252121b3c29a15c29`


## Content

---
title: "F5 Networks Endpoint Inspector – Browser-to-RCE?"
page_title: "F5 Networks Endpoint Inspector - Browser-to-RCE? | Pen Test Partners"
url: "https://www.pentestpartners.com/security-blog/f5-networks-endpoint-inspector-browser-to-rce/"
final_url: "https://www.pentestpartners.com/security-blog/f5-networks-endpoint-inspector-browser-to-rce/"
authors: ["Dave U. Ramdon"]
programs: ["F5"]
bugs: ["RCE"]
publication_date: "2019-06-26"
added_date: "2022-11-14"
source: "pentester.land/writeups.json"
original_index: 5185
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

![F5 Networks Endpoint Inspector – Browser-to-RCE?](https://www.pentestpartners.com/wp-content/uploads/2019/06/rce-me.png)

  * Vulnerabilities and Disclosures 

# F5 Networks Endpoint Inspector – Browser-to-RCE?

###  Dave U. Ramdon 

**26 Jun 2019** 5 Min Read 

  * [ ![](https://www.pentestpartners.com/wp-content/uploads/2025/05/linkedin-icon-footer.svg) ](https://www.linkedin.com/company/pen-test-partners/)
  * [ ![](https://www.pentestpartners.com/wp-content/uploads/2025/05/x-icon-footer.svg) ](https://x.com/PentestPartners)
  * [ ![](https://www.pentestpartners.com/wp-content/uploads/2025/05/youtube-icon-footer.svg) ](https://www.youtube.com/channel/UC2HCAhj6JiOsV_PcMFrjykw)

Also on this page ▾

  * Related services
  * Related blogs

If a bug falls in the forest, and the vendor denies that it’s a bug, is it still a bug? ?

### TL;DR?

The F5 Endpoint Inspector is an application which can be called from a web browser to scan a client for compliance.

We found it can be abused to run arbitrary code, triggered by visiting a malicious website.

There’s a few pre-requisites to get it working, and it’s a bit tougher to get it working “cleanly” (without the user having to click much).

We reported this issue to F5, who say it is “not considered a vulnerability”. So they won’t be fixing it any time soon, apparently.

### Eh? Let me see?

Ok, let’s have a look at this not-a-bug:

Here’s what’s happening:

  * We browse to http://naughty.website/. That website contains a “specially-crafted” f5-epi:// URI. This causes the F5 Endpoint Inspector to run.
  * A UAC box pops up, obviously trying to run a process signed by the legitimate F5 Networks certificate.
  * Then we get powershell.exe popping up, running as a subprocess of f5instd.exe, at high integrity (that’s with admin privileges).

To be fair, this is the “clean” version of the exploit. I’ll talk about the “dirty” version later.

### F5 says it’s NOT a bug, so what’s the problem?

They say there’s too many pre-requisites for them to consider it a bug.

Here are the basic pre-requisites to not-exploit this not-a-bug:

  * The affected user has to have admin privileges, so they can click through the UAC popup.
  * The attacker has to have a **trusted** code-signing certificate to sign a malicious CAB file.

That’s all.

If you want to not-exploit the not-a-bug cleanly (with only a clean, UAC popup for an F5-signed binary), the CAB file has to be signed by “F5 Networks Inc”, “F5 Networks” or “uRoam Inc”. The f5instd.exe binary checks for those strings in the “Signer Name” field of the signature:

![](https://www.pentestpartners.com/wp-content/uploads/2019/06/signername1.png)

It’s up to you to decide how realistic it would be to get a trusted code-signing certificate with any of those names. I will say, that “uRoam Inc” may not actually exist, since F5 bought it in 2003. That’s a little tip if you fancy [trying one of the more elaborate workarounds to execute arbitrary code](https://www.wikihow.com/Incorporate-a-Business).

![](https://www.pentestpartners.com/wp-content/uploads/2019/06/wikhow.png)

However, regardless, even if the “Signer Name” in the CAB signature isn’t one of those three strings, arbitrary code **will still run**. The user just has to click through another warning.

This is (what I guess I’m calling) the “dirty” version:

**Note:** a URL whitelist pop up box usually shows up on a new site, but it’s really inconsistent

Another prompt asks the user if they really want to extract the malicious CAB file, despite the fact it’s signed by “Your Employer!” rather than F5 or uRoam.

Anyway, that’s the reason F5 say it’s NOT a bug. So I guess it’s not a bug! Don’t worry about it.

### What did F5 actually say?

F5 said this to us:

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteOpen.png)

_Respective teams have reviewed the report you have shared and it was determined that the findings is not considered a vulnerability._

_The installation popup clearly shows the signer and the name and also displays a warning message. This behavior is no different from user downloading a file from internet and clicking on it to run it in the browser._

_There is no automatic privilege escalation here either. If the installation required admin rights and user does not have those, he won’t be able to install the package._

![](https://www.pentestpartners.com/wp-content/uploads/2018/07/QuoteClose.png)

### What do we say?

I think… that I…. disagree. Here’s a few questions:

  * Why allow CABs signed by 3rd party certificates at all? Blocking all 3rd party certificate would definitely make this less easy to exploit?
  * Why not check more than just the “Signer Name” field in the certificate before extracting and processing the CAB? It’s, y’know, a certificate. There’s other bits of it you can check.
  * Why are you updating your software by extracting CAB files in 2019? There are better ways to do this.
  * “Also, uhh, this is less of a question and more of a statement”: yes, this is different from a user downloading a file from the internet and clicking on it to run it.

On top of this, **F5 are a CVE Numbering Authority (CNA)**. So they decide what gets given CVEs. **They decide what is considered insecure** in their own products.

Is there an inherent conflict of interest in having companies decide what’s a vulnerability and what’s not?

### “Pls show me how to do the pwn”

I’m going to hold off on details for the minute. Maybe F5 will change their minds. Let’s see.

### Timeline

23/05/2019 – Reported to F5  
27/05/2019 – Confirmation of receipt from F5, key exchange  
29/05/2019 – Issue given a tracking number by F5.  
01/06/2019 – We check with F5 for updates.  
03/06/2019 – F5 request a CVSS score estimate from us.  
03/06/2019 – We share a CVSS score with them. No response.  
19/06/2019 – We check for an update.  
19/06/2019 – F5 reply saying it’s not an issue.

### External Infrastructure Testing

Test your internet-facing systems for vulnerabilities that attackers could exploit to gain unauthorised access.

[Learn more](https://www.pentestpartners.com/service/external-infrastructure-testing/)

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
