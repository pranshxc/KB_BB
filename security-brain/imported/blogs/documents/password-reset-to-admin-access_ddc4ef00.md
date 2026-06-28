---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-01_password-reset-to-admin-access.md
original_filename: 2022-03-01_password-reset-to-admin-access.md
title: Password Reset to Admin Access
category: documents
detected_topics:
- jwt
- access-control
- command-injection
- password-reset
- otp
- api-security
tags:
- imported
- documents
- jwt
- access-control
- command-injection
- password-reset
- otp
- api-security
language: en
raw_sha256: ddc4ef00907e5690673c37971dc3ab244ea3ce6dd6ef4d075af9bf828142b3da
text_sha256: 754039bf659a2d165e14f38e1a41d42504b02c109f1fa27a1b9fe4474750f6df
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Password Reset to Admin Access

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-01_password-reset-to-admin-access.md
- Source Type: markdown
- Detected Topics: jwt, access-control, command-injection, password-reset, otp, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `ddc4ef00907e5690673c37971dc3ab244ea3ce6dd6ef4d075af9bf828142b3da`
- Text SHA256: `754039bf659a2d165e14f38e1a41d42504b02c109f1fa27a1b9fe4474750f6df`


## Content

---
title: "Password Reset to Admin Access"
url: "https://medium.com/techiepedia/password-reset-to-admin-access-3b2a649bdc3"
authors: ["Jesse Clark (@Hogarth45_)"]
bugs: ["Account takeover", "Authentication bypass", "Password reset"]
publication_date: "2022-03-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2861
scraped_via: "browseros"
---

# Password Reset to Admin Access

Member-only story

Password Reset to Admin Access
Jess
Follow
2 min read
·
Mar 1, 2022

82

2

While testing a web application that used a web GUI over the top of an API, I noted the calls to the API where authorized with a JWT token set in a Authorization header.

When requesting a password reset you are emailed a link to a form to update the password.
The password reset function would interact with the same API as the rest of the app, except now using a TEMP token, since obviously you cannot be authenticated at this time.

Press enter or click to view image in full size
100% secure password

Seeing this I decided to use the most popular open source hacking tool.
Copy & Paste

Dropping the TEMP token into the other API calls saved in Burp’s history, I was able to confirm that the TEMP token add admin authorization and would allow access to all data and functions in the environment.

Press enter or click to view image in full size
So hack

Since the temp token is something anyone can generate using the system, it is very important to ensure you test the authorization around it and be sure to not overlook the simple mechanisms surrounding authentication.

Do Follow Techiepedia for more Interesting write-ups!
