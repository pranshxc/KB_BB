---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-06_crypto-bounty-program-got-me-500-rate-limit-bypass.md
original_filename: 2024-05-06_crypto-bounty-program-got-me-500-rate-limit-bypass.md
title: Crypto bounty program got me $500 — Rate Limit Bypass
category: documents
detected_topics:
- password-reset
- rate-limit
- command-injection
- otp
- api-security
- mobile-security
tags:
- imported
- documents
- password-reset
- rate-limit
- command-injection
- otp
- api-security
- mobile-security
language: en
raw_sha256: a4d91634a9c085c042e2f45cf8968d03c712650fe3ea965b33bd896aac140210
text_sha256: 735922ccfc274cd372398edfe2b73a472c09216c78db6849f133e128b6d8095b
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Crypto bounty program got me $500 — Rate Limit Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-06_crypto-bounty-program-got-me-500-rate-limit-bypass.md
- Source Type: markdown
- Detected Topics: password-reset, rate-limit, command-injection, otp, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `a4d91634a9c085c042e2f45cf8968d03c712650fe3ea965b33bd896aac140210`
- Text SHA256: `735922ccfc274cd372398edfe2b73a472c09216c78db6849f133e128b6d8095b`


## Content

---
title: "Crypto bounty program got me $500 — Rate Limit Bypass"
url: "https://mo9khu93r.medium.com/crypto-bounty-program-got-me-500-rate-limit-bypass-d573f7b7d390"
authors: ["mo9khu93r"]
programs: ["Kraken"]
bugs: ["Rate limiting bypass"]
bounty: "500"
publication_date: "2024-05-06"
added_date: "2024-05-11"
source: "pentester.land/writeups.json"
original_index: 304
scraped_via: "browseros"
---

# Crypto bounty program got me $500 — Rate Limit Bypass

Crypto bounty program got me $500 — Rate Limit Bypass
viperx9
Follow
3 min read
·
May 6, 2024

369

3

Web3 security will be the future of bug bounty.

For a small bug on web3, you could got 2x comparing a medium or high severity bug on web.

The vulnerability is fixed so now, I can disclose the target. First response from the target[Kraken]-

Press enter or click to view image in full size
Automatic Reply from The Company

Today I will tell you, how I secured $500 from a rate limit bypass.

How it started-

I was working as web pentester intern at a company. My boss gave me a target to hunt, unfortunately it was a public 😂 crypto program.

Initial Phase-

As you all know crypto targets are very secure and the chance of getting a bug is 0.000001% but something is better than nothing 🤫

I tried every possible way to find at least a single bug but nothing worked. I reported a bug called- password reset token not expiring after issuance of new one

But it got N/A 🤖

The Bug 🤑-

After trying several things I reached to the forgot password functionality to check for password reset poisoning but the functionality was safe from it.

I also checked for email triggering i.e., no rate limit on requesting password reset links.

But after every 5 attempts the account got locked for 3 minutes 🥴

I tried a simple bypass i.e., adding null characters after the email- e.g. \n \0 \x00 %0 etc., but nothing worked.

You should try all these.

The Bypass 😈-

After trying above bypasses, another bypass hit my mind- add a space after the email.

Get viperx9’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And ya that worked for me…😇

Steps to reproduce-
1. Intercept the forgot password request.
2. Send it to repeater, forward it, you will get the response that link to reset is sent ,forward it 4 times more, everything will be fine till here i.e., till now you received 5 password reset links in email. Now send one more time and you will be blocked for 3 minutes.
3. Now add a space after the email i.e.,
email=’email@gmail.com ‘ [see the space before the last quote in the email].
4. Send the above request 5 times, you will get 5 more links in the email and after that again you will be blocked.
5. Repeat step 3 i.e., add another space and in this way, adding a single space after every 5 attempts we have successfully bypassed the no rate limit.
Report ☠️-

I prepared a report and I haven’t used intruder for the POC. I just did what I showed you in steps to reproduce above. And after 3 days I got the email which I showed you above that I was awarded $500 and they assigned it low severity because a user can block these emails.

NOTE 💸-

If you’re interested in crypto and want to mine, Pi Network is a mobile app that lets you mine a new cryptocurrency called Pi directly from your phone.

Features-

Low Battery Usage

Minimal Data Usage

Passive Mining

User-Friendly Interface

No Overheating Issues

Boost your mining 4x with my invite code ➡ ️mineWi3Me

Link- https://minepi.com/mineWi3Me

Thanks for reading 🌹

#bugbounty #vulnerability #crypto #hacking
