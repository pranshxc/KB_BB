---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-05_easy-account-takeover-on-dell-subdomain.md
original_filename: 2023-02-05_easy-account-takeover-on-dell-subdomain.md
title: Easy Account Takeover on dell subdomain
category: documents
detected_topics:
- password-reset
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- password-reset
- command-injection
- otp
- rate-limit
language: en
raw_sha256: c2b808e155a66b8b26ba3b50108b68f0b53d51f08efc4fa721a1269c1d366952
text_sha256: 2dfe662002556cdd5cf9dc1edabf8a6858129f8d5c85a28e210c36b54efeb60b
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Easy Account Takeover on dell subdomain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-05_easy-account-takeover-on-dell-subdomain.md
- Source Type: markdown
- Detected Topics: password-reset, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `c2b808e155a66b8b26ba3b50108b68f0b53d51f08efc4fa721a1269c1d366952`
- Text SHA256: `2dfe662002556cdd5cf9dc1edabf8a6858129f8d5c85a28e210c36b54efeb60b`


## Content

---
title: "Easy Account Takeover on dell subdomain"
page_title: "Account Takeover on Dell Inc. السلام عليكم ورحمة الله وبركاته | by Mohamed Fares | Medium"
url: "https://medium.com/@2os5/easy-account-takeover-on-dell-subdomain-6297460741fd"
authors: ["Mohamed Fares (@_2os5)"]
programs: ["Dell"]
bugs: ["Password reset", "Account takeover"]
publication_date: "2023-02-05"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 1575
scraped_via: "browseros"
---

# Easy Account Takeover on dell subdomain

Account Takeover on Dell Inc
Mohamed Fares
Follow
1 min read
·
Feb 6, 2023

265

5

السلام عليكم ورحمة الله وبركاته

My name is Mohamed fares and this is my first write up

this account takeover took 3 hours to find it

I started collecting subdomains and then filtering them

I found a subdomain that has sign-up and login page

I made two accounts and started testing

I tested every function there but nothing was found, and the last thing I was testing is resetting the password I tried everything I know, and I was going to give up

while testing I found that the two emails received the same reset token!!!

how did I do that?? I did not know how I did that!

Get Mohamed Fares’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

then I tried what did I do and I figured out that the request was not protected from rate limits like (capatche) or token

anyway here is the steps

1-hacker account trying to reset his password using forget password function

2- write the email in the reset field and intercept the request

3- hold that request and do not forward it

4- send the request to the repeater and in the repeater change the email to (victim email)

5- now you have two requests (one in intercept on) and (one on repeater)

6- send the two requests in the same time and you will get the same reset password token in the victim email and hacker email

AND YEAH I CHANGED THE VICTIM’S PASSWORD USING THAT RESET PASSWORD

Thanks for reading

My Twitter : _2os5
