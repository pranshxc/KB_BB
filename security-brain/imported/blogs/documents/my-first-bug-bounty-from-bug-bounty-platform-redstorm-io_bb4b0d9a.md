---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-17_my-first-bug-bounty-from-bug-bounty-platform-redstormio.md
original_filename: 2020-09-17_my-first-bug-bounty-from-bug-bounty-platform-redstormio.md
title: My First Bug Bounty From Bug Bounty Platform redstorm.io
category: documents
detected_topics:
- otp
- command-injection
- csrf
tags:
- imported
- documents
- otp
- command-injection
- csrf
language: en
raw_sha256: bb4b0d9adbc2e7d8a6e833a15517c5cde0c148f963ad18abb875031f068dd855
text_sha256: d349f8cdb9ff3e23ea36d434e76e83b884ec7d9f8c2b5b3725180096cb97f7a3
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# My First Bug Bounty From Bug Bounty Platform redstorm.io

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-17_my-first-bug-bounty-from-bug-bounty-platform-redstormio.md
- Source Type: markdown
- Detected Topics: otp, command-injection, csrf
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `bb4b0d9adbc2e7d8a6e833a15517c5cde0c148f963ad18abb875031f068dd855`
- Text SHA256: `d349f8cdb9ff3e23ea36d434e76e83b884ec7d9f8c2b5b3725180096cb97f7a3`


## Content

---
title: "My First Bug Bounty From Bug Bounty Platform redstorm.io"
url: "https://medium.com/@novan.rmd/my-first-bug-bounty-from-bug-bounty-platform-redstorm-io-50958f6adc90"
authors: ["Novan Aziz Ramadhan (@novan_rmd)"]
programs: ["RedStorm"]
bugs: ["CSRF"]
publication_date: "2020-09-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4258
scraped_via: "browseros"
---

# My First Bug Bounty From Bug Bounty Platform redstorm.io

My First Bug Bounty From Bug Bounty Platform redstorm.io
Novan Aziz Ramadhan
Follow
2 min read
·
Sep 17, 2020

76

Hi, how are you? i hope you are doing great, this is my first bug bounty from bug bounty platform on redstorm.io

My bug bounty was bypassing OTP Verification SMS, but before we started i will explain what is redstorm.io and OTP

Bug Bounty Platform Redstorm.io

RedStorm is a concierge-based solution model that is designed to be as flexible with your SDLC, for the sake of providing the awareness in dealing with security threats without the need for you to be bogged down with high security maintenance costs.

What is OTP?

A one-time password (OTP), also known as one-time PIN or dynamic password, is a password that is valid for only one login session or transaction, on a computer system or other digital device.

At that day i was reading around on redstorm.io, and i noticed Indodax Bug Bounty Program, so i tried to find some bugs on there, at the first i’m trying to find a host header injection but i got no luck at all.

Don’t Give Up!

I try to register a new account, and i was asked to enter the phone number when registering the account, so i input a random phone number and finished register account.

Get Novan Aziz Ramadhan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After that i verify my email and i asked to verify my phone number, then crossed my mind to bypass the sms verification, so i fired up my Burpsuite - capture the request send it to repeater and here’s what i got

csrf_token=[TOKEN]&pin=

Then i try to input 6 random number and BOOM! here’s the response from my Burp

csrf_token=[TOKEN]&pin=123456

{“success”:”Terima kasih, verifikasi telah berhasil!”}

Happy xD

I immediately report it to their bug bounty program.

Time Line :

8 September - Initial Report
9 September - New Update
10 September - Valid Bug
17 September - Rewarded

Thanks for reading my story, i hope you enjoy it. Happy hacking !

Please support me :

https://paypal.me/novanazizramadhan
