---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1355537'
original_report_id: '1355537'
title: Script breaking tag (Forces website to render blank) (Informative)
weakness: Unchecked Error Condition
team_handle: xvideos
created_at: '2021-09-30T16:08:45.937Z'
disclosed_at: '2021-10-23T14:50:08.754Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 33
asset_identifier: www.xvideos.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- unchecked-error-condition
---

# Script breaking tag (Forces website to render blank) (Informative)

## Metadata

- HackerOne Report ID: 1355537
- Weakness: Unchecked Error Condition
- Program: xvideos
- Disclosed At: 2021-10-23T14:50:08.754Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
This is a bug affecting core HTML and JS elements on the site via Search 

## Steps To Reproduce:


  1. Open https://www.xvideos.com
  2. Click to search enter payload=  "<!--<script>" (without quotes) 
  3. Hit enter or search, watch the page break and not load any content (content is loaded in console, renders page blank) 

To note this can possibly be expanded to XSS or another injection type.

xvideobroken2.png shows the HTML content cut off in the source of the page. 

## Supporting Material/References:


F1466873: xvideobroken.PN
F1466876: xvideobroken2.PNG

## Impact

Breaks page rendering due to broken JS (Script and HTML close tags) Seems to render the website inoperable. Also seems to hang and causes memory leak due to trying to constantly load content it can't.

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
