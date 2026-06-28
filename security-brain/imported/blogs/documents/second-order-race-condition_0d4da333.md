---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-10_second-order-race-condition.md
original_filename: 2021-06-10_second-order-race-condition.md
title: Second Order Race Condition
category: documents
detected_topics:
- command-injection
- otp
- race-condition
tags:
- imported
- documents
- command-injection
- otp
- race-condition
language: en
raw_sha256: 0d4da333681c940c9fc19e4292fc6abc4c576492a605e409b8aa07c008674f78
text_sha256: d94ea4f9c8148dec52d845e70095972c1fe9123bbe7ea4969d4d946bfdaa8849
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Second Order Race Condition

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-10_second-order-race-condition.md
- Source Type: markdown
- Detected Topics: command-injection, otp, race-condition
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `0d4da333681c940c9fc19e4292fc6abc4c576492a605e409b8aa07c008674f78`
- Text SHA256: `d94ea4f9c8148dec52d845e70095972c1fe9123bbe7ea4969d4d946bfdaa8849`


## Content

---
title: "Second Order Race Condition"
url: "https://0xdekster.medium.com/second-order-race-condition-be8aaf774783"
authors: ["Prasoon Gupta (@0xdekster)"]
bugs: ["Race condition"]
bounty: "1,000"
publication_date: "2021-06-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3588
scraped_via: "browseros"
---

# Second Order Race Condition

Second Order Race Condition
Prasoon Gupta
Follow
2 min read
·
Jun 9, 2021

543

4

Hi everyone , I have found this bug on a public program on h1 some times back.

The website is having a registration process in which you have to fill your phone number to be able to register.

After providing phone number, email, username & details , you have to verify the phone number by giving 6 digit OTP code for successful verification.

After providing 6 digit OTP ,and verifying the captcha service and then hit register and intercepted this request.

So i just intercepted this POST Register request in burp and then started playing with this request’s parameters.

So what i tried is basically using this single “OTP Verified & Captcha verified” request to register multiple accounts with just different usernames.

I send this POST request to turbo intruder and then just manipulated parameters with injection point as -

username- abc123%s , email- abc123%s@gmail[dot]com

Get Prasoon Gupta’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then used the turbo intruder’s default race.py script with injections points customisation according to number of parameters.

Then just Attack this request .

Press enter or click to view image in full size

Then in the status code of the Turbo Intruder, i have got 3 requests as “302”, which basically means i have created 3 different accounts by using “Single OTP verification and single Captcha Verification”.

Timeline

25th Nov 2019 Submitted the report

25th Nov 2019 Triaged , marked it as High

28th Nov 2019 $1,000 Bounty

Press enter or click to view image in full size
