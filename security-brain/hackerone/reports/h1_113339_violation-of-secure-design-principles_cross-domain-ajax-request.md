---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '113339'
original_report_id: '113339'
title: Cross-domain AJAX request
weakness: Violation of Secure Design Principles
team_handle: paragonie
created_at: '2016-01-28T19:57:14.162Z'
disclosed_at: '2016-06-17T01:57:05.426Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Cross-domain AJAX request

## Metadata

- HackerOne Report ID: 113339
- Weakness: Violation of Secure Design Principles
- Program: paragonie
- Disclosed At: 2016-06-17T01:57:05.426Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi Paragonie Team, 

While reviewing  your website i discovered that there are Cross-domain AJAX requests being sent, though you are implementing Content-Security-Policy header but Internet Explorer uses experimental X-Content-Security-Policy header according to Wikipedia info (https://en.wikipedia.org/wiki/Content_Security_Policy#Status)

Reference from Hacker one reports:- 
https://hackerone.com/reports/97191
https://hackerone.com/reports/97948

Please also find screenshot attached

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
