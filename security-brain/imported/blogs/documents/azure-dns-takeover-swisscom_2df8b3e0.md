---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-22_azure-dns-takeover-swisscom.md
original_filename: 2023-05-22_azure-dns-takeover-swisscom.md
title: Azure DNS Takeover @ Swisscom
category: documents
detected_topics:
- command-injection
- business-logic
- cloud-security
tags:
- imported
- documents
- command-injection
- business-logic
- cloud-security
language: en
raw_sha256: 2df8b3e0273ac4ad73b150a4a4a919135ecb4a8f99312b44102554174f39daac
text_sha256: fef7abb80e58d23107c37b5c6920a3b04fcf1575f4e4756710024723caca0266
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Azure DNS Takeover @ Swisscom

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-22_azure-dns-takeover-swisscom.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, cloud-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `2df8b3e0273ac4ad73b150a4a4a919135ecb4a8f99312b44102554174f39daac`
- Text SHA256: `fef7abb80e58d23107c37b5c6920a3b04fcf1575f4e4756710024723caca0266`


## Content

---
title: "Azure DNS Takeover @ Swisscom"
url: "https://medium.com/@husein.ayoub/azure-dns-takeover-swisscom-7c6aacb38e8"
authors: ["Hussein Ayoub"]
programs: ["Swisscom"]
bugs: ["DNS takeover"]
publication_date: "2023-05-22"
added_date: "2023-05-22"
source: "pentester.land/writeups.json"
original_index: 1128
scraped_via: "browseros"
---

# Azure DNS Takeover @ Swisscom

Azure DNS Takeover @ Swisscom
Hussein Ayoub
Follow
3 min read
·
May 22, 2023

8

1

Introduction:

This writeup details the discovery of a DNS takeover vulnerability in Swisscom. The vulnerability allowed an attacker to gain full control over the vulnerable domain target.com . The vulnerability is already fixed by Swisscom’s CSIRT.

NOTE: Please check the following blog post by Project Discovery for a deep dive into DNS takeovers https://blog.projectdiscovery.io/guide-to-dns-takeovers/

Discovery:

Back when i started hunting for bugs on Swisscom’s assets in 2019, there was no clear / defined scope about the in-scope domains and assets eligible for their bug bounty program. Luckily, they recently compiled a list of in-scope , oos domains under https://github.com/swisscom/bugbounty/tree/main/scope , so i took the list of eligible domains and started running a bunch of Nuclei templates against them.

As most of the hunters do when approaching a new asset, discovering subdomain takeovers & DNS misconfigurations is a must before digging into specific business logic / web app related bugs. To do so, i gathered a list of subdomains from bunch of open-source tools and passed them as input to the following nuclei template.

id: servfail-refused-hosts

info:
  name: DNS Servfail Host Finder
  author: pdteam
  severity: info
  description: A DNS ServFail error occurred. ServFail errors occur when there is an error communicating with a DNS server. This could have a number of causes, including an error on the DNS server itself, or a temporary
  networking issue.
  classification:
  cwe-id: CWE-200
  tags: dns,takeover
  metadata:
  max-request: 1

dns:
  - name: "{{FQDN}}"
  type: A

  matchers:
  - type: word
  words:
  - "SERVFAIL"
  - "REFUSED"

# Enhanced by mp on 2022/03/14

After 2 hours of scanning and going over nuclei’s output, i got multiple hostnames flagged as vulnerable, but most of them were false positives or DNS take over wasn’t possible. One of the flagged domains caught my eye after performing a dig +trace target.com , it had dangling NS records pointing to Azure.

Get Hussein Ayoub’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Walking through this reference to check if the takeover is possible/obvious https://github.com/indianajson/can-i-take-over-dns , Azure DNS Takeover was included as an Edge case and no further clarification was available, even on Twitter’s Infosec Timeline 😞. So i decided to report it anyway, hoping that Swisscom’s security team will accept it without an actual PoC, just dangling NS records 😅

I immediately got an N/A on my submission as they needed more evidence that the domain can be really taken over.

The program manager showed me a screenshot of him trying to register the domain in his personal Azure account but he never got any NS records with numbers lower than 30 , although he tried registering it in different locations, but still gave me the opportunity to try even further and the submission will be reviewed again.

Press enter or click to view image in full size

Azure offers 100$ in credit for students ( subscription type differs from personal account ) so why not taking advantage of it and trying to register the domain ? To my surprise, on the first try i got NS records with a number lower than 10 , so i started creating/deleting the domain in different locations until i got the exact same ones. Gathered the screenshots quickly and registered a subdomain pointing to google.com 😅 , re-sent the details and got the following reply 😁

Shoutout to Antoine and the whole Swisscom CSIRT for running a great bug bounty program !

Report timeline

25.01.2023 14:09 Initial report

25.01.2023 15:50 Report closed as Rejected

25.01.2023 16:42 Sent more details with actual PoC

25.01.2023 17:04 Reported Triaged

27.01.2023 17:45 Issue Fixed

03.02.2023 09:50 Bounty Awarded
