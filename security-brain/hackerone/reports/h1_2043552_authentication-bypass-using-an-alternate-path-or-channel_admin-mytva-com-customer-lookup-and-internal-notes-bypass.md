---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2043552'
original_report_id: '2043552'
title: Admin.MyTVA.com Customer lookup and internal notes bypass
weakness: Authentication Bypass Using an Alternate Path or Channel
team_handle: tennessee-valley-authority
created_at: '2023-06-29T20:14:54.611Z'
disclosed_at: '2023-10-13T12:32:36.833Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: http://admin.mytva.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- authentication-bypass-using-an-alternate-path-or-channel
---

# Admin.MyTVA.com Customer lookup and internal notes bypass

## Metadata

- HackerOne Report ID: 2043552
- Weakness: Authentication Bypass Using an Alternate Path or Channel
- Program: tennessee-valley-authority
- Disclosed At: 2023-10-13T12:32:36.833Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
The admin.mytva.com site does not properly secure the admin only endpoints, which can allow an attacker to bypass the login and take actions like looking up customers. The endpoints can be enumerated through the forgot password function.

## Steps To Reproduce:


  1. Navigate to https://admin.mytva.com/Account/ForgotPassword.aspx and enter 'admin' as the ID
  2. Wait on the admin email to appear (this should also be restricted)
  3. Attempt to send the reset password and capture the request with BURP
4. Review the response to the request for new endpoints. Some of them that will stand out are:
/Evaluation/EditNotes.aspx?ProjectId=
/Evaluation/HOEvalDetailWONav.aspx?ProjectID=
/Tools/Customer/AddressLookup.aspx
5. The endpoints do not protect themselves for bruteforcing either, so the attacker can now attempt to retrieve further information or add internal/customer notes

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

Unprotected endpoints may lead to a data breach. It would be recommended to check the logs for previous attacks

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
