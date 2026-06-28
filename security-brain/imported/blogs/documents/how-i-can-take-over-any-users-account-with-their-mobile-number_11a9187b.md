---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-06_how-i-can-take-over-any-users-account-with-their-mobile-number.md
original_filename: 2021-09-06_how-i-can-take-over-any-users-account-with-their-mobile-number.md
title: How I can take over any user’s account with their mobile number
category: documents
detected_topics:
- xss
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- xss
- command-injection
- otp
- rate-limit
language: en
raw_sha256: 11a9187b569b485bab6c13d6d86587bf13cd4072b377a85a36c0fcac8b1596a9
text_sha256: f6978edcdff4fc3d2f74143757c728dfd6f77b3116e94fa096ebc6f57ea1d3a7
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I can take over any user’s account with their mobile number

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-06_how-i-can-take-over-any-users-account-with-their-mobile-number.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `11a9187b569b485bab6c13d6d86587bf13cd4072b377a85a36c0fcac8b1596a9`
- Text SHA256: `f6978edcdff4fc3d2f74143757c728dfd6f77b3116e94fa096ebc6f57ea1d3a7`


## Content

---
title: "How I can take over any user’s account with their mobile number"
url: "https://medium.com/@katikitala.sushmitha078/how-i-can-take-over-any-users-account-with-their-mobile-number-6d820a364cad"
authors: ["Sushmitha Katikitala"]
bugs: ["Account takeover", "OTP bypass", "Authentication bypass"]
publication_date: "2021-09-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3342
scraped_via: "browseros"
---

# How I can take over any user’s account with their mobile number

How I can take over any user’s account with their mobile number
Sushmitha Katikitala
Follow
3 min read
·
Sep 6, 2021

471

2

Hi everyone! Hope you all are healthy and safe. This is my first write-up on one of the findings in a private program where I was able to completely take over any user’s account with their mobile number.‌

Before starting, guys please ignore if any grammatical mistakes.‌

Let assume the website to be redacted.com. Like every other bug bounty hunter, I started understanding how the website was working. And started testing for XSS on all the input fields of the website. But I didn't expect that I can get XSS vulnerability so easily in the search field. {payload :"><script>alert(document.domain)</script>}‌

Get Sushmitha Katikitala’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In redacted.com, there is a user registration page to create an account. I entered all the required fields and click on the submit.

User registration page

After clicking on the Submit button, it is redirecting to the page where we need to enter OTP which has been sent to the mobile number.

Here I tried to brute force a 6-digit OTP number using Burp intruder. But it didn’t work. So, I have checked the requests in burp history. In that POST request, one parameter caught my eye i.e. "action=otpreg".

Press enter or click to view image in full size

I thought that maybe the OTP is being generated in response to this request. When I saw the response to this request, it generating OTP in base64 format.

Press enter or click to view image in full size

When I decoded the base64 OTP code, I got the same OTP number that I received on my mobile. Now I entered the decoded base64 OTP number and intercepted the request in burp to check the response. Here it is matching the"userotp" and "genreatedotp" for validation.

Press enter or click to view image in full size

After forwarding the request, the account was successfully got registered.‌

What if the company is following the same process for the login page. So, I entered the registered mobile number and captured the request in the burp, and BOOMMMMMMMM!!!!!!! They are following the same process. Immediately I decoded the base64 code and entered OTP and submitted the request. I was successfully able to enter the account.‌

Using this, I can take over any user’s account using their mobile number.‌

Thanks for reading this !!.

Happy researching….
