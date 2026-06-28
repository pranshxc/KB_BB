---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-17_3-minutes-xss.md
original_filename: 2018-08-17_3-minutes-xss.md
title: 3 Minutes & XSS!
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 53aa919c237a7fbe2ca0d2a37540598077f3af0c862e7fd30851cda03bc7d13d
text_sha256: 984b675f465fa8ee0dcb26fb649784e4a09d5b0d44cb1ff82d62f85bdb8a8c53
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# 3 Minutes & XSS!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-17_3-minutes-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `53aa919c237a7fbe2ca0d2a37540598077f3af0c862e7fd30851cda03bc7d13d`
- Text SHA256: `984b675f465fa8ee0dcb26fb649784e4a09d5b0d44cb1ff82d62f85bdb8a8c53`


## Content

---
title: "3 Minutes & XSS!"
url: "https://medium.com/bugbountywriteup/3-minutes-xss-71e3340ad66b"
authors: ["Ashish Jha"]
programs: ["Edmodo"]
bugs: ["XSS"]
publication_date: "2018-08-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5747
scraped_via: "browseros"
---

# 3 Minutes & XSS!

3 Minutes & XSS!
Ashish
Follow
2 min read
·
Aug 17, 2018

199

1

Hello wonderfull readers, Myself Ashish Jha back with another of my write-up, Yes you heard it right it was a “3 minutes and xss”, Now as an hacker i always try to be as much efficient as possible and always try to find bugs fast(It’s just my curiosity), Whenever i start pentesting any stuff i keep a rough record of the amount of time i took finding the bug.

Let me narrate you this one:

So the website i was pentesting was edmodo.com(I asked them for a public disclosure), It was just in the morning that i wanna pentest edmodo that day and in the noon i started it , Follow along.

Step 1:

I did a simply recon using knockpy and found a subdomain go.edmodo.com,

I went their and clicked on signup, which then redirected me to:

https://www.edmodo.com/onboarding?school_suggestion_test_variant=controlass&language=en_GB

Press enter or click to view image in full size
Redirection image

Step 2:

Get Ashish’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I just added some <> in the first parameter —[ school_suggestion_test_variant=controlass<>], To see whether they get embedded into the source code, Then i found these brackets getting embedded between the <script> tags , WHAT NEED MORE!!!!!!!

Press enter or click to view image in full size
<script> tags embedded!

Step 3:

<img src=x onerror=”alert(xss by ashish)”>, BOOOOOM XSS

Press enter or click to view image in full size

This was my 3 minutes recon and xss, hope you may find it helpfull.

I then headed towards my mail and sent them the report, After a couple of days they replied back for rewarding the swags, And they are really awesome!

My overall experience with edmodo security team was really awesome(10/10).

Mug, Stickers, Badges, t-shirt

Thank you guys for reading, Write for you after a while!
