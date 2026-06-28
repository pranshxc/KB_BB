---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-06_how-i-found-a-critical-p1-bug-in-5-minutes-using-a-cellphone-bug-bounty.md
original_filename: 2022-02-06_how-i-found-a-critical-p1-bug-in-5-minutes-using-a-cellphone-bug-bounty.md
title: How I found a critical P1 bug in 5 minutes using a cellphone — Bug Bounty
category: documents
detected_topics:
- sqli
- command-injection
tags:
- imported
- documents
- sqli
- command-injection
language: en
raw_sha256: 5d84a466fe94e2a16a13a1951cc242b5c0f3837fbfdf1577fd3e1c470a3928c6
text_sha256: 6e8cf44fc9bc9eabdaa2d4cb0e6b313d246fde4981929b07e12d71544bd1a7a3
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I found a critical P1 bug in 5 minutes using a cellphone — Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-06_how-i-found-a-critical-p1-bug-in-5-minutes-using-a-cellphone-bug-bounty.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `5d84a466fe94e2a16a13a1951cc242b5c0f3837fbfdf1577fd3e1c470a3928c6`
- Text SHA256: `6e8cf44fc9bc9eabdaa2d4cb0e6b313d246fde4981929b07e12d71544bd1a7a3`


## Content

---
title: "How I found a critical P1 bug in 5 minutes using a cellphone — Bug Bounty"
url: "https://medium.com/@mrempy/how-i-found-a-critical-p1-bug-in-5-minutes-using-a-cellphone-bug-bounty-303ebec3edd6"
authors: ["Mr Empy (@mr_empy)"]
bugs: ["SQL injection"]
publication_date: "2022-02-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2935
scraped_via: "browseros"
---

# How I found a critical P1 bug in 5 minutes using a cellphone — Bug Bounty

Top highlight

How I found a critical P1 bug in 5 minutes using a cellphone — Bug Bounty
Br0sck
Follow
2 min read
·
Feb 6, 2022

765

11

Hello Hackers, I’m MrEmpy, I’m 16 years old and welcome to my first story about a critical bug I found on the phone.

Let’s start, I had received a private invitation from a Bug Bounty program, so I accepted the invitation and went to see the assets that were in scope, I started searching for login forms using Google Dork, I used a simple dork.

site:*.target.com intext:login

I was having coffee at work with my cell phone and I took the short time to look for something, I didn’t intend to stay long, and then I found a subdomain that caught my attention. I started testing time based SQL injection, I used the following payload:

admin’ and (select * from(select(sleep(40)))SQLI) and ‘abc’ = ‘abc

Luckily for me, the server only returned a response after 40 seconds. I quickly used the Kiwi Browser to capture the POST request for use in SQLMap.

Press enter or click to view image in full size

It really was SQL Injection! I couldn’t believe I got my first P1 CRITICAL failure in less than 5 MINUTES and still on PHONE. You know that joy that makes you want to scream “YEEEEEEEEEEEESSSS” but I couldn’t because I was in a company at the afternoon coffee time.

Get Br0sck’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As soon as I got home I grabbed my notebook and ran to report the failure.

Press enter or click to view image in full size

Fortunately the fault was marked as triaged.

That was my story, I hope you enjoyed it, I will bring more Bug Bounty stories as time goes by, so follow me for more stories like this ;)

Thanks for reading my story,

- MrEmpy
