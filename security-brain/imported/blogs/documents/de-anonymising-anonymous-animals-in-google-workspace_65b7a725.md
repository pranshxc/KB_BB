---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-29_de-anonymising-anonymous-animals-in-google-workspace.md
original_filename: 2021-04-29_de-anonymising-anonymous-animals-in-google-workspace.md
title: De-anonymising Anonymous Animals in Google Workspace
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: 65b7a725757e55ea583c66cc78b01b5f836f48603c04d0218283ce7399009724
text_sha256: 919dd7c5aa7e766eb23112e5a4a752eb4345158d9c8a5afa309ed6b1041a7187
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# De-anonymising Anonymous Animals in Google Workspace

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-29_de-anonymising-anonymous-animals-in-google-workspace.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `65b7a725757e55ea583c66cc78b01b5f836f48603c04d0218283ce7399009724`
- Text SHA256: `919dd7c5aa7e766eb23112e5a4a752eb4345158d9c8a5afa309ed6b1041a7187`


## Content

---
title: "De-anonymising Anonymous Animals in Google Workspace"
page_title: "[#0003] De-anonymising Anonymous Animals in Google Docs products | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0003"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0003"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Google"]
bugs: ["Privacy issue", "Information disclosure"]
publication_date: "2021-04-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3696
---

#0003  
Vendor: Google  
Status: fixed  
Reported: Jan 29, 2021  
Disclosed: Apr 29, 2021 (90 days) 

# De-anonymising Anonymous Animals in Google Docs products

**Summary:**

In products that use the same real-time collaboration system as Google Docs, “Anonymous Animals” can leak the underlying user’s identity by exposing the real `userId` of the victim. If the attacker already knows the `userId` of a given victim, she can de-anonymise the victim when the victim is an “Anonymous Animal”.

**Core Issue:**

Every active Google Docs user is polling the `/bind` endpoint for new real-time events. If a new user opens the document, every already connected user will receive a “connection event” from the `/bind` endpoint with the new user’s user object which includes the new user’s name, profile picture, and among others, the `userId`.

This `userId` is unique for only one product. So for example Docs, Sheets and Slides use different `userId`s for the same underlying Google user.

The core issue is that when a user is an “Anonymous Animal”, her `userId` should also be anonymous, and not the same as her real identity’s `userId`. Currently a user’s real `userId` and “Anonymous Animal” `userId` is the same, allowing an attacker to de-anonymise a victim.

**Steps to reproduce:**

  1. Create 2 Google accounts: `Attacker` and `Victim`
  2. [`Attacker`] Create a new Google Docs document and invite `Victim` using her email address, as a viewer
  3. [`Attacker`] Start monitoring the `/bind` responses
  4. [`Victim`] Open the Google Docs created in `Step 2.`
  5. [`Attacker`] See the victim’s user object in the `/bind` responses, and note the victim’s `userId`
  6. [`Attacker`] Create a new Google Docs document and share it to `anyone with the link` -> `Viewer`
  7. [`Attacker`] Start monitoring the `/bind` responses
  8. [`Victim`] Open the Google Docs created in `Step 6.`
  9. [`Attacker`] See the Anonymous Animal’s user object in the `/bind` responses, and see that this `userId` is the same `userId` previously noted in `Step 5.`

**Impact:**

This issue **could be used to de-anonymise victims just by making them visit a malicious link/website** which could redirect to/embed an attacker controlled e.g. Google Docs, which when opened by the victim, leaks the victim’s `userId` to the attacker.

This requires a targeted attack, since an attacker needs to have pre-collected mapping data between `userId`s and Google accounts.

I wanted to find a way to increase the impact and convert a `userId` to a name/email, but I didn’t have any success. If it’s somehow possible to convert a `userId` to a name/email, it would allow mass de-anonymisation of every Google user who visits a malicious link.

**[Disclosure Warning]:**

_This is a new system I am experimenting with:_

**This issue is subject to a 90 day disclosure deadline.** On `2021-04-29` this report with all additional comments will be publicly disclosed. Sensitive details from the report/comments such as names/email addresses will be redacted. If you would like to redact additional information or if for some reason the issue can’t be fixed until the deadline, let me know in a comment.

Thank you!
