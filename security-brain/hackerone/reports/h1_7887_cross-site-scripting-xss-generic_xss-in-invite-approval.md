---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7887'
original_report_id: '7887'
title: XSS in invite approval
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localize
created_at: '2014-04-17T19:07:27.982Z'
disclosed_at: '2014-04-18T01:07:14.874Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in invite approval

## Metadata

- HackerOne Report ID: 7887
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localize
- Disclosed At: 2014-04-18T01:07:14.874Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

If a translator's name is set as “><svg onload="prompt(/xss/);"> and requests to join a project, and the project admin clicks on the review to accept it, it results in an xss.

Screen:
attacker/translator:
http://prntscr.com/3ax1ca

contributor/admin:
http://prntscr.com/3ax1ix

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
