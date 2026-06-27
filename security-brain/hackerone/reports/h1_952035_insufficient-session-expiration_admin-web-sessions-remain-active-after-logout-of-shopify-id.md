---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '952035'
original_report_id: '952035'
title: Admin web sessions remain active after logout of Shopify ID
weakness: Insufficient Session Expiration
team_handle: shopify
created_at: '2020-08-05T18:59:11.082Z'
disclosed_at: '2020-09-14T18:59:43.268Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- insufficient-session-expiration
---

# Admin web sessions remain active after logout of Shopify ID

## Metadata

- HackerOne Report ID: 952035
- Weakness: Insufficient Session Expiration
- Program: shopify
- Disclosed At: 2020-09-14T18:59:43.268Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

previously on #837729 a session is still valid and the store password can be seen.

this time I report that the session is still valid despite changing the email address on the shopify account.

## summary: accounts that have changed email addresses still have permission to enter the store through another browser, so old emails can still have access to the store

## steps for reproduction
1. Change your account email (the account has handled several stores) and confirm (I use Firefox)
2. The email account has been successfully replaced
3. open another browser (chrome beta) and log in with the old email, here you are asked to enter the code from the email and you have successfully logged in the account
4. Try opening your shop and logging in with your old email (here I was directed to enter and still have full access, even after changing my email address).

please see the https://150hy.myshopify.com store (test store) and ████@wearehackerone.com and ██████+top@wearehackerone.com accounts (password = ██████████)

## Impact

access not revoke after changed email address on accounts shopify

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
