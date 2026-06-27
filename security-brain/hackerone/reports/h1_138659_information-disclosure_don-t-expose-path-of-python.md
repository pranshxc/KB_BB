---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '138659'
original_report_id: '138659'
title: don't expose path of Python
weakness: Information Disclosure
team_handle: gratipay
created_at: '2016-05-13T16:29:06.675Z'
disclosed_at: '2016-05-13T20:49:41.685Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# don't expose path of Python

## Metadata

- HackerOne Report ID: 138659
- Weakness: Information Disclosure
- Program: gratipay
- Disclosed At: 2016-05-13T20:49:41.685Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Team,
While testing the web application I've found that if you enter the 3 or more strings including % then web application is exposing the path of Python in error.Application exposing path of Python in error when you enter the 3 or more strings including % .. if you only enter the 2 strings it will show you the 404 not found page

### POC : 
 
`https://gratipay.com/%ff/` [3 strings]  
**Request is undecodable.(/app/.heroku/python/lib/python2.7/encodings/utf_8.py:16)**

 
`https://gratipay.com/%f/` [ 2 strings] - **404 Not Found**

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
