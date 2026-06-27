---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '168078'
original_report_id: '168078'
title: Content Spoofing possible in concrete5.org
weakness: Violation of Secure Design Principles
team_handle: concretecms
created_at: '2016-09-13T17:30:28.851Z'
disclosed_at: '2017-07-23T10:30:48.396Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- violation-of-secure-design-principles
---

# Content Spoofing possible in concrete5.org

## Metadata

- HackerOne Report ID: 168078
- Weakness: Violation of Secure Design Principles
- Program: concretecms
- Disclosed At: 2017-07-23T10:30:48.396Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

An attacker can include any arbitrary text using specially crafted concrete5 url.
This is done using character /%0d%0a.
**Input**
https://www.concrete5.org/%0d%0ahas%20moved%20to%20www.evil.com.Please%20visit%20evil.com%20Present%20resource

**Output**
The requested URL / has moved to www.evil.com.Please visit evil.com Present resource was not found on this server.

This attacks are difficult to perform but they may spoof the user in downloading malwares since user believes the text to be coming from yelp site.

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
