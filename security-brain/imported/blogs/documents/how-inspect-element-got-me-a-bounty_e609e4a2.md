---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-06_how-inspect-element-got-me-a-bounty.md
original_filename: 2020-02-06_how-inspect-element-got-me-a-bounty.md
title: How Inspect Element Got me a Bounty
category: documents
detected_topics:
- command-injection
- otp
tags:
- imported
- documents
- command-injection
- otp
language: en
raw_sha256: e609e4a2318b49125c6e020177c60f0513a76f30c8cbac8ef383f3a5c582f409
text_sha256: 2bcd7ffe1d001f711293da8a9fe399f674b3491b36df32fcd31c94f93adda034
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How Inspect Element Got me a Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-06_how-inspect-element-got-me-a-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `e609e4a2318b49125c6e020177c60f0513a76f30c8cbac8ef383f3a5c582f409`
- Text SHA256: `2bcd7ffe1d001f711293da8a9fe399f674b3491b36df32fcd31c94f93adda034`


## Content

---
title: "How Inspect Element Got me a Bounty"
url: "https://medium.com/@hetroublemakr/how-inspect-element-got-me-a-bounty-58d3a9946225"
authors: ["Aditya Soni (@hetroublemakr)"]
bugs: ["Client-side enforcement of server-side security"]
publication_date: "2020-02-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4782
scraped_via: "browseros"
---

# How Inspect Element Got me a Bounty

Member-only story

How Inspect Element Got me a Bounty
Aditya Soni
Follow
2 min read
·
Feb 6, 2020

157

1

Hello guys, I recently encountered an amazing bypass to change my Phone Number in an application that doesn’t allow anyone to change its Phone number after registration. An Easy Win!

Case Study

As this was a private program all illustrations of vulnerabilities will be represented with the host as redact.com

The application had a Registration page where a user could register a new username and password which allowed him to log in to the application via the login page.

While doing the registration. In the end, the web application sends an OTP to the phone number to verify it. Till now it was all normal like every other application.

When opened “My Account”. It looked like this

And looked like every other account info page with not many options available, like as you can see email address and Mobile number options are disabled by default.
And I started playing with it, I opened Inspect Element and changed the value of Mobile Phone from ******3203 to ******3213
