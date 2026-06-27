---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '156196'
original_report_id: '156196'
title: Error page Text Injection.
weakness: Violation of Secure Design Principles
team_handle: phabricator
created_at: '2016-08-03T04:09:01.607Z'
disclosed_at: '2016-08-25T14:17:42.313Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Error page Text Injection.

## Metadata

- HackerOne Report ID: 156196
- Weakness: Violation of Secure Design Principles
- Program: phabricator
- Disclosed At: 2016-08-25T14:17:42.313Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

AS we can see in report an user or attacker is able to inject his text into error page and can trap to user to visit other site by adding following link /test/%2f../It%20has%20been%20changed%20by%20a%20new%20one%20https://www.malicious.com%20so%20go%20to%20the%20new%20one%20since%20this%20one

A text injection and a missconfiguration of the 404 page which can be used in phishing.

POC URL: blog.trello.com/test/%2f../It%20has%20been%20changed%20by%20a%20new%20one%20https:

URl:-https://www.phacility.com//test/%2f../It%20has%20been%20changed%20by%20a%20new%20one%20https://www.malicious.com%20so%20go%20to%20the%20new%20one%20since%20this%20one

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
