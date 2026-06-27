---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '119494'
original_report_id: '119494'
title: Full Path Disclosure In EasyDB
weakness: Information Disclosure
team_handle: paragonie
created_at: '2016-02-29T17:26:30.545Z'
disclosed_at: '2017-10-16T05:53:39.984Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- information-disclosure
---

# Full Path Disclosure In EasyDB

## Metadata

- HackerOne Report ID: 119494
- Weakness: Information Disclosure
- Program: paragonie
- Disclosed At: 2017-10-16T05:53:39.984Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

as reported in #115337
about a full path disclosure in EasyDB

you fixed some of them in last commits
but `single` function is vulnerable too and not fixed yet!

    if(count($params) != count($params,COUNT_RECURSIVE)){
                throw new \InvalidArgumentException("Invalid params");
    }
this will check $params to be 1d array,
add this code before line 366 in EasyDB.php


Regards

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
