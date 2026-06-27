---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '782764'
original_report_id: '782764'
title: xss in /users/[id]/set_tier endpoint
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: ratelimited
created_at: '2020-01-24T19:03:14.075Z'
disclosed_at: '2020-01-25T07:27:32.522Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: https://github.com/gtsatsis/RLAPI-v3-OOP
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# xss in /users/[id]/set_tier endpoint

## Metadata

- HackerOne Report ID: 782764
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: ratelimited
- Disclosed At: 2020-01-25T07:27:32.522Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
[add summary of the vulnerability]
Hello there ! I found an XSS since you forgot to add the json content-type response header right there:
https://github.com/gtsatsis/RLAPI-v3-OOP/blob/508d3c610ccc9076753bdc81151a5e8d76871a3e/src/Controller/UserController.php#L93
The tier parameter is therefore returned with the wrong Content-Type (text/html).
I have been able to verify the existance of the XSS.
Note that you can bypass the '\' added to both " & / by using comments such as:
## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Deploy to a test instance
  2. Create one admin user with correct api key filled in the database
  3. the /users/[id]/set_tier "tier" POST parameter is vulnerable to XSS injection.

## Supporting Material/References:


  * Selection_033.png =>burp capture attached

## Impact

Reflected cross site scripting should be fixed, as an user might be able to steal cookies/escalate privileges.

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
