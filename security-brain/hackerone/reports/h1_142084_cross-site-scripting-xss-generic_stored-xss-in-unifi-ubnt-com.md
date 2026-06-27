---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '142084'
original_report_id: '142084'
title: Stored XSS in unifi.ubnt.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: ui
created_at: '2016-05-30T16:37:07.967Z'
disclosed_at: '2016-11-26T19:37:56.762Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in unifi.ubnt.com

## Metadata

- HackerOne Report ID: 142084
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: ui
- Disclosed At: 2016-11-26T19:37:56.762Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Dear @ubnt-matt,

I've found a stored xss in unifi.ubnt.com

##Step to reproduce :##
```
Step 1: Login to unifi.ubnt.com
Step 2: Connect latest unifi controller with unifi.ubnt.com via cloud access.
Step 3: Create site with any name in that controller.
Step 4: Click on launch site in unifi.ubnt.com then you will again redirect to unifi.ubnt.com with controls.
Step 5: Create Network with xss payload "><img src=x onerror=prompt(document.cookie)>
Step 6: XSS will execute.
```

**Note : ** force WebRTC should we enable.

I've attached screenshot of the same.
let me know if you need more info.

Best Regard
Shubham

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
