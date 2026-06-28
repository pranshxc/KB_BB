---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-03_bugbounty-adding-money-using-response-modification.md
original_filename: 2020-05-03_bugbounty-adding-money-using-response-modification.md
title: '#BugBounty — Adding Money Using Response Modification'
category: documents
detected_topics:
- command-injection
- business-logic
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- business-logic
- api-security
- mobile-security
language: en
raw_sha256: 6c6800c9eec47309b3f120ac39d97ccd2f26edb8925b0e73c533996ae7c0976f
text_sha256: 666a2c2a8329abce01d87a242836bef6ddb3463f724fc0ad1f62a8d271984ea3
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — Adding Money Using Response Modification

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-03_bugbounty-adding-money-using-response-modification.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `6c6800c9eec47309b3f120ac39d97ccd2f26edb8925b0e73c533996ae7c0976f`
- Text SHA256: `666a2c2a8329abce01d87a242836bef6ddb3463f724fc0ad1f62a8d271984ea3`


## Content

---
title: "#BugBounty — Adding Money Using Response Modification"
url: "https://medium.com/@sandeepkumarsingh1902/bugbounty-adding-money-using-response-modification-334448d34251"
authors: ["Line_no 6"]
bugs: ["Payment tampering", "Logic flaw"]
publication_date: "2020-05-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4611
scraped_via: "browseros"
---

# #BugBounty — Adding Money Using Response Modification

#BugBounty — Adding Money Using Response Modification
Line_no 6
Follow
2 min read
·
May 3, 2020

203

Hello Everyone,

One thing i have learnt with the hacking community is sharing is caring. If you have some nice findings you should definitely share it, so here i am with a blog after a very long time. This vulnerability was one of my interesting finding.I usually keep by burp open all the time. Meanwhile i was trading on a cryptocurrency trading platform. Going forward we will use “abc.com” for the trading platform.

I saw a deal where the ripple (a cryptocurrency) was trading at very low rate. But unfortunately i was not having money in my wallet. So i added money in my wallet. Meanwhile after adding the money i looked at the burp logs, which looks as the normal request.

But out of curiosity I thought of playing with the request. Immediately i turn on burp intercept. Repeated the same process of adding money but this time i deliberately failed the process instead of adding money, so when the command was going from the payment gateway back to “abc.com”, i changed the response with the earlier successful response with a change in timestamp and transaction id.

Press enter or click to view image in full size
A failed transaction going from payment gateway to host.
Press enter or click to view image in full size
A failed transaction replaced with a successful request.

To my surprise i got a notification stating money was added successfully to my wallet. I immediately went to transaction history and i was surprised to see money was added successfully.

Press enter or click to view image in full size

I quickly followed up with the team, they was fast enough to fix.

Press enter or click to view image in full size

And this is how I was able to add money in my wallet without paying for it.

Get Line_no 6’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Report details-

14-April-2020 — Bug reported to the concerned company.

15-April-2020 — Bug was marked fixed.

15-April-2020 — Re-tested and confirmed the fix.

02-May-2020 — Rewarded.

Thanks for reading!
