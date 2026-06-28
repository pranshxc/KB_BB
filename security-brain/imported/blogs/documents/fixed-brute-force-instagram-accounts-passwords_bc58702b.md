---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-05_fixed-brute-force-instagram-accounts-passwords.md
original_filename: 2019-03-05_fixed-brute-force-instagram-accounts-passwords.md
title: 'Fixed : Brute-force Instagram account’s passwords'
category: documents
detected_topics:
- rate-limit
- command-injection
tags:
- imported
- documents
- rate-limit
- command-injection
language: en
raw_sha256: bc58702b7dbaa61ecbc71aa2209c3447a883b0d09ad3c1d2af19350bbd142f0a
text_sha256: dcc87c986487ca489bff54bc21f22b6f60c44e5920b49b4b42008469b7f2d8a6
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: true
---

# Fixed : Brute-force Instagram account’s passwords

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-05_fixed-brute-force-instagram-accounts-passwords.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: True
- Raw SHA256: `bc58702b7dbaa61ecbc71aa2209c3447a883b0d09ad3c1d2af19350bbd142f0a`
- Text SHA256: `dcc87c986487ca489bff54bc21f22b6f60c44e5920b49b4b42008469b7f2d8a6`


## Content

---
title: "Fixed : Brute-force Instagram account’s passwords"
url: "https://medium.com/@addictrao20/fixed-brute-force-instagram-accounts-passwords-938471b6e9d4"
authors: ["Sameer Rao"]
programs: ["Meta / Facebook"]
bugs: ["Bruteforce", "Rate limiting bypass"]
publication_date: "2019-03-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5377
scraped_via: "browseros"
---

# Fixed : Brute-force Instagram account’s passwords

Fixed : Brute-force Instagram account’s passwords
Sameer Rao
Follow
2 min read
·
Mar 5, 2019

34

Description :
We can add an Instagram account to a Facebook Page having a role on the page as an admin or editor. Adding an Instagram account to Facebook Page will allow us to create Instagram ads in Ads Manager without needing to connect to the Instagram account to a Business Manager.

There is an endpoint to connect Instagram account through the mobile browser or “mbasic.facebook.com”

POST /Redacted HTTP/1.1
Host: mbasic.facebook.com

fb_dtsg: — sanitized —
jazoest: — sanitized —
username: VICTIM_INSTAGRAM_USERNAME
password=***REDACTED***
page_id: ATTACKER_PAGE_ID

Login Security:
Facebook uses a rate-limiting mechanism to protect the login request from being password guesses. I could attempt only max 20 wrong passwords in a day. If I exceed 20 attempts, it fired “too many requests.” and then a further request will be blocked.

What was Bug here?

At the endpoint, Facebook failed to block attempts over Victim Account on the server side.
The limit was 20 requests “each Facebook Account.”

Get Sameer Rao’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Bypassing a Rate Limiting:

1 Facebook Account = 20 wrong password attempts were possible at a time.
10 Facebook Accounts = 200wrong password attempts.

At this point, I didn’t have a million user account’s to try out more attempts.

According to Facebook, we also can create a test account for Facebook applications.

[ref- https://developers.facebook.com/docs/apps/test-users/ ]
Each Facebook application can create 2000Test Accounts ( like one we can create using “/whitehat/accounts/”)

I created around 15 Facebook Apps.

15 apps x 2000 Test Accounts = 30,000 Test Users in a Single Facebook User Account.
I created 10 Regular Facebook User Accounts.
That mean, 10x30,000 = 300,000Test users

So Finally, I could attempt 6,000,000 passwords daily.

Timeline

Sep 21, 2018 — Report Sent
Sep 25, 2018 — Clarification requested by Facebook
Sep 26, 2018 — Clarification sent
Oct 3, 2018 -Triaged
Oct 3, 2018 — Closed as Informative( Impact is minimal)
Oct 4, 2018 -More details sent.
Oct 8,2018 — Triaged
Oct 26, 2018 — Ask for updates.
Nov 8,2018 — Fixed.
Nov 14,2018 — Bounty Awarded.
