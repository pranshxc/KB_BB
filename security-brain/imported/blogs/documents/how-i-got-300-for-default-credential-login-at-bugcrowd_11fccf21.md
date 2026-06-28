---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-12_how-i-got-300-for-default-credential-login-at-bugcrowd-.md
original_filename: 2023-12-12_how-i-got-300-for-default-credential-login-at-bugcrowd-.md
title: How I got $300 for Default Credential Login at Bugcrowd 🎉
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 11fccf21ca329cef94a316117a5b0c9c7446a3f1c087ac466c2233ebbfae283e
text_sha256: 68c35c117b0e4830d91d21ad48a001f31ebf7fa8c1243821de1c96daa121ad71
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# How I got $300 for Default Credential Login at Bugcrowd 🎉

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-12_how-i-got-300-for-default-credential-login-at-bugcrowd-.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `11fccf21ca329cef94a316117a5b0c9c7446a3f1c087ac466c2233ebbfae283e`
- Text SHA256: `68c35c117b0e4830d91d21ad48a001f31ebf7fa8c1243821de1c96daa121ad71`


## Content

---
title: "How I got $300 for Default Credential Login at Bugcrowd 🎉"
url: "https://medium.com/@avbhijitdutta99/how-i-got-300-for-default-credential-login-at-bugcrowd-30368eb698f7"
authors: ["Abhijit Dutta (@Abhijit9799)"]
bugs: ["Default credentials"]
bounty: "300"
publication_date: "2023-12-12"
added_date: "2023-12-26"
source: "pentester.land/writeups.json"
original_index: 637
scraped_via: "browseros"
---

# How I got $300 for Default Credential Login at Bugcrowd 🎉

Cyberbeat
 highlighted

Member-only story

How I got $300 for Default Credential Login at Bugcrowd 🎉
Cyberbeat
Follow
2 min read
·
Dec 12, 2023

77

1

Press enter or click to view image in full size
Photo by AltumCode on Unsplash

Hi everyone, its cyberbeat again! Today I’m here to tell you about a very easy bug that I found out and hopefully will help everyone motivate you find more bugs.

So there was a target that I was hacking on and I was using Shodan to look for vulnerabilities. Oh by the way, Shodan is a search engine specifically designed for internet-connected devices and systems. Unlike traditional search engines that index web content, Shodan indexes information about devices on the internet. It’s often referred to as a “search engine for hackers” because it can be used to find devices and systems that may have security vulnerabilities. I specifically use this to find vulnerabilities in the target that I’m trying to hack.

Back to the story, I figured out an IP that was pointing to the target. The shodan link was looking something like www.shodan.io/host/xx.xx.xx.xx . Upon further investigation, I ran a port scan and found out that one of the port 8855, there was a login panel there (https://xx.xx.xx.xx:8855/site). I wanted to bypass the admin panel to gain access so I tried SQLMap which it failed. It didn’t clicked in my mind but suddenly when I tried admin/admin it…
