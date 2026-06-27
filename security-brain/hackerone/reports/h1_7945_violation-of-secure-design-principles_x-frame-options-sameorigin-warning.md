---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7945'
original_report_id: '7945'
title: x-frame options-sameorigin warning
weakness: Violation of Secure Design Principles
team_handle: respondly
created_at: '2014-04-18T03:31:10.325Z'
disclosed_at: '2014-05-18T04:26:51.669Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# x-frame options-sameorigin warning

## Metadata

- HackerOne Report ID: 7945
- Weakness: Violation of Secure Design Principles
- Program: respondly
- Disclosed At: 2014-05-18T04:26:51.669Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

As the x-frame options set to same-origin it still may be vulnerable to clickjacking attacks how?
by using this code
<iframe src="link " sandbox="allow-top-navigation allow-same-origin allow-scripts"></iframe>

Better explanation: http://www.skeletonscribe.net/2012/06/x-frame-options-sameorigin-warning.html

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
