---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '897385'
original_report_id: '897385'
title: 2FA bypass by sending blank code
weakness: Improper Authentication - Generic
team_handle: glassdoor
created_at: '2020-06-13T08:41:22.866Z'
disclosed_at: '2020-07-02T13:40:30.885Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 277
asset_identifier: https://www.glassdoor.com/*
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# 2FA bypass by sending blank code

## Metadata

- HackerOne Report ID: 897385
- Weakness: Improper Authentication - Generic
- Program: glassdoor
- Disclosed At: 2020-07-02T13:40:30.885Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** █████████. This is a failure in null check of the entered code. In simple terms, the 2FA while logging in can be bypassed by sending a blank code. This could be because of incorrect comparison of entered code with true code. A pre-validation (may be null check) before comparing the codes would fix the issue

Affected URL or select Asset from In-Scope: Glassdoor 2FA
Affected Parameter: code
Vulnerability Type: Improper Authentication
Browsers tested: Browser independent

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1.  Login to Glassdoor and navigate to https://www.glassdoor.com/member/account/securitySettings_input.htm
  2. Enable 2FA
  3. Logout
  4. Login again and notice OTP is asked
  5. Now using Burp suite intercept the POST request by sending incorrect code. [Do not forward]
  6. Before forwarding the request to server, remove the code and forward
  7. Turnoff Intercept and notice that your login request has been fulfilled


## Supporting Material/References (screenshots, logs, videos):
* ███████

## Impact

2FA Protection bypass. Attacker could gain access despite the 2FA protection by victim

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
