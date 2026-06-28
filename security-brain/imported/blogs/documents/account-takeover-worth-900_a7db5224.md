---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-16_account-takeover-worth-900.md
original_filename: 2019-06-16_account-takeover-worth-900.md
title: Account Takeover Worth $900
category: documents
detected_topics:
- sso
- command-injection
- otp
- csrf
tags:
- imported
- documents
- sso
- command-injection
- otp
- csrf
language: en
raw_sha256: a7db5224e8dedbd4ada224a7c6257ebc9d459fcc1fb9db87d9ea2fd4d0f0b4b8
text_sha256: 5984d452e4f5671cc6ad7fb78643696a9edf204588b3f0f0cf9082dd5cba8e42
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover Worth $900

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-16_account-takeover-worth-900.md
- Source Type: markdown
- Detected Topics: sso, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `a7db5224e8dedbd4ada224a7c6257ebc9d459fcc1fb9db87d9ea2fd4d0f0b4b8`
- Text SHA256: `5984d452e4f5671cc6ad7fb78643696a9edf204588b3f0f0cf9082dd5cba8e42`


## Content

---
title: "Account Takeover Worth $900"
url: "https://medium.com/@saadahmedx/account-takeover-worth-900-cacbe10de58e"
authors: ["Saad Ahmed (@XSaadAhmedX)"]
bugs: ["Account takeover", "CSRF"]
bounty: "900"
publication_date: "2019-06-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5210
scraped_via: "browseros"
---

# Account Takeover Worth $900

Account Takeover Worth $900
Saad Ahmed
Follow
2 min read
·
Jun 17, 2019

181

2

Hello guy’s I am back with another POC again this bug I found in PRIVATE program using on bugcrowd so without wasting the time let get started!

let assume the website private.com I created an account looking for CSRF Account Takeover but the website is secure & there is CSRF token also I try many method to bypass but failed so I started to play with it’s subdomain & I found one of it’s subdomain super.private.com when I try to login I used my main account credential & it worked here so most of developer they secure only main website

I started playing with this website the thing I am afraid of if a change account detail here hope it not redirect me to main site profile page & lucky it not redirect me :D

Get Saad Ahmed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I try to change the email & there is also a CSRF token when I saw that I am closing the burp suite but a give a last try & remove the CSRF token and boom it worked! email change Account Takeover

I made report & reported to the team & told them I can takeover main site accounts since the main site is TIER 1 :V & got this replay from the team

Press enter or click to view image in full size

Lesson: Never Give UP!

./Logout
