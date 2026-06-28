---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-20_bypass-2fa-like-a-boss.md
original_filename: 2020-06-20_bypass-2fa-like-a-boss.md
title: Bypass 2FA like a Boss
category: documents
detected_topics:
- rate-limit
- command-injection
- mfa
tags:
- imported
- documents
- rate-limit
- command-injection
- mfa
language: en
raw_sha256: a14205dec63b1a569b4f8501cc1bc54fcbe536c8eadc3d56a9b6ed0093ccb365
text_sha256: ca6215915d7d7105166a62a3719331f39f2c2c35a7f97888852480d375960ebd
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass 2FA like a Boss

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-20_bypass-2fa-like-a-boss.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, mfa
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `a14205dec63b1a569b4f8501cc1bc54fcbe536c8eadc3d56a9b6ed0093ccb365`
- Text SHA256: `ca6215915d7d7105166a62a3719331f39f2c2c35a7f97888852480d375960ebd`


## Content

---
title: "Bypass 2FA like a Boss"
url: "https://medium.com/bugbountywriteup/bypass-2fa-like-a-boss-378787707ba"
authors: ["Seqrity (@seQrity)"]
bugs: ["Lack of rate limiting", "Bruteforce"]
publication_date: "2020-06-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4481
scraped_via: "browseros"
---

# Bypass 2FA like a Boss

Bypass 2FA like a Boss
Seqrity
Follow
2 min read
·
Jun 20, 2020

506

5

This write-up is about a public program, but the disclosure policy is enabled on this program, so we assume the domain is: domain.com

In the recon process, I’ve found that two websites are the same :

www.domain.com
beta.domain.com

2FA was enabled on www.domain.com, and when you create an account on this domain, you can log in on beta.domain.com without entering the 2FA code.

By default, the 2FA was disabled. So, I‘ve decided to try bypassing 2FA and enabling it on www.domain.com. After entering the username and password, you should enter 6 characters (digits and chars), and after 5 minutes, the code will be expired. Therefore, brute force doesn’t work here.

Open Burp and intercept request after entering a password, and change Host header to beta.domain.com

Get Seqrity’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Enter 000000 in twofactorcode field

Press enter or click to view image in full size

And forward request, BOOOM.

I successfully logged in to www.domain.com without entering the correct code.

Report: 14 May 2020

Fixed: 15 May 2020

First Response: 19 May 2020

Bounty: They didn’t pay bounty and said our developers fix that before reviewing your report!!!

My Twitter: https://twitter.com/seqrity9
