---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-18_my-first-case-of-ssrf-using-dirsearch.md
original_filename: 2023-04-18_my-first-case-of-ssrf-using-dirsearch.md
title: My First Case of SSRF Using Dirsearch
category: documents
detected_topics:
- ssrf
- command-injection
- cloud-security
- supply-chain
tags:
- imported
- documents
- ssrf
- command-injection
- cloud-security
- supply-chain
language: en
raw_sha256: ac224bb37a1ffbf81b2c3a8d00cd002b22a9f7149d6aa5805d8c7ea0ffbab796
text_sha256: 1228502a3a2604827d34333988191f8018f96abd23ad5d4dbc9d246c4ac244d8
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# My First Case of SSRF Using Dirsearch

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-18_my-first-case-of-ssrf-using-dirsearch.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `ac224bb37a1ffbf81b2c3a8d00cd002b22a9f7149d6aa5805d8c7ea0ffbab796`
- Text SHA256: `1228502a3a2604827d34333988191f8018f96abd23ad5d4dbc9d246c4ac244d8`


## Content

---
title: "My First Case of SSRF Using Dirsearch"
url: "https://goziem.medium.com/my-first-case-of-ssrf-using-dirsearch-b916f0f1e94b"
authors: ["Mba-oji Chiagoziem (@g0ziem)"]
bugs: ["SSRF"]
publication_date: "2023-04-18"
added_date: "2023-05-08"
source: "pentester.land/writeups.json"
original_index: 1252
scraped_via: "browseros"
---

# My First Case of SSRF Using Dirsearch

Top highlight

My First Case of SSRF Using Dirsearch
Mba-oji Chiagoziem
Follow
2 min read
·
Apr 18, 2023

278

8

Hello, I am a 16-year-old bug bounty hunter. I would like to appreciate God Almighty for helping me to find this bug.

This is my first Medium Blog Post and in this blog post, I will share my experience of finding my first SSRF vulnerability using Dirsearch and explain the steps I took to discover it.

Server-Side Request Forgery (SSRF) is a type of web application vulnerability that allows an attacker to send HTTP/HTTPS requests from the server to a third-party domain, potentially leading to sensitive data disclosure or even remote code execution.

I started by getting all the subdomains of my target using Subfinder by Project Discovery.

subfinder -d target.com | tee target.txt

It happened while I was going through the Usage of Dirsearch on Github, I found an option that I have never used before on Dirsearch, which was the deep recursive option.

Get Mba-oji Chiagoziem’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I then decided to use the option, and this was the final command:

python3 dirsearch.py -l target.txt --deep-recursive

Although it took time because I had to fuzz over 300 subdomains, I found a directory that was like:

targetconnect-dev.target.com/proxy.stream

but because I used the deep-recursive option, Dirsearch did another fuzzing on the proxy.stream parameter. It then found another parameter which then made the full URL like:

targetconnect-dev.target.com/proxy.stream?origin=https://google.com

I visited the URL and it rendered google.com to me, so I tried rendering other URLs to be sure there was no whitelisting involved and they rendered. So I tried using an Out Of Band Interaction Tester (OOB) like BurpSuite Collaborator but I didn’t have one so I used an alternative, and it worked. I received a pingback.

I now searched the parameter on Google and found a tweet where someone tried to use the AWS Metadata URL, so I tried using it, and behold, it worked. I was able to view the AWS Metadata credentials.

I quickly created a nuclei template to test other subdomains for the same bug type and I found another subdomain that was vulnerable to SSRF via the proxy.stream?origin parameter and I immediately reported it.

Press enter or click to view image in full size

Thanks for reading the blog post, if you have any questions, DM me on Twitter.

Goodbye.
