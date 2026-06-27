---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '387007'
original_report_id: '387007'
title: '[idp.fr.cloud.gov] Open Redirect'
weakness: Open Redirect
team_handle: gsa_bbp
created_at: '2018-07-26T04:18:20.909Z'
disclosed_at: '2018-11-01T18:49:53.069Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: idp.fr.cloud.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# [idp.fr.cloud.gov] Open Redirect

## Metadata

- HackerOne Report ID: 387007
- Weakness: Open Redirect
- Program: gsa_bbp
- Disclosed At: 2018-11-01T18:49:53.069Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Description:** Open Redirect

**Domain:** idp.fr.cloud.gov

**Steps To Reproduce:**
Open URL:
```
https://idp.fr.cloud.gov//blackfan.ru/..;/css
```

**HTTP Response**
```
HTTP/1.1 302 Found
...
Location: //blackfan.ru/..;/css/
...
```

## Impact

A web application accepts a user-controlled input that specifies a link to an external site, and uses that link in a Redirect. This simplifies phishing attacks.

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
