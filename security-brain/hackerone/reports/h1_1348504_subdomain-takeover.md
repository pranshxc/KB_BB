---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1348504'
original_report_id: '1348504'
title: Subdomain Takeover
team_handle: mailru
created_at: '2021-09-22T16:27:05.457Z'
disclosed_at: '2022-01-25T08:25:06.796Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
asset_identifier: Ext. B Scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
---

# Subdomain Takeover

## Metadata

- HackerOne Report ID: 1348504
- Weakness: 
- Program: mailru
- Disclosed At: 2022-01-25T08:25:06.796Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
Actually team this bug is similar to my previous bug which I submitted-██████

Issue details:-
Subdomain takeover vulnerabilities occur when a subdomain (subdomain.example.com) is pointing to a service (e.g. GitHub pages, Heroku, etc.) that has been removed or deleted. This allows an attacker to set up a page on the service that was being used and point their page to that subdomain. For example, if subdomain.example.com was pointing to a GitHub page and the user decided to delete their GitHub page, an attacker can now create a GitHub page, add a CNAME file containing subdomain.example.com, and claim subdomain.example.com.
Here  is motiondesign.geekbrains.ru, wantdigital.geekbrains.ru, productowner.geekbrains.ru subdomains pointing towards unclimed readymag page so this domain can be taken over and can be used to do any type of attacks mostly i can make a fake login page on your behalf and spoof your users, this is a critical vulnerability and needs to be fixed.

Vulnerable url:-
https://motiondesign.geekbrains.ru/
https://wantdigital.geekbrains.ru/
https://productowner.geekbrains.ru/

Poc:-
https://domains.readymag.com/

Note: every subdomain are pointing to same cname.

Fix:-
Remove the cname entry or claim the subdomain.

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
