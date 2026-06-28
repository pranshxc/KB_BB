---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-22_2fa-bypass-using-custom-cookie-parameter.md
original_filename: 2023-05-22_2fa-bypass-using-custom-cookie-parameter.md
title: 2FA Bypass Using Custom Cookie Parameter
category: documents
detected_topics:
- mfa
- command-injection
- automation-abuse
- cloud-security
- mobile-security
tags:
- imported
- documents
- mfa
- command-injection
- automation-abuse
- cloud-security
- mobile-security
language: en
raw_sha256: 94e66296620e376265bdb7e95243a3a4ca0b43ef5d55165afd5b417c296bfb53
text_sha256: ac2815adbc73e9a166f8a0e6f599a6b5e18c744c701f26e2b5e4454243902eab
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# 2FA Bypass Using Custom Cookie Parameter

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-22_2fa-bypass-using-custom-cookie-parameter.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, automation-abuse, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `94e66296620e376265bdb7e95243a3a4ca0b43ef5d55165afd5b417c296bfb53`
- Text SHA256: `ac2815adbc73e9a166f8a0e6f599a6b5e18c744c701f26e2b5e4454243902eab`


## Content

---
title: "2FA Bypass Using Custom Cookie Parameter"
url: "https://medium.com/@sharp488/2fa-bypass-using-custom-cookie-parameter-cb270c8557d2"
authors: ["Sharat Kaikolamthuruthil (@sharp488)"]
bugs: ["2FA / MFA bypass", "Android"]
publication_date: "2023-05-22"
added_date: "2023-05-22"
source: "pentester.land/writeups.json"
original_index: 1130
scraped_via: "browseros"
---

# 2FA Bypass Using Custom Cookie Parameter

Top highlight

2FA Bypass Using Custom Cookie Parameter
Sharat Kaikolamthuruthil
Follow
2 min read
·
May 22, 2023

181

4

2FA Bypass Using Custom Cookie Parameter

Hello All,

This write-up is about a 2FA bypass which was found in a private program on HackerOne. A few months ago, this company had newly implemented 2FA feature in their application.

Summary:

I immediately started testing it since it was a new feature. Surprisingly I was able to bypass the 2FA. The cookie received during the 2FA verification process could access the internal edit profile page of the account. Here an attacker could easily change the email id or phone number to permanently take over the account. I reported this to the program as soon as I found it. The next day it was marked as duplicate as some other researcher had submitted the same issue before me.

Since the program was running a promotion for 2FA related bugs I decided to test further to see if there are any other flaws. As I was exploring the application, I noticed that they had an APK version of it. This was not explicitly mentioned in the program scope, but I decided to take a look at it anyway. I installed the APK and tried logging in with a 2FA enabled account. The application logged in successfully without prompting for the 2FA code. Thus 2 factor authentication was bypassed. I immediately checked the request in burp and found that the domain was in scope. So I reported this to the program ASAP.

Root Cause:

Get Sharat Kaikolamthuruthil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At first I thought that the developers had not implemented 2FA in their APK. So, I decided to compare the requests from Web App & APK (as both domains were different but in scope) to find the root cause. I realized that the APK request had an extra parameter UKAppMode=true; passed in cookie which led to the 2FA bypass.

Press enter or click to view image in full size
Custom Cookie Parameter Value

If this parameter was added to Web App request, we could bypass 2FA there as well.

This was triaged as HIGH severity bug.

Hope you all enjoyed reading this.

Have a good day!! 😃

Disclaimer: For educational purpose only please do not try for malicious or unauthorized actions.
