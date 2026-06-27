---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1504410'
original_report_id: '1504410'
title: XSS via Mod Log Removed Posts
weakness: Cross-site Scripting (XSS) - Stored
team_handle: reddit
created_at: '2022-03-09T00:56:21.748Z'
disclosed_at: '2022-03-10T23:18:17.088Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 206
asset_identifier: www.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS via Mod Log Removed Posts

## Metadata

- HackerOne Report ID: 1504410
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: reddit
- Disclosed At: 2022-03-10T23:18:17.088Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I have discovered an XSS vulnerability regarding the mod notes feature. Specifically, the XSS payload executes when the victim removes a post in a subreddit and opens up the mod notes of the attacker.

## Steps To Reproduce:

1. The attacker creates a new post with the title containing the XSS payload.
2. The victim (mods of the subreddit) then must remove your post.
3. The payload executes when a victim (subreddit mod) opens up your mod notes. Sometimes, the mod notes are displayed when the victim hovers on your profile (this is true when a recent mod action has been taken on the user). 

## Supporting Material/References:

█████
█████

## Impact

Impact Below:

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
