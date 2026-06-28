---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-25_how-i-hacked-into-a-bugcrowd-public-program.md
original_filename: 2018-02-25_how-i-hacked-into-a-bugcrowd-public-program.md
title: How i Hacked into a bugcrowd. public program
category: documents
detected_topics:
- command-injection
- mobile-security
tags:
- imported
- documents
- command-injection
- mobile-security
language: en
raw_sha256: 555f3d6207ab57a2bfaf297a465946b7fb2491b364450fdb6fd3536846897894
text_sha256: 5c1d2ed28a420f5bbe0716978c5cc175ad061051f675406766b16bb392b2e559
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How i Hacked into a bugcrowd. public program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-25_how-i-hacked-into-a-bugcrowd-public-program.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `555f3d6207ab57a2bfaf297a465946b7fb2491b364450fdb6fd3536846897894`
- Text SHA256: `5c1d2ed28a420f5bbe0716978c5cc175ad061051f675406766b16bb392b2e559`


## Content

---
title: "How i Hacked into a bugcrowd. public program"
url: "https://infosecwriteups.com/how-i-hacked-into-a-bugcrowd-public-program-fcfdd4fb1b69"
authors: ["Vishnuraj"]
bugs: ["RCE"]
publication_date: "2018-02-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5962
scraped_via: "browseros"
---

# How i Hacked into a bugcrowd. public program

How i Hacked into a bugcrowd. public program
vishnuraj
Follow
2 min read
·
Feb 25, 2018

677

3

Hello to all readers,

This article is about a remote code execution that i found in one of highest paying public program on bugcrowd. Offcourse for privacy purposes, we will not disclose the name of the program, so lets call it site.com

Cyber security pioneers emphasize on the fact that if you want to hack a target whether it be a Website, a Mobile app or an IoT device, you should follow the six step methodology.

This is what most researchers and bug bounty hunters fail to follow. Every hack has to be carried out via the methodology otherwise chances of success decrease drastically. This article about me following this simple approach and Hacking into

Step No#1: Information Gathering

Firstly, I visited the Bugcrowd program

I saw their scope is wide *.site.com

Step No#2: Network Mapping

Get vishnuraj’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Next i used the knockpy tool to look for sub domains on this host

From that tool found a number of unused sub domains which lead me to narrow down my search one in particular that was utils.site.com

Step No#3: Vulnerability Identification

onto which i did a simple port scan which revealed using JBoss AS version 4

I found that A remote code execution vulnerability exists in the version

Step No#4: Penetration

Next i used jexboss tool to test if the exploit was valid or not

and

I downloaded the executable exploit file from exploit-db and executed the exploited :)

One thing i have learned over the years is that if an application is tested thoroughly and with complete focus, there is always something that one can find, we just have to be willing to look into it a little deeper

Press enter or click to view image in full size

thanks shahmeer :)
