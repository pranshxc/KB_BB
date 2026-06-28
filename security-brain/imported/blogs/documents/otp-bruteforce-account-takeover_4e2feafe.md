---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-29_otp-bruteforce-account-takeover.md
original_filename: 2020-03-29_otp-bruteforce-account-takeover.md
title: OTP Bruteforce- Account Takeover
category: documents
detected_topics:
- rate-limit
- command-injection
- otp
tags:
- imported
- documents
- rate-limit
- command-injection
- otp
language: en
raw_sha256: 4e2feafeaceebd5d8d1c89dc174f34ffeb628248258124c6552cb05eb14b5f1c
text_sha256: db05af4929075186551abdec428c0cad2439feb089b748731809d07539f619bb
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# OTP Bruteforce- Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-29_otp-bruteforce-account-takeover.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `4e2feafeaceebd5d8d1c89dc174f34ffeb628248258124c6552cb05eb14b5f1c`
- Text SHA256: `db05af4929075186551abdec428c0cad2439feb089b748731809d07539f619bb`


## Content

---
title: "OTP Bruteforce- Account Takeover"
url: "https://medium.com/@ranjitsinghnit/otp-bruteforce-account-takeover-faaac3d712a8"
authors: ["Ranjit Kumar"]
bugs: ["OTP bruteforce", "Account takeover"]
publication_date: "2020-03-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4683
scraped_via: "browseros"
---

# OTP Bruteforce- Account Takeover

OTP Bruteforce- Account Takeover
Th3Y0ungM0nk
Follow
3 min read
·
Mar 30, 2020

92

1

This is my first 4 digit bounty in $$$$ and was really excited when I discovered a simple yet critical vulnerability in one of the private programme.

This attack is very similar to https://thehackernews.com/2016/03/hack-facebook-account.html only difference is that the attack was on the login functionality itself .

Login mechanism: Enter the mobile no , user receives an otp . Enter the otp and login into the webapplication.

Flaw was that rate limiting was not on place and thus gave an attacker endless opportunities to brute force a 6-digit code and login into any account.

Response for Valid OTP

Press enter or click to view image in full size

Response for Invalid Otp

Press enter or click to view image in full size

So , now we had two different responses for a valid and an invalid otp that were processed during the authentication process.

Get Th3Y0ungM0nk’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I curiously validated in intruder if rate limiting was present or not and if it can be bypassed — just following the bug hunting strategy (doubt on everything that is in front of you).

And NO RATE LIMITING even after 50 wrong attempts :)

I could have exploited it in intruder , but because most of the programme handlers are not expert in information security and may/may not have idea of BurpSuite/Intruder — I decided to write up an exploit (which I always love to present things to give the enduser a fair idea on the other side that how in real world it can be exploited)

Exploit Code(This was something similar-with few omitted part)

Press enter or click to view image in full size

Fire up the exploit and bruteforce OTP.

Press enter or click to view image in full size

Note: Images are just for demo purpose and very much identical to the actual one , I can’t share the original poc exploit or screenshots.

And voilla, after certain hundred iterations we were able to login into the app. I have hidden the cookie part from exploit code which actually was finally replaced in browser using cookie editor EditThisCookie — https://github.com/ETCExtensions/Edit-This-Cookie and account takeover was completed.

I quickly created the POC , sent it and was triaged within hours and fixed in a day!

This was my highest bounty and has boosted my morale to explore this beautiful world of bug hunting.
