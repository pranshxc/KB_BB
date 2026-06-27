---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '38157'
original_report_id: '38157'
title: '[qiwi.com] Open Redirect'
weakness: Open Redirect
team_handle: qiwi
created_at: '2014-12-03T20:25:50.841Z'
disclosed_at: '2016-10-24T22:23:03.713Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- open-redirect
---

# [qiwi.com] Open Redirect

## Metadata

- HackerOne Report ID: 38157
- Weakness: Open Redirect
- Program: qiwi
- Disclosed At: 2016-10-24T22:23:03.713Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

PoC (Chrome):
https://qiwi.com/main.action#/\google.com/

Уязвимый фрагмент кода:
https://static.qiwi.com/js/qiwi_com/qiwi.min.js?v=3.3.9
if(this.wc.hash&&Aa(this.wc.hash,"#/"))return this.wc.href=this.wc.hash.substring(1).replace(/^\/+/,"/"),this;

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
