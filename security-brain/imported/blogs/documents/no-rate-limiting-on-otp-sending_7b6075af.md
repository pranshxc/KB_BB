---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-02_no-rate-limiting-on-otp-sending.md
original_filename: 2022-02-02_no-rate-limiting-on-otp-sending.md
title: No Rate Limiting on OTP sending
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
raw_sha256: 7b6075af32301c7292b1743c5ba7030649168d267ec993261180377d35ab480e
text_sha256: 1ef194751d9269c58b0d7c4d75bd7d0cc7321015927a631764b74db51e9c146a
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# No Rate Limiting on OTP sending

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-02_no-rate-limiting-on-otp-sending.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, otp
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `7b6075af32301c7292b1743c5ba7030649168d267ec993261180377d35ab480e`
- Text SHA256: `1ef194751d9269c58b0d7c4d75bd7d0cc7321015927a631764b74db51e9c146a`


## Content

---
title: "No Rate Limiting on OTP sending"
url: "https://medium.com/@noob_master/no-rate-limiting-on-otp-sending-39a3a9fc93f6"
authors: ["nOOb_mAsTeR"]
bugs: ["Bruteforce", "Lack of rate limiting"]
publication_date: "2022-02-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2950
scraped_via: "browseros"
---

# No Rate Limiting on OTP sending

No Rate Limiting on OTP sending
nOOb_mAsTeR
Follow
3 min read
·
Feb 2, 2022

15

1

Firstly I would like to say that this is my first ever writeup for the InfoSec community and I may not be so good at presenting the explanation, please bear on that. So, its been a year or maybe a bit more than that when I started into cybersecurity. It was this concept of BugBounty which drove me to start reading all about web, request-response, and related information. For the last 6 months I had stopped learning bugbounty stuffs maybe because I had lost the hope of getting any bounties. Last year in 2020 at the month of November I thought to start of with BugBounties again with the target that I needed to get better at Web Pentesting which I was very weak and which still I am though.

Now coming to the bug.

What is Rate Limiting?

A rate limiting algorithm is used to check if the user session (or IP-address) has to be limited based on the information in the session cache. In layman’s language if a client sends too many requests within a given timeframe, the server takes up rate limiting in different ways to prevent the rate of request.

Get nOOb_mAsTeR’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now the website which I tested for was registering new users by sending OTP’s to phone number before any details is provided. Generally in this type of systems once a OTP is sent it is valid for a certain time and then we need to click on some resend button for sending another OTP . But in this website there was nothing as such resend button or something, which caught my attention.

Now I intercepted the request of “Send OTP” funtionality and send it to the repeater. Now I sent the request and a OTP was sent to my phone. Then I send the same request again without any delay after sending the first one. But this time response contained that “OTP can be send after one minute”. So I thought let’s send the request after a minute. And after one minute I could send the same request and I received a different OTP. Now I closely observed after what time I could exactly send the request again and it came out to be 40 seconds. So, now it was cleared that if I could automate the process, then I could send multiple OTP’s after every 40 seconds.

I remembered that there was a option called throttle in intruder tab of Burp. So I sent the request to intruder and set the throttle to 40 seconds and payload type to Null payloads and started the attack. And BOOM!!!!!! It was sending OTP after every 40 seconds and spamming my phone.

I reported the issue and got responses very fast within a day and got my first bounty within a month I guess. The bounty was less maybe but to me it was probably huge because it is my first ever bounty. Thank you everyone for reading the writeup.
