---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '237927'
original_report_id: '237927'
title: Stored XSS templates -> 'call for action' feature
team_handle: mixmax
created_at: '2017-06-08T08:04:58.056Z'
disclosed_at: '2017-06-09T17:41:09.049Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
---

# Stored XSS templates -> 'call for action' feature

## Metadata

- HackerOne Report ID: 237927
- Weakness: 
- Program: mixmax
- Disclosed At: 2017-06-09T17:41:09.049Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Jeff,

Reporting the Stored XSS in template section on 'call for action' button. (Already discussed in mail)
1] Login to Mixmax and navigate to template section
2] Click on enhance and select call for action button
3] Enter anything in button text and in URL enter XSS payload (javascript:alert(document.cookie))
4] Insert the button and click it to execute XSS.

Impact : XSS can be stored in template and when Team manager/admin uses that template and clicks the button , our XSS executes 

Thank you

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
