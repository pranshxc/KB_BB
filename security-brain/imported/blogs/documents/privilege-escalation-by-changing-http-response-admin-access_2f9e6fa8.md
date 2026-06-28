---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-10_privilege-escalation-by-changing-http-response-admin-access.md
original_filename: 2020-06-10_privilege-escalation-by-changing-http-response-admin-access.md
title: Privilege Escalation by Changing HTTP Response (Admin Access)
category: documents
detected_topics:
- sso
- idor
- access-control
- command-injection
- rate-limit
tags:
- imported
- documents
- sso
- idor
- access-control
- command-injection
- rate-limit
language: en
raw_sha256: 2f9e6fa8a59396d4707db14106dd8f26420c30fc9e8c94bf799d7dcc965787fc
text_sha256: 53f3935bd57da6dc77f1413b7f8f2bd845b2fe57ce35b9a27a8be39953037606
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege Escalation by Changing HTTP Response (Admin Access)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-10_privilege-escalation-by-changing-http-response-admin-access.md
- Source Type: markdown
- Detected Topics: sso, idor, access-control, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `2f9e6fa8a59396d4707db14106dd8f26420c30fc9e8c94bf799d7dcc965787fc`
- Text SHA256: `53f3935bd57da6dc77f1413b7f8f2bd845b2fe57ce35b9a27a8be39953037606`


## Content

---
title: "Privilege Escalation by Changing HTTP Response (Admin Access)"
url: "https://medium.com/@bachrudinashari/privilege-escalation-by-changing-http-response-admin-access-5e67c44713f6"
authors: ["Bachrudin Ashari Pujakusuma (@Bachrudinashari)"]
bugs: ["Privilege escalation"]
bounty: "563"
publication_date: "2020-06-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4511
scraped_via: "browseros"
---

# Privilege Escalation by Changing HTTP Response (Admin Access)

Privilege Escalation by Changing HTTP Response (Admin Access)
A story about how I got a bug from a marketplace in Indonesia.
Bachrudin Ashari Pujakusuma
Follow
2 min read
·
Jun 10, 2020

152

Press enter or click to view image in full size
Figure 1 Privilege Escalation

Hello everyone, this was my first writeup for this community. I hope you enjoy it!

I discovered this vulnerability in April, the target was a marketplace in Indonesia. Let’s say the target is Redacted.com. The target has few websites and uses single sign-on (SSO) to login on their website. Single sign-on (SSO) is a session and user authentication service that permits a user to use one set of login credentials to access multiple applications or websites.

Now register to redacted.com and complete the registration, go to profile and intercept this request with burp suite to see the HTTP responses. I found “is_admin”:false parameter in the HTTP Response which caught my attention. Then I did subdomain enumeration with Sublist3r and found admin.redacted.com.

admin.redacted.com need a credential to log in, but realize the website use SSO to authenticate the users. So, go to admin.redacted.com and intercept this request, change “is_admin”:false parameter to “is_admin”:true. Booom I was a success login as admin. I able to edit (deleted, add) products, edit (deleted, add)banners, etc.

Press enter or click to view image in full size
Figure 2 Flow of Execution

Why does this happen?

Get Bachrudin Ashari Pujakusuma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

admin.redacted.com validates only on the frontend, the frontend takes the “is_admin” parameter to validates the user is admin or not, so the attacker can perform man in the middle attack (MITM), with changing the HTTP response to be “is_admin” = true.

Timeline of the Report

April 17, 2020 : Report Sent

April 21, 2020 : Triaged

May 8, 2020 : Bounty Rewarded (Rp 8.000.000)

References
From 3,99 to 1,650 USD (Part I) — Simple Vertical Privilege Escalation by Changing HTTP Response
A story about how I got several simple bugs (1 P2, 1 P3, and 2 P4s) on a target (that just allow Specific Country Code…

medium.com

https://portswigger.net/web-security/access-control
