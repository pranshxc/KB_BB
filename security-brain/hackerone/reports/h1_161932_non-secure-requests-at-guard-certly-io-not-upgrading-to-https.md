---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161932'
original_report_id: '161932'
title: Non secure requests at guard.certly.io not upgrading to https
team_handle: certly
created_at: '2016-08-21T13:59:29.494Z'
disclosed_at: '2016-10-05T16:42:17.149Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
---

# Non secure requests at guard.certly.io not upgrading to https

## Metadata

- HackerOne Report ID: 161932
- Weakness: 
- Program: certly
- Disclosed At: 2016-10-05T16:42:17.149Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The issue is of http requests not upgrading to https at before mentioned domain.
Thus can allow an attack to steal important info like credentials and all other type of info.

Your domain is hsts preloaded so automatically upgraded to https , but the browsers who don't have this mentioned support like safari can allow attack.
Steps:
1. Go to http://guard.certly.io( in safari or Firefox hsts off manually).
2.go to sign in page.
3.no https enforced.
   The attack is very similar to the https://hackerone.com/reports/158186 , so you can follow that for further 
Impact.

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
