---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '260299'
original_report_id: '260299'
title: observer.com URL should HTTPS
team_handle: legalrobot
created_at: '2017-08-15T12:07:23.223Z'
disclosed_at: '2017-09-14T21:09:28.853Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: www.legalrobot-test.com
asset_type: URL
max_severity: none
tags:
- hackerone
---

# observer.com URL should HTTPS

## Metadata

- HackerOne Report ID: 260299
- Weakness: 
- Program: legalrobot
- Disclosed At: 2017-09-14T21:09:28.853Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#Summary

This is just for the awareness to use HTTPS everywhere, even for outgoing links - where it's possible.
Treat this report with some salt, not as in hashes.

#Navigate to:

       https://www.legalrobot-uat.com/press/

Example page (In the lower part where you find the observer.com Link):

observer redirect to HTTPS after click, but cookie is sent on the network before that.

See my attached photo. {F212950}

Related Issue : #1093

Thanks!

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
