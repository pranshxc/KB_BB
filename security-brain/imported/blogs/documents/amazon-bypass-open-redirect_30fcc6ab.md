---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-19_amazon-bypass-open-redirect.md
original_filename: 2017-11-19_amazon-bypass-open-redirect.md
title: Amazon Bypass Open Redirect
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 30fcc6ab81a4230e75c116aaf07e5413e5de9df5e5d9061e26fb7b5087459e8f
text_sha256: 2132464dadcca1ef1ebfa919b5fd04cddc46065a823debaa7bf487709ac06553
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Amazon Bypass Open Redirect

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-19_amazon-bypass-open-redirect.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `30fcc6ab81a4230e75c116aaf07e5413e5de9df5e5d9061e26fb7b5087459e8f`
- Text SHA256: `2132464dadcca1ef1ebfa919b5fd04cddc46065a823debaa7bf487709ac06553`


## Content

---
title: "Amazon Bypass Open Redirect"
url: "https://medium.com/@honcbb/amazon-bypass-open-redirect-12609c879dff"
authors: ["Honc (@honcbb)"]
programs: ["Amazon"]
bugs: ["Open redirect"]
publication_date: "2017-11-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6045
scraped_via: "browseros"
---

# Amazon Bypass Open Redirect

Amazon Bypass Open Redirect
Honc
Follow
1 min read
·
Nov 20, 2017

5

When I first tried to find a loophole in Amazon, I found this station, URL A parameter caught my attention：

Press enter or click to view image in full size

https://primenow.amazon.com/onboard?sourceUrl=％2F

From this variable name I can daydream this is the page after the jump

I started building a proof-of-concept for this.

I found that if you simply enter the URL (for example, ?sourceUrl=facebook.com) failed

Doesn’t mean it’s not going to work out, I’ll try. Use the “//” symbol to bypass

But using //symbol to bypass > ?sourceUrl=//facebook.com Success

Get Honc’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Finally “ // “ bypassing, the final POC is

Poc Payload:

https://primenow.amazon.com/onboard?sourceUrl=//facebook.com
https://primenow.amazon.com/onboard?sourceUrl= //Your_Website.com

This is my private video demonstration Poc：

錄製_2017_02_01_00_23_27_794.mp4
Edit description

drive.google.com

Timeline
2017/02/01 12:32 Provide vulnerability details to Amazon Security Team
2017/02/01 02:44 Receive automatic response
2017/02/02 08:04 Receive response from Matt that inspection is in progress
2017/03/17 1:26 Received the Amazon Security Team (Matt) reply: Yes, it fixes
