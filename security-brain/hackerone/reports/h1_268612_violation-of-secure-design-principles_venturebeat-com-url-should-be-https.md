---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '268612'
original_report_id: '268612'
title: Venturebeat.com URL should be HTTPS
weakness: Violation of Secure Design Principles
team_handle: legalrobot
created_at: '2017-09-15T11:28:48.816Z'
disclosed_at: '2017-10-20T05:50:06.300Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: www.legalrobot-test.com
asset_type: URL
max_severity: none
tags:
- hackerone
- violation-of-secure-design-principles
---

# Venturebeat.com URL should be HTTPS

## Metadata

- HackerOne Report ID: 268612
- Weakness: Violation of Secure Design Principles
- Program: legalrobot
- Disclosed At: 2017-10-20T05:50:06.300Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

This is just for the awareness to use HTTPS everywhere, even for outgoing links - where it's possible.
 
##Navigate to:

         https://www.legalrobot-uat.com/

Example page (In the lower part where you find the observer.com Link):

observer redirect to HTTPS after click, but cookie is sent on the network before that.

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
