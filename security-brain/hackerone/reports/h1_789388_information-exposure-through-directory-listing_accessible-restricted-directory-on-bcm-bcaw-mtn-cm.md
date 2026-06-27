---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '789388'
original_report_id: '789388'
title: Accessible Restricted directory on [bcm-bcaw.mtn.cm]
weakness: Information Exposure Through Directory Listing
team_handle: mtn_group
created_at: '2020-02-05T16:24:56.718Z'
disclosed_at: '2020-07-15T08:54:21.365Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: mtn.cm
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-exposure-through-directory-listing
---

# Accessible Restricted directory on [bcm-bcaw.mtn.cm]

## Metadata

- HackerOne Report ID: 789388
- Weakness: Information Exposure Through Directory Listing
- Program: mtn_group
- Disclosed At: 2020-07-15T08:54:21.365Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
* There are some exposed `directory/files` publicly accessible for anyone, when it should be restricted on the server

## Steps To Reproduce:
* Go to `http://bcm-bcaw.mtn.cm/wp-content/uploads/` and navigate between available folders

==**Poc:**== {F707036}

## Impact

>
* Every uploaded data can be accessible through this directory listing vulnerability
* This might include several private/confidential data
>

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
