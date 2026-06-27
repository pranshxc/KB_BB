---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '233402'
original_report_id: '233402'
title: Possible Subdomain Takeover
weakness: Insufficiently Protected Credentials
team_handle: mixmax
created_at: '2017-05-30T21:50:10.773Z'
disclosed_at: '2017-05-31T03:24:37.053Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- insufficiently-protected-credentials
---

# Possible Subdomain Takeover

## Metadata

- HackerOne Report ID: 233402
- Weakness: Insufficiently Protected Credentials
- Program: mixmax
- Disclosed At: 2017-05-31T03:24:37.053Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

None of the weakness categories really fit this so I apologize for that.

The subdomain `sales.mixmax.com` points to `151.101.16.229`, a `webflow.io` proxy server. Because it 404s, this leads me to believe that a subdomain takeover is possible through the webflow service as whatever this is pointing to is unused. 

Due to odd DNS configurations I'm not 100% sure on this but thought I'd make you aware just in case.

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
