---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-02_my-write-up-about-uber-cross-site-scripting-by-help-of-knoxss.md
original_filename: 2017-09-02_my-write-up-about-uber-cross-site-scripting-by-help-of-knoxss.md
title: My write up about UBER Cross-site scripting by help of KNOXSS
category: documents
detected_topics:
- xss
- command-injection
- rate-limit
- information-disclosure
tags:
- imported
- documents
- xss
- command-injection
- rate-limit
- information-disclosure
language: en
raw_sha256: f83ce0c37af09fc26b56f8ecc3f8c0c8187a2fec672cbec0cb4202bcb839de75
text_sha256: 8126409ae1b477adbf52d1e410d3fb37a2c60f45384d72d9cc683503ba327a17
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# My write up about UBER Cross-site scripting by help of KNOXSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-02_my-write-up-about-uber-cross-site-scripting-by-help-of-knoxss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `f83ce0c37af09fc26b56f8ecc3f8c0c8187a2fec672cbec0cb4202bcb839de75`
- Text SHA256: `8126409ae1b477adbf52d1e410d3fb37a2c60f45384d72d9cc683503ba327a17`


## Content

---
title: "My write up about UBER Cross-site scripting by help of KNOXSS"
url: "https://medium.com/@Alra3ees/my-write-up-about-uber-cross-site-scripting-by-help-of-knoxss-b1b56f8d090"
authors: ["Emad Shanab (@Alra3ees)"]
programs: ["Uber"]
bugs: ["Reflected XSS"]
bounty: "500"
publication_date: "2017-09-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6112
scraped_via: "browseros"
---

# My write up about UBER Cross-site scripting by help of KNOXSS

My write up about UBER Cross-site scripting by help of KNOXSS
Emad Shanab
Follow
2 min read
·
Sep 2, 2017

349

Sorry for my bad English

This is my first write up about bug bounty.

but i will do it to support the great man @brutelogic and his great tool @knoxss_me

It was a dream to find XSS in uber and be in uber HOF

So i made a purchase to @knoxss_me ( pro version) and start looking for XSS in uber sub domains

I used some tools to extract sub domains like Sublist3r and aquatone

After a long time of looking i have found this sub domain

https://payment-providers.uber.com

So i noticed that it is not show any thing just a white page

so i started brute force to get any bugs or directory listing or any valid parameters or files

I used dirb tool in kali linux to brute force valid parameters

https://tools.kali.org/web-applications/dirb

And after some time i got this end point

Get Emad Shanab’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://payment-providers.uber.com/health/

Press enter or click to view image in full size

So i fired up the @knoxss_me and for my good luck i got the magic XSS box from @knoxss_me service

KNOXSS service

I was very happy to got it and i tweeted about it before report it

But my signal in hackerone is too low so i sent an email to uber support email and Rob Fletcher from uber support team white listed my account to report it in hackerone

Press enter or click to view image in full size

Final report to uber

uber Cross site scripting

After that i reported it and they triaged it and got 500$

Press enter or click to view image in full size

Thanks to @brutelogic and @knoxss_me and special thanks to @knowledge_2014 for supporting me

Time line:-
07/08/2017 Email sent to security-abuse@uber.com

07/08/2017 Got replay from Rob Fletcher said Ok, cool, you’re account should be whitelisted

07/08/2017 Reported to uber hackerone page

08/08/2017 changed the status to Triaged and rewarded with a $500 bounty

23/08/2017 closed the report and changed the status to Resolved

25/08/2017 decided that this report is not eligible for a bounty because payment-providers.uber.com isn’t typically used in a web browser
