---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '686015'
original_report_id: '686015'
title: Administrator access to staging.railto.com
team_handle: railto
created_at: '2019-09-01T16:13:57.433Z'
disclosed_at: '2019-10-03T00:36:05.480Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 66
asset_identifier: '*.railto.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Administrator access to staging.railto.com

## Metadata

- HackerOne Report ID: 686015
- Weakness: 
- Program: railto
- Disclosed At: 2019-10-03T00:36:05.480Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hey team,

While doing some recon for railto sub-domains. i came across a most critical bug which lets me complete access of https://staging.railto.com. i can add anything and removing anythings as i got the ADMIN level privilege. 

##Steps
  1. Go to https://staging.railto.com/admin  url.
  2. Set username as admin and password as password to login the admin page. Since password is too easy to guess, i was like what... after finding this bug.
  3. If unauthorized people has got this bug then he could use it in a bad way.
I didn't want to move forward because i am not an admin of this page and i dont want you guys in trouble.  If it is not enough then i will provide a detail poc

## Impact

Admin of the page is simple enough.

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
