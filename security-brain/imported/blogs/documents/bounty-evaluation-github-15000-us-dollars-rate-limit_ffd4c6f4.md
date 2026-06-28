---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-28_bounty-evaluation-github-15000-us-dollars-rate-limit.md
original_filename: 2021-12-28_bounty-evaluation-github-15000-us-dollars-rate-limit.md
title: Bounty Evaluation GitHub = $15,000 US Dollars | Rate Limit
category: documents
detected_topics:
- rate-limit
- command-injection
- password-reset
- otp
- api-security
tags:
- imported
- documents
- rate-limit
- command-injection
- password-reset
- otp
- api-security
language: en
raw_sha256: ffd4c6f49ffa5c7766478fbe41c12b83caa8449823b57cc3e78befe0fd3b086e
text_sha256: c10ae2eae7c0d125f2fb1454c588edd49bdee0ba440e1cb6185a2e953b61d6c9
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Bounty Evaluation GitHub = $15,000 US Dollars | Rate Limit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-28_bounty-evaluation-github-15000-us-dollars-rate-limit.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, password-reset, otp, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `ffd4c6f49ffa5c7766478fbe41c12b83caa8449823b57cc3e78befe0fd3b086e`
- Text SHA256: `c10ae2eae7c0d125f2fb1454c588edd49bdee0ba440e1cb6185a2e953b61d6c9`


## Content

---
title: "Bounty Evaluation GitHub = $15,000 US Dollars | Rate Limit"
url: "https://medium.com/@taniyatesting11/bounty-evaluation-github-15-000-us-dollars-rate-limit-d6c07d73c948"
authors: ["Taniya Agarwal"]
programs: ["GitHub"]
bugs: ["Bruteforce", "Email verification bypass", "Account takeover"]
bounty: "15,000"
publication_date: "2021-12-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3055
scraped_via: "browseros"
---

# Bounty Evaluation GitHub = $15,000 US Dollars | Rate Limit

Bounty Evaluation 
GitHub
 = $15,000 US Dollars | Rate Limit
Taniya Agarwal
Follow
3 min read
·
Dec 28, 2021

1.1K

12

I found the bug on GitHub website where, I bypassed the login authentication. In this walk through I will show it was done. Let’s Understand what rate limit is and how not configuring correctly can leading to business disruption. GitHub needs no introduction, it’s an open source software development platform. I found the bug through HackerOne platform where I bypassed the email verification.

Brute Forcing:

After finding the relevant website to attack, I created an online account in github with my email address. I tried loggin in, it asked for code which was configured to be sent to my email. The problem here was that they did not configure the number of attempts that can be considered from a single account.

Get Taniya Agarwal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I used burpsuite to capture the code that was sent to me, but could be brute forced through multiple attempts as the rate limit is not configured. I used the attacking method as cluster bomb and changed the payload type to number. I also configured the payload position. If you don’t know the working of the burpsuite, you can checkout learning module BurpSuite@ 
TryHackMe
 here: https://tryhackme.com/module/learn-burp-suite

Press enter or click to view image in full size

Interesting information about this attack was the developer had configured single parameter for each OTP number. Essentially, it means that the there were 6 paramters in total for 6 digit OTP. I initially had difficulties finding the numeric OTP value, but after long hours of madness I discovered how developer had designed the code.

Press enter or click to view image in full size

I started the attack and after some time, I checked there was a slightly large response size. When I matched the bruteforce attempt with the actual code, it was a match.

Press enter or click to view image in full size

In bug bounties, there is a critical statement that is impact of your bug. Impact can be accelerated with the help of critical thinking. I exaplained GitHub security team that since GitHub accounts are used to sign-in as third party verification, this is a high impact vulnerability.

Leave some claps and follow me on Medium for information of bug bounties.
See you at the bank!!
