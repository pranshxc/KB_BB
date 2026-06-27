---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '141676'
original_report_id: '141676'
title: Bime Unable to load Data Sources
weakness: Memory Corruption - Generic
team_handle: bime
created_at: '2016-05-28T12:08:35.151Z'
disclosed_at: '2016-06-27T21:31:53.263Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
tags:
- hackerone
- memory-corruption-generic
---

# Bime Unable to load Data Sources

## Metadata

- HackerOne Report ID: 141676
- Weakness: Memory Corruption - Generic
- Program: bime
- Disclosed At: 2016-06-27T21:31:53.263Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

The BIME unable to load the datasource, when user has created larger number of data source , and as a result it's throws error poppup and the __enduser can't do any thing, the entire PAGE got broken, can't delete any datasources__ which leads entire BIME functionality broken

__This is Error Popup Message__ Attached the screenshot FYR
```
An Error Occurred 
```

Steps to Reproduce 
login to  my BIME __https://document.bime.io__ with my credentials
```
anish2good@yahoo.co.in
Document@123
```
Click on Data sources as result you can see the Error Popup

Once Confirm the Vulnerability, I will change my password

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
