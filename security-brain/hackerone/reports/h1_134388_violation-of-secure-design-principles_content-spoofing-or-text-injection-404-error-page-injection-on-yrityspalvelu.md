---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '134388'
original_report_id: '134388'
title: Content Spoofing or Text Injection (404 error page injection on yrityspalvelu)
weakness: Violation of Secure Design Principles
team_handle: localtapiola
created_at: '2016-04-25T11:39:50.092Z'
disclosed_at: '2016-11-10T09:26:50.011Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content Spoofing or Text Injection (404 error page injection on yrityspalvelu)

## Metadata

- HackerOne Report ID: 134388
- Weakness: Violation of Secure Design Principles
- Program: localtapiola
- Disclosed At: 2016-11-10T09:26:50.011Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Vulnerability Description: Application allows users to inject any content on the 404 not found webpage

Vulnerable Location: https://yrityspalvelu.tapiola.fi/a1/has%20been%20changed%20by%20a%20new%20one%20https://www.attacker.com%20so%20go%20to%20the%20new%20one%20since%20this%20one

Fix : just use a 404 page that don't include attacker text

Reference links: Below are the links which will help you to understand more about this issue including the remediation
https://hackerone.com/reports/106350
https://hackerone.com/reports/102327
https://hackerone.com/reports/111860

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
