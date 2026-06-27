---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '194017'
original_report_id: '194017'
title: 'Open redirect - user interaction needed (verkkopalvelu.lahitapiola.fi/e2/..)
  - based on #179328'
weakness: Open Redirect
team_handle: localtapiola
created_at: '2016-12-26T07:58:58.529Z'
disclosed_at: '2020-07-06T17:06:10.094Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- open-redirect
---

# Open redirect - user interaction needed (verkkopalvelu.lahitapiola.fi/e2/..) - based on #179328

## Metadata

- HackerOne Report ID: 194017
- Weakness: Open Redirect
- Program: localtapiola
- Disclosed At: 2020-07-06T17:06:10.094Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello __Team__

>Open redirect in this report 
> is not totally fixed 

__Poc__ :-
1. Open this link
```
https://verkkopalvelu.lahitapiola.fi///example.com/%2f../e2/kotivakuutus/vakuutuslaskuri/#/
```
2. Wait for it to load
3. Click on sv
It loads to _example.com_

I tried it in android, crome

Regards
SANTHOSH

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
