---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1587374'
original_report_id: '1587374'
title: Campaign Account Balance and History Disclosed in API Response
weakness: Insecure Direct Object Reference (IDOR)
team_handle: linkedin
created_at: '2022-05-31T15:31:20.333Z'
disclosed_at: '2022-11-30T19:31:34.579Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: www.linkedin.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Campaign Account Balance and History Disclosed in API Response

## Metadata

- HackerOne Report ID: 1587374
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: linkedin
- Disclosed At: 2022-11-30T19:31:34.579Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

During the security assessment of the application, it has been observed that server-side authorization checks are not implemented on the 'GET /campaign-manager-api/campaignManagerAccounts/:campaignId/accountCredits?q=account' HTTP request. As a result, an attacker can fetch the campaign wallet amount details like 'totalCreditAmount', and 'remaining credit amount' history of all the victim's account.

###Steps to reproduce:
1. Log in to LinkedIn.
2. Create an advertising account. 
███
3. After creating the account go to - the https://www.linkedin.com/campaignmanager/accounts/XXXXX/billing/transactions page.
4. Intercept the vulnerable requests and replay the request using the victim's campaign id. The response will disclose the campaign wallet details and history.
███████

###Vulnerable Request:
```
GET /campaign-manager-api/campaignManagerAccounts/█████████████/accountCredits?q=account HTTP/2
Host: www.linkedin.com
```

###IDs for testing:
███████████████████
████████████
█████████████████
█████████████████
The ids are in series so can be brute forced

## Impact

An attacker can access the complete wallet details like available amount and used amounts and the deposit history of victim's campaign account.

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
