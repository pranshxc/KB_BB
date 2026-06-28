---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-30_bypassing-otp-via-reset-password.md
original_filename: 2020-07-30_bypassing-otp-via-reset-password.md
title: Bypassing OTP via reset password
category: documents
detected_topics:
- otp
- rate-limit
- command-injection
- api-security
tags:
- imported
- documents
- otp
- rate-limit
- command-injection
- api-security
language: en
raw_sha256: efdd58d764b667ba8ba1373165f04ddedbaf7c5770eb2093335700e6fddcae0d
text_sha256: 552ef3ca677eae0307abfe0ad33e72725ba124481bc3a4f491ec1b6c37eb3b35
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing OTP via reset password

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-30_bypassing-otp-via-reset-password.md
- Source Type: markdown
- Detected Topics: otp, rate-limit, command-injection, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `efdd58d764b667ba8ba1373165f04ddedbaf7c5770eb2093335700e6fddcae0d`
- Text SHA256: `552ef3ca677eae0307abfe0ad33e72725ba124481bc3a4f491ec1b6c37eb3b35`


## Content

---
title: "Bypassing OTP via reset password"
page_title: "Account Takeover Through Reset Abuse: Why OTP Alone Isn’t Enough | by AHZ | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/bypassing-otp-via-reset-password-f004a29020c"
authors: ["Ahmed Cj (@0x0Cj)"]
bugs: ["OTP bypass"]
publication_date: "2020-07-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4365
scraped_via: "browseros"
---

# Bypassing OTP via reset password

Account Takeover Through Reset Abuse: Why OTP Alone Isn’t Enough
AHZ
Follow
3 min read
·
Jul 31, 2020

188

1

In this write-up, I will explain how I was able to bypass the one-time password by resetting the password via email address.

Press enter or click to view image in full size

I discovered this vulnerability in a private program, I will name it: target.com, Before we keep going on explaining we should consider that this vulnerability occurred due to wrong application of the reset password method via API which led to the leakage of the user live token in the response.

W
hile I was doing recon in this target, I realized that all functions without exception are directly related to one API, This target was an interface for it’s API, So it made sense to start with functions scanning for bugs, And while I was checking the account settings, I found OTP by phone number option, So I turned it ON and logged out.

I directly logged in and decided to check for rate limit bypassing and other bugs related to OTP, But unfortunately, there was a rate limit implementation in the API itself and I wasn’t able to bypass it.

Press enter or click to view image in full size
Rate limit mechanism response

I checked also if I can bypass OTP by resetting my password via email address, But the app will ask me to sign in again with my new password and insert the 6 digits OTP code that was sent via SMS, So I wasn’t able to bypass it this way.

So it was time to check for every request and it’s response, I turned my intercept ON and started by checking the reset password method responses, Nothing was interesting, I logged into my testing account email and checked the reset password link, The token in the link was complex and I couldn’t brute-force it.

Get AHZ’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I requested the link and inserted my new password, I pressed change my password button and checked the response, I could confirm that the reset password API method sets a new live token for my account and leaked the token in the response, By this live token, I was able to use all the methods in the account via API without the need to sign into the app interface.

Press enter or click to view image in full size
Token leakage in response

But I chose to find a way to stop the OTP without signing in, And after checking the account settings I was able to find the API request that stops the OTP via phone number, So I entered the request in the repeater, And I was able to stop the OTP via API live token and logged into the app interface.

Press enter or click to view image in full size
Disable OTP API request
Summary

I was able to bypass the OTP by resetting password via email address, We should consider that I was able to use every method in the account via the leaked API live token in the reset password method response, But I preferred to find away to stop the OTP, And I stopped it via disabling OTP API request, And therefore I was able to open my account without the need to insert the OTP code.

Timeline

Report (Jul 7th).
First response (Jul 7th).

Don’t forget to follow me on Twitter so you don’t miss my new writeups and articles. Thank you for reading my first writeup, Appreciated.
