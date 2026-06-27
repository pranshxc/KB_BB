---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1040533'
original_report_id: '1040533'
title: '[intensedebate.com] XSS Reflected POST-Based'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: automattic
created_at: '2020-11-22T12:04:54.180Z'
disclosed_at: '2021-01-15T21:20:46.577Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 42
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [intensedebate.com] XSS Reflected POST-Based

## Metadata

- HackerOne Report ID: 1040533
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: automattic
- Disclosed At: 2021-01-15T21:20:46.577Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello, i have found a XSS Reflected POST-Based in `https://www.intensedebate.com/ajax.php`.

Vulnerable(s) URL :

```POST /https://www.intensedebate.com/ajax.php```

Vulnerable(s) Parameter(s):

```
$_POST['txt'];
```

Payload

```
azertyuiop<<><img+src="x"/onerror="prompt(document.cookie)">
```

##Steps to reproduce
1. Open the xss.html and will you see a javascript pop-up

You can  also follow me into the video POC.

Thank you, good bye.

## Impact

A attacker can perform a phishing attack or perform a CORS attack

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
