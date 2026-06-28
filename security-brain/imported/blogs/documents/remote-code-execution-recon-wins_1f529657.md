---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-04_remote-code-execution-recon-wins.md
original_filename: 2019-06-04_remote-code-execution-recon-wins.md
title: REMOTE CODE EXECUTION ! 😜 Recon Wins
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 1f5296575f06fd1aab903962bbf047e376e114d7cfb54253ab5eb6796f2bae5c
text_sha256: a1cf4d8ad0db967a13c0f68a2cc930cf20dccf876a14b9d461278784e10285b7
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# REMOTE CODE EXECUTION ! 😜 Recon Wins

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-04_remote-code-execution-recon-wins.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `1f5296575f06fd1aab903962bbf047e376e114d7cfb54253ab5eb6796f2bae5c`
- Text SHA256: `a1cf4d8ad0db967a13c0f68a2cc930cf20dccf876a14b9d461278784e10285b7`


## Content

---
title: "REMOTE CODE EXECUTION ! 😜 Recon Wins"
url: "https://medium.com/@vishnu0002/remote-code-execution-recon-wins-e9c1db79f3da"
authors: ["Vishnuraj"]
bugs: ["RCE"]
publication_date: "2019-06-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5231
scraped_via: "browseros"
---

# REMOTE CODE EXECUTION ! 😜 Recon Wins

REMOTE CODE EXECUTION ! 😜 Recon Wins
vishnuraj
Follow
2 min read
·
Jun 4, 2019

276

3

Hello to readers,

This article is about the funniest remote code execution that i have ever found in a public program on bug crowd. Off course for privacy purposes, we will not disclose the name of the program, so lets call it abc.com

So as always, I was following the regular Recon steps.

Step No#1: Information Gathering

Firstly, I visited the Bugcrowd platform and checked for a program. For a change, I tried a public program this time.

I saw their scope is wide *.site.com (Which is the greatest relief for a bug hunter. Wide scope = more bugs :P )

Step No#2: Subdomain Mapping

Next i used the amass tool to look for sub domains for this host.

From the scan result, I found a number of unused sub domains which led me to narrow down my search to one in particular . Let’s say that was beta.alpha.xyz.internal.abc.com

Get vishnuraj’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Step No#3: Vulnerability Identification

After looking into that, I was shocked to see that the website which i found is hosting the Damn Vulnerable Web Application . That looked weird.

Why should a website host something like DVWA, that has a mother-load of vulnerabilities.

Press enter or click to view image in full size

Step No#4: Penetration

I continued with the testing and I used the default login password “ admin “ “admin” and logged in to the website and uploaded a php shell and got a reverse shell . I found that it was still exploitable, but stopped it here and reported to the program.

Press enter or click to view image in full size

It was a quick response that I got back from the program. I have never seen a bug getting fixed this fast. Within, one hour everything got addressed and fixed.

Press enter or click to view image in full size

Well, it was one of the weirdest and funniest bug I have ever found. It was shocking to see a big reputed company making simple mistakes like this.
Thanks to Bugcrowd and team in helping to resolve the issue fast!!
