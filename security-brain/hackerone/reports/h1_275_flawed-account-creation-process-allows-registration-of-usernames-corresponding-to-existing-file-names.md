---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '275'
original_report_id: '275'
title: Flawed account creation process allows registration of usernames corresponding
  to existing file names
team_handle: security
created_at: '2013-11-07T10:39:04.352Z'
disclosed_at: '2015-06-08T11:39:31.040Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
---

# Flawed account creation process allows registration of usernames corresponding to existing file names

## Metadata

- HackerOne Report ID: 275
- Weakness: 
- Program: security
- Disclosed At: 2015-06-08T11:39:31.040Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The account creation process allows to set up account names corresponding to names of server ressources, e.g. I just successfully created an account robots.txt which results in a profile path of https://hackerone.com/robots.txt and results in an bugged account as accessing account settings etc is impossible.

I'd recommend moving away from filtering names and from profiles being available directly under .com/ and changing it to something more reliable like .com/users/profilename

The robots.txt account can be deleted. I only created it for testing purpose.

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
