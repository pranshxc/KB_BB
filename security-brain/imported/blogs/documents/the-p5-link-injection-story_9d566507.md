---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-10_the-p5-link-injection-story.md
original_filename: 2020-06-10_the-p5-link-injection-story.md
title: The “P5” Link Injection Story
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 9d566507a1f0142da6da20faa5befbed7a474697a84b9a1b813040b101107afb
text_sha256: ac93912fcd84b228db16cf43b4fe3036bfb45c8e995fa84257129907697c8bf0
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# The “P5” Link Injection Story

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-10_the-p5-link-injection-story.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `9d566507a1f0142da6da20faa5befbed7a474697a84b9a1b813040b101107afb`
- Text SHA256: `ac93912fcd84b228db16cf43b4fe3036bfb45c8e995fa84257129907697c8bf0`


## Content

---
title: "The “P5” Link Injection Story"
url: "https://medium.com/@silentbronco/the-p5-link-injection-story-2632e61f62b7"
authors: ["Silent Bronco (@silentbronco)"]
bugs: ["Hyperlink injection"]
publication_date: "2020-06-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4513
scraped_via: "browseros"
---

# The “P5” Link Injection Story

The “P5” Link Injection Story
Tushar Bhardwaj
Follow
2 min read
·
Jun 10, 2020

29

Hello guys! As soon as I posted this tweet, I got loads of DMs asking questions about it, so I decided to do a small writeup. Even though it is a P5 in bug crowd, it was triaged in this program. So, Let’s begin!

Press enter or click to view image in full size
P5 → P4 →P?

It was my mom’s and sister’s birthday(Yes, they’re b’day twins), so I decided to order some food. After placing an order, the restaurant sent an “Order Successful” email, which confirmed that the order was placed successfully.

Press enter or click to view image in full size
Order Successful Email

The email had the items I had ordered and the restaurant's address. Now here’s the thing:

PH.NO is rendered as a link.

As you can see above “PH.NO” under the restaurant address is blue in color, which means it is a link. I sent in a report mentioning that “PH.NO” is rendered as a link and not as text, and they said that it is because of the email provider, however, they assured that they might fix this later by using “Ph:” instead of “PH.NO”.

Get Tushar Bhardwaj’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Thank you so much for reading this one. I’ll be doing some more writeups in the coming days. For updates, follow me on twitter if you haven't already: https://twitter.com/silentbronco. My DMs are always open to everyone!

Have a great day!
