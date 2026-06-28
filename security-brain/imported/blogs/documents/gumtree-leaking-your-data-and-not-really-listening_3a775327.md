---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-15_gumtree-leaking-your-data-and-not-really-listening.md
original_filename: 2021-12-15_gumtree-leaking-your-data-and-not-really-listening.md
title: Gumtree – leaking your data and not really listening
category: documents
detected_topics:
- sso
- idor
- command-injection
- cloud-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- sso
- idor
- command-injection
- cloud-security
- mobile-security
- supply-chain
language: en
raw_sha256: 3a775327b40c8c055591e46c4e325a1931f6d8ed210fbbc8b08dd7a76581c592
text_sha256: b65e6c81bc6682e2b4bc5fbbc0ec60db610546143a6ce68bf249cad649f7e5e7
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Gumtree – leaking your data and not really listening

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-15_gumtree-leaking-your-data-and-not-really-listening.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, cloud-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `3a775327b40c8c055591e46c4e325a1931f6d8ed210fbbc8b08dd7a76581c592`
- Text SHA256: `b65e6c81bc6682e2b4bc5fbbc0ec60db610546143a6ce68bf249cad649f7e5e7`


## Content

---
title: "Gumtree – leaking your data and not really listening"
page_title: "Gumtree – leaking your data and not really listening | Pen Test Partners"
url: "https://www.pentestpartners.com/security-blog/gumtree-leaking-your-data-and-not-really-listening/"
final_url: "https://www.pentestpartners.com/security-blog/gumtree-leaking-your-data-and-not-really-listening/"
authors: ["Alan Monie (@AlanMonie)"]
programs: ["Gumtree"]
bugs: ["IDOR"]
publication_date: "2021-12-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3085
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

![Gumtree – leaking your data and not really listening](https://www.pentestpartners.com/wp-content/uploads/2024/09/gtree-headline-1024x512.png)

  * Security Blog 
  * Vulnerabilities and Disclosures 

# Gumtree – leaking your data and not really listening

###  Alan Monie 

**15 Dec 2021** 7 Min Read 

  * [ ![](https://www.pentestpartners.com/wp-content/uploads/2025/05/linkedin-icon-footer.svg) ](https://www.linkedin.com/company/pen-test-partners/)
  * [ ![](https://www.pentestpartners.com/wp-content/uploads/2025/05/x-icon-footer.svg) ](https://x.com/PentestPartners)
  * [ ![](https://www.pentestpartners.com/wp-content/uploads/2025/05/youtube-icon-footer.svg) ](https://www.youtube.com/channel/UC2HCAhj6JiOsV_PcMFrjykw)

Also on this page ▾

  * Related services
  * Related blogs

Sometimes finding vulnerabilities is as simple as… just looking.

### TL;DR

  1. Gumtree is a UK-based site where users can advertise items for sale.
  2. It leaked the PII of sellers to other users of the site within the HTML source of the adverts. Email address, postcode, GPS location, and the seller’s surname (via an IDOR) were all leaked.
  3. They abdicate responsibility for vulnerability disclosure to a bug bounty programme who didn’t seem to know what to do with responsible disclosure.

### Introduction

Gumtree claims to take user security and privacy seriously. They hide your surname and use an internal messaging system to allow buyer/seller communication, without revealing user’s email addresses. It’s a huge site that until recently was owned by eBay, so they must be pretty secure…. right?

### Leaky location data: F12

The site was super leaky. Every advert on the site included the seller’s postcode or GPS coordinates – even if the seller requested the map of their location to be hidden. It leaked the sellers email address, and their full name was available via a simple IDOR vulnerability.

One of my neighbours recently tried to sell a TV on Gumtree only for a random person, who hadn’t made prior contact, turn up at his house when he wasn’t at home. The neighbour called me to say that his youngest daughter was in the house and was scared because the guy wouldn’t leave. There are good reasons for not wanting to publish your location on the internet.

In the example below, the seller had, quite sensibly, disabled the map of their location, but the source HTML leaked their postcode. This is more accurate location data than the general map would have shown. This allows an attacker to identify a street or even a partial street.

![](https://www.pentestpartners.com/wp-content/uploads/2021/12/gtree1.png)

Figure 1 – Advert with no exact location data

![](https://www.pentestpartners.com/wp-content/uploads/2021/12/gtree2.png)

Figure 2 – Postcode leaked in the HTML

![](https://www.pentestpartners.com/wp-content/uploads/2021/12/gtree3.png)

Figure 3 – Leaked email address

### Leaky name information

The site also has an API which appears to be used exclusively for iOS. One of the endpoints was vulnerable to an IDOR attack. This leaked the full name of the user, as well as some other minor information, and didn’t require any authentication.

![](https://www.pentestpartners.com/wp-content/uploads/2021/12/gtree4.png)

Figure 4 – Leaking PII without authentication

Gumtree obviously knows that publishing a user’s full name on the site is a bad idea because they only show a first name in the advert. It’s a shame their APIs leak that information to anyone who has a look.

### Leaky email addresses

In October the governor of Missouri threatened to prosecute a local journalist who found some Social Security Numbers in the HTML source of the Department of Elementary and Secondary Education’s web site. This type of response isn’t uncommon when trying to disclose information to a vendor. It’s not often they are grateful, and usually they want to keep it quiet, don’t respond, or they don’t understand and want to sue you.

![](https://www.pentestpartners.com/wp-content/uploads/2021/12/gtree5.png)

Inspired by Governor Parson, I developed a multi-stage process to view sensitive information belonging to other Gumtree users:

  1. View an advert on gumtree.com
  2. Press F12
  3. Read
  4. The
  5. Sellers
  6. Email
  7. Address
  8. In
  9. The
  10. HTML

Sometimes big sites don’t even get the basics right.

It was surprising to see other users email addresses being leaked in the HTML source. I know Gumtree previously had used the concept of masked email addresses, and the email field may have been used for that. However, it’s a serious oversight to leak the email address of every seller in their adverts.

Gumtree was not protecting the location of its sellers or their PII data, and was leaking it on every advert. Sending this type of data to a third-party is, in my opinion, a clear data breach under UK GDPR laws. Any user could unintentionally access the PII of any seller.

### Disclosure

Gumtree had a security.txt page on their web site. It simply pointed us to Zerocopter who managed their bug bounties. I prefer to engage with companies directly, so I wasn’t keen on reporting through a third-party bug bounty programme, but I had no choice.

Unfortunately, Zerocopter required us to agree to a non-disclosure process before they would accept our vulnerability report. We believe in full disclosure, so that wasn’t something we were prepared to sign up to. After carefully reading the extensive legal jargon, it appeared that there was a clause for security researchers to publicly disclose after the issue was fixed, but forcing researchers to agree to multiple pages of legal text makes it time-consuming and potentially expensive in legal fees to **simply let a site owner know of a security issue**.

People trying to do the right thing should not be forced into a legal agreement. If you want to be made aware of all security issues on your platform, and as quickly as possible, outsourcing your vulnerability disclosure process is not the answer.

**Date**| **Action**  
---|---  
11/11/2021| Emailed [[email protected]](/cdn-cgi/l/email-protection#4a392f293f38233e330a2d3f273e382f2f64292527) and [[email protected]](/cdn-cgi/l/email-protection#c5ada0a9a9aa85a2b0a8b1b7a0a0eba6aaa8) about their PII leak  
12/11/2021| Emailed [[email protected]](/cdn-cgi/l/email-protection#b3d7c3dcf3d4c6dec7c1d6d69dd0dcde)  
12/11/2021| Received email from customer support acknowledging the issue and informing me they sent it to the relevant department  
16/11/2021| Received email from customer support saying that the email address leak had been fixed and they had self-reported to the ICO  
17/11/2021| Emailed [[email protected]](/cdn-cgi/l/email-protection#b7d3c7d8f7d0c2dac3c5d2d299d4d8da) again to let them know there were still other information leaks  
19/11/2021| Submitted reports via zerocopter  
01/12/2021| Gumtree fixed the IDOR  
06/12/2021| Gumtree fixed the postcode leak  
  
I initially sent emails to security@ and hello@ on the 11th November, and because it was leaking PII, I tried to contact their Data Protection Officer. I contacted them twice explaining that their site was leaking PII (12th and 17th November), but I never received a reply. Their customer service team did reply and said that the report had been forwarded onto an internal department, but again I never received a reply from their security team or DPO.

On the 16th November the customer service team replied letting me know that they had fixed the email address disclosure, and self-reported to the Information Commissioners Office. Well done Gumtree, that was a fast fix, and it’s great that you informed the ICO. There was, however, no mention of the location data leakage, or the IDOR, so on the 19th November I resorted to trying to report via Zerocopter.

Using a third-party also makes the disclosure process very clinical, and there was no direct thanks or feedback from Gumtree, however there was a monetary reward of 500-3000 Euros for the IDOR vulnerability because they had marked it as high risk.

HOWEVER, after the issue was fixed, I was informed that **no reward was payable** because – “This is a Responsible Disclosure report, meaning that receiving a reward is a bonus in itself”.

So, because I followed their rules on responsible disclosure, no reward was payable!

After I queried which of their rules I’d broken on responsible disclosure, they changed their mind and paid the minimum. I’m sure Gumtree would be horrified to find that their responsible disclosure process tied the hands of researchers, created a feeling of ungratefulness, and tried to avoid paying a bounty.

Outsourcing the vulnerability disclosure process abdicates your responsibility for vulnerabilities in your software and creates a cultural disconnect between your security team and the information security community.

### Conclusion

Site owners need to ensure that they are handling user’s data securely, and application level DLP systems can be useful to monitor for things like email addresses being leaked from web pages that should not contain email addresses.

Engage with security researchers directly. You’ll be made aware of issues on your site quicker, you’ll build up a relationship, and we’re on hand to retest and advise on the best fix for the vulnerability.

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
