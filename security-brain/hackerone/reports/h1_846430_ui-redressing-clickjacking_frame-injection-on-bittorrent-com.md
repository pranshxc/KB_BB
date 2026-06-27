---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '846430'
original_report_id: '846430'
title: frame injection on bittorrent.com
weakness: UI Redressing (Clickjacking)
team_handle: btfs
created_at: '2020-04-10T13:03:26.405Z'
disclosed_at: '2020-05-05T20:51:13.700Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
tags:
- hackerone
- ui-redressing-clickjacking
---

# frame injection on bittorrent.com

## Metadata

- HackerOne Report ID: 846430
- Weakness: UI Redressing (Clickjacking)
- Program: btfs
- Disclosed At: 2020-05-05T20:51:13.700Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi team,
headers.php is injectable.

you can see on IE browsers.

FULL URL : https://www.bittorrent.com/scripts/site/headers.php?_=1586521900793&callback=%3ciframe%20src%3d%22http%3a%2f%2fgoogle.com%2f%3f%22%3e%3c%2fiframe%3e

## Impact

fix them

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
