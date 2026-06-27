---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '360797'
original_report_id: '360797'
title: Authenticated reflected XSS on liberapay.com via the back_to parameter when
  leaving a team.
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: liberapay
created_at: '2018-06-01T13:46:52.416Z'
disclosed_at: '2018-06-02T13:18:47.669Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Authenticated reflected XSS on liberapay.com via the back_to parameter when leaving a team.

## Metadata

- HackerOne Report ID: 360797
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: liberapay
- Disclosed At: 2018-06-02T13:18:47.669Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

###Poc :

<https://en.liberapay.com/jio/membership/leave?back_to=http://example.com/>

Click the cancel button its redirect to 3rd party site.


Regards,
techguy

## Impact

This vulnerability could redirect users to the attackers websites for phishing attacks.

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
