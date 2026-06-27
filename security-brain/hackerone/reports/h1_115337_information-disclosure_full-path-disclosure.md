---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '115337'
original_report_id: '115337'
title: Full Path Disclosure
weakness: Information Disclosure
team_handle: paragonie
created_at: '2016-02-08T07:19:36.004Z'
disclosed_at: '2016-03-09T14:41:24.320Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# Full Path Disclosure

## Metadata

- HackerOne Report ID: 115337
- Weakness: Information Disclosure
- Program: paragonie
- Disclosed At: 2016-03-09T14:41:24.320Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi

as reported in email,
there is a full path disclosure in EasyDB

you fixed some of them in last commit
add this code before and "execute($params)" function call!

    if(count($params) != count($params,COUNT_RECURSIVE)){
                throw new \InvalidArgumentException("Invalid params");
    }

this will check $params to be 1d array,


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
