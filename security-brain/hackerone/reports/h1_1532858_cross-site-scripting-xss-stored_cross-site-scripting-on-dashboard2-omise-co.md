---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1532858'
original_report_id: '1532858'
title: Cross-site scripting on dashboard2.omise.co
weakness: Cross-site Scripting (XSS) - Stored
team_handle: omise
created_at: '2022-04-06T21:18:50.534Z'
disclosed_at: '2022-05-24T11:54:30.797Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: dashboard2.omise.co
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Cross-site scripting on dashboard2.omise.co

## Metadata

- HackerOne Report ID: 1532858
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: omise
- Disclosed At: 2022-05-24T11:54:30.797Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Cross-site scripting (XSS) is an attack vector that injects malicious code into a vulnerable web application.
Stored XSS, also known as persistent XSS, is the more damaging of the two. It occurs when a malicious script is injected directly into a vulnerable web application.

Steps To Reproduce:
1. Log in to your account.
2. Visit https://dashboard.omise.co/test/settings 
3. Under Export - Specify the metadata that you want to include in your export option. Enter <script>alert(2)</script> in all four parameters including Charge, Transfer, Refund, Dispute.
4. Click on Update settings.
5. Click on Try our new dashboard, XSS will Trigger or log out and log in again, and XSS will Trigger.

POC:
Attached Video.

## Impact

Code injected into a vulnerable application can exfiltrate data or install malware on the user's machine. Attackers can masquerade as authorized users via session cookies, allowing them to perform any action allowed by the user account.

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
