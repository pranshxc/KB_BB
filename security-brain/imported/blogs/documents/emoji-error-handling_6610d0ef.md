---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-19_emoji-error-handling.md
original_filename: 2020-09-19_emoji-error-handling.md
title: Emoji error handling
category: documents
detected_topics:
- xss
- sqli
- command-injection
tags:
- imported
- documents
- xss
- sqli
- command-injection
language: en
raw_sha256: 6610d0ef8545e6daa3bcfcbedd40f3bd628ab1f68005304c7ffb2daa6ee6b2b1
text_sha256: 315491b5a539d45cfaace5e37c4d6f934aba62aa99274d3897244c5f24f2623b
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Emoji error handling

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-19_emoji-error-handling.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `6610d0ef8545e6daa3bcfcbedd40f3bd628ab1f68005304c7ffb2daa6ee6b2b1`
- Text SHA256: `315491b5a539d45cfaace5e37c4d6f934aba62aa99274d3897244c5f24f2623b`


## Content

---
title: "Emoji error handling"
url: "https://medium.com/@Sheshasai/emoji-error-handling-ba11f1bdb8a6"
authors: ["shesha sai_c (@Cyb3r_4ss4s1n)"]
bugs: ["SQL injection"]
publication_date: "2020-09-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4254
scraped_via: "browseros"
---

# Emoji error handling

Emoji error handling
shesha sai_c
Follow
2 min read
·
Sep 19, 2020

35

1

Hello hunters! hope you are safe and doing well in this pandemic situation.

This write up is all about a bug i recently found in an bounty program lets call it as redacted.com- because the program does not allow public disclosure.

let’s dive in!

i started testing the redacted.com for XSS vulnerabilities i tried to bypass the waf to trigger an alert and also tried with blind XSS but of no use.

then i thought why not use emoji as payload to check the response i tried the emoji XSS payload from here: hackerone , but no luck it is escaping all the data.

so i tried only the emoji character to see how the site is going to respond.

BOOM! it worked and started throwing the error messages with sql code used by the application.

Get shesha sai_c’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps to reproduce:

visit: https://redacted.com/profile_update.
in the input field below give 😯.
click on save and done.
you will get the error disclosing the sql code as shown in the below screenshot.
Press enter or click to view image in full size
sql statements in the error response.

Tip:

when you get stuck take a step back and start over again.
Think out of the box, understand the application and how it handles your input.
sometimes you can also use the ancient symbols or characters as payload.

Bounty 🤑: $$$ awarded

i have tried for sql injection along with time-based, it didn’t worked. if you have any ideas that you can increase more impact to this i would love to hear them, please comment below.

if you feel the write-up useful give me a clap.

if you have any questions reach out to me cyb3r_4ss4s1n

Stay Home Stay Safe.
