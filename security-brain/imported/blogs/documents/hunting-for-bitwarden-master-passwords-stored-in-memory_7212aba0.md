---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-08_hunting-for-bitwarden-master-passwords-stored-in-memory.md
original_filename: 2023-06-08_hunting-for-bitwarden-master-passwords-stored-in-memory.md
title: Hunting for Bitwarden master passwords stored in memory
category: documents
detected_topics:
- cloud-security
- api-security
- mobile-security
- supply-chain
- sso
- access-control
tags:
- imported
- documents
- cloud-security
- api-security
- mobile-security
- supply-chain
- sso
- access-control
language: en
raw_sha256: 7212aba0020a4f1a60acf7dfad1ed5485c4f546edfb2c1c2c7052553ca3fec6a
text_sha256: ee733d1e3fc611ac769c1f38d85becbed465aa0832880c1065dccf967ded63c7
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: true
---

# Hunting for Bitwarden master passwords stored in memory

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-08_hunting-for-bitwarden-master-passwords-stored-in-memory.md
- Source Type: markdown
- Detected Topics: cloud-security, api-security, mobile-security, supply-chain, sso, access-control
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: True
- Raw SHA256: `7212aba0020a4f1a60acf7dfad1ed5485c4f546edfb2c1c2c7052553ca3fec6a`
- Text SHA256: `ee733d1e3fc611ac769c1f38d85becbed465aa0832880c1065dccf967ded63c7`


## Content

---
title: "Hunting for Bitwarden master passwords stored in memory"
page_title: "Hunting for Bitwarden master passwords stored in memory | Hexiosec Blogs"
url: "https://redmaple.tech/blogs/2023/extract-bitwarden-vault-passwords/"
final_url: "https://hexiosec.com/blog/extract-bitwarden-vault-passwords/"
authors: ["Naz Markuta (@NazMarkuta)"]
programs: ["Bitwarden"]
bugs: ["Information disclosure", "Memory leak", "Local Privilege Escalation"]
publication_date: "2023-06-08"
added_date: "2023-07-04"
source: "pentester.land/writeups.json"
original_index: 1066
---

__ In -- days the NCSC turns off Mail & Web Check. 

[Gain advice on practical next steps](/solutions/ncsc-web-check-mail-check-alternative)

[ ![Hexiosec logo](/brand/logo_hexiosec.svg) ![Hexiosec logo](/brand/logo_hexiosec_darkbg.svg) ](/)

☰

  * [Home](/)
  * Products

[![](/brand/logo_asm.svg) __](/asm)[![](/brand/logo_transfer.svg)__](/transfer)

[Hexiosec ASM](/asm)

Hexiosec ASM helps you identify, monitor, and secure digital assets. Gain real-time insights, prioritise risks, and protect against cyber threats with our expert-developed attack surface management platform.

Features

  * [Asset Discovery](/asm/asset-discovery)
  * [Vulnerability Detection](/asm/vulnerability-scanning)
  * [Cloud Connector for AWS, Azure & GCP](/asm/cloud-connector)
  * [Actionable Cyber Insights](/asm/reporting)
  * [Gain Access to Detailed Scan Data](/asm/detailed-data)
  * [Cyber Risk Management](/asm/cyber-risk-management)

Use Cases

  * [NCSC Web and Mail Check Replacement](/solutions/ncsc-web-check-mail-check-alternative)
  * [Manage Your Attack Surface](/solutions/attack-surface-management)
  * [Technical Due Diligence](/solutions/due-diligence)
  * [Inform Lead Qualification](/solutions/lead-qualification)
  * [Third-Party Supply Chain Risks](/solutions/third-party-supply-chain-risks)
  * [Evolving Threat Landscape](/asm/evolving-threat-landscape)

External Attack Surface Management

  * [FAQ](/asm#asm-faq)
  * [Pricing](/asm/pricing)
  * [Sign in](https://asm.hexiosec.com)
  * [Book a Demo](/asm/demo)

Hexiosec ASM Resources

  * [Product Updates](/blog/?filter=Product%20Features)
  * [User Guides](https://docs.hexiosec.com/asm)
  * [API Documentation](https://asm.hexiosec.com/api/ui)
  * [Jisc Chest Agreement](/jisc-chest/)
  * [Videos](https://www.youtube.com/@Hexiosec/videos)

[Hexiosec Transfer](/transfer)

Hexiosec Transfer provides secure file transfer with end-to-end encryption and UK data sovereignty. Designed for organisations that need control, compliance, and confidentiality.

Features & Benefits

  * [All Features Overview](/transfer/features)
  * [Microsoft Outlook Integration](/transfer/outlook-addin)
  * [True End-to-End Encrypted File Transfer](/transfer/end-to-end-encryption)
  * [GDPR-Compliant Secure File Transfer](/transfer/gdpr)

Hexiosec Transfer Resources

  * [User Guides](https://transfer-docs.hexiosec.com/)
  * [CLI Documentation](https://transfer-docs.hexiosec.com/integrations/cli/)
  * [Jisc Chest Agreement](/jisc-chest/)

Secure File Transfer

  * [FAQ](/transfer#transfer-faq)
  * [Pricing](/transfer/pricing)
  * [Sign in](https://transfer.hexiosec.com)
  * [Book a Demo](/transfer/demo)

  * [Services](/services/)

[![](/brand/logo_services.svg) __](/services/)[__Cyber Security Testing __](/services/technical-security-testing)[__Secure Digital Transformation __](/services/secure-digital-transformation)[__Cyber Advisory & Assessment __](/services/cyber-security-improvement)

[Services Overview](/services/)

Experts dedicated to solving your most complex cyber security challenges. Stay ahead of threats and vulnerabilities with our suite of cyber services.

[Cyber Security Testing](/services/technical-security-testing)

We provide security and penetration testing services. We can test all applications, services, networks, infrastructures and devices.

Cyber Security Testing Services

  * [Penetration Testing](/services/technical-security-testing#pentesting)
  * [Endpoint Security Tests](/services/technical-security-testing#endpoint)
  * [Microsoft 365 and Google Workspace Security Reviews](/services/technical-security-testing#office)
  * [Application Security Testing](/services/test-application-security)
  * [Device Security Review](/services/protect-devices)

[Case Studies](/case-studies)
  * [Providing a Complete Application Test](/services/client-stories/app-test)
  * [Testing if a Corporate Laptop is Actually Locked Down](/services/client-stories/device-test)
  * [Finding and Testing Online Assets](/services/client-stories/external-test)
  * [Testing Microsoft 365 Configuration Security](/services/client-stories/m365-test)
  * [Testing a Giant Corporate Network](/services/client-stories/network-test)

[Secure Digital Transformation](/services/secure-digital-transformation)

Transform your organisation securely with Hexiosec's Secure Digital Transformation services. Enhance cyber resilience, protect sensitive data, and adopt new technologies with confidence and expert guidance.

Secure Digital Transformation Services

  * [Secure Cloud Infrastructure Build](/services/secure-digital-transformation#cloudinf)
  * [Secure Cloud Design and Architecture](/services/secure-digital-transformation#clouddesign)
  * [Secure Cloud Application Development](/services/secure-digital-transformation#cloudapp)
  * [Firmware Development](/services/secure-digital-transformation#firmware)
  * [Private LLMs and AI Solutions](/services/secure-digital-transformation#ml)
  * [Secure Cloud Migration](/services/safely-use-cloud)

[Case Studies](/case-studies)
  * [Building a Secure Cloud Infrastructure](/services/client-stories/secure-cloud-build)
  * [Custom Radio Firmware](/services/client-stories/radio-firmware-dev)
  * [Delivering 40% Cloud Cost Savings](/services/client-stories/cloud-costs)
  * [Streamlining Cloud Processing with Argo](/services/client-stories/cloud-processing)

[Cyber Advisory & Assessment](/services/cyber-security-improvement)

Enhance your company's cyber security with Hexiosec's expert evaluations, maturity assessments, and virtual CISO services. Our team provides tailored advice and implements systematic improvements to safeguard your business against evolving threats.

Advisory & Assessment Services

  * [Cyber Risk Assessments](/services/online-discovery-services#external)
  * [Cyber Security Maturity Assessment](/services/cyber-security-improvement#maturity)
  * [Cyber Security Advisory Services](/services/cyber-security-improvement#advisory)
  * [DevSecOps Review](/services/cyber-security-improvement#devsecops)
  * [Bespoke Research](/services/cyber-security-improvement#research)
  * [Cloud Security Management](/services/manage-cloud-security)
  * [Secure Code Review](/services/build-applications-securely)

[Case Studies](/case-studies)
  * [Providing Cyber Security Leadership](/services/client-stories/strategy)
  * [Locking Down IoT Devices](/services/client-stories/device-lockdown)
  * [Protecting Software Intellectual Property](/services/client-stories/ip-protection)

  * Resources & Insights

[__Blogs __](/blog/)

__

Documentation & Resources

__

[Blogs](/blog/)

Keep up to date on the latest cyber threats with the latest news, insights, and technical blogs from the Hexiosec team.

Featured Blogs

[ ![](/blog/software-security-code-of-practice-self-assessment-guide/DSITAmb3-Update-Header.webp) ](/blog/software-security-code-of-practice-self-assessment-guide/)[A Practical Guide to the Software Security Code of Practice Self-Assessment](/blog/software-security-code-of-practice-self-assessment-guide)

[ ![](/blog/software-security-code-of-practice-self-assessment/DSITAmb2-Update-Header.webp) ](/blog/software-security-code-of-practice-self-assessment/)[What We Found - Our Self-Assessment Against the 14 Principles](/blog/software-security-code-of-practice-self-assessment)

[ ![](/blog/ncsc-web-check-mail-check-what-to-do-next/WebCheck-MailCheck-Next-Header.webp) ](/blog/ncsc-web-check-mail-check-what-to-do-next/)[NCSC Web Check and Mail Check Are Gone - Here's What to Do Next](/blog/ncsc-web-check-mail-check-what-to-do-next)

Recent Blogs

[ ![](/blog/asm-may-2026-update/May26-Update-Header.webp) ](/blog/asm-may-2026-update/)[New ASM Features and Improvements | May 2026](/blog/asm-may-2026-update)

[ ![](/blog/asm-april-2026-update/April26-Update-Header.webp) ](/blog/asm-april-2026-update/)[New ASM Features and Improvements | April 2026](/blog/asm-april-2026-update)

[ ![](/blog/software-security-code-of-practice-adoption/DSITAmb1-Update-Header.webp) ](/blog/software-security-code-of-practice-adoption/)[Why Hexiosec Adopted the UK Software Security Code of Practice](/blog/software-security-code-of-practice-adoption)

Documentation & Resources

Find product documentation, user guides, API references, and other helpful resources to get the most out of our services.

Product Documentation

  * [Hexiosec ASM User Guides](https://docs.hexiosec.com/asm)
  * [Hexiosec Transfer User Guides](https://transfer-docs.hexiosec.com/)

API Documentation

  * [Hexiosec ASM API Documentation](https://asm.hexiosec.com/api/ui)
  * [Hexiosec Transfer CLI Documentation](https://transfer-docs.hexiosec.com/integrations/cli/)

More Resources

  * [Open Source](https://github.com/hexiosec)
  * [Videos](https://www.youtube.com/@Hexiosec/videos)
  * [Product Updates](/blog/?filter=Product%20Features)

  * Clients & Partners

  * [Case Studies](/case-studies)
  * [MSPs](/solutions/managed-service-providers)
  * Company

  * [History](/about)
  * [Our People](/people)
  * [Careers](/careers)
  * [Contact Us](/contact)
  * [Latest News](/news)

[Contact Us](/contact/)

  * [Home](/)
  * Products __

  *  * Hexiosec ASM __

  * [Hexiosec ASM](/asm)

Features

  * [Asset Discovery](/asm/asset-discovery)
  * [Vulnerability Detection](/asm/vulnerability-scanning)
  * [Cloud Connector for AWS, Azure & GCP](/asm/cloud-connector)
  * [Actionable Cyber Insights](/asm/reporting)
  * [Gain Access to Detailed Scan Data](/asm/detailed-data)
  * [Cyber Risk Management](/asm/cyber-risk-management)

Use Cases

  * [NCSC Web and Mail Check Replacement](/solutions/ncsc-web-check-mail-check-alternative)
  * [Manage Your Attack Surface](/solutions/attack-surface-management)
  * [Technical Due Diligence](/solutions/due-diligence)
  * [Inform Lead Qualification](/solutions/lead-qualification)
  * [Third-Party Supply Chain Risks](/solutions/third-party-supply-chain-risks)
  * [Evolving Threat Landscape](/asm/evolving-threat-landscape)

External Attack Surface Management

  * [FAQ](/asm#asm-faq)
  * [Pricing](/asm/pricing)
  * [Sign in](https://asm.hexiosec.com)
  * [Book a Demo](/asm/demo)

Hexiosec ASM Resources

  * [Product Updates](/blog/?filter=Product%20Features)
  * [User Guides](https://docs.hexiosec.com/asm)
  * [API Documentation](https://asm.hexiosec.com/api/ui)
  * [Jisc Chest Agreement](/jisc-chest/)
  * [Videos](https://www.youtube.com/@Hexiosec/videos)
  * Hexiosec Transfer __

  * [Hexiosec Transfer](/transfer)

Features & Benefits

  * [All Features Overview](/transfer/features)
  * [Microsoft Outlook Integration](/transfer/outlook-addin)
  * [True End-to-End Encrypted File Transfer](/transfer/end-to-end-encryption)
  * [GDPR-Compliant Secure File Transfer](/transfer/gdpr)

Hexiosec Transfer Resources

  * [User Guides](https://transfer-docs.hexiosec.com/)
  * [CLI Documentation](https://transfer-docs.hexiosec.com/integrations/cli/)
  * [Jisc Chest Agreement](/jisc-chest/)

Secure File Transfer

  * [FAQ](/transfer#transfer-faq)
  * [Pricing](/transfer/pricing)
  * [Sign in](https://transfer.hexiosec.com)
  * [Book a Demo](/transfer/demo)
  * Services __

  *  * [Services Overview](/services/)
  * Cyber Security Testing __

  * Cyber Security Testing Services

  * [Penetration Testing](/services/technical-security-testing#pentesting)
  * [Endpoint Security Tests](/services/technical-security-testing#endpoint)
  * [Microsoft 365 and Google Workspace Security Reviews](/services/technical-security-testing#office)
  * [Application Security Testing](/services/test-application-security)
  * [Device Security Review](/services/protect-devices)
[Case Studies](/case-studies)
  * [Providing a Complete Application Test](/services/client-stories/app-test)
  * [Testing if a Corporate Laptop is Actually Locked Down](/services/client-stories/device-test)
  * [Finding and Testing Online Assets](/services/client-stories/external-test)
  * [Testing Microsoft 365 Configuration Security](/services/client-stories/m365-test)
  * [Testing a Giant Corporate Network](/services/client-stories/network-test)
  * Secure Digital Transformation __

  * Secure Digital Transformation Services

  * [Secure Cloud Infrastructure Build](/services/secure-digital-transformation#cloudinf)
  * [Secure Cloud Design and Architecture](/services/secure-digital-transformation#clouddesign)
  * [Secure Cloud Application Development](/services/secure-digital-transformation#cloudapp)
  * [Firmware Development](/services/secure-digital-transformation#firmware)
  * [Private LLMs and AI Solutions](/services/secure-digital-transformation#ml)
  * [Secure Cloud Migration](/services/safely-use-cloud)
[Case Studies](/case-studies)
  * [Building a Secure Cloud Infrastructure](/services/client-stories/secure-cloud-build)
  * [Custom Radio Firmware](/services/client-stories/radio-firmware-dev)
  * [Delivering 40% Cloud Cost Savings](/services/client-stories/cloud-costs)
  * [Streamlining Cloud Processing with Argo](/services/client-stories/cloud-processing)
  * Cyber Advisory & Assessment __

  * Advisory & Assessment Services

  * [Cyber Risk Assessments](/services/online-discovery-services#external)
  * [Cyber Security Maturity Assessment](/services/cyber-security-improvement#maturity)
  * [Cyber Security Advisory Services](/services/cyber-security-improvement#advisory)
  * [DevSecOps Review](/services/cyber-security-improvement#devsecops)
  * [Bespoke Research](/services/cyber-security-improvement#research)
  * [Cloud Security Management](/services/manage-cloud-security)
  * [Secure Code Review](/services/build-applications-securely)
[Case Studies](/case-studies)
  * [Providing Cyber Security Leadership](/services/client-stories/strategy)
  * [Locking Down IoT Devices](/services/client-stories/device-lockdown)
  * [Protecting Software Intellectual Property](/services/client-stories/ip-protection)
  * Resources & Insights __

  *  * [Blogs](/blog/)
  * Documentation & Resources __

  * Product Documentation

  * [Hexiosec ASM User Guides](https://docs.hexiosec.com/asm)
  * [Hexiosec Transfer User Guides](https://transfer-docs.hexiosec.com/)

API Documentation

  * [Hexiosec ASM API Documentation](https://asm.hexiosec.com/api/ui)
  * [Hexiosec Transfer CLI Documentation](https://transfer-docs.hexiosec.com/integrations/cli/)

More Resources

  * [Open Source](https://github.com/hexiosec)
  * [Videos](https://www.youtube.com/@Hexiosec/videos)
  * [Product Updates](/blog/?filter=Product%20Features)
  * Clients & Partners __

  *  * [Case Studies](/case-studies)
  * [MSPs](/solutions/managed-service-providers)
  * Company __

  *  * [History](/about)
  * [Our People](/people)
  * [Careers](/careers)
  * [Contact Us](/contact)
  * [Latest News](/news)
  * [Contact Us](/contact)

![White shape | Hexiosec Logo](/brand/company_logo_only_white.svg)![](/blog/extract-bitwarden-vault-passwords/cover.webp)

[ Research & Case Studies ](/blog/?type=Research+%26+Case+Studies)

# Hunting for Bitwarden master passwords stored in memory

![Naz Markuta](/headshots/naz-headshot-black.png)

8 June 2023

|

12 min Read

|

[Naz Markuta](https://www.linkedin.com/in/naz-markuta/)

[ ](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fhexiosec.com%2Fblog%2Fextract-bitwarden-vault-passwords%2F "Share on LinkedIn") [ ](https://twitter.com/intent/tweet?url=https%3A%2F%2Fhexiosec.com%2Fblog%2Fextract-bitwarden-vault-passwords%2F&text=Hunting+for+Bitwarden+master+passwords+stored+in+memory "Share on X") [ ](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fhexiosec.com%2Fblog%2Fextract-bitwarden-vault-passwords%2F "Share on Facebook") [ ](/blog/index.xml "RSS Blog Feed")

## Contents

  *  * TL;DR
  * Background
  * How to find a known password?
  * Chromium web extensions
  * Desktop app
  * How to find an unknown password?
  * Looking for patterns
  * Memory regions
  * Developing a tool
  * Windows APIs
  * Offensive Go libraries
  * BW-dump
  * Download
  * Conclusion

**A blog post on how I was able to identify unknown master passwords stored in the memory of the Bitwarden web extension and desktop client, after a vault has been locked. I also cover the decisions made for developing a proof of concept to automate the process of extracting potential passwords.**

## TL;DR

It is possible to identify unknown Bitwarden master passwords in memory, even after a vault is locked. We developed a proof of concept tool, called BW-dump, that works on Windows platforms. It was tested with Bitwarden desktop app version (2023.2.0).

**The video belows shows a quick demo** (getting the master password from the Bitwarden web browser extension)  There should have been a video here but your browser does not seem to support it. 

**Update (17/08/2023)** : This particular issue has been assigned CVE-2023-38840

**Update (20/07/2023)** : A patch was released on GitHub ([5813](https://github.com/bitwarden/clients/pull/5813)) which fixes the vulnerability. Bitwarden Desktop version 2023.7.0 and below are vulnerable.

## Background

A few years ago, a GitHub issue relating to the Bitwarden client application ([Erase Master Password in memory after login](https://github.com/bitwarden/desktop/issues/476)) was reported. This issue references an article by a German IT magazine who had tested different password managers.

Some of the tests involved checking whether master passwords are leaked before and after locking, and as a user myself I was curious, so I tried the tests myself.

I started off by focusing on the Bitwarden web browser extension (both for Chrome and MSEdge), where a initial proof of concept was developed. However, after an update in either Chrome and/or Bitwarden fixed the issue, so I was no longer able to identify the password in memory. I then moved onto the Bitwarden Desktop App, where the issue is still present.

## How to find a known password?

To locate a _known_ master password in memory, one can use a tool like [Process Hacker](https://processhacker.sourceforge.io/). Process Hacker allows users to inspect every process that is currently running on their system. It also provides access to process memory space, including a neat string search feature.

### Chromium web extensions

When looking at web browser processes (Chrome or MSEdge) with Process Hacker, you’ll notice there are several child processes. Each process has its own functionality and purpose. This includes web browser extensions, each of which will have a unique process:

![Process Hacker showing multiple Microsoft Edge child processes including extension processes](images/msedge-multiple-processes.webp)

To identify processes associated to web extensions you can inspect the `Command Line` options of each child process, and search for the string `--extension-process`. On Chrome browsers you will have to keep in mind that there are a few default extensions already installed.

Here is an example of an `MSEdge.exe` extension process:

![Edge extension process properties with command line containing –extension-process flag](images/msedge-command-line.webp)

For completeness, the full command line options were:
  
  
  "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --type=renderer --extension-process 
  --disable-gpu-compositing --lang=en-GB --js-flags=--ms-user-locale= --device-scale-factor=1 
  --num-raster-threads=1 --renderer-client-id=19 --time-ticks-at-unix-epoch=-1677594276672537 
  --launch-time-ticks=198758688 --mojo-platform-channel-handle=3960 
  --field-trial-handle=2072,i,6587025175849962187,10098860286187380106,131072 /prefetch:1
  

I couldn’t find a way to identity a browser extension associated with a specific process by only using the `Command Line` option, so I had to checked them all manually. There is probably a better way of doing this.

Anyway, now that an extension process has been identified, we can go ahead and start looking for strings in memory. To do this, first go to process properties, and select the **memory tab**. Next, click on **strings** and select the default settings (unless your test password is 8 characters) type out your plaintext master password as the search query.

![Process Hacker memory strings search showing Bitwarden master password in Edge extension process](images/bw-msedge-memory.webp)

**Where are web extensions stored on a Windows system?**

The Bitwarden extension on MSEdge is installed in folder:
  
  
  %LocalAppData%\Microsoft\Edge\User Data\Default\Local Extension Settings\***REDACTED-SUSPECT-TOKEN***Depending on how many profiles you have in your web browser, instead of `Default`, it could be `Profile X`, where `X` is the profile number. Also keep in mind that each web browser has a unique ID for each extension. For example the Bitwarden web extension has the following IDs:

  * For MSEdge - `jbkfoedolllekgbhcbcoahefnbanhhlh`
  * For Chrome - `nngceckbapebfimnlniiiahkandclblb`

### Desktop app

The Bitwarden desktop application is built using Electron, which is similar to Chromium browsers. It too creates child processes for individual program features. Instead of `--extension-process` in the Command Line options, search for `--no-zygote`. This is the child process where most sensitive memory data is cached, including the master password.

Here is an example of the `Bitwarden.exe` Command Line options:
  
  
  "C:\Users\Tester\AppData\Local\Programs\Bitwarden\Bitwarden.exe" --type=renderer 
  --user-data-dir="C:\Users\Tester\AppData\Roaming\Bitwarden" 
  --app-path="C:\Users\Tester\AppData\Local\Programs\Bitwarden\resources\app.asar" 
  --no-sandbox --no-zygote --first-renderer-process --lang=en-GB --device-scale-factor=1 
  --num-raster-threads=1 --renderer-client-id=4 --time-ticks-at-unix-epoch=-1677594276676209 
  --launch-time-ticks=5708174183 --mojo-platform-channel-handle=2428 
  --field-trial-handle=1892,i,2828961307611671252,14266672126368596536,131072 
  --disable-features=SpareRendererForSitePerProcess,WinRetrieveSuggestionsOnlyOnDemand /prefetch:1
  

And here is an example of the master password found in plaintext in the memory of that child process:

![Process Hacker memory view of Bitwarden desktop process with plaintext master password visible](images/bitwarden-desktop-memory-password.webp)

## How to find an unknown password?

Searching for a known password is quite trivial, but searching for a password that you don’t know is much harder. Especially if you don’t know the length, or where to look. It’s like looking for a needle in a field of haystacks (memory regions).

### Looking for patterns

**Note** : _The following section is based on the Bitwarden MSEdge Chromium extension, which has since been patched. However, the same process was applied to the Bitwarden desktop client, which is still vulnerable._

The best place to start is looking at the bytes around a known master password. For this, I used Process Hacker to generate several process memory dumps, which I then searched through using [010 Editor](https://www.sweetscape.com/010editor/).

Here is an example of a master password found in a memory dump: ![010 Editor hex view of memory dump highlighting master password bytes](images/msedge-memory-dump-010-editor.webp)

Each time I took a snapshot, I restarted the process, unlocked the vault, and then locked it again. I observed that a few hex bytes remained consistent, even after a system reboot. You will notice in the above screenshot that at offset `0x0140` (different for new processes), the following bytes are shown, which I refer to as the password prefix pattern:
  
  
  1  2  3  4  5  6  7  8  9 10 11 12
  Byte: 04 00 00 00 13 00 00 00 01 B1 6C AB XX XX XX ... 00 00
  

Here, `XX` represents an actual master password character byte. Apart from the null byte terminators, the other bytes were unknown. To try figure out what the other bytes represent I did a few tests.

**What happens to these bytes when you change your master password?**

Changing a master password by adding an extra character changes the pattern in two ways:
  
  
  1  2  3  4  5  6  7  8  9 10 11 12
  Before: 04 00 00 00 13 00 00 00 01 B1 6C AB XX XX XX ... 00 00
  After:  04 00 00 00 14 00 00 00 01 C3 5E 54 XX XX XX ... 00 00
  

  * The 5th byte looks like it represents the master password length, as it increments by one, to `0x14` . The password `only the be$t bacons` contains 20 characters (including the spaces), which is `14` in hex.
  * The 10th, 11th, and 12th bytes `0xC35E54` are also changed, although what they are for isn’t obvious.

**What happens when you rotate the encryption keys?**

Bitwarden allows users to rotate account encryption keys, a useful feature when you think your account has been compromised. This option is only available while changing the master password, and is is not enabled by default:

> Rotating your account’s encryption key generates a new encryption key that is used to re-encrypt all Vault data. You should consider rotating your encryption key if your account has been compromised such in a way that someone has obtained your encryption key.
> 
> [Bitwarden Docs](https://bitwarden.com/help/account-encryption-key/#rotate-your-encryption-key)

I opted to change the password back to my previous password, `only the be$t bacon`, so it’s easier to follow. And then I used the option to rotate encryption keys. This produced the following password memory entry:
  
  
  1  2  3  4  5  6  7  8  9 10 11 12 
  Before: 04 00 00 00 14 00 00 00 01 C3 5E 54 XX XX XX XX XX XX ...
  After:  04 00 00 00 13 00 00 00 01 B1 6C AB XX XX XX XX XX XX ...
  

You’ll notice that the 5th, 10th, 11th, and 12th bytes have been changed, and are back to the same as the original screenshot. This means these last three bytes (just before the password) are somehow related to the password plaintext itself, and not the encryption key, which is what I initially thought.

**What happens to these bytes when you use a different Windows version?**

In _some_ cases, when using a different Windows version like 10 or 11, the first byte changes. But I found it not to be consistent enough, as it might be `05`, `02`, or `04` regardless of the version.
  
  
  1  2  3  4  5  6  7  8  9 10 11 12 
  Before: 04 00 00 00 14 00 00 00 01 C3 5E 54 XX XX XX XX XX XX ...
  After:  05 00 00 00 13 00 00 00 01 B1 6C AB XX XX XX XX XX XX ...
  

I tried out other tests but didn’t get much further.

With the information learned so far we known certain bytes remain static. We also know that some are dynamic and depend on the master password. Nevertheless, we can use this data to create a search pattern using a simple regular expression.

To quickly summarise the above I will use the following search template (in 010Editor syntax) as the password prefix pattern:
  
  
  1  2  3  4  5  6  7  8  9 10 11 12
  Byte: 04 00 00 00 ?? 00 00 00 01 ?? ?? ?? ... 00 00
  

  * 1st byte `04` \- possibly Windows version specific.
  * 2nd, 3rd, 4th bytes `00 00 00` \- some kind of separator.
  * 5th byte `??` is master password length - must be `0x08` or above since Bitwarden registration requires passwords to have a minimum of 8 characters.
  * 6th, 7th, and 8th bytes `00 00 00` \- another separator.
  * 9th `01` \- possibly a platform indicator i.e. Windows = `01` and Linux = `03` (not confirmed).
  * 10th, 11th, 12th bytes `?? ?? ??` \- relate to the master password somehow.
  * 13th byte is the start of the actual master password.

This is equivalent to a basic regular expression such as:
  
  
  (\x04|\x05|\x02)\x00\x00\x00[^\x00]\x00\x00\x00\x01[^\x00][^\x00][^\x00]
  

Now we have a search pattern, we need to find the right memory region.

**Note** : The regex search pattern for Bitwarden Desktop app proof of concept is completely different `\x01(?:[^\x00]{3})(?:[(\x20-\x7E)]{8,})`, which results in a large list of potential passwords strings. This could be improved by filtering out known static strings.

### Memory regions

When reviewing a process’s memory with Process Hacker, you’ll notice there are dozens of memory regions, several megabytes worth. Many of which will likely contain results matching the above regex pattern, leading to multiple false positives.

![Process Hacker memory regions list for Bitwarden process](images/bw-memory-regions.webp)

To help filter out false positives, I started to focus on a specific memory region where the password is located, and looked for more patterns. I noticed that each time a new process was started, it contained a static string of bytes at the beginning of the region. This can be seen in the screenshot below:

![Hex view showing static UTF-16 CSS font-face string at start of memory region](images/bw-memory-region-static-font-css.webp)

You can see what appears to be a CSS (Cascading Style Sheet) resource, along with other attributes. It is encoded with UTF-16 Big Endian, typically seen on Windows platforms. To decode this value one can use [CyberChef](https://gchq.github.io/CyberChef/) with the options **From Hex** and **Decode Text (UTF-16 BE)**.

Do that and we get the following:
  
  
  @font-face {
  font-family: "Open Sans";
  font-style: italic;
  font-weight: 300;
  font-display: auto;
  src: url(../popup/fonts/Open_Sans-italic-300.woff) format("woff");
  unicode-range: U+0-10FFFF;
  }
  

I now had a static string which I knew existed in the same memory region as the master password, and a search pattern to use. To make searching more efficient, I applied another filter to only include specific memory regions.

To inspect memory regions types and protections you can use Process Hacker, or the [VMMap](https://learn.microsoft.com/en-us/sysinternals/downloads/vmmap) sysinternals tool by Microsoft, which is shown below.

![VMMap highlighting a private data memory region with read/write protection](images/vmmap-memory-region-type.webp)

As shown, the selected memory region (where the master password is found) has a memory type of **Private Data** with **Read/Write** Protection. The size (188 KB) varied between 150 KB - 260 KB, which was also used as a search criterion.

Now that I had good understanding of what to search for, I started to think about building a tool to try automate the process.

## Developing a tool

I decided to take this opportunity to get more familiar with working with Windows API calls and Golang. My goal was to simulate the same actions performed with Process Hacker, but with a few key benefits.

These are:

  * Doesn’t require Admin privileges - uses the permissions of the logged-in user.
  * Automatically find the right processes.
  * Choose specific memory regions rather than scanning ALL regions.
  * Search for patterns in those memory regions.
  * Filter out possible matches.

I’m not going to go into any real details on the programming side in this blog - as it’s already too long. But I would like to mention the resources I used for development.

### Windows APIs

Microsoft has an extensive list of Windows API functions available for developing Windows programs. The [Windows App Development](https://learn.microsoft.com/en-us/windows/win32/api/_base/) online document is probably the best resource for low-level Windows development. For anything memory related, I recommend reviewing the `memoryapi.h` section found [here](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/).

### Offensive Go libraries

There are dozens of offensive security Go libraries available. I opted to use the following because they worked well during initial testing, and were simple for me to understand.

  * Getting a list of processes (<https://github.com/shirou/gopsutil>)
  * Reading process memory (<https://github.com/0xrawsec/golang-win32>)

To help get a better understanding of Windows API bindings for Golang, I used the Black Hat Go book by Tom Steele, Chris Patten, and Dan Kottmann, which is available on [No Starch Press](https://nostarch.com/blackhatgo). I also used a few examples they provided as a template for my tool.

## BW-dump

BW-dump is a Windows based tool that is capable of extracting master vault passwords from a locked Bitwarden vault. The tool is written in Golang, and makes use of Windows API functions. For the tool to work, you need two requirements:

  * A supported process running.
  * The vault must have been unlocked at least once.

Here is a screenshot of extracting a master password from Bitwarden Desktop (2023.2.0):

![BW-dump output showing multiple extracted master password candidates](images/bw-desktop-example.webp)

You’ll notice results may include the password several times, sometimes with extra characters. This was because it was much harder to figure out the length of the master password to know where the string ends. The earlier version of the tool (which worked on the web browser extension) was much more reliable.

### Download

The proof of concept tool can be downloaded from [my GitHub](https://github.com/markuta/bw-dump), which also includes a release binary. BW-dump version `v1.0.2` only works with the Bitwarden desktop client due to a patch released a few months for the web extension.

**Note** : Since the tool reads the memory of other processes, and I didn’t bother with applying any sort of obfuscation techniques, Windows Defender will rightly flag the compiled binary as malicious.

## Conclusion

Reviewing closed GitHub issues (marked as stale) can lead to interesting bits of research. This blog demonstrates a relatively simple approach to identifying patterns inside process memory, which can be used to find unknown master vault passwords. We developed a proof of concept tool to automate the process.

## Related Posts

[View all blogs](/blog/)

[![](/blog/iot-network-analysis-vmware/AnalysingIoT-Inbody.webp) ](/blog/iot-network-analysis-vmware/)

[ Technical Tutorials & Explainers ](/blog/?type=Technical+Tutorials+%26+Explainers) ## [Analysing IoT Device Network Traffic with VMware Bridge ](/blog/iot-network-analysis-vmware/)

![Naz Markuta](/headshots/naz-headshot-black.png)

[Naz Markuta](https://www.linkedin.com/in/naz-markuta/)

12 December 2023

[![](/blog/dll-hijacking-and-proxying/DLLHijacking-Inbody.webp) ](/blog/dll-hijacking-and-proxying/)

[ Research & Case Studies ](/blog/?type=Research+%26+Case+Studies) ## [Exploiting DLL Hijacking in Windows Electron Apps ](/blog/dll-hijacking-and-proxying/)

![Naz Markuta](/headshots/naz-headshot-black.png)

[Naz Markuta](https://www.linkedin.com/in/naz-markuta/)

18 October 2023

[![](/blog/iris-security-advisory/blog-image.jpg) ](/blog/iris-security-advisory/)

[ Research & Case Studies ](/blog/?type=Research+%26+Case+Studies) ## [Discovering Vulnerabilities In The Iris Mobile App & API ](/blog/iris-security-advisory/)

![Naz Markuta](/headshots/naz-headshot-black.png)

[Naz Markuta](https://www.linkedin.com/in/naz-markuta/)

9 January 2023

[![](/blog/which-privacy/Smart-Spies-Which-Inbody.webp) ](/blog/which-privacy/)

[ Research & Case Studies ](/blog/?type=Research+%26+Case+Studies) ## [Testing Smart Device Privacy - Our Work for Which? ](/blog/which-privacy/)

![Scott Lester](/headshots/scott-headshot-black.png)

[Scott Lester](https://www.linkedin.com/in/scottjameslester/)

5 November 2024

[![](/blog/sme-policies/PoliciesSMEs-Inbody.webp) ](/blog/sme-policies/)

[ Expert Insights & Advice ](/blog/?type=Expert+Insights+%26+Advice) ## [What policies do I need in place as a small business? ](/blog/sme-policies/)

![Claire Gurney](/headshots/generic-person-headshot-black.png)

[Claire Gurney]()

15 November 2023

[![](/blog/vulnerability-identification/vuln-identification.webp) ](/blog/vulnerability-identification/)

[ Technical Tutorials & Explainers ](/blog/?type=Technical+Tutorials+%26+Explainers) ## [Vulnerability Identification: Key Concepts And Terms Explained ](/blog/vulnerability-identification/)

![Lauren Palmer](/headshots/lauren-headshot-black.png)

[Lauren Palmer](https://www.linkedin.com/in/lauren-palmer-30444793/)

24 October 2023

About Naz Markuta 

Naz is a technical Cyber Security professional with experience in technical research, penetration testing and vulnerability research. Naz has found credited vulnerabilities in hardware devices, mobile and web applications. At Hexiosec he helped to deliver our cyber security consulting services, until his departure in April 2024. 

![Naz Markuta](/headshots/Naz_Markuta-bw.webp)

[ ![](/brand/logo_asm.svg) ](/asm)

See your real [external attack surface](/blog/what-is-attack-surface-management) \- without the noise 

[Find out more](/asm)

[ Book a demo ](/asm/demo)

[ ![](/brand/logo_transfer.svg) ](/transfer)

Secure file transfer with [true E2EE](/blog/what-is-end-to-end-encryption) \- trusted by UK Government 

[Find out more](/transfer)

[ Book a demo ](/transfer/demo)

![White Hexiosec logo](/img/logo/main_bg_dark_hu_7af64e511250ef51.webp)

Suites 201-203  
Eagle Tower  
Montpellier Drive  
Cheltenham  
GL50 1TA  

__[+44 (0) 1242 474970](tel:+44%20%280%29%201242%20474970)

  * Products 
  * [Hexiosec ASM](/asm)
  * [Hexiosec Transfer](/transfer)
  * [Hexiosec ASM Pricing](/asm/pricing)
  * [Hexiosec Transfer Pricing](/transfer/pricing)

  * [Services](/services/)
  * [Secure Digital Transformation](/services/secure-digital-transformation)
  * [Online Discovery Services](/services/online-discovery-services)
  * [Cyber Security Testing](/services/technical-security-testing)
  * [Cyber Advisory & Assessment](/services/cyber-security-improvement)
  * [Secure Cloud Migration](/services/safely-use-cloud)
  * [Cloud Security Management](/services/manage-cloud-security)
  * [Secure Code Review](/services/build-applications-securely)
  * [Application Security Testing](/services/test-application-security)
  * [Device Security Review](/services/protect-devices)

  * Resources 
  * [Blogs](/blog/)
  * [Hexiosec ASM User Guides](https://docs.hexiosec.com/asm)
  * [Hexiosec Transfer User Guides](https://transfer-docs.hexiosec.com/)
  * [Hexiosec ASM API Documentation](https://asm.hexiosec.com/api/ui)
  * [Hexiosec ASM Product Updates](/blog/?filter=Product%20Features)
  * [Hexiosec Transfer CLI Documentation](https://transfer-docs.hexiosec.com/integrations/cli/)
  * [Open Source](https://github.com/hexiosec)
  * [Videos](https://www.youtube.com/@Hexiosec/videos)
  * [LinkedIn User Community](https://www.linkedin.com/groups/14100490/)

  * Company 
  * [Contact Us](/contact)
  * [Careers](/careers)
  * [History](/about)
  * [Latest News](/news)
  * [Our People](/people)

[![NCSC Cyber Essentials logo](/logos/Cyber-Essentials-Badge-High-Res.png)](https://www.ncsc.gov.uk/cyberessentials/overview) [![NCSC Cyber Essentials Plus logo](/logos/Cyber-Essentials-Plus-Badge-High-Res.png)](https://www.ncsc.gov.uk/cyberessentials/overview) [![The Cyber Scheme NCSC-Assured Certified Testers](/logos/TCS_registered-certified-testers-logo2.webp)](https://thecyberscheme.org/) [![Crown Commercial Service procurement frameworks](/logos/ccs.png)](https://www.crowncommercial.gov.uk/) [![Home Office's Accelerated Capability Environment procurement framework](/logos/ACE-Vivace.png)](https://www.vivace.tech/) [![JOSCAR Registered Supplier](/logos/joscar.png)](https://hellios.com/joscar/)

© 2026 [Hexiosec](/). All rights reserved.

[Hexiosec Terms of Service](/terms/) [Privacy Policy](/privacy/) [Coordinated Disclosure Policy](/disclosure/)

Cookie Settings

[ ](https://www.linkedin.com/company/hexiosec/) [ ](https://github.com/RedMapleTech) [ ](https://www.youtube.com/@hexiosec)

![](https://px.ads.linkedin.com/collect/?pid=4616956&fmt=gif)
