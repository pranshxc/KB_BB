---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-05_otp-leaking-through-cookie-leads-to-account-takeover.md
original_filename: 2022-12-05_otp-leaking-through-cookie-leads-to-account-takeover.md
title: OTP Leaking Through Cookie Leads to Account Takeover
category: documents
detected_topics:
- otp
- oauth
- access-control
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- otp
- oauth
- access-control
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 671bf57711d24ed765766845c5318fd58e9194125ba30a7233c4a3923401beaf
text_sha256: 765e6dd643443f41129fbbd4c776ebf6af72af9a77a9abe1021932a850e3992c
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# OTP Leaking Through Cookie Leads to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-05_otp-leaking-through-cookie-leads-to-account-takeover.md
- Source Type: markdown
- Detected Topics: otp, oauth, access-control, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `671bf57711d24ed765766845c5318fd58e9194125ba30a7233c4a3923401beaf`
- Text SHA256: `765e6dd643443f41129fbbd4c776ebf6af72af9a77a9abe1021932a850e3992c`


## Content

---
title: "OTP Leaking Through Cookie Leads to Account Takeover"
url: "https://ag3n7.medium.com/otp-leaking-through-cookie-leads-to-account-takeover-4fb96f255e2f"
authors: ["ag3n7"]
bugs: ["Information disclosure", "Account takeover"]
publication_date: "2022-12-05"
added_date: "2022-12-05"
source: "pentester.land/writeups.json"
original_index: 1813
scraped_via: "browseros"
---

# OTP Leaking Through Cookie Leads to Account Takeover

1

OTP Leaking Through Cookie Leads to Account Takeover
OTP Bypass
ag3n7
Follow
3 min read
·
Dec 5, 2022

143

2

Press enter or click to view image in full size
leakage

Hello Hackers,

This time I am going to discuss an OTP leaking vulnerability that leads to account takeover in an e-commerce website.

Let’s Start

What is OTP?
A one-time password, also known as a one-time PIN, one-time authorization code or dynamic password, is a password that is valid for only one login session or transaction, on a computer system or other digital device
(source: wikipedia)

While searching for a bug bounty program on google, I got an e-commerce website. I started to check the website’s register and login page, I intercepted the requests and started searching for any sensitive data but I didn’t find anything.

After I registered an account and while trying to login, then I figured out the interesting thing on that website. I should have found the vulnerability in the register page itself.

Let’s Discuss it

Get ag3n7’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After Registration, there were two options to login: with the password or with OTP

Login Page

I used Login with OTP, entered the registered number, and clicked LOGIN WITH OTP

Validate OTP

Then I checked the cookies, there is a new cookie appeared ‘otpcookies’ with the OTP value.

otp

I entered the OTP and validated it.

Successfully LoggedIn

We successfully loggedin to the account.

We can takeover any account by knowing their mobile number only. We can use the same method to register the account, and the most interesting part was there was no validation of mobile number and email id, which means we can register even with non-existing numbers and emails. These all happened on an e-commerce website :(

I reported the issue to the admin and they responded within hours, and accepted the bug. After that no response from their side and no updates till now. Let’s wait.

Thank You For Reading ….

Follow me on :

Twitter: https://twitter.com/ag3n7apk

Linkedin: https://www.linkedin.com/in/abhijith-pk-ag3n7/
