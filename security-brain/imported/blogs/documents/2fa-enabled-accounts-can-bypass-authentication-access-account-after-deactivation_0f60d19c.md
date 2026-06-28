---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-27_2fa-enabled-accounts-can-bypass-authentication-access-account-after-deactivation.md
original_filename: 2022-11-27_2fa-enabled-accounts-can-bypass-authentication-access-account-after-deactivation.md
title: 2FA Enabled Accounts Can Bypass Authentication & Access Account After Deactivation
category: documents
detected_topics:
- command-injection
- mfa
- otp
tags:
- imported
- documents
- command-injection
- mfa
- otp
language: en
raw_sha256: 0f60d19c69976da4e29a489fb4e1ccabcedebb6d59c11ea8388ab1cdaaa108c3
text_sha256: 2f5c583e72d780655bf5080aaee6a32a4688cacfaeff9c68a0d1c4a2f305b690
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# 2FA Enabled Accounts Can Bypass Authentication & Access Account After Deactivation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-27_2fa-enabled-accounts-can-bypass-authentication-access-account-after-deactivation.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, otp
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `0f60d19c69976da4e29a489fb4e1ccabcedebb6d59c11ea8388ab1cdaaa108c3`
- Text SHA256: `2f5c583e72d780655bf5080aaee6a32a4688cacfaeff9c68a0d1c4a2f305b690`


## Content

---
title: "2FA Enabled Accounts Can Bypass Authentication & Access Account After Deactivation"
url: "https://medium.com/@sharp488/2fa-enabled-accounts-can-bypass-authentication-access-account-after-deactivation-8276a586be82"
authors: ["Sharat Kaikolamthuruthil (@sharp488)"]
bugs: ["Authentication bypass", "Account takeover"]
publication_date: "2022-11-27"
added_date: "2022-11-30"
source: "pentester.land/writeups.json"
original_index: 1849
scraped_via: "browseros"
---

# 2FA Enabled Accounts Can Bypass Authentication & Access Account After Deactivation

2FA Enabled Accounts Can Bypass Authentication & Access Account After Deactivation
Sharat Kaikolamthuruthil
Follow
2 min read
·
Nov 27, 2022

103

2

2FA Enabled Accounts Can Bypass Authentication & Access Account After Deactivation

Hello All,

This write-up is about a bug which allowed an account with 2FA enabled to access the organisation after being deactivated.

So after testing the 2FA feature of the application I noticed that the application does not require credentials but only the 2FA code to fetch you the session ID. Which means authentication can be bypassed.

After logging in, the application redirected to a page which is used to trigger 2FA of the account. It could be triggered without any cookie value.

After entering the code, application would return a session ID.

Since this bug does not pose a huge threat I decided to dig deeper into chaining this bug and escalating it into a High vulnerability.

Then I deactivated the account and tried to login but the application returned an error message.

Get Sharat Kaikolamthuruthil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now using the repeater in burp suite I sent a request to trigger 2FA code for the deactivated account. The application did send an SMS code.

Press enter or click to view image in full size
Request to trigger 2FA Code

Again using repeater I submitted the code in the SMS verification request as shown below. The application returned a valid session ID.

Press enter or click to view image in full size
SMS verification request

Using this session ID I was able to access the account thus bypassing the deactivation.

Root Cause:

Upon deactivation, the application only disabled the user’s login credentials. It did not deactivate the trigger SMS option for that account.

Since the application’s authentication was based on only 2FA code, user’s could successfully obtain session ID even after deactivation & access the account.

This was triaged as HIGH severity bug.

Have a good day!! 😃

Disclaimer: For educational purpose only please do not try for illegal activities.
