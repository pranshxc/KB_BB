---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1004412'
original_report_id: '1004412'
title: Possible LDAP username and password disclosed on Github
weakness: Information Disclosure
team_handle: acronis
created_at: '2020-10-10T04:47:03.679Z'
disclosed_at: '2021-08-17T17:15:17.971Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
asset_identifier: Other Acronis Domains
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- information-disclosure
---

# Possible LDAP username and password disclosed on Github

## Metadata

- HackerOne Report ID: 1004412
- Weakness: Information Disclosure
- Program: acronis
- Disclosed At: 2021-08-17T17:15:17.971Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary
The file hosted at https://github.com/mlanin/go/blob/3dbd856c3f542c54e512a295ac498c79cd952ed6/.env.testing  contains the following information:
**LDAP_DOMAIN=███
LDAP_BASE_DN=███
LDAP_ADMIN_USER=███████
LDAP_ADMIN_PASSWORD=██████**

## Recommendations
Verify if credentials are still in use if so remove the file from GitHub and reset passwords.

## NOTE
Please let me self-close this report if the credentials do not belong to Acronis or are not active. I took a better safe than sorry approach.

## Impact

Although I was not able to find any port open on the ███████ server, if the credentials are valid they can be used by insider threats for lateral movement and privilege escalation.

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
