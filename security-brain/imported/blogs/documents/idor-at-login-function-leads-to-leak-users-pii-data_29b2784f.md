---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-30_idor-at-login-function-leads-to-leak-users-pii-data.md
original_filename: 2022-08-30_idor-at-login-function-leads-to-leak-users-pii-data.md
title: IDOR at Login function leads to leak user’s PII data
category: documents
detected_topics:
- api-security
- idor
- command-injection
- rate-limit
- information-disclosure
tags:
- imported
- documents
- api-security
- idor
- command-injection
- rate-limit
- information-disclosure
language: en
raw_sha256: 29b2784f6d170e935d34e63b859bb05f7b7e48a2f25c28bdf26cb354b3b2b376
text_sha256: f5c02a0c1c5cdc124ff362227dd15d354c7a299e359f93e592c8c7f19861729a
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR at Login function leads to leak user’s PII data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-30_idor-at-login-function-leads-to-leak-users-pii-data.md
- Source Type: markdown
- Detected Topics: api-security, idor, command-injection, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `29b2784f6d170e935d34e63b859bb05f7b7e48a2f25c28bdf26cb354b3b2b376`
- Text SHA256: `f5c02a0c1c5cdc124ff362227dd15d354c7a299e359f93e592c8c7f19861729a`


## Content

---
title: "IDOR at Login function leads to leak user’s PII data"
url: "https://eslam3kl.medium.com/idor-at-login-function-leads-to-leak-users-pii-data-d77e6613e9e0"
authors: ["Eslam Akl (@eslam3kll)"]
bugs: ["IDOR", "Information disclosure"]
publication_date: "2022-08-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2240
scraped_via: "browseros"
---

# IDOR at Login function leads to leak user’s PII data

IDOR at Login function leads to leak user’s PII data
Eslam Akl
Follow
2 min read
·
Aug 31, 2022

125

4

Hello @All. Today we will talk about one of my latest findings at a private program. The vulnerable function is the login function that manages the attacker to replace the username and leak the PII for any registered user.

Let’s start the bug’s reproduction steps, and if you need to see a quick definition for the IDOR, just check this malicious user 1234

Press enter or click to view image in full size
Steps to reproduce

1. At the vulnerable subdomain, you have a login function that requires to enter your username first and then if it’s valid, you will proceed to the next step to enter your password.

Get Eslam Akl’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2. After entering a random user test I surprised that there’s an existent user called test and I obtained all his PII data in the response. The endpoint seems likehttps://subdomain.target.com/v1.0.0/dev/userfirm/<username>

Press enter or click to view image in full size

3. Send this request to the intruder and try with any leaked usernames to be more real.

Press enter or click to view image in full size

By this way we can obtain most of the system users’ info like

Username
First/Last name
Email address
Phone number
Telephone
Firm Name
User ID

After reporting the bug resolved and marked as P1

Mitigation/Fixing

1. Restrict the repose to not include any sensitive data, the developers needs these sensitive info to send them to another function, but they forget to restrict them far away the attacker's view. They can replace the PII data with a sentence like:

{"userExist":"true", "errors": null}

2. Add a throttling control at the specified API endpoint to stop any brute forcing attempts.

That All :)

Stay in touch

GitHub | LinkedIn | Twitter

Thank you ❤
