---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-31_bypassing-2-factor-authentication-for-facebook-business-manager-bounty-1000-usd.md
original_filename: 2021-08-31_bypassing-2-factor-authentication-for-facebook-business-manager-bounty-1000-usd.md
title: 'Bypassing 2-Factor Authentication for Facebook Business Manager (Bounty: 1000
  USD)'
category: documents
detected_topics:
- mfa
- command-injection
- otp
tags:
- imported
- documents
- mfa
- command-injection
- otp
language: en
raw_sha256: c3eb5261c6593fda832221ee12c4cdddd5afbb0b3e94292641bc528a8dc5cefc
text_sha256: 80f87e43ce604b690f3eb6d589ca32b35701534e5ce4bab645504ab4ebc97c5a
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing 2-Factor Authentication for Facebook Business Manager (Bounty: 1000 USD)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-31_bypassing-2-factor-authentication-for-facebook-business-manager-bounty-1000-usd.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, otp
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `c3eb5261c6593fda832221ee12c4cdddd5afbb0b3e94292641bc528a8dc5cefc`
- Text SHA256: `80f87e43ce604b690f3eb6d589ca32b35701534e5ce4bab645504ab4ebc97c5a`


## Content

---
title: "Bypassing 2-Factor Authentication for Facebook Business Manager (Bounty: 1000 USD)"
page_title: "[WRITE-UP] Bypassing 2-Factor Authentication for Facebook Business Manager (Bounty: 1000 USD) | by Shubham Bhamare | InfoSec Write-ups"
url: "https://theshubh77.medium.com/bypassing-2-factor-authentication-for-facebook-business-manager-bounty-1000-usd-c78c858459d6"
authors: ["Shubham Bhamare (@theshubh77)"]
programs: ["Meta / Facebook"]
bugs: ["2FA / MFA bypass"]
bounty: "1,000"
publication_date: "2021-08-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3366
scraped_via: "browseros"
---

# Bypassing 2-Factor Authentication for Facebook Business Manager (Bounty: 1000 USD)

[WRITE-UP] Bypassing 2-Factor Authentication for Facebook Business Manager (Bounty: 1000 USD)
Shubham Bhamare
Follow
2 min read
·
Aug 31, 2021

397

Press enter or click to view image in full size

Hi guys, it’s Shubham Bhamare again. In this write-up, I’m going to tell you how I bypassed 2-Factor Authentication for Facebook Business Manager (now Meta Business Suite) using a very simple trick.

Due to this issue, an attacker was able to make changes in victim’s Facebook Business Manager account. However, access to victim’s personal Facebook account was needed.

Without wasting time, let’s start! 👉

===

Setup and Scenario:

An attacker (ABC) has access to victim (XYZ)’s personal Facebook account. XYZ has enabled 2-Factor Authentication for Business Manager (Because it’s necessary to enable it before using Business Manager account.)

Platform: Facebook Web

===

Reproduction steps:

As ABC has access to the XYZ’s personal Facebook account, but he/she wants to make changes in the XYZ’s Business Manager account which is not accessible due to 2FA is enabled. So, first of all, go to ABC’s Business Manager account and intercept and copy the request of any action you want to make from XYZ’s Business Manager.
Now, as you’ve XYZ’s Facebook account access, copy his/her cookies and fb_dtsg token and replace it in the Business Manager request that we’ve previously captured. Also, you’ll have to replace ABC’s business_id with XYZ’s business_id in this request. When it’s done, forward this modified request. You’ll see the action is successfully completed from XYZ’s Business Manager account. This way, you can make any action on XYZ’s Business Manager account.

===

Get Shubham Bhamare’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Bounty:

1000 USD

Press enter or click to view image in full size

===

Timeline:

May 05, 2019: Report sent

May 08, 2019: Pre-triaged

June 14, 2019: Triaged

July 24, 2019: 1000 USD bounty awarded

July 25, 2019: Issue fixed

===

Thank you for reading! Stay tuned for my next write-up, and don’t forget to follow me on Facebook, Twitter, LinkedIn, and Instagram. 😊

===

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
