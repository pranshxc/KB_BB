---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '475114'
original_report_id: '475114'
title: Github repo's wiki publicly editable
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2019-01-05T17:51:56.299Z'
disclosed_at: '2020-01-31T13:19:27.853Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-access-control-generic
---

# Github repo's wiki publicly editable

## Metadata

- HackerOne Report ID: 475114
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2020-01-31T13:19:27.853Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

Github repo's wiki page is publicly editable. This enables an attacker to edit the wiki pages of the affected repo's. Adding content that may link to malicious code libraries that would be installed and used by developers or information that may mislead users.

**POC link**
https://github.com/nextcloud/news-android/wiki
https://github.com/nextcloud/Android-SingleSignOn/wiki
https://github.com/nextcloud/weather/wiki

## Impact

This enables an attacker to edit the wiki pages of the affected repo's. Adding content that may link to malicious code libraries that would be installed and used by developers or information that may mislead users.

Thank you.

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
