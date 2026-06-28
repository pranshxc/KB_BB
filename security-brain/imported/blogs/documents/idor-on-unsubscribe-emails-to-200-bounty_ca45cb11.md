---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-06_idor-on-unsubscribe-emails-to-200-bounty.md
original_filename: 2022-11-06_idor-on-unsubscribe-emails-to-200-bounty.md
title: IDOR on Unsubscribe emails to $200 bounty.
category: documents
detected_topics:
- idor
- access-control
- command-injection
- otp
tags:
- imported
- documents
- idor
- access-control
- command-injection
- otp
language: en
raw_sha256: ca45cb112ccbc406b239b73fe1e11b88f853eb59d19e95ed8606b6b52b167e12
text_sha256: 2d404f31dc9ee0c64e3ed856ffa61a87e3254656b9fdf03f5220682865ce0845
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: true
---

# IDOR on Unsubscribe emails to $200 bounty.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-06_idor-on-unsubscribe-emails-to-200-bounty.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: True
- Raw SHA256: `ca45cb112ccbc406b239b73fe1e11b88f853eb59d19e95ed8606b6b52b167e12`
- Text SHA256: `2d404f31dc9ee0c64e3ed856ffa61a87e3254656b9fdf03f5220682865ce0845`


## Content

---
title: "IDOR on Unsubscribe emails to $200 bounty."
url: "https://medium.com/@shellyshubh/idor-on-unsubscribe-emails-to-200-bounty-ae16fb783b01"
authors: ["shbugger1"]
bugs: ["IDOR"]
bounty: "200"
publication_date: "2022-11-06"
added_date: "2022-11-08"
source: "pentester.land/writeups.json"
original_index: 1943
scraped_via: "browseros"
---

# IDOR on Unsubscribe emails to $200 bounty.

IDOR on Unsubscribe emails to $200 bounty.
shbugger1
Follow
2 min read
·
Nov 6, 2022

38

2

Recently I got an invitation from a financial website. I registered my account but initially was unable to find anything.

I check my emails very often, I have a habit to read all the emails to avoid all that mess. One email was from the same website, it was a price alert for bitcoin.

Get shbugger1’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After reading the email, one thing caught my attention.

I thought that it might be vulnerable to IDOR if an attacker could unsubscribe anyone. The unsubscribe link was like this -

https://emails.target.com/unsubscribe?data=eyJ1c2VyX2lkIjoic29tZSB1c2VyIGlkIiwicHJlZmVyZW5jZSI6InByaWNlX2FsZXJ0cyIsInNvdXJjZSI6ImVtYWlsLnJldGFpbC5wcmljZV9hbGVydCIsInByb2R1Y3RfaWQiOiIiLCJkb21haW4iOiIiLCJtZXNzYWdlX3R5cGVfaWQiOiIifQ%3D%3D--c9d65485530ba1984abac2be***REDACTED-SUSPECT-TOKEN***Now I was sure that the part before %3D was a base64 encoded string and after it was a token. After decoding I got this -

base64 - eyJ1c2VyX2lkIjoic29tZSB1c2VyIGlkIiwicHJlZmVyZW5jZSI6InByaWNlX2FsZXJ0cyIsInNvdXJjZSI6ImVtYWlsLnJldGFpbC5wcmljZV9hbGVydCIsInByb2R1Y3RfaWQiOiIiLCJkb21haW4iOiIiLCJtZXNzYWdlX3R5cGVfaWQiOiIifQ 6
decoded -
{"user_id":"some user id","preference":"price_alerts","source":"email.retail.price_alert"} 
token - 
c9d65485530ba1984abac2be***REDACTED-SUSPECT-TOKEN***So I took the decoded string to https://base64decode.org/ changed the user id and encoded it back again and modified the url for that. After visiting that url

So I reported this issue, after two weeks it was triaged and I was rewarded with $200 as bounty

Press enter or click to view image in full size

Thanks for reading.
