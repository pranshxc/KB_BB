---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-28_multiple-rxss.md
original_filename: 2023-12-28_multiple-rxss.md
title: Multiple RXSS
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: eb53d5fc3248637bfb80643bd0c3a33cc99a54e8699b4b29f4cdc635bba6ec2b
text_sha256: bd4524a112063917569e935c6dc730a6143adad5ae882ee989682264139f22c7
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple RXSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-28_multiple-rxss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `eb53d5fc3248637bfb80643bd0c3a33cc99a54e8699b4b29f4cdc635bba6ec2b`
- Text SHA256: `bd4524a112063917569e935c6dc730a6143adad5ae882ee989682264139f22c7`


## Content

---
title: "Multiple RXSS"
url: "https://medium.com/@0xchoudhary/multiple-rxss-f3f796287f34"
authors: ["Sushil Choudhary (@0xchoudhary)"]
bugs: ["Reflected XSS"]
publication_date: "2023-12-28"
added_date: "2024-01-02"
source: "pentester.land/writeups.json"
original_index: 592
scraped_via: "browseros"
---

# Multiple RXSS

Multiple RXSS
Sushil Choudhary
Follow
1 min read
·
Dec 28, 2023

67

2

Hello Everyone, I am back with another write-up…

For 2–3 weeks I am busy with my exams. After finishing the exam I back to hunting. I decided to hunt on VDP which has a broad scope because in that bug hunting is easy.

I chose a program which is recently launched and has so many scopes. I picked up one domain. let’s call it <>.com

Get Sushil Choudhary’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At first, I added it burp crawler (professional burp) and started it. After minimizing it I started exploring the website and I found an admin panel CMS that was vulnerable I was happy but is Authenticated.

Then i jumped to my Burp and guess what i found Multiple Reflected Cross-site scripting. YEAH, IT’S TRAIGED TIME. Before I reported it I was afraid because most RXSS are out of scope. Then I read and it’s not out of scope.

I reported it and after 4 hours I got a response. AAAH AS I TOLD YOU IT’S TRAIGED TIME. My report was valid and got triaged.

POC: <>.com/project/someting/fileame.html</sCrIpT><sCrIpT>alert(1)</ScRiPt>

Press enter or click to view image in full size
