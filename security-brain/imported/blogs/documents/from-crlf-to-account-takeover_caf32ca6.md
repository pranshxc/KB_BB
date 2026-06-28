---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-03_from-crlf-to-account-takeover.md
original_filename: 2020-06-03_from-crlf-to-account-takeover.md
title: From CRLF to Account Takeover
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
language: en
raw_sha256: caf32ca6ae75dd1544727541af967186336e4bb2c937f9a89f87a04c8708e954
text_sha256: d3af13abe9c6afe38bebeefedccabd972435c4307ae7d962c356fc14e6fbdef0
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# From CRLF to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-03_from-crlf-to-account-takeover.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `caf32ca6ae75dd1544727541af967186336e4bb2c937f9a89f87a04c8708e954`
- Text SHA256: `d3af13abe9c6afe38bebeefedccabd972435c4307ae7d962c356fc14e6fbdef0`


## Content

---
title: "From CRLF to Account Takeover"
url: "https://medium.com/@valeriyshevchenko/from-crlf-to-account-takeover-a94d7aa0d74e"
authors: ["Valeriy Shevchenko (@Krevetk0Valeriy)"]
bugs: ["CRLF injection", "HTTP response splitting", "Reflected XSS", "Account takeover"]
publication_date: "2020-06-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4532
scraped_via: "browseros"
---

# From CRLF to Account Takeover

Member-only story

From CRLF to Account Takeover
Valeriy Shevchenko
Follow
7 min read
·
Jun 3, 2020

197

Press enter or click to view image in full size

Many people don’t like client-side vulnerabilities. I’m not a fan of such vulnerabilities as well. And I try to spend less time searching for them. You can’t surprise anyone with endless alert-boxes on the pages. But sometimes these alerts boxes can be worth their weight in gold. Especially if the execution of javascript is necessary for the chain to exploit a serious problem. Under a serious problem today we are talking about stealing user account.

In a classic XSS attack scenario, there is always reading user data, getting a token from local storage or cookies, modifying user data, changing data to steal an account. Typically, the hijacking is carried out through a change of email or password. To protect against that classic attack scenario came CSRF tokens. But these methods of protection can sometimes be bypassed by passing an empty token value, or do not pass at all csrf token in the request, or pass token but from another user session. There is a lot of tricks to bypass that protection layer and perfectly explained from 0ang3el here and here. But the advent of a global browser policy is not far off and will kill classic XSS+CSRF attacks with SameSite by default. Now we still have time to use the CSRF features because the release of changes in browsers has been slightly shifted due to the situation in the world.
