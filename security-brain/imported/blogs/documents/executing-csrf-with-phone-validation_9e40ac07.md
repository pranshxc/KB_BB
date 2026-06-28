---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-04_executing-csrf-with-phone-validation.md
original_filename: 2021-06-04_executing-csrf-with-phone-validation.md
title: Executing CSRF With Phone Validation
category: documents
detected_topics:
- csrf
- command-injection
- otp
- automation-abuse
- cors
tags:
- imported
- documents
- csrf
- command-injection
- otp
- automation-abuse
- cors
language: en
raw_sha256: 9e40ac07e21099ac5041986056b233dcd3596577fca0e826d17d15ee6e083830
text_sha256: 6b278234da4c7888b60f75c0f61973c956eb88865a293d8c3a69e893072b07ef
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Executing CSRF With Phone Validation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-04_executing-csrf-with-phone-validation.md
- Source Type: markdown
- Detected Topics: csrf, command-injection, otp, automation-abuse, cors
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `9e40ac07e21099ac5041986056b233dcd3596577fca0e826d17d15ee6e083830`
- Text SHA256: `6b278234da4c7888b60f75c0f61973c956eb88865a293d8c3a69e893072b07ef`


## Content

---
title: "Executing CSRF With Phone Validation"
url: "https://infosecwriteups.com/executing-csrf-with-phone-validation-103c525dd310"
authors: ["Greg Gibson"]
bugs: ["CSRF"]
publication_date: "2021-06-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3598
scraped_via: "browseros"
---

# Executing CSRF With Phone Validation

Member-only story

Executing CSRF With Phone Validation
How to Programmatically Harvest the OTP
Greg Gibson
Follow
5 min read
·
Jun 4, 2021

77

When I submit a vulnerability on a Bug Bounty program, I typically seek to build an exploit that automates as much of the Proof of Concept as possible to:

Ensure it’s 100% clear the exploit can do what I’m claiming.
Simplify reproduction for both the triage team and the company — if the reproduction steps require the team to simply navigate to a URL you supply, you can eliminate any confusion.
Have fun! Building things is a great way to learn new tech.

I recently identified a Cross Origin Resource Sharing (CORS) vulnerability on an API that allowed a user to add a phone number to their account. In what is a fairly common flow, the user first would submit their phone number, the application would text a six digit One Time Password (OTP) to that phone number, and the user would then enter the OTP into the website to prove it was in fact their legitimate phone number.

This flow can provide both validations — by ensuring users enter a phone number they control, and security — as it makes it difficult for an attacker to take advantage of a Cross-Site Request Forgery (CSRF) vulnerability as you must make two distinct API calls with a dynamic value triggered by the first (and importantly delivered…
