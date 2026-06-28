---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-17_otp-verification-bypass.md
original_filename: 2020-04-17_otp-verification-bypass.md
title: OTP Verification Bypass
category: documents
detected_topics:
- command-injection
- otp
tags:
- imported
- documents
- command-injection
- otp
language: en
raw_sha256: a3e97e0b3ba9b7dd7cc803f894aee736f2f8db2e67871706a67767d0984afe65
text_sha256: 537c9c5861ac2c0c584533fec17ec687a7b8e5c3f7a4f3ca24b236be1260547d
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# OTP Verification Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-17_otp-verification-bypass.md
- Source Type: markdown
- Detected Topics: command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `a3e97e0b3ba9b7dd7cc803f894aee736f2f8db2e67871706a67767d0984afe65`
- Text SHA256: `537c9c5861ac2c0c584533fec17ec687a7b8e5c3f7a4f3ca24b236be1260547d`


## Content

---
title: "OTP Verification Bypass"
url: "https://medium.com/@rat010/otp-verification-bypass-ee17d68f8425"
authors: ["Kanhaiya Kumar Singh"]
bugs: ["OTP bypass"]
publication_date: "2020-04-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4650
scraped_via: "browseros"
---

# OTP Verification Bypass

OTP Verification Bypass
Kanhaiya Kumar Singh
Follow
2 min read
·
Apr 17, 2020

46

2

Hello guys, I am Kanhaiya Kumar Singh and this is my first write-up about my finding on OTP Bypass.

Description Of Vulnerability :

First of all let’s assume Website is example.com and this is the Simplest Bug (Vulnerability) that i found. When i created an account in example.com i received one OTP in my email id for verifying email. When i entered the correct OTP and checking the Response to this Request. Response code is very simple HTTP/1.1 200 Created and {} then i think let’s bypass OTP Verification.

Steps To Reproduce :

Create an account using abc123@gmail.com.
One OTP Sent into abc123@gmail.com email id.
Paste that correct OTP and Capture the Request into Burp. Now right click on the Request and click on Do Intercept >Response To This Request .
Press enter or click to view image in full size

4. This is the response code.

5. Now again create one account victim123@gmail.com.

Get Kanhaiya Kumar Singh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

6. Again one OTP sent into victim123@gmail.com email id.

7. But i don’t have any access to Victim email account. Let’s Bypass OTP Verification.

8. Enter any wrong OTP and capture the request into Burp. Now right click on the Request and click on Do Intercept >Response To This Request.

Press enter or click to view image in full size

9. See the response there is an error message HTTP/1.1 400 Bad Request and {“error”: “user_not_verified”}

10. Now replace that error message with this HTTP/1.1 200 Created and {}

11. Boom Account Verified Successfully.

Timeline:
Bug Reported: 5 February 2020
Bug Triaged: 6 February 2020
Bounty Rewarded: € xxx

I hope you enjoyed this reading.

Thank You!
~Kanhaiya Kumar Singh (https://twitter.com/rat760)

Follow me on Twitter
