---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164137'
original_report_id: '164137'
title: Possible content spoofing due to missing error page
weakness: Violation of Secure Design Principles
team_handle: legalrobot
created_at: '2016-08-29T11:06:16.554Z'
disclosed_at: '2016-09-06T05:05:18.561Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Possible content spoofing due to missing error page

## Metadata

- HackerOne Report ID: 164137
- Weakness: Violation of Secure Design Principles
- Program: legalrobot
- Disclosed At: 2016-09-06T05:05:18.561Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

the domain https://www.legalrobot-uat.com is vulnerable to content spoofing.
visit the following link for POC.

https://www.legalrobot-uat.com/%0D%0AContent-Type%3A%20text%2Fhtml%0D%0A%0D%0AIt%20has%20been%20changed%20by%20a%20new%20one%20https://www.Attacker.com%20so%20go%20to%20the%20new%20one%20since%20this%20one

kindly find attached image.

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
