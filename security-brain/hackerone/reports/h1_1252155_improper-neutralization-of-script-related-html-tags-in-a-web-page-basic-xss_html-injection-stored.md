---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1252155'
original_report_id: '1252155'
title: HTML INJECTION  (STORED)
weakness: Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic
  XSS)
team_handle: judgeme
created_at: '2021-07-06T03:16:24.783Z'
disclosed_at: '2023-02-01T03:35:18.184Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: judge.me
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-neutralization-of-script-related-html-tags-in-a-web-page-basic-xss
---

# HTML INJECTION  (STORED)

## Metadata

- HackerOne Report ID: 1252155
- Weakness: Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS)
- Program: judgeme
- Disclosed At: 2023-02-01T03:35:18.184Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi team!

I found a way to inject arbitrary html which is also persistent or stored.
Unfortunately I could not execute javascript code, however I think that being stored html it is important to take a look, attackers could use this vulnerability for phishing attacks for example.

###PoC

https://judge.me/profile/y5YJe35X

You can see in the product description how I can add various html elements.

###To reproduce this:

In your profile judge.me go to "my public profile" then my recommendations, now add some html tags in description and then press "add recommendation"


{F1366217}

## Impact

Attackers can use this vulnerability to carry out phishing attacks. It is important to mention again that the stored html code has more impact, the victim does not need user interaction as in the case of the reflected xss.
Also, an attacker could generate good ratings and fake reviews by using html about your product to build trust.

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
