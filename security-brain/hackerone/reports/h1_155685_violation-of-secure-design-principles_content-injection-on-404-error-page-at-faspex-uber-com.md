---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '155685'
original_report_id: '155685'
title: Content injection on 404 error page at faspex.uber.com
weakness: Violation of Secure Design Principles
team_handle: uber
created_at: '2016-07-31T21:41:23.953Z'
disclosed_at: '2016-08-12T17:21:12.393Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content injection on 404 error page at faspex.uber.com

## Metadata

- HackerOne Report ID: 155685
- Weakness: Violation of Secure Design Principles
- Program: uber
- Disclosed At: 2016-08-12T17:21:12.393Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

INTRO:

i want to report a text injection and a missconfiguration of the 404 page which can be used in phishing at faspex.uber.com

EXPLOITABILITY:

PoC link : https://faspex.uber.com/faspex.uber.com/%2f../It%20has%20been%20changed%20by%20a%20new%20one%20http://www.evil.com%20so%20go%20to%20the%20new%20one%20since%20this%20one

IMPACT:

The issue can be used for an attacker to spoof content and phishing purposes

FIX:

Use a Predefined 404 page  will fix the issue,

Please let me know if any more info needed,

Best Regards,

@ak1t4

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
