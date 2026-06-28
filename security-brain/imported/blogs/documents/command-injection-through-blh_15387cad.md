---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-14_command-injection-through-blh.md
original_filename: 2019-11-14_command-injection-through-blh.md
title: Command Injection Through BLH
category: documents
detected_topics:
- command-injection
- cloud-security
- idor
- rate-limit
tags:
- imported
- documents
- command-injection
- cloud-security
- idor
- rate-limit
language: en
raw_sha256: 15387cad19b0414f9422287089dda25fd5f8d36ad3b01c63983f781fffe190da
text_sha256: f34770c78e1ce001e0d8d3e4d5f0ba91de8001f982385f5e9ef10170fd514873
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Command Injection Through BLH

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-14_command-injection-through-blh.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security, idor, rate-limit
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `15387cad19b0414f9422287089dda25fd5f8d36ad3b01c63983f781fffe190da`
- Text SHA256: `f34770c78e1ce001e0d8d3e4d5f0ba91de8001f982385f5e9ef10170fd514873`


## Content

---
title: "Command Injection Through BLH"
url: "https://medium.com/@trapp3rhat/command-injection-through-blh-3c32614bb395"
authors: ["Shankar R (@trapp3r_hat)"]
programs: ["Meta / Facebook"]
bugs: ["Broken link hijacking"]
publication_date: "2019-11-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4946
scraped_via: "browseros"
---

# Command Injection Through BLH

Command Injection Through BLH
Shankar Ramakrishnan
Follow
3 min read
·
Nov 14, 2019

232

4

Hi I am Shankar Ramakrishnan (@trapp3r_hat) from India. I hope you all doing good. I am a security researcher from the last few years. Yes absolutely am doing bug bounty in the part-time because I am working as a Lead Security Consultant at Peneto Labs Pvt Ltd.

Thank you guys to appreciating my previous blog posts

In this blog I am going to explain about nice bug which is leads to command injection on the victim without aware of installing malicious file.

Bug Type: Broken Link Hijacking(BLH)

Concept:

Almost everyone has heard of subdomain hijacking but what about broken link hijacking. These two vulnerabilities are very similar the major difference is that one involves a subdomain while the other involves an expired link on a page.

Here I have found the BLH in official Facebook github repository which is leads to command injection on the victim without any user awareness. Because the user trusts the malicious file which is delivered from the broken link which is takeover by the attacker using Broken Link Hijacking attack

Thanks to Sreeram KL who guided me to learn about this bug.

Enumeration:

I have found a broken link using simple github dork

DORK: org:facebook “s3.amazonaws.com”

Note: You can replace the other services which are also vulnerable to sub-domain takeover vulnerability. Because we can takeover the services which is pointed to the broken link can be used by the attacker against the target.

While analyzing the dork results, I came across some Shell files that
contained reference to an s3 bucket which doesn’t exist anymore:

Press enter or click to view image in full size

An attacker can simply takeover that bucket and place a malicious ZIP file in the same path as shown in the above image “/memnn/kvmemnn/data.tar.gz”

Get Shankar Ramakrishnan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps To Reproduce:
1,Create an Amazon s3 bucket named “fair-data”
2,Create a folder called “memnn”
3,Create another folder called “kvmemnn”
4,Place your malicious ZIP file named “data.tar.gz”

Press enter or click to view image in full size

Impact:

Here the attacker can able to make command injection attack in the victim machines. Because the official facebook github repository has broken link been placed inside the bash file which is controlled by the attacker. The victim trusts the shell file which is mentioned in the facebook repository

Status: Fixed

Reward: 500$ on 16 Jan 2020

The facebook team has simply removed the file “Setup_Processed_Data.sh” from the repository

Response from the Facebook:

Due to some limitations to make the command injection vulnerability needs some user interaction to run the file once it is downloaded i.e “Setup_Processed_data.sh” . So the FB team has marked my report as “Informative”. This is my 4th Informative bug from FB this year😜😜😜

Picture: Facebook Response

After some analysis Facebook team has rewarded bounty on 17 Jan 2020.

Press enter or click to view image in full size

References:

Broken Link Hijacking Burp Plugin
Broken Link Hijacking (BLH) is lesser known attack.there is an brief introduction & exploitation about it by…

medium.com

Broken Link Hijacking - How expired links can be exploited.
Broken Link Hijacking (BLH) exists whenever a target links to an expired domain or page. Broken Link Hijacking comes in…

edoverflow.com

Broken Link Hijacking - s3 buckets
Tutorgeeks hackerone bugcrowd proof of concept cobalt vulnerabilities bug bounty security penetration testing…

tutorgeeks.blogspot.com

Broken Link Hijacking - Ghostlulz Hacks
Before we get started I have started a slack group dedicated to hacking. We welcome everyone from beginner to advanced…

ghostlulz.com
