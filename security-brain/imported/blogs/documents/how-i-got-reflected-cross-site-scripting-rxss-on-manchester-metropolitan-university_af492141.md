---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-07_how-i-got-reflected-cross-site-scriptingrxss-on-manchester-metropolitan-universi.md
original_filename: 2021-08-07_how-i-got-reflected-cross-site-scriptingrxss-on-manchester-metropolitan-universi.md
title: How I got Reflected Cross Site Scripting(RXSS) on Manchester Metropolitan University
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: af49214141d1862aa87ae17d2418a01f9b6d7f733473c23dae60fddcf63e83d6
text_sha256: 5d9c890ec258f97930c7d14768115b571048ea965aa75e2fabbc1076dc5a6328
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I got Reflected Cross Site Scripting(RXSS) on Manchester Metropolitan University

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-07_how-i-got-reflected-cross-site-scriptingrxss-on-manchester-metropolitan-universi.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `af49214141d1862aa87ae17d2418a01f9b6d7f733473c23dae60fddcf63e83d6`
- Text SHA256: `5d9c890ec258f97930c7d14768115b571048ea965aa75e2fabbc1076dc5a6328`


## Content

---
title: "How I got Reflected Cross Site Scripting(RXSS) on Manchester Metropolitan University"
url: "https://santoshdbobade.medium.com/how-i-got-reflected-cross-site-scripting-rxss-on-manchester-metropolitan-university-700b36cb4f53"
authors: ["Santosh Bobade (@Santosh88267387)"]
programs: ["Manchester Metropolitan University"]
bugs: ["XSS"]
publication_date: "2021-08-07"
added_date: "2022-11-08"
source: "pentester.land/writeups.json"
original_index: 3439
scraped_via: "browseros"
---

# How I got Reflected Cross Site Scripting(RXSS) on Manchester Metropolitan University

Santosh Bobade
 highlighted

How I got Reflected Cross Site Scripting(RXSS) on Manchester Metropolitan University
Santosh Bobade
Follow
2 min read
·
Aug 7, 2021

96

Hello Everyone
I hope you all are going well and good
So this is my third blog regarding bug hunting

If you want to read my previous 2 blogs regarding my findings click on the following link

how I got appreciation from Harvard University(harvard.edu):

Santosh Bobade - Medium
Hello guys, my name is Santosh Bobade. This is my first write-up, so any spelling mistake and grammatical mistake…

santoshdbobade.medium.com

how I got the hall of fame from Universiteit Utrecht(uu.nl)

An Accidental XSS on uu.nl
Hello guys, I hope you enjoyed my previous blog. Today I am talking about how I got an accidental XSS on uu.nl Let's…

santoshdbobade.blogspot.com

So let’s start

First I was collecting all the URLs using the gau tool

GAU tool is a very much impressive tool made by Corben Leo

Link for gau tool:
https://github.com/lc/gau

By using grep command I sort out the URL which contains utm_ parameter

command:
cat url.txt | grep “utm_”

I would recommend to you if you got the following parameter then check each of them will be reflected or not

utm_source=
utm_compaign=
utm_medium=

Get Santosh Bobade’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

but in our case, utm_compaign value is reflected to in input tag

Press enter or click to view image in full size

now its time to balance the tag

My payload:

test”/><img src=x onerror=prompt(document.domain)>

Press enter or click to view image in full size

Check-in browser

boom….!

Press enter or click to view image in full size

After 10–15 days the security team fix the issue and received thankful mail from the Manchester Metropolitan University

Press enter or click to view image in full size

I also disclosed some interesting video POC regarding my submission on youtube

Youtube: https://www.youtube.com/channel/UCD1HKXD7o-mLV9jmkS-emGw

LinkedIn: https://www.linkedin.com/in/santosh-bobade-531094192/

Twitter Handle: https://twitter.com/Santosh88267387

Thanks for reading….!
