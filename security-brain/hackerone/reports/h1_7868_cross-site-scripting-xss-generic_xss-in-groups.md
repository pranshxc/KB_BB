---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7868'
original_report_id: '7868'
title: XSS in Groups
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localize
created_at: '2014-04-17T18:22:55.326Z'
disclosed_at: '2014-04-18T00:27:01.686Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in Groups

## Metadata

- HackerOne Report ID: 7868
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localize
- Disclosed At: 2014-04-18T00:27:01.686Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Visit the following link after logging in:
http://www.localize.io/pages/create_project/3D

Add a new group with an XSS string (as group name) and you will see the XSS execting.


String used:
<object data=data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoNCk+></object>?

Thanks,
Ben

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
