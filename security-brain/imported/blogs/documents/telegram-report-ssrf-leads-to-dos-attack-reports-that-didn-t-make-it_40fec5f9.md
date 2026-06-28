---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-27_telegram-report-ssrf-leads-to-dos-attack-reports-that-didnt-make-it.md
original_filename: 2021-07-27_telegram-report-ssrf-leads-to-dos-attack-reports-that-didnt-make-it.md
title: 'Telegram Report: SSRF leads to DOS attack [Reports that didn''t make it]'
category: documents
detected_topics:
- ssrf
- command-injection
- rate-limit
- automation-abuse
tags:
- imported
- documents
- ssrf
- command-injection
- rate-limit
- automation-abuse
language: en
raw_sha256: 40fec5f9df7bf0a9c9c469300ff08092ca5a326f5cc5b8035c7c4d933651f209
text_sha256: a25edd3311babfc03964a6c68c8d841cbd550829d1562374c586629a22113a0a
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Telegram Report: SSRF leads to DOS attack [Reports that didn't make it]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-27_telegram-report-ssrf-leads-to-dos-attack-reports-that-didnt-make-it.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `40fec5f9df7bf0a9c9c469300ff08092ca5a326f5cc5b8035c7c4d933651f209`
- Text SHA256: `a25edd3311babfc03964a6c68c8d841cbd550829d1562374c586629a22113a0a`


## Content

---
title: "Telegram Report: SSRF leads to DOS attack [Reports that didn't make it]"
url: "https://medium.com/bug-bounty/telegram-report-ssrf-leads-to-dos-attack-908bea5f5802"
authors: ["Philippe Delteil (@PhilippeDelteil)"]
programs: ["Telegram"]
bugs: ["SSRF", "DoS"]
publication_date: "2021-07-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3474
scraped_via: "browseros"
---

# Telegram Report: SSRF leads to DOS attack [Reports that didn't make it]

Member-only story

Telegram Report: SSRF leads to DOS attack [Reports that didn't make it]
Summary
Philippe Delteil
Follow
2 min read
·
Jul 27, 2021

10

1

When a Telegram user (or bot) sends a message containing an URL to another user, the Telegram Bot sends a request to check the URL. This is a privacy issue in my view, because URLs and some parts of your conversations are being read by a machine, the end-to-end encryption is not enforced in this case. We also detect that if (by mistake) you append text to the URLs that text will be send to the bot as well.

We discovered this issue when I accidentally send a Burp Collaborator link to a collage and I received a HTTP and DNS on my client.

But, besides the privacy concern, what if we could use this behavior to send many requests to a target host?

I used a python script to send messages to a Telegram bot, every message contains 70 URLs that are actually the same domain with a different path. I discovered that a filter was not allowing to repeat the URLS, but I only needed to add something in the end to bypass it.

I’m aware of the size limit of every message and also the rate limit to send messages to the bot, around 100 is the upper limit.

Steps To Reproduce

1. Create a Telegram bot.
2. Configure [this tool](https://github.com/MikeWent/notify-send-telegram) to send messages the bot.
3. Fire-up Burp and get Collaborator payload. (In this example is ucaao50j385xwc1hc3on5z9w1n7fv4.burpcollaborator.net)
4. Use this script
