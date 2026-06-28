---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-15_subdomain-takeover-in-azure-trafficmanager-for-fun-profit.md
original_filename: 2023-12-15_subdomain-takeover-in-azure-trafficmanager-for-fun-profit.md
title: Subdomain Takeover in Azure Trafficmanager for Fun & Profit
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- cloud-security
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- cloud-security
language: en
raw_sha256: 8d26511742b3a3a29f4604caee7eb50fe4d9fba9e4ba1f5ee8cde5eddd7fd407
text_sha256: 68b6a30a6af8def0567faf1b24c417419ae03ecd0f137ad3355841345da49bb2
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# Subdomain Takeover in Azure Trafficmanager for Fun & Profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-15_subdomain-takeover-in-azure-trafficmanager-for-fun-profit.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, cloud-security
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `8d26511742b3a3a29f4604caee7eb50fe4d9fba9e4ba1f5ee8cde5eddd7fd407`
- Text SHA256: `68b6a30a6af8def0567faf1b24c417419ae03ecd0f137ad3355841345da49bb2`


## Content

---
title: "Subdomain Takeover in Azure Trafficmanager for Fun & Profit"
url: "https://padsalatushal.medium.com/subdomain-takeover-in-azure-trafficmanager-for-fun-profit-09c858ca3d0e"
authors: ["Padsala Tushal (@PadsalaTushal)"]
bugs: ["Subdomain takeover"]
publication_date: "2023-12-15"
added_date: "2024-01-10"
source: "pentester.land/writeups.json"
original_index: 620
scraped_via: "browseros"
---

# Subdomain Takeover in Azure Trafficmanager for Fun & Profit

Subdomain Takeover in Azure Trafficmanager for Fun & Profit
Padsala Tushal
Follow
3 min read
·
Dec 16, 2023

208

1

Introduction:

In the dynamic world of cybersecurity, where vulnerabilities lurk in unexpected corners, the concept of subdomain takeovers has become a compelling arena for exploration. This article delves into a real-world scenario involving the Company’s infrastructure, unraveling the intricacies of subdomain takeovers within Azure Traffic Manager.

The fundamentals seemed clear: identify a dangling domain and claim it, then showcase a Proof of Concept (PoC). Yet, the execution proved more intricate than anticipated. I invested significant time in understanding the process of uploading a PoC across various Microsoft Azure Trafficmanager services. Given the scarcity of comprehensive resources available online and the inherent confusion in navigating this terrain, I felt compelled to document my journey to aid others facing similar challenges.

So How did I find subdomain takeovers?

I was doing recon on a private target with a huge scope and assets on Bugcrowd. I fired up my VPS. collected the domains in scope and added them to a file and started my recon.

First I did Subdomain Enumeration with subfinder and assetfinder.

subfinder -dL domains.txt -all -recursive -o subs.txt
cat domains.txt | assetfinder --subs-only | tee -a subs2.txt

Then, I started combining and filtering them. Then I did an HTTP Probing with httpx.

cat subs.txt subs2.txt | sort -u | tee -a all-subs.txt
cat all-subs.txt | httpx | tee -a live-subs.txt

after checking live subdomains manually I found 3 subdomains that were giving 404. I ran the dig command on them.

securemftpptemp.target.com -> azsu-tm-core-ngfw-emftpreprod-002.trafficmanager.net
securemfttemp.target.com -> azsu-tm-core-ngfw-emft-002.trafficmanager.net
ukras1.target.com -> azsu-tm-c-eucprod-infra-pulse-test.trafficmanager.net

i checked https://github.com/EdOverflow/can-i-take-over-xyz for checking that those subdomains are vulnerable or not. but that doesn’t have docs about taking over the Azure trafficmanager.net service. then after a quick Google search, I found an amazing article about taking over Azure services. https://godiego.co/posts/STO-Azure/

Get Padsala Tushal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

the domain points to a trafficmanager CNAME that doesn’t seem to be registered. To check it, I went to the Azure portal and tried registering it.

Press enter or click to view image in full size

after successfully registering the Azure trafficmanager profile I set its outgoing endpoint to my VPS IP which is running an HTTP server with my POC code.

after a few minutes, I ran the dig command again to check.

Press enter or click to view image in full size

then I quickly checked the subdomain and it worked.

Press enter or click to view image in full size

I did the same process for the other two subdomains.

I quickly reported to a private program on Bugcrowd.

Timeline:

01/12/2023 : Discover and takeover the subdomains

02/12/2023: Reported to bugcrowd

05/12/2023: Changed the state to Triaged

08/12/2023: Changed the state to Resolved

Suggestions are most welcome as always. I will try to keep posting my findings. If you got anything from it, you can press the clap icon below, and don’t forget to follow me on Twitter & Linkedin as well.
See you all next time. :)
