---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-22_story-of-unexpected-bugs.md
original_filename: 2021-08-22_story-of-unexpected-bugs.md
title: Story Of Unexpected Bugs
category: documents
detected_topics:
- idor
- xss
- command-injection
- api-security
tags:
- imported
- documents
- idor
- xss
- command-injection
- api-security
language: en
raw_sha256: 9b714f56af6b28dc26c2043f426b315e03c846b6471a5f465d10f628bff01a29
text_sha256: d64d59a3236aa32dd4e782168f6cbaa9d5204f9b3b4ea748f583a67fdb2d951a
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Story Of Unexpected Bugs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-22_story-of-unexpected-bugs.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `9b714f56af6b28dc26c2043f426b315e03c846b6471a5f465d10f628bff01a29`
- Text SHA256: `d64d59a3236aa32dd4e782168f6cbaa9d5204f9b3b4ea748f583a67fdb2d951a`


## Content

---
title: "Story Of Unexpected Bugs"
url: "https://medium.com/@nehpatel/story-of-unexpected-bugs-75734d51ac57"
authors: ["Neh Patel (@thecyberneh)"]
bugs: ["IDOR", "XSS"]
publication_date: "2021-08-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3400
scraped_via: "browseros"
---

# Story Of Unexpected Bugs

Story Of Unexpected Bugs
Neh Patel
Follow
2 min read
·
Aug 22, 2021

278

2

Hello, amazing hackers, My name is Neh Patel and I’m a bug hunter.

I’ve been thinking about writing about my findings for a while, so here we go.

Please let me know if you notice any spelling errors.

Let's start,

It was about 2 or 2:30 am at midnight and I was reading some books related to hacking and I was just going to bed at that time I decided to check the email.

In a mail, at the end of that mail, there was a button or link called “unsubscribe”.As we all know, it was for unsubscribing from that company’s mail notification

Press enter or click to view image in full size

I thought about checking this “unsubscribe” link. There was a parameter called “email” in that link

https://target.maintarget.com/cgi-bin/qsurveyadmin.dll?request=exclude&idx=63364C&email=30316E6568706174656C6F6666696369616C40676D61696C2E636F6D&language=English&languagecharset=utf-8&source=1

I was thinking that what if I change the value of the “email” param. It’s interesting but the value of that param is encoded in some format so I decided to decode that value

I copied that link and paste it into notepad and checking for different encoding. I checked that with base64, md5, and other popular encryption methods but found nothing.

Get Neh Patel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After some time, I noticed that in that value there are only A to F and 0 to 9 digits. I got it It’s Hexadecimal value of plain email address

After decoding I got my real email address but in all CAPITAL letters. I decided to change that value so I took a fake email address, change all letter into CAPITAL letters and encode it into Hexadecimal, Copy that encoded string and paste it at the place of the real value of the “email” param.

Boom… I found IDOR, we can unsubscribe from anyone’s email.

But I did not stop that bug, I write a simple XSS payload

<script>alert(document.domain)</script>

and again make all letter into capitals, encode it into Hexadecimal and paste it as a value of the “email” param.

Press enter or click to view image in full size

Again Its XSS Yeah I did it … I did it …. I did it

Thanks for reading my write-up! Throw a heart to this story, If you liked please share it to your hacker friends .. Will be back with another write-up shortly.
