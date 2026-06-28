---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-04_fiverr-email-restriction-bypassed-bounty-100.md
original_filename: 2021-11-04_fiverr-email-restriction-bypassed-bounty-100.md
title: Fiverr email restriction bypassed | Bounty 100$
category: documents
detected_topics:
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- business-logic
- api-security
language: en
raw_sha256: ba60bf10e01477d3db775a57d17b7ed989f24d67ee505099e8c7257a49786fa9
text_sha256: 0cc91c02ec462193df749ea4c361c1fc94be1c50f4c4883f2e6a4bf038a15933
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Fiverr email restriction bypassed | Bounty 100$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-04_fiverr-email-restriction-bypassed-bounty-100.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `ba60bf10e01477d3db775a57d17b7ed989f24d67ee505099e8c7257a49786fa9`
- Text SHA256: `0cc91c02ec462193df749ea4c361c1fc94be1c50f4c4883f2e6a4bf038a15933`


## Content

---
title: "Fiverr email restriction bypassed | Bounty 100$"
url: "https://thinkermaruf.medium.com/fiverr-email-restriction-bypassed-36b797cb7e9"
authors: ["Maruf Hosan"]
programs: ["Fiverr"]
bugs: ["Logic flaw"]
bounty: "100"
publication_date: "2021-11-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3196
scraped_via: "browseros"
---

# Fiverr email restriction bypassed | Bounty 100$

Md Maruf Hosan (0xMaruf)
 highlighted

Fiverr email restriction bypassed | Bounty $100
Md Maruf Hosan (0xMaruf)
Follow
Nov 3, 2021

24

Hello brothers!
I told myself let’s post a gig on fiverr and let it be there.
I wanted to put my email address on the gig description so that the clients can contact me outside.

while doing this…………

I got a restriction :
Description may not contain an email address. Reminder: Communicating with other users outside of Fiverr is not permitted

then i found the main issue “@” sign was not allowed there.

Get Md Maruf Hosan (0xMaruf)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Simple bypass:
plain>html_enc> = didn't work
plain>html_enc>url_enc> = bypassed
payload “@” = “%26%23%78%34%30%3b”

Press enter or click to view image in full size

Bounty : 100$

https://twitter.com/0xmaruf

https://facebook.com/0xmaruf

Log in or sign up to view
See posts, photos and more on Facebook.

facebook.com
