---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1638347'
original_report_id: '1638347'
title: String length restriction byepass at https://callerfeel.mtnonline.com/profile/feedback.html
weakness: Violation of Secure Design Principles
team_handle: mtn_group
created_at: '2022-07-15T17:47:12.058Z'
disclosed_at: '2022-09-07T08:48:50.330Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: mtnonline.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# String length restriction byepass at https://callerfeel.mtnonline.com/profile/feedback.html

## Metadata

- HackerOne Report ID: 1638347
- Weakness: Violation of Secure Design Principles
- Program: mtn_group
- Disclosed At: 2022-09-07T08:48:50.330Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi, hope you are well :)

I found that the attacker can bye pass the lenght restriction of user name at the feedback form

## Steps To Reproduce:
{F1823237}

## Impact

Attacker can make the receiver page to delay and can cause application level dos

##Mitigation:
Restrict the lenght of the string in backend too not only front end 

Best regards
@aliyugombe

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
