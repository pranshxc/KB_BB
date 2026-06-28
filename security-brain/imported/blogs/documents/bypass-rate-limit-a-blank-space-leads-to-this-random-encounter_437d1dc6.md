---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-14_bypass-rate-limit-a-blank-space-leads-to-this-random-encounter.md
original_filename: 2022-04-14_bypass-rate-limit-a-blank-space-leads-to-this-random-encounter.md
title: Bypass Rate Limit — A blank space leads to this random encounter!
category: documents
detected_topics:
- rate-limit
- sso
- command-injection
- password-reset
- otp
- mobile-security
tags:
- imported
- documents
- rate-limit
- sso
- command-injection
- password-reset
- otp
- mobile-security
language: en
raw_sha256: 437d1dc602936d33bee01ace34f0414e200ae8951da8cf657fa84206c138eb1d
text_sha256: a5bb7b5102171ff1cadac00327df21a28f36cff0a89009794f9326b02aeaccec
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass Rate Limit — A blank space leads to this random encounter!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-14_bypass-rate-limit-a-blank-space-leads-to-this-random-encounter.md
- Source Type: markdown
- Detected Topics: rate-limit, sso, command-injection, password-reset, otp, mobile-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `437d1dc602936d33bee01ace34f0414e200ae8951da8cf657fa84206c138eb1d`
- Text SHA256: `a5bb7b5102171ff1cadac00327df21a28f36cff0a89009794f9326b02aeaccec`


## Content

---
title: "Bypass Rate Limit — A blank space leads to this random encounter!"
url: "https://infosecwriteups.com/bypass-rate-limit-a-blank-space-leads-to-this-random-encounter-e18e72fbf228"
authors: ["Roxst4r (@mveswar98)"]
bugs: ["Password reset", "Rate limiting bypass"]
publication_date: "2022-04-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2714
scraped_via: "browseros"
---

# Bypass Rate Limit — A blank space leads to this random encounter!

Bypass Rate Limit — A blank space leads to this random encounter!
Roxst4r
Follow
3 min read
·
Apr 14, 2022

106

1

Hello All, Hope you are having a great time!

Let me get straight into the vulnerability that I’ve found. There is a website named “example.com”, I cannot disclose the name of the site yet. As I was testing through the login functionalities, I tried resetting the password. The functionality was like, when I request for password reset the server sends OTP to my email and mobile number.

Lucky me have added my mobile number there or I would not have found this issue(-you will understand this as we go along-). So Sometimes LUCK plays a major role in Bug Bounty ~

At first, I just sent the password reset request to Intruder and tried with null payloads, adding arbitrary values etc.., — but failed as it has rate limiting enabled after 20 requests. So I tried by adding X-Forwarded-Host:127.0.0.1 , X-Forwarded-Client, X-Client-IP and all other header stuffs which didn’t work either. So I tried with IP Rotate(a Burp Extension- which allows you to easily spin up API Gateways across multiple regions) which failed as well, as it was not IP based. But something (strong gut feel ) made me work on it again and again. So I tried with adding %00 ( null byte at the end of email )and other encoded chars which didn’t work too.

The Lucky part ~

That’s when I remembered reading a blog that adding a space at the end of the email may help to bypass rate limiting, which failed initially. To my luck I created one account (without mobile number) and, as I occasionally use this website for booking activities I already had my personal account(one with phone number verified) .

Get Roxst4r’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The Request and Response without space-

Press enter or click to view image in full size

I was testing the whole time with the test account and I randomly(Lucky me) chose my personal account and added a space at the end of my email and saw that the OTP are not sent to my email (as there is space at the end), but as the mobile number is associated with the email, the OTP’s were sent to my mobile. ~ Bypassed ~

The Request and Response after adding space-

Press enter or click to view image in full size

With the help of this bug, I was able to Bypass rate limiting and send huge requests to the victim’s mobile number, and I know this might not be a big vulnerability, but I hope this kind of little things might help you in different scenarios as you go along the Bug Hunting Journey.

I do welcome suggestions and corrections as I may not be all right, as I am still learning things.

Thank y’all ~
