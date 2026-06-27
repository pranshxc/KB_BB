---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1397804'
original_report_id: '1397804'
title: open redirect to a remote website which can phish users
weakness: Open Redirect
team_handle: concretecms
created_at: '2021-11-10T19:58:19.033Z'
disclosed_at: '2022-11-25T18:08:35.649Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: https://github.com/concrete5/concrete5
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- open-redirect
---

# open redirect to a remote website which can phish users

## Metadata

- HackerOne Report ID: 1397804
- Weakness: Open Redirect
- Program: concretecms
- Disclosed At: 2022-11-25T18:08:35.649Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

By Adding some extra headers in the request I noticed that  the user is redirected to a remote website. This can lead to stealing a user credentials (phishing) on a remote server.

These headers can be added either using a MITM attack or by chaining with another vulnerability such as request smuggling, header injection more commonly abusing a reverse proxy that sits in front of the website.

ps:crayons

## Impact

This can lead to stealing a user credentials (phishing) on a remote server or planting malware on the user's computer.

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
