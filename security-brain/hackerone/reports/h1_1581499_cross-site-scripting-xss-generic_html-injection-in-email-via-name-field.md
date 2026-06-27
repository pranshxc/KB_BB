---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1581499'
original_report_id: '1581499'
title: HTML Injection in email via Name field
weakness: Cross-site Scripting (XSS) - Generic
team_handle: security
created_at: '2022-05-26T00:34:30.141Z'
disclosed_at: '2022-09-18T09:24:10.106Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 69
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HTML Injection in email via Name field

## Metadata

- HackerOne Report ID: 1581499
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: security
- Disclosed At: 2022-09-18T09:24:10.106Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Gents,
I would like to report an issue where attackers are able to inject HTML into the `Name` field at `app.qualified.dev`.

### Steps to reproduce:
1. Please register at https://app.qualified.dev/signup
2. Inject the `Name`field with any HTML payload.
3. Open the victim's test email, HTML will be executed.

### Proof of concept:
+ {F1744498}

## Impact

HTML Injection

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
