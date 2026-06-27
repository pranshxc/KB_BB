---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '791293'
original_report_id: '791293'
title: Modify Host Header which is sent to email
weakness: Code Injection
team_handle: endless_group
created_at: '2020-02-08T18:40:32.664Z'
disclosed_at: '2020-02-12T12:24:39.537Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 30
asset_identifier: (*).theendlessweb.com
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- code-injection
---

# Modify Host Header which is sent to email

## Metadata

- HackerOne Report ID: 791293
- Weakness: Code Injection
- Program: endless_group
- Disclosed At: 2020-02-12T12:24:39.537Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Modify host header and include the fake website in password reset email.  Password reset mail is taking source domain from request header host, which can be modified using burp suite and the modified link is sent to the victims email

## Steps To Reproduce:

  1. Go to  https://da.theendlessweb.com:2222/
  2. Start burp suite
  3. Enter username and click on Send me a Link
  4. Intercep the request and modify the URL to some other custom url
  5. Forward the modified request
  6. Password reset email will be sent.
  7. Check your email and you will see the new url (which was configured in step 4) in the email.

## Supporting Material/References:

  * Snapshots in attachment

## Impact

With this, attacker can make any victim to visit their custom website and can affect the victim in many ways

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
