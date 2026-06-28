---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-13_account-takeover-via-otp-bruteforce-apigee-api.md
original_filename: 2020-06-13_account-takeover-via-otp-bruteforce-apigee-api.md
title: Account Takeover via OTP Bruteforce (Apigee API)
category: documents
detected_topics:
- rate-limit
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- rate-limit
- command-injection
- password-reset
- otp
language: en
raw_sha256: 70d8d3383147f9b99b9a558d64f11886d99a839320d525a23f7a52ac1949cd68
text_sha256: 93adb918115f04dd2fb0bb548195c900b31265a67c810ef4f3680bb9b19acc2c
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover via OTP Bruteforce (Apigee API)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-13_account-takeover-via-otp-bruteforce-apigee-api.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `70d8d3383147f9b99b9a558d64f11886d99a839320d525a23f7a52ac1949cd68`
- Text SHA256: `93adb918115f04dd2fb0bb548195c900b31265a67c810ef4f3680bb9b19acc2c`


## Content

---
title: "Account Takeover via OTP Bruteforce (Apigee API)"
url: "https://medium.com/@vishnu0002/account-takeover-via-otp-bruteforce-apigee-api-9b5481c642df"
authors: ["Vishnuraj"]
bugs: ["OTP bypass", "Bruteforce", "Lack of rate limiting"]
publication_date: "2020-06-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4504
scraped_via: "browseros"
---

# Account Takeover via OTP Bruteforce (Apigee API)

Press enter or click to view image in full size
Account Takeover via OTP Bruteforce (Apigee API)
vishnuraj
Follow
2 min read
·
Jun 13, 2020

89

1

Hi All

This is a short post on one of my findings in a Bugcrowd Private program, which could result in account takeover of any user by an attacker.

Vulnerability Type :

A2:2017 -Broken Authentication

Product Area:

E-commerce

Attack Vector:

Password Reset

Impact:

Unauthorized access to any User account

Proof of Concept:

The password reset functionality in this application was based on OTP validation. When we want to reset the password of an account, we just need to click on the reset button and an OTP will be sent to the user account email. The flaw here was that rate limiting was not set in place and thus giving an attacker endless opportunities to brute force a 6-digit OTP.

Get vishnuraj’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Here within some time, I was able to reset the password of an account by intercepting the request for OTP validation and bruteforcing the 6 digit number. Using this, it is possible to change and reset the password of any account, by changing the user data and brute-forcing the reset OTP.

Vulnerable request
Press enter or click to view image in full size

Response

Press enter or click to view image in full size

Brute forcing the OTP successfully allowed me to set new password for any E commerce user.

Disclosure Timeline:

11 Jul 2019 : Report sent to Bugcrowd Program.

4 Feb 2020 : Verified the fix

Related Reports : https://thehackernews.com/2016/03/hack-facebook-account.html
