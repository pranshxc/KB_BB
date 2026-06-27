---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '631589'
original_report_id: '631589'
title: Web Cache poisoning attack leads to User information Disclosure and more
weakness: Violation of Secure Design Principles
team_handle: lyst
created_at: '2019-06-28T18:46:28.485Z'
disclosed_at: '2022-03-22T11:53:55.922Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
asset_identifier: '*.lyst.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Web Cache poisoning attack leads to User information Disclosure and more

## Metadata

- HackerOne Report ID: 631589
- Weakness: Violation of Secure Design Principles
- Program: lyst
- Disclosed At: 2022-03-22T11:53:55.922Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello

Your Web-Server is vulnerable to web cache poisoning attacks.
This means, that the attacker are able to get another user Information.

If you are logged in and visit this website (For example):
https://www.lyst.com/shop/trends/mens-dress-shoes/blahblah.css

Then the server will store the information in the cache, BUT with the logged in user information.
A non-logged-in user can then visit this website and see the information contained therein.

In that case, this url: https://www.lyst.com/shop/trends/mens-dress-shoes/blahblah.css can be visited in Private Mode and still you will be shown as "LOGGED IN" and then check the Source code you will get your email, member id ,etc..


Some informations about the attack:
https://www.blackhat.com/docs/us-17/wednesday/us-17-Gil-Web-Cache-Deception-Attack.pdf

The screenshots with the steps are in the attachments.

## Impact

Web cache poisoning attack can be used to steal user informations like email, name and member id which is important for the login security feature.

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
