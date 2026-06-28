---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-03_idor-leads-to-leak-private-details.md
original_filename: 2022-01-03_idor-leads-to-leak-private-details.md
title: IDOR leads to leak Private Details
category: documents
detected_topics:
- idor
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- api-security
language: en
raw_sha256: 1d686aab4b6b11c365fa81338f852b15f3331abada7db49a31ddb1f1da32441b
text_sha256: 802f3530e269dfe2815f6b1e4fb825ed8cbb1d1d3fd9158b48cc1ced46bda7c6
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR leads to leak Private Details

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-03_idor-leads-to-leak-private-details.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `1d686aab4b6b11c365fa81338f852b15f3331abada7db49a31ddb1f1da32441b`
- Text SHA256: `802f3530e269dfe2815f6b1e4fb825ed8cbb1d1d3fd9158b48cc1ced46bda7c6`


## Content

---
title: "IDOR leads to leak Private Details"
url: "https://infosecwriteups.com/idor-leads-to-leak-private-details-866563365490"
authors: ["annonymous"]
bugs: ["IDOR"]
publication_date: "2022-01-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3035
scraped_via: "browseros"
---

# IDOR leads to leak Private Details

IDOR leads to leak Private Details
annonymous
Follow
2 min read
·
Jan 3, 2022

61

I Wish you Merry Christmas & happy new year to you readers. May this year bring us nothing more than love, joy, happiness, P1,P2 bugs,Bounties and laughter😊😊.So let’s get start.

What is IDOR?

IDOR vulnerability is known as Insecure direct object reference.

Insecure direct object references (IDOR) are a type of access control vulnerability that arises when an application uses user-supplied input to access objects directly.

Let’s assume target program is : https://www.program.com

I have started recon process. Here I have found that It doesn’t have large scope. It has a very less domains.

Small Tip : What I do when I Found such a small scope target!!

1 > Fuzzing using Seclists github repository : https://github.com/danielmiessler/SecLists

2 > Capture & check for all the request manually in burpsuit

As per above stated I have Started fuzzing with wordlist of Seclists github repository & created account on the target website & capture all the request in the burpsuit. Then I have started analyzing all the request, When hanging out with this requests I came to know that there was an endpoint

/endpoint/id/info

Get annonymous’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Looks interesting 😎😎.immediately I have sent this request to the Intruder.

In this endpoint, I started playing with id in burpsuit. At the time of creating account Target program assign me a unique id. So my final path is look alike

https://target.com/endpoint/xxxx/info

I have randomly added some wordlists in the payload for the sniper attack in the intruder & booom💥💥💥.

It comes with other user’s details like ID ,auth_details ,Org_name ,Private subdomain info.

Straightaway I have reported this issue to the target program & they have catch this issue & gave me few bucks for the appreciation.

TimeLine:
05/06/2021 : Reported
07/06/2021 : Status-Accepted
20/06/2021 : Rewarded

Conclusion : Don’t miss any endpoint during Hunting

Follow:

Twitter : https://twitter.com/OwnRadius

Thank you so much for reading…
