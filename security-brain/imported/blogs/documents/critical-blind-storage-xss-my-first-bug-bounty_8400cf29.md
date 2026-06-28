---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-08_critical-blind-storage-xss-my-first-bug-bounty-.md
original_filename: 2021-04-08_critical-blind-storage-xss-my-first-bug-bounty-.md
title: (CRITICAL) Blind Storage XSS — My first Bug Bounty 💰
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
raw_sha256: 8400cf29a0ba186616a3aa26c7cb749926855968d8dcd8938344411cb93cf027
text_sha256: a195ee7f3614b75f1a56f04ed40eb8af35ba3e5ad7cb43be9746ecb305667e4d
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# (CRITICAL) Blind Storage XSS — My first Bug Bounty 💰

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-08_critical-blind-storage-xss-my-first-bug-bounty-.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `8400cf29a0ba186616a3aa26c7cb749926855968d8dcd8938344411cb93cf027`
- Text SHA256: `a195ee7f3614b75f1a56f04ed40eb8af35ba3e5ad7cb43be9746ecb305667e4d`


## Content

---
title: "(CRITICAL) Blind Storage XSS — My first Bug Bounty 💰"
url: "https://gatolouco.medium.com/critical-blind-storage-xss-my-first-bug-bounty-d318f6ba570c/"
authors: ["Benjamin Walter"]
programs: ["CS Money"]
bugs: ["Blind XSS"]
bounty: "1,000"
publication_date: "2021-04-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3753
scraped_via: "browseros"
---

# (CRITICAL) Blind Storage XSS — My first Bug Bounty 💰

(CRITICAL) Blind Storage XSS — My first Bug Bounty 💰
Benjamin Mauss
Follow
2 min read
·
Apr 8, 2021

452

1

What is the impact of a XSS on support chat?

Imagine, a hacker with full access to the support account and able to spread the XSS for every user on the platform.

Press enter or click to view image in full size
How it happens

During my tests on cs.money I sent an image to the supporter, got the request and sent to burp repeater. I noticed that I was able to break the HTML code by inject a double quote on the file name.

Okay, we have a very interesting thing here. How can we escalate the HTML injection to a XSS? Easy!

Press enter or click to view image in full size

But how did I knew that the XSS was being triggered on the support client? Well, I just asked him and he confirmed. 🍭

Get Benjamin Mauss’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Just in case they ask for a real impact, I crafted a payload that sends the supporter cookies to my server:

Press enter or click to view image in full size
I had some limitations like no dots or spaces
But how can it be so danger?

Imagine if instead of a alert(123) payload I craft a payload that (as supporter) sends another payload for every single user . When the user read the message, the XSS will trigger, allowing the hacker to steal private information, do unauthorized requests, buy, sell skins and so on.

Result

CS Money awarded me with a $1000 bounty (the critical bounty for support.cs.money). They tried to close as critical, but because the maximum severity on subdomains is high, they closed as high and awarded me as critical.

Press enter or click to view image in full size

My report got on top rank of Hacktivity feed just a few hours after I open disclosure.
