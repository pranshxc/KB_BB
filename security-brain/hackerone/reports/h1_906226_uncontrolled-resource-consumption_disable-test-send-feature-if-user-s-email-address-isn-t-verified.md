---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '906226'
original_report_id: '906226'
title: disable test send feature if user's email address isn't verified
weakness: Uncontrolled Resource Consumption
team_handle: trycourier
created_at: '2020-06-23T16:04:24.378Z'
disclosed_at: '2020-06-30T00:28:18.131Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: api.trycourier.app
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# disable test send feature if user's email address isn't verified

## Metadata

- HackerOne Report ID: 906226
- Weakness: Uncontrolled Resource Consumption
- Program: trycourier
- Disclosed At: 2020-06-30T00:28:18.131Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
There is no mechanism to limit the request in places while send the preview email

## Steps To Reproduce:
There is a weak account registration process, which allow user to register and login without any email confirmation.
L'say say for example that i'm the user A that want to send a phishing email or perform DOS against a targeted user

  1. Registration process by using the victim email address
  2. Craft the email example 
  3. Proced with the sent to me functionality to try the email send
  4. Intercept the request with a Proxy (Burp)
  5. Resend the request any times you want 

## Supporting Material/References:

CWE-400: Uncontrolled Resource Consumption
https://cwe.mitre.org/data/definitions/400.html

Below i have attached the evidence for the POC

## Impact

The most common result of resource exhaustion is denial of service.

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
