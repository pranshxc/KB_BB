---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '134124'
original_report_id: '134124'
title: Stored self-XSS at m.uber.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-04-23T22:24:12.693Z'
disclosed_at: '2016-07-08T23:28:11.320Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored self-XSS at m.uber.com

## Metadata

- HackerOne Report ID: 134124
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-07-08T23:28:11.320Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

There is a stored self-XSS vulnerability at m.uber.com in displaying the uber invite code. If the user sets the invite code at `<script>alert(document.domain)</script>` value using the main personal area at the uber.com and then signs into the m.uber.com the XSS is fired.

Possible other user exploitation case can be the following:
The attacker sends messages to everyone with text:

```
I have worked at Uber and I know the secret invite code using by employees 
so invite friends using it gets you a $10000 discount for every invited friend. 
Set your invite code to this value:
EMPLOYEE_2016_04_oidkjnfkerjnoidkjnfkerjnoidkjnfkerjnoidkjnfkerjnoidkjnfkerjn<script>eval(atob('YWxlcnQoZG9jdW1lbnQuZG9tYWluKQ=='))</script>oidkjnfkerjnoidkjnfkerjnoidkjnfkerjnoidkjnfkerjnoidkjnfkerjn
```
The unlimited invite code length makes easier to hide a payload inside it. So user will set his invite code to this value and next time he will visit the m.uber.com the XSS will fire.

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
