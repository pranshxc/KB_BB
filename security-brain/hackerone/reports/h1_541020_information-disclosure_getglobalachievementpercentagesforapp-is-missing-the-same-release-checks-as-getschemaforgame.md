---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '541020'
original_report_id: '541020'
title: GetGlobalAchievementPercentagesForApp is missing the same release checks as
  GetSchemaForGame
weakness: Information Disclosure
team_handle: valve
created_at: '2019-04-17T08:05:52.286Z'
disclosed_at: '2020-02-19T23:28:10.645Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: api.steampowered.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# GetGlobalAchievementPercentagesForApp is missing the same release checks as GetSchemaForGame

## Metadata

- HackerOne Report ID: 541020
- Weakness: Information Disclosure
- Program: valve
- Disclosed At: 2020-02-19T23:28:10.645Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

`GetGlobalAchievementPercentagesForApp` API method can be used to reveal achievement names/percentages for games that have not been released yet.

This is not a problem with `GetSchemaForGame` method, which leads me to believe the other method is missing all the relevant checks.

https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v2/?gameid=██████
https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v1/?appid=████

`GetGlobalAchievementPercentagesForApp` should have the same release state checks as `GetSchemaForGame` as to not leak achievement names.

## Impact

This can be used to reveal and leak work-in-progress achievements for games that have not been released yet.

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
