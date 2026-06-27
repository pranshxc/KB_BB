---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146314'
original_report_id: '146314'
title: Deny access to download.nextcloud.com + folders
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2016-06-21T21:16:58.318Z'
disclosed_at: '2016-06-21T21:36:20.339Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Deny access to download.nextcloud.com + folders

## Metadata

- HackerOne Report ID: 146314
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2016-06-21T21:36:20.339Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

hi,
you should to deny access here: https://download.nextcloud.com/ + all folders because everyone can see your files on the server.

this is not a bug, but it's important to keep secret your files.


to resolve this issue:
In an .htaccess file you need to use:
Deny from  all


regards
armfox97

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
