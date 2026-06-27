---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '126049'
original_report_id: '126049'
title: Cross-site Scripting (XSS)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-03-25T20:08:37.485Z'
disclosed_at: '2016-05-06T22:08:13.849Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross-site Scripting (XSS)

## Metadata

- HackerOne Report ID: 126049
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-05-06T22:08:13.849Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The website located at https://login.uber.com/applications suffers from a stored Cross-site Scripting (XSS) vulnerability.

Reproduction Steps:
Create a new application with name as the following vector, and try to delete the same app.

*Vector* : "><img src=x onerror=prompt(1)>

Note that the XSS payload has fired.

Possible Scenarios:
1. Attacker gets added as an admin or developer for an app
2. Adds an app with an XSS vector as a name
3. Victim sees the unusual app and attempts to delete it.


Or:

1. Attacker creates an app with XSS-y name
2. Adds victim as an admin
3. Victim joins the app and attempts to delete it

I’ve tested this in the latest Firefox and Chrome. 
Attached to this report is the screenshot of this issue occurring in Chrome.

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
