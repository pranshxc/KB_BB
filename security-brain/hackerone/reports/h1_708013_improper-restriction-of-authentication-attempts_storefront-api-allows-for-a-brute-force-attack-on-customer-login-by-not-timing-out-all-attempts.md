---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '708013'
original_report_id: '708013'
title: StoreFront API allows for a brute force attack on customer login by not timing
  out ALL attempts
weakness: Improper Restriction of Authentication Attempts
team_handle: shopify
created_at: '2019-10-04T22:13:38.873Z'
disclosed_at: '2019-10-07T20:12:54.095Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# StoreFront API allows for a brute force attack on customer login by not timing out ALL attempts

## Metadata

- HackerOne Report ID: 708013
- Weakness: Improper Restriction of Authentication Attempts
- Program: shopify
- Disclosed At: 2019-10-07T20:12:54.095Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It seems that the service used for login purposes could be brute forced. the system fails when the password is incorrect, after some unsuccessful attempts the following message is shown:

 
{"data":{"customerAccessTokenCreate":null},"errors":[{"message":"Login attempt limit exceeded. Please try again later.","locations":[{"line":1,"column":10}],"path":["customerAccessTokenCreate"]}]}

 
However, it still possible to continue brute forcing and if you try with the real password it will work again. So in our case, we have been able to perform brute force attack.  

We feel Shopify should enforce the "limit exceeded" error for BOTH valid and invalid passwords.

## Impact

If the brute force attack succeeds, the attacker will then gain access to that user's shopify account, including contact information and order history.

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
