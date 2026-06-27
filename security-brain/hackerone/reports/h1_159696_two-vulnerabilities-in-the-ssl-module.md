---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159696'
original_report_id: '159696'
title: Two vulnerabilities in the ssl module
team_handle: ibb
created_at: '2016-08-16T09:41:04.755Z'
disclosed_at: '2019-11-12T09:01:44.536Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
asset_identifier: Python (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# Two vulnerabilities in the ssl module

## Metadata

- HackerOne Report ID: 159696
- Weakness: 
- Program: ibb
- Disclosed At: 2019-11-12T09:01:44.536Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I found two vulnerabilities in python's ssl module. 

The first is a Py_XDECREF call on an object which isn't owned, leading to use-after-free and/or double free scenarios.
The second vulnerability is an uninitialized variable use. 
  
I described both issues in detail in a mail to the PSRT. The mail and fix for both issues is here:

https://bugs.python.org/issue27773

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
