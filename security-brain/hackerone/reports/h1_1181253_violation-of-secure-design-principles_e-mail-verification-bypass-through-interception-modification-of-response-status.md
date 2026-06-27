---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1181253'
original_report_id: '1181253'
title: e-mail verification bypass through interception & modification of response
  status
weakness: Violation of Secure Design Principles
team_handle: gsa_vdp
created_at: '2021-04-30T15:12:40.815Z'
disclosed_at: '2021-09-02T14:46:49.499Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 22
asset_identifier: tams.preprod.gsa.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# e-mail verification bypass through interception & modification of response status

## Metadata

- HackerOne Report ID: 1181253
- Weakness: Violation of Secure Design Principles
- Program: gsa_vdp
- Disclosed At: 2021-09-02T14:46:49.499Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

During registration of account at https://tams.preprod.gsa.gov, e-mail verification (code validation) can be bypassed through intercepting & modifying the response status-from "success":false to "success":true
Video {F1284281} is for reference.

##Steps To Reproduce
1. Open User Registration  Url - https://tams.preprod.gsa.gov/userEmailReg
2. Enter the email & submit.
3. Prompt to enter the verification code will appear.
4. Enter any wrong value (6 digits), submit & capture in burp.
5.Before submitting, select the option in burp - Do Intercept response to this request
6. After receiving the response. Modify the value false to true for success parameter.
7. You would be able to continue the registration process. 
8. A pop up appears in the next stage. You can close & go ahead with registration process.

## Impact

Bypass of e-mail verification processes.

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
