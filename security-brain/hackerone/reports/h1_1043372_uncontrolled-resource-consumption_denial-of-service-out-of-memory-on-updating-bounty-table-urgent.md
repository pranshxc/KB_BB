---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1043372'
original_report_id: '1043372'
title: Denial Of Service (Out Of Memory) on Updating Bounty Table [Urgent]
weakness: Uncontrolled Resource Consumption
team_handle: security
created_at: '2020-11-25T11:25:38.691Z'
disclosed_at: '2021-02-02T20:06:13.293Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 83
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Denial Of Service (Out Of Memory) on Updating Bounty Table [Urgent]

## Metadata

- HackerOne Report ID: 1043372
- Weakness: Uncontrolled Resource Consumption
- Program: security
- Disclosed At: 2021-02-02T20:06:13.293Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

**Summary:**
There is a bug in Updating Bounty Table section causing Denial Of Service , specifically loading up the memory usage (Out Of Memory). This happens when you visit a corrupted bounty table of a target program.

I didn't figure out yet how this issue happened but I am reporting it now immediately because it affects all hackers who view the bounty table of  the target affected program.

**Description:**
The issue happened with me when I was clicking on a notification telling that `Clario has updated their bounty table`.
So I clicked on it to see the updated bounty table and suddenly my browser tab crashed and a message showed telling `Error code: Out Of Memory`.
I tried it from two hackerone accounts and they results with the same issue.

### Steps To Reproduce

1. Navigate to the notification: https://hackerone.com/clario/bounty_table_versions?nid=115515717&utm_campaign=user_652675&utm_content=team_url&utm_medium=email&utm_source=bounty_table_update
2. You will not be able to click on any button (Ex: profile or Inbox).
3.  After short while, Browser will crash.

### Optional: Your Environment (Browser version, Device, etc)
Google Chrome.

### Optional: Supporting Material/References (Screenshots)
Please see the attached image and quick video PoC

██████████

{F1093466}

### Optional: Did you use [recon data made available by HackerOne](https://github.com/Hacker0x01/helpful-recon-data) to find this vulnerability?

no

## Impact

Denial Of Service (Out Of Memory) - Crashing whole Browser (happened with me) and loading up computer resources (CPU and RAM).

Kind Regards.

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
