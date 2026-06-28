---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-25_a-5000-account-takeover.md
original_filename: 2020-07-25_a-5000-account-takeover.md
title: A $5000 Account Takeover
category: documents
detected_topics:
- otp
- command-injection
- password-reset
- api-security
tags:
- imported
- documents
- otp
- command-injection
- password-reset
- api-security
language: en
raw_sha256: 275d610bc8f2c5353d18d8b9f88bf68f7bde59c459d1c4d3d38381294d5b0efa
text_sha256: aa4c2ff76f86a1dd9d31ab92bdbd42175e2e9b912360ee08c3f34cce01da26ed
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# A $5000 Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-25_a-5000-account-takeover.md
- Source Type: markdown
- Detected Topics: otp, command-injection, password-reset, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `275d610bc8f2c5353d18d8b9f88bf68f7bde59c459d1c4d3d38381294d5b0efa`
- Text SHA256: `aa4c2ff76f86a1dd9d31ab92bdbd42175e2e9b912360ee08c3f34cce01da26ed`


## Content

---
title: "A $5000 Account Takeover"
page_title: "$5000 Account Takeover. Hey there!!! | by neelam | Medium"
url: "https://medium.com/@vneelam609/5000-account-takeover-bf7749746981"
authors: ["neelam"]
bugs: ["Account takeover", "Password reset"]
bounty: "5,000"
publication_date: "2020-07-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4388
scraped_via: "browseros"
---

# A $5000 Account Takeover

Member-only story

neelam
Follow
3 min read
·
Jul 25, 2020

431

1

A $5000 Account Takeover

Hey there!!!

This is my first write up on bug bounty and going to continue writing much more interesting one as soon as I will receive my rewards :p

This write up is based on my a few months back earned $5000 as many people were asking me about the technique….so let’s follow the steps

Bug Type- Account takeover via OTP

Technical Details-

This bug I found on highest paying bug bounty program-oops!! Don’t ask me the name of program :D

I always keep looking for something interesting and which should cause a business impact.

Test case 1- Verify for Case Sensitiveness

Check if any quotes or forward slash is working on a parameter or throwing any output in response.

Test case 2-Check for types of characters OTP supports

It can be Only Digits, Only Alphabets, and Alphanumeric.

Test case 3- How many times a user can provide invalid OTP?

Verify that after temporary blocking of the email account, the system does not send the one-time password.

These are the few test cases I tried, there are many though you can go with this necessary checklist.

Test case 4- Captured the request and understanding the behavior of the app as to how it shows in response.

Let’s first see the first verified response…
