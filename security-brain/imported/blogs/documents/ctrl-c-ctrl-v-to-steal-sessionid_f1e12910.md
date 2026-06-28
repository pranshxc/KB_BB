---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-18_ctrlc-ctrlv-to-steal-sessionid.md
original_filename: 2017-07-18_ctrlc-ctrlv-to-steal-sessionid.md
title: ctrl+c & ctrl+v to Steal SESSIONID
category: documents
detected_topics:
- command-injection
- clickjacking
tags:
- imported
- documents
- command-injection
- clickjacking
language: en
raw_sha256: f1e12910029fe9c696f87c4baebaa576bce173a6a16cd09203b6b7b333d65c75
text_sha256: 08224b8435fc2097309a3f443c52c28323457cd2d8aa52784c1ec094491572f1
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# ctrl+c & ctrl+v to Steal SESSIONID

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-18_ctrlc-ctrlv-to-steal-sessionid.md
- Source Type: markdown
- Detected Topics: command-injection, clickjacking
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `f1e12910029fe9c696f87c4baebaa576bce173a6a16cd09203b6b7b333d65c75`
- Text SHA256: `08224b8435fc2097309a3f443c52c28323457cd2d8aa52784c1ec094491572f1`


## Content

---
title: "ctrl+c & ctrl+v to Steal SESSIONID"
url: "https://medium.com/@arbazhussain/ctrl-d5ffc7b0640e"
authors: ["Arbaz Hussain (@ArbazKiraak)"]
bugs: ["Clickjacking"]
bounty: "100"
publication_date: "2017-07-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6154
scraped_via: "browseros"
---

# ctrl+c & ctrl+v to Steal SESSIONID

ctrl+c & ctrl+v to Steal SESSIONID
Arbaz Hussain
Follow
1 min read
·
Jul 19, 2017

16

Severity : Medium

Complexity: Medium

Get Arbaz Hussain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Weakness: Missing Click-jacking Header

During directory brute-forcing for 2–3 days , I Came Across Following Endpoint .

https://site.com/ping/ loggedIn

Response :

{
“type”: “Ping”,
“loggedIn”: true,
“username”: “arbazkiraak007”,
“sessionId”: “54CA86A999CB2DE0CD87F1EB37289261-n3”,
“instanceId”: “i-3c2662af”
}

Which Cointain’s the Cookie Header Value i.e SESSIONID in Response.
Their Application have Good Protection Against Click-jacking Vector’s on each and Every Endpoint But They missed Adding X-FRAME-OPTION Header to this endpoint .
Press enter or click to view image in full size
Created a Simple Demonstration of Stealing SESSIONID By Copy paste Game!
