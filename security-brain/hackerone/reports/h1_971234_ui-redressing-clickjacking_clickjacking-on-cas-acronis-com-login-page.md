---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '971234'
original_report_id: '971234'
title: Clickjacking on cas.acronis.com login page
weakness: UI Redressing (Clickjacking)
team_handle: acronis
created_at: '2020-08-31T13:45:40.449Z'
disclosed_at: '2020-11-03T09:10:26.593Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking on cas.acronis.com login page

## Metadata

- HackerOne Report ID: 971234
- Weakness: UI Redressing (Clickjacking)
- Program: acronis
- Disclosed At: 2020-11-03T09:10:26.593Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Steps To Reproduce:

    Create a new HTML file
Source code:
<!DOCTYPE HTML>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>I Frame</title>
</head>
<body>
<h2>Clickjacking Vulnerability</h2>
<iframe src="https://cas.acronis.com/" frameborder="0" height="700px" width="850px"></iframe>
</body>
</html>
 
    Save the file as whatever.html
    Open document in browser 

Reference: https://hackerone.com/reports/591432

FIX-
The vulnerability can be fixed by adding "frame-ancestors 'self';" to the CSP (Content-Security-Policy) header.
NOTE

Best Regards,
Dgirl

## Impact

Attacker may tricked user, sending them malicious link then user open it clicked some image and their account unconsciously has been deactivated

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
