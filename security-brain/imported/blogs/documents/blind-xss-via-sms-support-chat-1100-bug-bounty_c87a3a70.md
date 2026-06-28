---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-03_blind-xss-via-sms-support-chat-1100-bug-bounty.md
original_filename: 2023-04-03_blind-xss-via-sms-support-chat-1100-bug-bounty.md
title: Blind XSS via SMS Support Chat — $1100 Bug Bounty!
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: c87a3a70e0779f9d1eaef1d9ec96131c0bdcef65fba40d49ac14aded0cfde1df
text_sha256: 2dd15302c57e99c43596ab47892812c9f1dd63a0864e385926548b7a44ff0f92
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Blind XSS via SMS Support Chat — $1100 Bug Bounty!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-03_blind-xss-via-sms-support-chat-1100-bug-bounty.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `c87a3a70e0779f9d1eaef1d9ec96131c0bdcef65fba40d49ac14aded0cfde1df`
- Text SHA256: `2dd15302c57e99c43596ab47892812c9f1dd63a0864e385926548b7a44ff0f92`


## Content

---
title: "Blind XSS via SMS Support Chat — $1100 Bug Bounty!"
url: "https://chevonphillip.medium.com/blind-xss-via-sms-support-chat-1100-bug-bounty-779a1e19cc51"
authors: ["Chevon Phillip (@ChevonPhillip)"]
bugs: ["Blind XSS", "Chatbot"]
bounty: "1,100"
publication_date: "2023-04-03"
added_date: "2023-04-06"
source: "pentester.land/writeups.json"
original_index: 1306
scraped_via: "browseros"
---

# Blind XSS via SMS Support Chat — $1100 Bug Bounty!

Blind XSS via SMS Support Chat — $1100 Bug Bounty!
Chevon Phillip
Follow
1 min read
·
Apr 4, 2023

85

2

Hello Hunters, This is a quick write-up on how my blind XSS payload executed within an internal support portal via an SMS support chat.

This company (example.com) had a support site allowing users to submit a support ticket. You can create a support ticket in three ways:

Email Support
Phone Call Support
Text messages SMS support

Option 3 stood out to me, and I decided to play around with this option. After a few minutes of creating a ticket, I decided to make another ticket, but this time injecting my blind XSS payload within the SMS message, which turned into a live SMS text between the support agent and myself.

Get Chevon Phillip’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Long Story Short…My payload got triggered after our chat ended with an internal note which also leaked the first and last name of the support agent and more.

Here is a redirected version of the PoC:

Press enter or click to view image in full size
PoC Image of Internal Portal
Takeaways:

Always try your blind XSS payloads in areas that are not likely to expect one, like a support SMS chat.

I hope you like this short write-up. If you want to see more, please follow me here and on Twitter. https://twitter.com/ChevonPhillip
