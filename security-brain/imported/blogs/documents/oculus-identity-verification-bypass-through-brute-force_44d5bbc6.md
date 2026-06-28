---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-09_oculus-identity-verification-bypass-through-brute-force.md
original_filename: 2019-09-09_oculus-identity-verification-bypass-through-brute-force.md
title: Oculus identity verification bypass through brute-force
category: documents
detected_topics:
- rate-limit
- otp
- command-injection
tags:
- imported
- documents
- rate-limit
- otp
- command-injection
language: en
raw_sha256: 44d5bbc6d2d70ccfcd522a0b5495bf9ae3a30f335e1724690ec2d0c2224412f9
text_sha256: 3b8fba169c87604154ad1753a4c765a8f2fc71737bde57c0fc59eb726a91cd79
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Oculus identity verification bypass through brute-force

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-09_oculus-identity-verification-bypass-through-brute-force.md
- Source Type: markdown
- Detected Topics: rate-limit, otp, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `44d5bbc6d2d70ccfcd522a0b5495bf9ae3a30f335e1724690ec2d0c2224412f9`
- Text SHA256: `3b8fba169c87604154ad1753a4c765a8f2fc71737bde57c0fc59eb726a91cd79`


## Content

---
title: "Oculus identity verification bypass through brute-force"
url: "https://medium.com/@karthiksoft007/oculus-identity-verification-bypass-through-brute-force-dbd0c0d3c37e"
authors: ["karthik kumar reddy (@karthiksunny007)"]
programs: ["Meta / Facebook"]
bugs: ["OTP bypass", "Lack of rate limiting"]
bounty: "750"
publication_date: "2019-09-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5042
scraped_via: "browseros"
---

# Oculus identity verification bypass through brute-force

Oculus identity verification bypass through brute-force
Karthik Kumar Reddy
Follow
2 min read
·
Sep 9, 2019

21

Title

brute froce attack near verify your identity and bypass identity verification

Oculus is avery secure web application which doesnt have any vulnerability but i found some that which has lack of rate limit near identity verification

The identity has been used in oculus near username parameter what that means whenever the user wants to change the username of the user account then user needs to be done this identity verification. How this identity verification works in oculus. Whenever the user wants to change the username the OTP will be sended to the registered mail of the user. Now the OTP is in 6digit number

Steps to reproduce :

Get Karthik Kumar Reddy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1)login to oculus
2)goto profile and change username
3)Oculus sends the 6-digit verification code to user through gmail
4)and for testing i have entered wrong code
5)actually the code is 483967 i have entered 486960
6)And captured that request in burpsuit now added 486960
7)And given payloads from 482000=>483970 total 1,971 payloads and started attack
8)At 483967 the length of the code is different all invalid payloads code=>1152,valid=>840
9)Now by seeing length i have confirmed it is the correct payload.that is same payload i got in mail for identity verification

Poc ::https://drive.google.com/file/d/1MPZSY_yB_dayKvXCur2zxDV_Y5tc01f3/view?usp=sharing

Reported on :28/may/2019

Triged on : 12/jun/2019

Rewarded on :9/july/2019

NOTE : i have awarded from facebook three times. I’ll post that remaining two reports ASAP
