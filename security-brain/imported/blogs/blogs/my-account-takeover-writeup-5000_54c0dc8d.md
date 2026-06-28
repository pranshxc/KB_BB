---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-21_my-account-takeover-writeup-5000.md
original_filename: 2022-11-21_my-account-takeover-writeup-5000.md
title: 'My Account Takeover Writeup: $5000'
category: blogs
detected_topics:
- rate-limit
- sso
- command-injection
- otp
tags:
- imported
- blogs
- rate-limit
- sso
- command-injection
- otp
language: en
raw_sha256: 54c0dc8d73eec9b65466f26fc7e89d8f88f28561aea90691b99444c25c685d55
text_sha256: 65db5ffc52f19f80b3710e2e8847b73d9a5aae71562bb592102ed6c7b2a76441
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# My Account Takeover Writeup: $5000

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-21_my-account-takeover-writeup-5000.md
- Source Type: markdown
- Detected Topics: rate-limit, sso, command-injection, otp
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `54c0dc8d73eec9b65466f26fc7e89d8f88f28561aea90691b99444c25c685d55`
- Text SHA256: `65db5ffc52f19f80b3710e2e8847b73d9a5aae71562bb592102ed6c7b2a76441`


## Content

---
title: "My Account Takeover Writeup: $5000"
url: "https://medium.com/@mrd17x/my-account-takeover-writeup-5000-6895492aa549"
authors: ["MRD7 (@_mrd7_)"]
bugs: ["Lack of rate limiting", "Bruteforce"]
bounty: "5,000"
publication_date: "2022-11-21"
added_date: "2022-11-25"
source: "pentester.land/writeups.json"
original_index: 1884
scraped_via: "browseros"
---

# My Account Takeover Writeup: $5000

My Account Takeover Writeup: $5000
MRD7
Follow
2 min read
·
Nov 21, 2022

156

4

Press enter or click to view image in full size

Hello everyone,

I’m MRD7.

Today, I’m sharing my one of my bug bounty writeup. This is about account takeover by abusing rate limit bug and scoring $5000 bounty for it.

We all know about rate limit bug.

Rate limit bug impact can range from no-impact to account takeover.

If you are bruteforcing alpha — numeric password in login page, it can be informative or P4.

But if you are brute-forcing 4–6 digit numerical OTP, then it can CRITICAL Bug.

So, I’m sharing how I abuse lack of rate limit to account takeover

Get MRD7’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

I got a private invite on Hackerone. It had 6- digit numerical OTP based login mechanism. Every time, user sign in to account, user has to enter OTP sent on email. If correct OTP entered, user will be redirected to account page.

The possible probability of OTP is 1 million ( 000000–999999). Well that’s sound really huge. But in reality it is easy to achieve thanks to cloud service provider like Amazon or Google.

This program already had 100’s of resolved report and was running for more than 2 years. With not so much expectation, I decided to brute force login OTP to victim’s account and to my surprise there was no rate limit mechanism which resulted in victim’s account takeover.

Press enter or click to view image in full size
I reported the bug and in less 24 hr., H1 analyst triaged the bug and company fixed the bug in less than another 15 hrs. and rewarded $5000 bounty for this.
Lesson: Test everything.
Press enter or click to view image in full size
Rewarded with $5000 bounty

Reference:

$30000 bounty for instagram takeover by abusing rate limit bypass

https://www.securityweek.com/instagram-account-takeover-vulnerability-earns-hacker-30000
