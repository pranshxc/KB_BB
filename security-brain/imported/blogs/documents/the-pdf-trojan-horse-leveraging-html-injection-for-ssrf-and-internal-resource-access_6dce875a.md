---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-05_the-pdf-trojan-horse-leveraging-html-injection-for-ssrf-and-internal-resource-ac.md
original_filename: 2024-07-05_the-pdf-trojan-horse-leveraging-html-injection-for-ssrf-and-internal-resource-ac.md
title: 'The PDF Trojan Horse: Leveraging HTML Injection for SSRF and Internal Resource
  Access'
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- automation-abuse
- cloud-security
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- automation-abuse
- cloud-security
language: en
raw_sha256: 6dce875ac0c4cb774d81f5cf436fc189b399a8ae39783b61b1e2d10115f6ce6e
text_sha256: 55ec747f979dcc3ccb358cb1f87e257ce639b3842fdfa0cdc0d91bc052e36939
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# The PDF Trojan Horse: Leveraging HTML Injection for SSRF and Internal Resource Access

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-05_the-pdf-trojan-horse-leveraging-html-injection-for-ssrf-and-internal-resource-ac.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `6dce875ac0c4cb774d81f5cf436fc189b399a8ae39783b61b1e2d10115f6ce6e`
- Text SHA256: `55ec747f979dcc3ccb358cb1f87e257ce639b3842fdfa0cdc0d91bc052e36939`


## Content

---
title: "The PDF Trojan Horse: Leveraging HTML Injection for SSRF and Internal Resource Access"
url: "https://uchihamrx.medium.com/the-pdf-trojan-horse-leveraging-html-injection-for-ssrf-and-internal-resource-access-fbf69efcb33d"
authors: ["Abdelrhman Amin (@0xUchihamrx)"]
bugs: ["HTML injection", "SSRF"]
publication_date: "2024-07-05"
added_date: "2024-08-14"
source: "pentester.land/writeups.json"
original_index: 191
scraped_via: "browseros"
---

# The PDF Trojan Horse: Leveraging HTML Injection for SSRF and Internal Resource Access

The PDF Trojan Horse: Leveraging HTML Injection for SSRF and Internal Resource Access
Abdelrhman Amin
Follow
3 min read
·
Jul 5, 2024

852

4

.بِسْم اللَّه الرَّحْمن الرَّحِيم . . اللَّهمَّ صَلِّ وَسلَّم وبارك على نَبِينَا مُحمَّد

In the name of God, the most gracious, the most merciful.
May Allah’s blessings and peace be upon our Prophet Muhammad.

Before we begin, I offer my prayers for my brothers in Palestine and Sudan, asking Allah to grant them unwavering strength and ultimate victory.

Introduction

In this writeup, I will detail the discovery of a critical SSRF vulnerability I found in a private Bug Bounty Program. This article explores how a low-severity bug like HTML injection (HTMLi) can be exploited via PDF generation to achieve SSRF, leading to access to AWS metadata and internal resources.

Press enter or click to view image in full size
Discovery of HTML Injection:

The web app is designed for company management, catering to both users and clients. Each user gets a unique subdomain to manage their company, such as hacker.target.com. After creating an account, I used the app like a normal user to gather information about its features. Once I had a good understanding, I started with the profile section. In the fields for username and company name, I tested a basic HTML payload like '"><h1>Mrx</h1> to see if it would execute. It worked, and the HTML injection payload executed successfully.

Press enter or click to view image in full size

This initially perceived as low-severity, Let’s try to make it more impactful.

SSRF via PDF Generation Attack:

During my exploration, I found a feature generating monthly PDFs containing statistical data. My mind lit up with the idea of launching an SSRF attack via PDF generation. You can learn more about this attack by checking out these slides.

Get Abdelrhman Amin’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I generated the PDF with the HTMLi payload and found that the HTMLi persisted in the PDF rendering. I realized the potential for SSRF exploitation.

Press enter or click to view image in full size

To validate this I replaced the HTMLi payload with an iframe payload pointing to a Burp Collaborator (<iframe src="http://Burp-Collaborator"></iframe>). Upon generating the PDF, I successfully received callbacks, confirming SSRF feasibility.

Exploiting SSRF:

To escalate the exploit, I attempted to access local resources by embedding <iframe src="http://127.0.0.1"></iframe> and regenerating the PDF. This action granted access to internal portals, demonstrating the exploitability of the SSRF vulnerability. Knowing the Target utilized AWS services, I targeted AWS metadata endpoints (<iframe src="http://169.254.169.254/latest/meta-data"></iframe>). Upon regenerating the PDF with modified payloads. and Boom! We got it!

Press enter or click to view image in full size

Let's proceed to access AWS credentials.(<iframe src="http://169.254.169.254/2021-07-15/meta-data/identity-credentials/ec2/security-credentials/ec2-instance"></iframe>). Upon regenerating the PDF with modified payloads. and I successfully accessed AWS credentials.

Press enter or click to view image in full size

I’ve submitted the report to the program. They acknowledged its severity as critical and rewarded me.

Thank you for taking the time to read, and I hope it proves beneficial to you.

Feel free to connect with me on Twitter or LinkedIn.
