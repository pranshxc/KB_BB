---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-27_improper-phone-number-validation-to-account-takeover.md
original_filename: 2021-09-27_improper-phone-number-validation-to-account-takeover.md
title: Improper phone number validation to account takeover
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- business-logic
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- business-logic
language: en
raw_sha256: 96c0219827964d7239014e4832e742dce29501a8c50f2f3a3ff983d303f659d7
text_sha256: 0c7fca00140cdbabfc2da24836f86f68c5949ec07188973ca6c43cb6a881d9dd
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Improper phone number validation to account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-27_improper-phone-number-validation-to-account-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `96c0219827964d7239014e4832e742dce29501a8c50f2f3a3ff983d303f659d7`
- Text SHA256: `0c7fca00140cdbabfc2da24836f86f68c5949ec07188973ca6c43cb6a881d9dd`


## Content

---
title: "Improper phone number validation to account takeover"
url: "https://sheshasai.medium.com/improper-phone-number-validation-to-account-takeover-f8b78b08ed05"
authors: ["shesha sai_c (@Cyb3r_4ss4s1n)"]
bugs: ["Logic flaw", "OTP bypass", "Account takeover"]
publication_date: "2021-09-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3283
scraped_via: "browseros"
---

# Improper phone number validation to account takeover

Improper phone number validation to account takeover
shesha sai_c
Follow
3 min read
·
Sep 27, 2021

196

Hi Everyone!

Hope you are doing well. I am back with another bug.

Whoami: I am Shesha Sai C, Im a bug bounty hunter and security researcher

Let us consider the site as redacted.com as the program does not support disclosures.

I know lot of you guys think this as such a drag but this blog is not about the target, it is about knowledge sharing.

Lets Dive in!

The application does not have much of scope to hunt on all it contains a signup and login page with phone number that shares OTP, No PII disclosure all technologies are up-to-date. Damn!!!! i know the feeling and i was like

Now, time where the story begins the signup page contain that the application allows only users from Russia to signup or enroll for an account, but we don’t have any Russian numbers.

Trail 1: trying to bypass this using my own number in the place of Russian ph number — no luck!, it accepts only numbers in Russian format

Trail 2: Tried with intercepting the Russian number field in burpsuite and without sending this to repeater changed the country code to +91 and my ph and send the request — guess what! it worked, i received a call for OTP validation

I have given the OTP and clicked on Verify it blocked me

Get shesha sai_c’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Trail 3: Tried with intercepting both the OTP generation request and OTP verification request in burpsuite and changing the number and country code- It Worked Amigos!!

Steps to Reproduce:

Visit the signup page: https://redacted.com/signup
Give any Russian phone number you can get it from receive-sms-online
Intercept the request and change it to your number and you will receive a call with OTP
Input this OTP and intercept on -> click on verify and again change the country code and number
You’re logged in as the Russian number user and same works with Login.

Tip: Once a great man said when you’re stuck take a cup of boost and try again- PS: it is me

Timeline: This bug was submitted 3 months back and was remediated.

Hope you learned something new and let’s catch up in next story.

If you have any queries please reach out to me on LinkedIn or Twitter i will be happy to help.
