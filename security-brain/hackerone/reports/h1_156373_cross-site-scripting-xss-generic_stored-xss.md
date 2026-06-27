---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '156373'
original_report_id: '156373'
title: Stored xss
weakness: Cross-site Scripting (XSS) - Generic
team_handle: algolia
created_at: '2016-08-03T20:56:27.457Z'
disclosed_at: '2016-09-07T12:14:22.510Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored xss

## Metadata

- HackerOne Report ID: 156373
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: algolia
- Disclosed At: 2016-09-07T12:14:22.510Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,i have found an stored xss which is reflected at https://www.algolia.com/explorer#?index=getstarted_actors&tab=explorer

Steps to produce:
1) Go to https://www.algolia.com/explorer#?index=getstarted_actors&tab=explorer and add "><img src=x onerror=alert(document.cookie);> as an attribute and keep it at top as in screenshot1

2) Go to  https://www.algolia.com/explorer#?index=getstarted_actors&tab=ranking and take the cursor on the ranking info(the trophy icon),and you will see a pop up alert of xss. (Screenshot2)
 I have tested it on Chrome and firefox its works on both.


P.S: I dont know why but my ip got banned when i was uploading the script to test could you unban me?

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
