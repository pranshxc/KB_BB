---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '272863'
original_report_id: '272863'
title: External links should be served in HTTPS.
weakness: Violation of Secure Design Principles
team_handle: legalrobot
created_at: '2017-09-29T01:50:00.238Z'
disclosed_at: '2017-10-19T20:47:54.321Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
asset_identifier: www.legalrobot.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- violation-of-secure-design-principles
---

# External links should be served in HTTPS.

## Metadata

- HackerOne Report ID: 272863
- Weakness: Violation of Secure Design Principles
- Program: legalrobot
- Disclosed At: 2017-10-19T20:47:54.321Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

#Summary:

This is just for the awareness to use HTTPS everywhere, even for outgoing links - where it's possible.

Treat this report with some salt, not as in hashes.

#Navigate to:

https://www.legalrobot.com/events/2017/06/12/ICAIL/

Some of the External Links on that Page redirects to HTTPS after click, but cookie is sent on the network before that.

See the Previous Reports:
https://hackerone.com/reports/260591

See the Attached Image.

Best Regards,
Anees Khan

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
