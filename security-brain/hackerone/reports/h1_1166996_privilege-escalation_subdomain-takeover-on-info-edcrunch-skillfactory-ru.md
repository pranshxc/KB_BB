---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1166996'
original_report_id: '1166996'
title: Subdomain takeover on "info-edcrunch.skillfactory.ru"
weakness: Privilege Escalation
team_handle: mailru
created_at: '2021-04-16T23:54:23.666Z'
disclosed_at: '2021-08-15T19:03:15.419Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 23
asset_identifier: 'Ext. O: Acquisitions, not integrated to Mail.Ru infrastructure
  and external cloud services'
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Subdomain takeover on "info-edcrunch.skillfactory.ru"

## Metadata

- HackerOne Report ID: 1166996
- Weakness: Privilege Escalation
- Program: mailru
- Disclosed At: 2021-08-15T19:03:15.419Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application
--
http://info-edcrunch.skillfactory.ru/

Here there is a skillfactory domain  (info-edcrunch.skillfactory.ru) which is pointing towards tilda pages so  this domain can be taken over can can be used to do any type of attacks mostly i can make a fake login page on your behalf and spoof your users, this is a critical vulnerability and needs to be fixed .

Steps to reproduce
--
go to
http://info-edcrunch.skillfactory.ru/

my Poc:

Elsfa7-110 takeover
--
Remediation
Remove the cname entry or claim the subdomain http://info-edcrunch.skillfactory.ru on tilda.cc

## Impact

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
