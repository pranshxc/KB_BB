---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '149154'
original_report_id: '149154'
title: Stored xss
weakness: Cross-site Scripting (XSS) - Generic
team_handle: algolia
created_at: '2016-07-04T09:19:09.496Z'
disclosed_at: '2016-08-03T14:55:35.760Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 41
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored xss

## Metadata

- HackerOne Report ID: 149154
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: algolia
- Disclosed At: 2016-08-03T14:55:35.760Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi ,i have found an xss issue here : https://www.algolia.com/explorer#?index=test&tab=ranking
Steps to reproduce :
1-Go to : https://www.algolia.com/explorer#?index=test&tab=ranking
2-At the Attributes to index add this script  :`"><img src=x onerror=prompt('XSS');> ` and press enter .
3-Click save 
You will see that the xss has been fired .
You can go to https://www.algolia.com/explorer#?index=test&tab=ranking again you will see that xss is fired again .

Thanks ,
Saleh

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
