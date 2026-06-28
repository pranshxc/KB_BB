---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-21_otp-brute-force-via-rate-limit-bypass.md
original_filename: 2021-03-21_otp-brute-force-via-rate-limit-bypass.md
title: OTP brute-force via rate limit bypass
category: documents
detected_topics:
- rate-limit
- otp
- command-injection
- api-security
tags:
- imported
- documents
- rate-limit
- otp
- command-injection
- api-security
language: en
raw_sha256: b8ea4c965a808e2b0e55dbf9009cdce9343a89ad66ff87f6e28c4f8bcf8c7566
text_sha256: d4944bb77067edd5bdc6cbf6ba5543dffc274d88ead5e5f20818ae7ce54eb0b2
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# OTP brute-force via rate limit bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-21_otp-brute-force-via-rate-limit-bypass.md
- Source Type: markdown
- Detected Topics: rate-limit, otp, command-injection, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `b8ea4c965a808e2b0e55dbf9009cdce9343a89ad66ff87f6e28c4f8bcf8c7566`
- Text SHA256: `d4944bb77067edd5bdc6cbf6ba5543dffc274d88ead5e5f20818ae7ce54eb0b2`


## Content

---
title: "OTP brute-force via rate limit bypass"
page_title: "OTP Brute-Force Via Rate Limit Bypass | by Bilal Muqeet. | System Weakness"
url: "https://bilalabdulmuqeet.medium.com/brute-forcing-otp-via-bypassing-rate-limit-c5ee6b25c2a8"
authors: ["Bilal Muqeet (@blmqt)"]
bugs: ["Bruteforce", "Lack of rate limiting", "OTP bypass"]
publication_date: "2021-03-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3799
scraped_via: "browseros"
---

# OTP brute-force via rate limit bypass

OTP Brute-Force Via Rate Limit Bypass
Bilal Muqeet.
Follow
4 min read
·
Mar 20, 2021

380

3

Hello everyone, sharing with you my first bug bounty write-up on how I was able to brute force an OTP (One Time Password) mechanism where rate limitation was in place, on a private bug bounty program.

As per my assumption, I am expecting, you already know about rate limiting. If not, allow me to clarify its concept for you. In simple bug-bounty terminology, a rate-limiting technique is implemented in order to restrict the number of requests being sent, that seem to be abnormal in nature.

I didn’t straight up bypass the rate limit feature at first. Instead, I noticed that the prevention was setup at a forget password endpoint. An OTP is sent at the supplied email address on the forget password page, that you will enter and then create your new password.

Press enter or click to view image in full size

When you intercept the request after clicking on the forget password button, what you get on a proxy, like Burp Suite is something like:

Press enter or click to view image in full size

Sending it to intruder, and repeating the request, by almost 20 times, got me responses like:

Press enter or click to view image in full size

I figured out a simple trick to toggle around with this rate limit technique, by adding an X-Forwarded-For header in the request.

You can find more details at: https://book.hacktricks.xyz/pentesting-web/rate-limit-bypass

Looped the request 50 times, from 127.0.0.1 till 127.0.0.50 (value of the X-Forwarded-For header).

Press enter or click to view image in full size

The attached screenshot below, shows 10 repeated requests, with the indication, emailSent: True. And that’s, what happened: My inbox was flooded with my desired number of OTPs.

Press enter or click to view image in full size

The rate limit on the forget password feature had been bypassed here.

I reported this vulnerability separately, but there’s another part to this entire scenario. Here, starts the part when the rate limit on the OTP is bypassed, hence launching a brute-force attack.

At this part when one has to input the OTP, inbox’d to them.

Get Bilal Muqeet.’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I supplied an incorrect OTP, and proxy’d that specific action:

Press enter or click to view image in full size

I repeated the same action by providing 5 incorrect OTPs, and the server responded with:

Rate limit occurrence.

Here, I tried to connect the dots. I thought that I had managed to bypass the rate limit feature on the forget password feature. Why not try the same technique here? After all, brute forcing an OTP can open doors to a possible account takeover in an instance I like this.

Press enter or click to view image in full size

In the highlighted portions of the above request, looped the host ID of the X-Forwarded-For parameter till 0 till 255, and supplied an arbitrary amount of 6 digit numbers in the tokenVerify parameter that takes place for the OTP.

When rate-limiting on OTP is placed:

Press enter or click to view image in full size
Response length 545 denotes rate limit present.

Note the response length after the first 5 requests. After the rate limit on OTP had been bypassed (Payload1 containing X-Forwarded-For, Payload2 for tokenVerify parameter):

Press enter or click to view image in full size
Response length 520 denoting normal workflow.

The payload set, indicating the successful OTP brute-force attempt, with the absence of a rate limit:

Press enter or click to view image in full size

Hope you enjoyed reading till here, Cheers!

Regards,

Bilal Abdul Muqeet.

P.S: For those asking about the bounty amount, it was a 4 digit plus.
