---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-30_bypassing-email-verification-of-high-profile-tech-company-.md
original_filename: 2023-07-30_bypassing-email-verification-of-high-profile-tech-company-.md
title: Bypassing email verification of high-profile tech company ($$$)
category: documents
detected_topics:
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- command-injection
- password-reset
- otp
language: en
raw_sha256: bdaf31ee77e3e6d615f4c99500abe7ad39a0b6d6e40abfafc2aa4d3573626043
text_sha256: 7d4278464d017aeeea370990df67e3b1f457239b304abef28a7792ec2bf94989
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing email verification of high-profile tech company ($$$)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-30_bypassing-email-verification-of-high-profile-tech-company-.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `bdaf31ee77e3e6d615f4c99500abe7ad39a0b6d6e40abfafc2aa4d3573626043`
- Text SHA256: `7d4278464d017aeeea370990df67e3b1f457239b304abef28a7792ec2bf94989`


## Content

---
title: "Bypassing email verification of high-profile tech company ($$$)"
url: "https://infosecwriteups.com/bypassing-email-verification-of-high-profile-tech-company-e592cc4a89ce"
authors: ["can1337 (@canmustdie)"]
bugs: ["Email verification bypass"]
publication_date: "2023-07-30"
added_date: "2023-07-31"
source: "pentester.land/writeups.json"
original_index: 895
scraped_via: "browseros"
---

# Bypassing email verification of high-profile tech company ($$$)

Bypassing email verification of high-profile tech company ($$$)
can1337
Follow
3 min read
·
Jul 29, 2023

930

6

Hi guys, after almost a year, I thought I should create a new write-up. Today, I’m gonna show you the email verification bypass vulnerability that I found at high-profile tech & software company. So I’ll call that company as “redacted” and let’s get started!

Basically, when you sign up with the redacted company, you have 48 hours to verify your email.

Press enter or click to view image in full size
(I want you to know that I have censored some tabs with company logo and product name for all images.)

As you can see in this picture, it is a demo intended for limited access by new users. During this time, you can use the application, but after 48 hours have passed, you cannot log in without verifying your email.

Press enter or click to view image in full size

And when you want to log in after 48 hours, you will see the tab below and you will need to verify your email. Yes, I waited 2 days for this.

When we click the “click to resend” button to continue using the account, we receive an email for email verification. Lemme show you that mail.

Press enter or click to view image in full size

At this point, I noticed that the token value sent in the mail for verification purposes is the same as the token value in the URL field in the second image.

Get can1337’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Take a look at this match, we can also view this token from the Burp Suite interface.

Press enter or click to view image in full size

You can easily see the match in all three images (first and second images for the verification area). This means that even if a user registered with an email that doesn’t have, he/she can use that email unlimitedly.

As a result, users can copy this token value and convert it to the URL format sent for email verification.

Press enter or click to view image in full size

Demo Steps:
1- Create a new account with admin@redacted.com mail at redacted.com
2- After 48 hours, you need to verify your account. Login to the site and you will see that email verification tab.
3- Copy the token value in URL section of verfication tab and paste here: www.redacted.com/Login/UserEmailConfirm?Token=*HERE*

The team accepted and fixed this report as email verification bypass and pre-auth account takeover and rewarded me $$$ bounty.

That’s all for now. Thanks for reading this far and I hope you liked it!

https://twitter.com/canmustdie
https://0xcan1337.github.io/
