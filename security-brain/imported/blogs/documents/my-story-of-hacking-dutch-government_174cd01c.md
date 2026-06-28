---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-12_my-story-of-hacking-dutch-government.md
original_filename: 2021-05-12_my-story-of-hacking-dutch-government.md
title: My story of hacking Dutch Government
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
raw_sha256: 174cd01c544b18704dbbc26cba8aa8a1135daeba56ff5ed1ca7b9255db54f209
text_sha256: 959c5589cdbd56b5141f0789e24a5f8f4b4223d6b578222cc5f585aa411778e0
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# My story of hacking Dutch Government

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-12_my-story-of-hacking-dutch-government.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `174cd01c544b18704dbbc26cba8aa8a1135daeba56ff5ed1ca7b9255db54f209`
- Text SHA256: `959c5589cdbd56b5141f0789e24a5f8f4b4223d6b578222cc5f585aa411778e0`


## Content

---
title: "My story of hacking Dutch Government"
url: "https://tuhin1729.medium.com/story-of-my-hacking-dutch-government-46b7a3c8b75a"
authors: ["Tuhin Bose (@tuhin1729_)"]
programs: ["Dutch Government"]
bugs: ["XSS"]
publication_date: "2021-05-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3660
scraped_via: "browseros"
---

# My story of hacking Dutch Government

My story of hacking Dutch Government
Tuhin Bose
Follow
2 min read
·
May 11, 2021

249

3

Hello guys! My name is Tuhin Bose (@tuhin1729). I am currently working as a Chief Technology Officer at Virtual Cyber Labs. In this write-up, I am going to share my experience of hacking Dutch Government.

So without wasting time, let’s start:

tuhin1729

At first, I was so confused because there are more than 1000 domains within the scope. But later I took a domain randomly from the list and started hunting on it. After 2–3 days of hunting, I started testing on https://rijkswaterstaat.archiefweb.eu/

In my initial recon process, I came across a parameter subsite. I quickly checked XSS there using a simple payload: “><script>alert(document.domain)</script>

And guess what! The payload was executed successfully.

Press enter or click to view image in full size

Final URL: https://rijkswaterstaat.archiefweb.eu/?subsite=bewustbodemgebruik%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E

Get Tuhin Bose’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I quickly made a proof of concept and reported it to them. After a month, I got a reply from them:

Press enter or click to view image in full size

Timeline:

15/10/20 — Reported Vulnerability

16/10/20 — Confirmed the vulnerability and informed the
organization.

03/12/20 — Resolved

04/12/20 — Got appreciation as Dutch Government T-shirt

04/01/21 — T-shirt delivered to my home

Press enter or click to view image in full size

Later, I got more than 10 T-shirts from them and it was really a nice experience :)

Follow me on Twitter: @tuhin1729_

Thanks for reading. I hope you enjoyed this blog.
