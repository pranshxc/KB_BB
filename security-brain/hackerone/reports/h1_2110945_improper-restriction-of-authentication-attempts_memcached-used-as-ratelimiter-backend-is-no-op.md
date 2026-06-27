---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2110945'
original_report_id: '2110945'
title: Memcached used as RateLimiter backend is no-op
weakness: Improper Restriction of Authentication Attempts
team_handle: nextcloud
created_at: '2023-08-15T16:38:47.878Z'
disclosed_at: '2023-11-12T08:06:18.886Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Memcached used as RateLimiter backend is no-op

## Metadata

- HackerOne Report ID: 2110945
- Weakness: Improper Restriction of Authentication Attempts
- Program: nextcloud
- Disclosed At: 2023-11-12T08:06:18.886Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
When Memcached is used as backend:
https://github.com/nextcloud/server/blob/c705b8fcb3de7910e67cd2ed2d2b38653f58962a/lib/private/Server.php#L787-L799

The following code block is problematic:
https://github.com/nextcloud/server/blob/90104bc1c448c6da2fd3e052fca75bb3fb261c87/lib/private/Memcache/Memcached.php#L135-L139

I guess we need to check the actual cache type and use the DB backend when Memcached is used?

## Impact

Any action that partly resets any cache entry will wipe rate limit attempts and future bruteforce protection (with https://github.com/nextcloud/server/pull/39870 )

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
