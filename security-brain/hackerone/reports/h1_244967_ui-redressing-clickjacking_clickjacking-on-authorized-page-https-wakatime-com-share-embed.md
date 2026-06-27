---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '244967'
original_report_id: '244967'
title: Clickjacking on authorized page https://wakatime.com/share/embed
weakness: UI Redressing (Clickjacking)
team_handle: wakatime
created_at: '2017-07-01T02:53:51.505Z'
disclosed_at: '2017-07-05T06:21:31.084Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking on authorized page https://wakatime.com/share/embed

## Metadata

- HackerOne Report ID: 244967
- Weakness: UI Redressing (Clickjacking)
- Program: wakatime
- Disclosed At: 2017-07-05T06:21:31.084Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hii,
https://wakatime.com/share/embed is vulnerabel to clickjaking.
Description:
I found the resource on https://wakatime.com/share/embed, which can be vulnerable to the Clickjacking.

Impact
The resource without X-Frame-Options potentially vulnerable to the Clickjacking. The vulnerability exist only for authenticated users (possible UI redressing in the Dashboard).As it is on a authenticated page so a attacker make many benefits of it and can click jack any user

Step-by-step Reproduction Instructions

Go to the https://wakatime.com/share/embed
Look to the response headers. or Create .html file with next content: <iframe src="https://wakatime.com/share/embed"></iframe>

Suggested Mitigation/Remediation Actions
Adding X-Frame-Options: DENY header will solve this problem.

Thnx plzz review it and fix as soon as possible.

Regards Piyush kumar

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
