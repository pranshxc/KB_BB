---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '594080'
original_report_id: '594080'
title: Privilege escalation allows to use iframe functionality w/o upgrade
weakness: Privilege Escalation
team_handle: infogram
created_at: '2019-06-02T17:09:25.032Z'
disclosed_at: '2019-06-05T08:03:55.287Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 31
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Privilege escalation allows to use iframe functionality w/o upgrade

## Metadata

- HackerOne Report ID: 594080
- Weakness: Privilege Escalation
- Program: infogram
- Disclosed At: 2019-06-05T08:03:55.287Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello team!

I've found a privilege escalation issue which allows to set iframes to the projects w/o upgrading.

### Steps to reproduce
- Login
- Navigate to the project
- Choose `integrations` and click the `IFrame`
- See that you'll get `upgrade now` notification
{F501019}
- Inspect the page with developer tool and choose the `upgrade` from `IFrame` icon
- Delete the `data-upgrade="true"` part
{F501023}
- Click the `IFrame` and see that you are able to add iframe to the page w/o upgrade
{F501024}


If you need any information please let me know.

Cheers!

## Impact

Users can use functionalities without paying

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
