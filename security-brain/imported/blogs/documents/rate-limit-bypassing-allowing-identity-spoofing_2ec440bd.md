---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-29_rate-limit-bypassing-allowing-identity-spoofing.md
original_filename: 2020-10-29_rate-limit-bypassing-allowing-identity-spoofing.md
title: Rate Limit Bypassing Allowing Identity Spoofing
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
raw_sha256: 2ec440bd4824a533acfd304c9a7b7efa08f8414ae066464c87514bb9a393bba8
text_sha256: 46f8f0310b4acc9da7efc0aa0bd39a668e08403ab68b082f90a9ed617e23dea3
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Rate Limit Bypassing Allowing Identity Spoofing

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-29_rate-limit-bypassing-allowing-identity-spoofing.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, otp
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `2ec440bd4824a533acfd304c9a7b7efa08f8414ae066464c87514bb9a393bba8`
- Text SHA256: `46f8f0310b4acc9da7efc0aa0bd39a668e08403ab68b082f90a9ed617e23dea3`


## Content

---
title: "Rate Limit Bypassing Allowing Identity Spoofing"
url: "https://0xt4144t.medium.com/rate-limit-bypassing-allowing-identity-spoofing-789b2fe2efa8"
authors: ["Mohamed Talaat (@T4144t)"]
bugs: ["Rate limiting bypass", "OTP bypass"]
publication_date: "2020-10-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4171
scraped_via: "browseros"
---

# Rate Limit Bypassing Allowing Identity Spoofing

Rate Limit Bypassing Allowing Identity Spoofing
Mohamed Talaat Saada (@t4144t)
Follow
2 min read
·
Oct 29, 2020

99

Introduction

While hunting on a program on H1 I needed to register an account to start exploring authenticated requests of the application, tried to register with my phone number but found that it only accepts phone numbers from specific country, so I wasn’t able to use my phone number and had to start attacking from this point only to get an account.

Control

To register an account the application was sending SMS to registered phone number then forcing 3 controls on verification function:

Press enter or click to view image in full size

1- Rate limit control that only allows 60 requests per minute.
2- Once exceeding the rate limit IP and phone will be blocked for some time.
3- A number of 6 digits will make brute force more harder.

Get Mohamed Talaat Saada (@t4144t)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So we will try to bypass rate limit enforced to increase allowed trials number and get the OTP value sent to the user’s phone.

Bypassing

Rate limiting is an API control that’s set by API developers in order to mitigate attacks such as: Brute Force, Resource Exhaustion Attack, DDOS (Distributed Denial of Service), .. .
It’s often used to protect authentication function such as: Login, Reset Password, Account Verification, 2 Factor Authentication or other function that send message or emails.

Press enter or click to view image in full size
Rate Limit Applied for only 60 requests per minute.

To bypass tried different techniques:

1- Changing some of request headers’ values to be different values like: user-agent, getting new cookie, changing source IP address but with no luck.

2- Secondly, tried adding new header with the following value:

X-Forwarded-For: 127.0.0.1

and once done, the response showed increase in the number of allowed trials from 60 to 6000 per minute! this mis-configuration maybe for testing purposes from local host!

Press enter or click to view image in full size
Response After Bypassing
Result

That allowed brute force OTP value and spoofing identity of any user by using his phone number if he’s still not registered.
