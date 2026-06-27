---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '284082'
original_report_id: '284082'
title: Javascript Payload reflected Back in Report Embed Code
weakness: Cross-site Scripting (XSS) - Stored
team_handle: infogram
created_at: '2017-10-30T07:13:24.858Z'
disclosed_at: '2017-12-12T14:53:09.069Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Javascript Payload reflected Back in Report Embed Code

## Metadata

- HackerOne Report ID: 284082
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: infogram
- Disclosed At: 2017-12-12T14:53:09.069Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1)Create new Report template 
2)Spoof its name with payload "></div> My Report <script type="text/javascript">alert(document.cookie);</script><div id="
3)Visit Back to your library list https://infogram.com/app/#/library
4)Select The Created report and click view on web,Click the Share Button
5)Copy & embed the code somewhere in html file you ll triage the Javascript exceution


The Payload is reflected in embed code and can compromise the embed code user's PRivacy.

Fix:Report/Project name need to be escaped properly

For reproduction of issue use:
https://infogram.com/greaterreport-classic-lessdivgreaterlessscriptgreateralerttestlessscriptgreater-1g0gmjzqk1y3p1q

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
