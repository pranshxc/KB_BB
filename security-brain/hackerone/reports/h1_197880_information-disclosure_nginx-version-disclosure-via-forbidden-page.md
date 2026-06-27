---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '197880'
original_report_id: '197880'
title: Nginx version disclosure via forbidden page
weakness: Information Disclosure
team_handle: yelp
created_at: '2017-01-12T16:56:58.119Z'
disclosed_at: '2017-11-21T18:28:30.178Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# Nginx version disclosure via forbidden page

## Metadata

- HackerOne Report ID: 197880
- Weakness: Information Disclosure
- Program: yelp
- Disclosed At: 2017-11-21T18:28:30.178Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

This information might help an attacker gain a greater understanding of the systems in use and potentially develop further attacks targeted at the specific version of Nginx.

Impact: 
An attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified.

Steps to reproduce: 
1. Go to ```https://engineeringblog.yelp.com/images/previews/```
2. Now the nginx version: ```nginx/1.11.3```  shows in bottom of the error page.

I hope this will fixed soon :)) 

Have a nice day guys,
~Ry

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
