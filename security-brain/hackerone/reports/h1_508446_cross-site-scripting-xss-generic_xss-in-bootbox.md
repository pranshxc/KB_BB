---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '508446'
original_report_id: '508446'
title: XSS in Bootbox
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nodejs-ecosystem
created_at: '2019-03-12T13:44:08.840Z'
disclosed_at: '2019-05-04T16:52:39.177Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in Bootbox

## Metadata

- HackerOne Report ID: 508446
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2019-05-04T16:52:39.177Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi.  
  
Sorry for taking the time with this report.  
  
This is already publicly disclosed issue at -[https://github.com/makeusabrew/bootbox/issues/661](https://github.com/makeusabrew/bootbox/issues/661)  
  
In essence all dialogs of bootbox vulnurable to XSS injections ( bootbox.alert("\<script\>alert(1);\</script\>"); )  

This is apparently a feature to allow injecting HTML in messages but it is not very clear from the documentation.  
Even though this issue has been reported for a while no changes were made to fix this issue or even update the documentation

Kind Regards,  
Yoni

## Impact

Websites using bootbox to display messages containing user input are vulnerable to XSS

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
