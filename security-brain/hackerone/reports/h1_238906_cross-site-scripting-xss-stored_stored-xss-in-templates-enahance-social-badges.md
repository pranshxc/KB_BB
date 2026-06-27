---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '238906'
original_report_id: '238906'
title: Stored XSS in Templates>Enahance>Social Badges
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mixmax
created_at: '2017-06-11T06:21:04.303Z'
disclosed_at: '2017-06-16T17:23:31.500Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in Templates>Enahance>Social Badges

## Metadata

- HackerOne Report ID: 238906
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mixmax
- Disclosed At: 2017-06-16T17:23:31.500Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, just like the report #237927, I found stored XSS in Templates>Enhance> Social Badges section.

1. Go to templates section and click on one of your templates.
2. Enhance> Social Badges.
3. Enter the payload: javascript:alert(1) in any of the social networking button url.
4. You'll see that the xss is being triggered.

Note: The similar social sections in Call to Action button are not accepting this payload, so but this is not fixed in Social Badges section.

Thanks.

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
