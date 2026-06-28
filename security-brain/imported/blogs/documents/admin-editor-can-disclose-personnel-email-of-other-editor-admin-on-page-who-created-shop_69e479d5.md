---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-16_admin-editor-can-disclose-personnel-email-of-other-editor-admin-on-pagewho-creat.md
original_filename: 2020-07-16_admin-editor-can-disclose-personnel-email-of-other-editor-admin-on-pagewho-creat.md
title: Admin ,Editor can disclose personnel email of other editor, admin on page(who
  created shop)
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 69e479d5497af5beb4a3f3c11dec77572a1fc1903292633efd0f6955a550cfb4
text_sha256: 11252f8bc89fd81f0e2a2b6125775cad67d96a23da5a39b5167b7838477091b0
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Admin ,Editor can disclose personnel email of other editor, admin on page(who created shop)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-16_admin-editor-can-disclose-personnel-email-of-other-editor-admin-on-pagewho-creat.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `69e479d5497af5beb4a3f3c11dec77572a1fc1903292633efd0f6955a550cfb4`
- Text SHA256: `11252f8bc89fd81f0e2a2b6125775cad67d96a23da5a39b5167b7838477091b0`


## Content

---
title: "Admin ,Editor can disclose personnel email of other editor, admin on page(who created shop)"
url: "https://medium.com/@yaala/admin-editor-can-disclose-personnel-email-of-other-editor-admin-on-page-who-created-shop-57c35ed9f9b7"
authors: ["The 3 Day Account Takeover"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "1,000"
publication_date: "2020-07-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4408
scraped_via: "browseros"
---

# Admin ,Editor can disclose personnel email of other editor, admin on page(who created shop)

abdellah yaala
Follow
1 min read
·
Jul 17, 2020

56

Admin ,Editor can disclose personnel email of other editor, admin on page(who created shop)

Press enter or click to view image in full size

Details & impact:

=========

Disclose personal email address of the person who created the store on the page

Reproduction step:

==========

===

1 — userA admin on page1 , who create a shop in the page

2- userB EDITOR ON page1 ,

with whiteliste accesstoken userB can disclose the personel email of userA

Get abdellah yaala’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

GET /page1_id?fields=commerce_merchant_settings&access_token=accesstoken_userB

Fix: facebook remove contact_email field in the response.

Video:

Timeline:

May 03, 2020 — Report Sent.

After exchanging some messages.

May 28, 2020 — Acknowledged by Facebook

July 08, 2020 — Fixed by Facebook

July 16, 2020 — 1000$ Bounty awarded by Facebook

Thanks facebook security teams

https://twitter.com/yaalaab
