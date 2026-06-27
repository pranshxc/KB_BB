---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1192159'
original_report_id: '1192159'
title: public webdav endpoint not bruteforce protected
team_handle: nextcloud
created_at: '2021-05-11T14:23:29.678Z'
disclosed_at: '2021-08-11T09:19:29.295Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# public webdav endpoint not bruteforce protected

## Metadata

- HackerOne Report ID: 1192159
- Weakness: 
- Program: nextcloud
- Disclosed At: 2021-08-11T09:19:29.295Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Again related to https://hackerone.com/reports/1173684

I am having some trouble finding the code.
However if you do

```
curl -u "RANDOM1:RANDOM2" -X PROPFIND https://server/public.php/webdav
```

And then check your `oc_bruteforce_attempts` table. You'll see there is no entry registered.

## Impact

Low just like on the other report. But should be fixed non the less.

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
