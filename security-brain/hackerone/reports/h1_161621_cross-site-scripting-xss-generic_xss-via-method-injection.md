---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161621'
original_report_id: '161621'
title: XSS Via Method injection
weakness: Cross-site Scripting (XSS) - Generic
team_handle: gratipay
created_at: '2016-08-20T14:02:47.376Z'
disclosed_at: '2016-09-01T11:43:56.356Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS Via Method injection

## Metadata

- HackerOne Report ID: 161621
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: gratipay
- Disclosed At: 2016-09-01T11:43:56.356Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi guys

i found a low risk vuln , when you request a page on gratipay.com with uncommon Method , the server responds with error message .

Invalid Method 'Invalid HTTP method:TTEGETTT
with out escaping chars 

so when you inject an html element with method you can trigger an XSS .


Steps to reproduce  
- make an http request with a method  like this 
<img|src='3'|onerror=alert(3)/>



Fix :
you should validate the method value before printing it back in responses

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
