---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1210458'
original_report_id: '1210458'
title: Serverinfo endpoints are not bruteforce protected nor are tokens properly generated
team_handle: nextcloud
created_at: '2021-05-27T10:48:41.001Z'
disclosed_at: '2021-06-16T08:39:22.233Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: nextcloud/serverinfo
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Serverinfo endpoints are not bruteforce protected nor are tokens properly generated

## Metadata

- HackerOne Report ID: 1210458
- Weakness: 
- Program: nextcloud
- Disclosed At: 2021-06-16T08:39:22.233Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The serverinfo app allows accessing the endpoints also via a custom token.

https://github.com/nextcloud/serverinfo/blob/9ae9dde028a684e53a1b37c9ba8e964ffe42a97f/lib/Controller/ApiController.php#L121

The token is set/generated via
https://github.com/nextcloud/serverinfo/blob/9ae9dde028a684e53a1b37c9ba8e964ffe42a97f/templates/settings-admin.php#L341

## Impact

There is no bruteforce protection on this endpoint in general. So a attacker can just fire off request. Combine this with that they have to generate a token on their own (which is usually a lot weaker) and in a lot of cases obtaining acccess should not be horribly hard.

I'd recommend

1. Add bruteforce protection to the endpoint
2. Have a button in the UI to generate a proper long random string

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
