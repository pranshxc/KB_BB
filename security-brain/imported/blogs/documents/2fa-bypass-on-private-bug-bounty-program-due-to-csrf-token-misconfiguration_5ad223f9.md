---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-22_2fa-bypass-on-private-bug-bounty-program-due-to-csrf-token-misconfiguration.md
original_filename: 2022-05-22_2fa-bypass-on-private-bug-bounty-program-due-to-csrf-token-misconfiguration.md
title: 2FA Bypass on private bug bounty program due to CSRF token misconfiguration
category: documents
detected_topics:
- mfa
- command-injection
- otp
- csrf
tags:
- imported
- documents
- mfa
- command-injection
- otp
- csrf
language: en
raw_sha256: 5ad223f95fe4d12ffeb287d19179872e9d0cf3b6d75aa9d3c477a9e7efe055d5
text_sha256: 9173db06434858f71b5dab88956b1ce153a109631d2123e86907a7b7af9c2b43
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# 2FA Bypass on private bug bounty program due to CSRF token misconfiguration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-22_2fa-bypass-on-private-bug-bounty-program-due-to-csrf-token-misconfiguration.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `5ad223f95fe4d12ffeb287d19179872e9d0cf3b6d75aa9d3c477a9e7efe055d5`
- Text SHA256: `9173db06434858f71b5dab88956b1ce153a109631d2123e86907a7b7af9c2b43`


## Content

---
title: "2FA Bypass on private bug bounty program due to CSRF token misconfiguration"
url: "https://medium.com/@sharp488/2fa-bypass-on-private-bug-bounty-program-due-to-csrf-token-misconfiguration-5a9c82151a1"
authors: ["Sharat Kaikolamthuruthil (@sharp488)"]
bugs: ["2FA / MFA bypass"]
publication_date: "2022-05-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2618
scraped_via: "browseros"
---

# 2FA Bypass on private bug bounty program due to CSRF token misconfiguration

2FA Bypass on private bug bounty program due to CSRF token misconfiguration
Sharat Kaikolamthuruthil
Follow
2 min read
·
May 22, 2022

133

2

Press enter or click to view image in full size
2 Factor Authentication Bypass

Hello Friends,

This is my first blog on web application security. In this I will share the first of many 2FA bypasses that I found on private bug bounty programs.

I won’t be disclosing the program name due to program policy but this website is a financial institute so 2FA is crucial for them.

Get Sharat Kaikolamthuruthil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Lets call the program redacted.com with 2FA enabled in the account we login.

First I captured the login request which has an authentication_token parameter passed in the body as show below.
Press enter or click to view image in full size
Now we delete the authentication_token and forward the login request.
The application will return the following error response with the URL redacted.com/login
Press enter or click to view image in full size
Here I changed the URL to redacted.com/edit and hit enter. The application redirected me to account settings page without 2FA prompt and I was able to access every single page inside the account.
Press enter or click to view image in full size

Here there was a CSRF token misconfiguration which allowed the user to login with a valid session before validating 2FA code and thus I was able to successfully bypass 2FA.

Video POC demonstrated on custom website :

Hope you guys learnt something new, have a good day. 😃

Thanks!!
