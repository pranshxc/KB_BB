---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '565736'
original_report_id: '565736'
title: View HackerOne challenge scope before challenge begins
weakness: Forced Browsing
team_handle: security
created_at: '2019-05-04T03:23:37.586Z'
disclosed_at: '2019-07-11T15:45:34.907Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 47
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- forced-browsing
---

# View HackerOne challenge scope before challenge begins

## Metadata

- HackerOne Report ID: 565736
- Weakness: Forced Browsing
- Program: security
- Disclosed At: 2019-07-11T15:45:34.907Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** Hi team, I have come across an issue where I am able to view a HackerOne challenge scope before the challenge begins. The issue here being that I can get an understanding of what the in-scope assets are before a challenge starts, allowing myself to start researching and finding bugs to hold on to until the challenge begins.

You can see this by going to the challenge's `scope_versions` page before the challenge starts and the scope is still hidden: `https://hackerone.com/{challengeName}/scope_versions`

The program policy states the scope will be displayed at a later date
>Congratulations! You've been invited to participate in a HackerOne Challenge. More details around the scope, bounty structure, etc. will be available when the Challenge begins.

### Steps To Reproduce

1. If you have access to a HackerOne challenge (before it starts, while the scope is hidden), access that challenge's `scope_versions` page. The current one I have access to is: ███
2. Notice you can see the current scope, and scope history of this challenge, displaying the in-scope assets for the challenge prior to release.
██████

## Impact

This gives an unfair advantage to the researcher's identifying the scope, as they are able to see the in-scope assets for the challenge, allowing them to do recon and research before the scope is announced. Given the limited time for the challenge, this could be used to manipulate the results and gather bugs before the challenge begins.

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
