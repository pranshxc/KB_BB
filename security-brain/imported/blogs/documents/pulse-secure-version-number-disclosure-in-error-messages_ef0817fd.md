---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-12_pulse-secure-version-number-disclosure-in-error-messages.md
original_filename: 2021-10-12_pulse-secure-version-number-disclosure-in-error-messages.md
title: Pulse Secure version number disclosure in error messages
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: ef0817fd37e2bfbbcebd3258a244b75a062753aff0f90624d04364efb37d80b1
text_sha256: cfa367ce40855e2c5c5aec36f9c1e1a82bbd88cd69329fc6906eb675cbb5ce3e
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Pulse Secure version number disclosure in error messages

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-12_pulse-secure-version-number-disclosure-in-error-messages.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `ef0817fd37e2bfbbcebd3258a244b75a062753aff0f90624d04364efb37d80b1`
- Text SHA256: `cfa367ce40855e2c5c5aec36f9c1e1a82bbd88cd69329fc6906eb675cbb5ce3e`


## Content

---
title: "Pulse Secure version number disclosure in error messages"
url: "https://medium.com/@mehdi.alouache/pulse-secure-version-number-disclosure-in-error-messages-143aa76c90cd"
authors: ["Mehdi Alouache"]
programs: ["Pulse Secure"]
bugs: ["Information disclosure"]
publication_date: "2021-10-12"
added_date: "2022-11-08"
source: "pentester.land/writeups.json"
original_index: 3246
scraped_via: "browseros"
---

# Pulse Secure version number disclosure in error messages

Pulse Secure version number disclosure in error messages
Mehdi Alouache
Follow
1 min read
·
Oct 12, 2021

1

Press enter or click to view image in full size

This article is a re-publication of something I wrote 5 months back, as I am merging my content on medium.com

As mentioned by OWASP, errors should be properly handled in order to ensure internal logic and additional information are not exposed in case of error message display : https://owasp.org/www-community/Improper_Error_Handling

All versions* of Pulse Secure Network Connect are affected by an Information Disclosure issue allowing an attacker to detect the version of the last patch applied, without being authenticated. The issue was reported to Pulse Secure by official way on HackerOne but the bounty was denied.

Version disclosure makes it easier to find the proper exploit to run on the Pulse Secure appliances.

Get Mehdi Alouache’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

*All versions to the date of publication of the article, May 2021

Identify Pulse Secure appliances in the wild

Pulse secure appliances can be spotted by using a simple Google dork :

inurl:”dana-na”

This is not an attempt to make you think about Manau

Fingerprint Pulse Secure Network Connect version

The version is disclosed is HTML comments if you trigger an error on an authentication page.

I wrote a script to get the result : https://github.com/MedAlch/pulse-fingerprint
