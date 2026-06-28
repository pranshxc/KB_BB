---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-12_broken-session-control-leads-to-access-the-admin-panel-even-after-revoking-the-a.md
original_filename: 2022-04-12_broken-session-control-leads-to-access-the-admin-panel-even-after-revoking-the-a.md
title: 'Broken session control leads to access the admin panel even after revoking
  the access!! — #ZOHO'
category: documents
detected_topics:
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: d7e7586c55c1dbdc26918f30827afff823f0c318a7ab4c74cd7d8814e52ff2de
text_sha256: 3d79159ded95eaa003147d7f2ddd82687c5e572988f40bd92660f82c6f3f6d18
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Broken session control leads to access the admin panel even after revoking the access!! — #ZOHO

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-12_broken-session-control-leads-to-access-the-admin-panel-even-after-revoking-the-a.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `d7e7586c55c1dbdc26918f30827afff823f0c318a7ab4c74cd7d8814e52ff2de`
- Text SHA256: `3d79159ded95eaa003147d7f2ddd82687c5e572988f40bd92660f82c6f3f6d18`


## Content

---
title: "Broken session control leads to access the admin panel even after revoking the access!! — #ZOHO"
url: "https://naveenroy008.medium.com/broken-session-control-leads-to-access-the-admin-panel-even-after-revoking-the-access-zoho-db219b19d2dd"
authors: ["Naveenroy"]
programs: ["Zoho"]
bugs: ["Broken Access Control"]
publication_date: "2022-04-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2724
scraped_via: "browseros"
---

# Broken session control leads to access the admin panel even after revoking the access!! — #ZOHO

Broken session control leads to access the admin panel even after revoking the access!! — #ZOHO
nave1n0x
Follow
2 min read
·
Apr 12, 2022

72

Hey Guy’s

Every IT Guy Know about the Zoho people plus, it is mostly used by the employees in the companies. Recently i found a vulnerability in Zoho people plus, the interesting thing is even after revoking the admin access, a user can still able to make changes on the Zoho people plus as a admin. All these changes are getting effected.

For example:

Let’s assume a scenario that the HR team by mistakenly or purposely giving admin access or any other role to the specific person in an organization. After sometime the HR team is revoking the access to that particular person, then also the user can able to access the admin features. They can change anything they want inside the admin panel and can perform all action that an admin can. The reason behind this issue is, After revoking access, here it is not checking whether the user is properly authorized for doing such action or not and the assigned token is not expiring after revoking the access.

Final POC Video:

Fix Status : Fixed

Get nave1n0x’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Reward: After panel meet… :)

So see y’all in a new write-up soon guys !!

Thanks for reading !!

Make sure to follow me on Twitter ;)

@Naveen
