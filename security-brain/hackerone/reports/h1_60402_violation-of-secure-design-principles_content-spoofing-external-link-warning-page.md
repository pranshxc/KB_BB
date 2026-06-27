---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '60402'
original_report_id: '60402'
title: Content Spoofing - External Link Warning Page
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2015-05-10T07:15:04.633Z'
disclosed_at: '2015-05-11T20:50:41.501Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content Spoofing - External Link Warning Page

## Metadata

- HackerOne Report ID: 60402
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2015-05-11T20:50:41.501Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Here is example link:
[Click Here](http://attackers.com/***************   is a fake website. Click Proceed to visit back HackerOne.)

Raw Data:
```
[Click Here](http://attackers.com/***************   is a fake website. Click Proceed to visit back HackerOne.)
```

Issue:
In External link warning page, this link shown as plain text and no forced URL encoded, leading an attacker to frame sentences and trick users. In given example, attacker can trick user to click 'Proceed' button saying it will redirect back to HackerOne but it wont. Though there will be written warning saying better to open in separate browser, bigger letter will be read by users first ;) . In redirected page, attacker can spoof HackerOne website or login page of same or any other phishing attacks.

Possible Fix:
URL Encode spaces to %20 which will convert spoofing content look like link.

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
