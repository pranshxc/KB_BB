---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '191890'
original_report_id: '191890'
title: DOM Based XSS in Discourse Search
weakness: Cross-site Scripting (XSS) - Generic
team_handle: discourse
created_at: '2016-12-17T07:29:05.576Z'
disclosed_at: '2017-01-10T00:08:01.948Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 29
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# DOM Based XSS in Discourse Search

## Metadata

- HackerOne Report ID: 191890
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: discourse
- Disclosed At: 2017-01-10T00:08:01.948Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

###Steps to Reproduce:

1. Load http://try.discourse.org
2.Now From Top Right Corner Click on Search Button 
3. Enter payload their 

###Payload:

@<script>prompt(1337)</script>gmail.com

4: Now in new windows that opens click on advance search and The XSS will Occur :) 
5: Now copy the link and send to victim there the XSS will Occur To 

Thanks
Khizer Javed

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
