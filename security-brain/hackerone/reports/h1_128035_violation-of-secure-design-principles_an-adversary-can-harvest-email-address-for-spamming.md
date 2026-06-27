---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '128035'
original_report_id: '128035'
title: An adversary can harvest email address for spamming.
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-04-03T19:05:00.382Z'
disclosed_at: '2016-04-05T19:04:06.160Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# An adversary can harvest email address for spamming.

## Metadata

- HackerOne Report ID: 128035
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2016-04-05T19:04:06.160Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The website is displaying email address. These email address can be harvested by
automated programs called bots and then used as a target for spamming.

1. Use any Email extractor tool or Add on. Here I have used Chrome Email Extractor Add on offered by
Mr. Alien.
2. In Browser open "https://gratipay.com/about/contact"
3. Observe that Email Extractor, extracts "support@gratipay.com" and “legal@gratipay.com”

Solution:
1. Captcha is one solution but not recommened.
2. Use email id as support(at)gratipay(dot)com (Not recommended)
3. Use images, in case of plain text (Not recommended)
4. To reduce the quantity of spam sent to anonymous mailbox addresses, consider hiding the email
address and instead providing a form that generates the email server-side, protected by a CAPTCHA if
necessary.
5. Code Obfuscation.

Nice read:
http://www.plynt.com/resources/learn/merchants/#entry-235
http://hivelogic.com/enkoder/
https://javascriptobfuscator.com/

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
