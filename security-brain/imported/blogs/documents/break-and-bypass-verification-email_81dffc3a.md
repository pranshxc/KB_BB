---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-07_break-and-bypass-verification-email.md
original_filename: 2019-08-07_break-and-bypass-verification-email.md
title: break and bypass verification email
category: documents
detected_topics:
- command-injection
- password-reset
- mfa
- otp
- rate-limit
tags:
- imported
- documents
- command-injection
- password-reset
- mfa
- otp
- rate-limit
language: en
raw_sha256: 81dffc3ac907185b16962b6a4403069741c4b670a462946d729e7147d59eead5
text_sha256: 2eaa4bd1536f48936f892fe79bd22ab5a6e12deaf4f4b21f157e0861a0d77672
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# break and bypass verification email

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-07_break-and-bypass-verification-email.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, mfa, otp, rate-limit
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `81dffc3ac907185b16962b6a4403069741c4b670a462946d729e7147d59eead5`
- Text SHA256: `2eaa4bd1536f48936f892fe79bd22ab5a6e12deaf4f4b21f157e0861a0d77672`


## Content

---
title: "break and bypass verification email"
url: "https://medium.com/@protostar0/break-and-bypass-verification-email-ac3359041272"
authors: ["Abdelhak Kharroubi"]
programs: ["Bukalapak"]
bugs: ["Open redirect", "Email verification bypass", "Weak crypto"]
publication_date: "2019-08-07"
added_date: "2022-10-12"
source: "pentester.land/writeups.json"
original_index: 5094
scraped_via: "browseros"
---

# break and bypass verification email

break and bypass verification email
Abdelhak Kharroubi
Follow
3 min read
·
Aug 7, 2019

34

1

with this issue ,i can register and verify my account with any email (not owned :D)

Severity : high

Description:

Press enter or click to view image in full size

when you register in bukalapak.com with email (example ha99999kou@gmail.com) you will get message in your email to verify account like this

when you click in button to verify ,you will go to this link

https://glimpse.bukalapak.com/redirect?link=https%3A%2F%2Fwww.bukalapak.com%2Fconfirmation%2FaGE5OTk5OWtvdUBnbWFpbC5jb206MjY1NTE%3D&llstttu=2fb35103376a858cf5f1ca33559ae9effae3a37a5f5367c8d2cac53b76e1db86&subject=Segera+Verifikasi+Email+Kamu&tag=confirmation&template_id=0&type=ClickEmail&user_email=ha99999kou%40gmail.com

first bug is this link vulnerable with open redirect :D

poc :

go to this link

https://glimpse.bukalapak.com/redirect?link=https%3A%2F%2Fwww.bing.com

will redirect to bing.com

the second bug is that

the first link will redirect you to confirmation page with token

https://www.bukalapak.com/confirmation/aGE5OTk5OWtvdUBnbWFpbC5jb206MjY1NTE=

this token “aGE5OTk5OWtvdUBnbWFpbC5jb206MjY1NTE=” is base64 encoded “ha99999kou@gmail.com:26551”

the issue is the the valid token can be generated it easily (the token is too weak)

this token can generate ( (email:random num with 5 digit) encoded with base64 )

you can use bruteforce crack 5 digit break in 15 min with low bandwidth (see video poc)

without go to email link :D

Get Abdelhak Kharroubi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

ps : i created many account ,always the random number is 5 digit

lets break this function (verification email):

first create wrong token with ha99999kou@gmail.com:12345 and encoded with base64 will be

“aGE5OTk5OWtvdUBnbWFpbC5jb206MTIzNDU=”

lets open this link in browser

https://www.bukalapak.com/confirmation/aGE5OTk5OWtvdUBnbWFpbC5jb206MTIzNDU=

Press enter or click to view image in full size

you will get message says token invalid

they send the token and other access_token in ajax request to https://api.bukalapak.com and get error message in response

Press enter or click to view image in full size

let’s compare valid token with invalid token in burp repeater

1- valid token with 200 status code

Press enter or click to view image in full size

| 2- invalid token with 400 status code

Press enter or click to view image in full size

now intercept this ajax request and do brute force for the 5 digit in burp intruder (with rules {prefix email and bse64 encode })to verify the new account ha999999kou@gmail.com (with rules see video)

Press enter or click to view image in full size

POc with step to reproduce in video “poc breack verification email.mp4”

impact

you can create account with any email not registered yet and verify it without owned the email
