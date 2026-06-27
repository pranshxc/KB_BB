---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '761573'
original_report_id: '761573'
title: Cross-Site Scripting through search form on mtnplay.co.zm
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mtn_group
created_at: '2019-12-19T10:13:18.267Z'
disclosed_at: '2021-06-08T05:40:47.001Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 38
asset_identifier: mtnplay.co.zm
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross-Site Scripting through search form on mtnplay.co.zm

## Metadata

- HackerOne Report ID: 761573
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mtn_group
- Disclosed At: 2021-06-08T05:40:47.001Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
There is a XSS vulnerability that can be triggered through a search form on mtnplay.co.zm

## Steps To Reproduce:
  1. Navigate to http://www.mtnplay.co.zm/smart/jqm.aspx
  2. Click on the search button (or go to this link: http://www.mtnplay.co.zm/smart/jqm.aspx?event=search&mnu=search&ctrlid=92)
  3. Click on the filter button 
  4. The XSS can be triggered in any field of that form by inputting a javascript payload (Track/Album/Artist)

## Demonstration: 
https://www.youtube.com/watch?v=doLHsUqnvgE

## Impact

Malicious javascript code can be injected into the application

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
