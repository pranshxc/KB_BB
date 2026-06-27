---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1287686'
original_report_id: '1287686'
title: '[ii.worki.ru ] emarsys  subdomain takeover'
weakness: Privilege Escalation
team_handle: mailru
created_at: '2021-08-02T20:01:21.791Z'
disclosed_at: '2021-09-28T06:20:26.197Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 31
asset_identifier: Ext. B Scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# [ii.worki.ru ] emarsys  subdomain takeover

## Metadata

- HackerOne Report ID: 1287686
- Weakness: Privilege Escalation
- Program: mailru
- Disclosed At: 2021-09-28T06:20:26.197Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi team 

 i am find a subdomain takeover vulnerbility in ii.worki.ru subdomain

the ii.worki.ru  which is delegated to emarsys.net , which is vulnerable to takeover.

CName :- ████████
Name: ii.worki.ru
Type:CNAME

when you search https://ii.worki.ru it redirects to █████████ 

which is emarsys.net service 

Remediation
Remove the cname entry or claim the subdomain ii.worki.ru on emarsys.net

## Impact

Impact
Risk
fake website
malicious code injection
users tricking
company impersonation
This issue can have really huge impact on the companies reputation someone could post malicious content on the compromised site and then your users will think it's official but it's not.

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
