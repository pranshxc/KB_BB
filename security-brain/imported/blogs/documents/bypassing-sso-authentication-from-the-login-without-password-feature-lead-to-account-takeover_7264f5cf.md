---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-20_bypassing-sso-authentication-from-the-login-without-password-feature-lead-to-acc.md
original_filename: 2023-02-20_bypassing-sso-authentication-from-the-login-without-password-feature-lead-to-acc.md
title: Bypassing SSO Authentication from the Login Without Password Feature Lead to
  Account Takeover
category: documents
detected_topics:
- otp
- sso
- command-injection
- cors
tags:
- imported
- documents
- otp
- sso
- command-injection
- cors
language: en
raw_sha256: 7264f5cfc12cc67379e383dc06ef6a9e0a74d401a4e439daa589a0790d92726b
text_sha256: 56ea06b3497d02a30bf5249d6c3bb87600efc41846b4f3ee870ef5e7e8706c73
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing SSO Authentication from the Login Without Password Feature Lead to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-20_bypassing-sso-authentication-from-the-login-without-password-feature-lead-to-acc.md
- Source Type: markdown
- Detected Topics: otp, sso, command-injection, cors
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `7264f5cfc12cc67379e383dc06ef6a9e0a74d401a4e439daa589a0790d92726b`
- Text SHA256: `56ea06b3497d02a30bf5249d6c3bb87600efc41846b4f3ee870ef5e7e8706c73`


## Content

---
title: "Bypassing SSO Authentication from the Login Without Password Feature Lead to Account Takeover"
url: "https://aidilarf.medium.com/bypassing-sso-authentication-from-the-login-without-password-feature-lead-to-account-takeover-d2322a33a208"
authors: ["Aidil Arief"]
bugs: ["Account takeover", "SSO", "OTP", "Authentication bypass"]
publication_date: "2023-02-20"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1507
scraped_via: "browseros"
---

# Bypassing SSO Authentication from the Login Without Password Feature Lead to Account Takeover

Bypassing SSO Authentication from the Login Without Password Feature Lead to Account Takeover
Aidil Arief
Follow
3 min read
·
Feb 20, 2023

211

2

Hi Everyone,

When I did Bug Hunting, I found the Login without Password feature. The Login without Password feature is a feature that is used for valid account users to log in without a password or valid account users can only log in using the OTP ( One-Time Password ) sent to the linked account email.

Press enter or click to view image in full size

Before continuing, I will provide a little information regarding these vulnerable websites in the form of :

The website supports the use of email on multiple accounts because the SSO they implement to log in only uses the username and not the linked email.

And here I, as an attacker, I have 2 accounts with different usernames that have been linked using the same emails, namely :

Username : attacker1
Press enter or click to view image in full size

2. Username : attacker2

Press enter or click to view image in full size

Then I tried going to the Login without Password feature. Then, I entered my account email. Following are screenshots:

Press enter or click to view image in full size

And after that, the OTP was sent to my email ( attacker ).

Press enter or click to view image in full size

Then I entered the OTP there, then you will get an account selection page for SSO login without a password like:

Press enter or click to view image in full size

Notes:

From the screenshot above on the account selection page for SSO login without a password, you are required to have 2 accounts with different usernames and linked to the same email. Because if you only have 1 account with that email, then when you enter the correct OTP in the SSO Login request without a password, you will not get an account selection page for an SSO login without a password as in the screenshot above, but you will be immediately redirected SSO login to your account.

If so, catch the request when selecting one of your accounts on the account selection page for SSO login without a password.

Get Aidil Arief’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Here’s the request:

POST /api/sso/login-without-password/auth HTTP/2
Host: sso.redacted.com
Cookie: [COOKIE]
User-Agent:
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Origin: https://www.redacted.com/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Content-Length: 226

{“track”:006,”action”:”login-without-password”,”code”:”[OTP]”,”token”:”22123w2DS4543jg23324e35SD==”,”username”:”attacker1"}

The following is a screenshot of the request :

Press enter or click to view image in full size

I can see that there are several parameters in there, and I was surprised to see the username parameter.

Because I was curious, I tried to replace the username parameter value with the victim’s username.

It worked, SSO redirected to the final Endpoint of the Victim account.

Press enter or click to view image in full size

Finally I got Account Takeover Vulnerability here.
