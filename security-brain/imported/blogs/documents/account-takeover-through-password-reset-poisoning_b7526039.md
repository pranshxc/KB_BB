---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-19_account-takeover-through-password-reset-poisoning_2.md
original_filename: 2019-12-19_account-takeover-through-password-reset-poisoning_2.md
title: Account Takeover Through Password Reset Poisoning
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- api-security
- cloud-security
language: en
raw_sha256: b75260392f50728e55b4371814395d1ca4510e13000742b5e831f7c98999acc9
text_sha256: f6c9453ea4308f0b0acf4ea3030ccfde23549854f377463eac76996c11a80575
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover Through Password Reset Poisoning

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-19_account-takeover-through-password-reset-poisoning_2.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `b75260392f50728e55b4371814395d1ca4510e13000742b5e831f7c98999acc9`
- Text SHA256: `f6c9453ea4308f0b0acf4ea3030ccfde23549854f377463eac76996c11a80575`


## Content

---
title: "Account Takeover Through Password Reset Poisoning"
url: "https://medium.com/@vbharad/account-takeover-through-password-reset-poisoning-72989a8bb8ea"
authors: ["Vishal Bharad"]
bugs: ["Password reset", "Account takeover"]
publication_date: "2019-12-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4878
scraped_via: "browseros"
---

# Account Takeover Through Password Reset Poisoning

Top highlight

Member-only story

Account Takeover Through Password Reset Poisoning
Vishal Bharad
Follow
3 min read
·
Dec 19, 2019

391

4

Introduction :

Hello, I am Vishal Bharad, I am Mechanical Engineer :D and working as Penetration Tester. I’m here to share about my findings on Full Account Takeover.

About the Vulnerability :

For Discovering the bug I have tested many tricks on the website. Assume redacted.com. When finding the bugs i decided that find some bugs on Forget Password Page.

I tried on many websites about 6 to 8 hours. Then after so many attempts I have found a big and interesting vulnerability which leads to Full Account Takeover

Tools Used for this Vulnerability:

BurpSuite
Ngrok Server

Steps to Reproduce:

Go to https://redacted.com/users/forgot_password and type username to get forget password link.
Capture this request in Burpsuite and add X-Forwarded-Host: bing.com

3. Then forward the request and check your email. You got an email of Password reset with token. Which looks Like (https://bing.com/users/reset_password/tqo4Xciu806oiR1FjX8RtIUc1DTcm1B5Kqb53j1fLEkzMW2GPgCpuEODDStpRaES)

Press enter or click to view image in full size

Here token is Leak to the bing.com. So Now to confirm this token is True or not. Put https://redacted.com instead of…
