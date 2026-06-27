---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '167206'
original_report_id: '167206'
title: Able to list user's public name, username, phone number, address, facebook
  ID...
weakness: Information Disclosure
team_handle: olx
created_at: '2016-09-09T19:33:31.359Z'
disclosed_at: '2018-12-17T22:21:51.918Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- information-disclosure
---

# Able to list user's public name, username, phone number, address, facebook ID...

## Metadata

- HackerOne Report ID: 167206
- Weakness: Information Disclosure
- Program: olx
- Disclosed At: 2018-12-17T22:21:51.918Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Through api-v2/items you can list all information of users (except email). As items are sequential, you can just make a script that crawls items from:

https://www.olx.com.ar/api-v2/items/822200000
to
https://www.olx.com.ar/api-v2/items/901858309

Example of sensible user information from random curl:
```
██████████
```
```
█████████
```

Example of random curl: 
```
$ curl https://www.olx.com.ar/api-v2/items/822200000
██████████
```

Let me know if you need anything else.

Cheers,
Luke.-

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
