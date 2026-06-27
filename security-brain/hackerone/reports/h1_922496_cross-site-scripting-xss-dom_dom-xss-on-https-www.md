---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '922496'
original_report_id: '922496'
title: DOM XSS on https://www.███████
weakness: Cross-site Scripting (XSS) - DOM
team_handle: deptofdefense
created_at: '2020-07-13T12:09:37.953Z'
disclosed_at: '2020-09-29T20:35:16.978Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM XSS on https://www.███████

## Metadata

- HackerOne Report ID: 922496
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: deptofdefense
- Disclosed At: 2020-09-29T20:35:16.978Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#Description
DOM XSS can be achieved due to missing sanitation  when setting the source of an iframe.

#POC
1. Visit https://www.████frame.html#javascript:alert(document.domain)
2. View alert

#Vulnerable Code
```javascript
function Load()
{
	str=document.location.hash,idx=str.indexOf('#')
	if(idx>=0) str=str.substr(1);
	if(str) PPTSld.location.replace(str);
}
```

## Impact

An attacker could execute arbitrary javascript on another user.

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
