---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1472721'
original_report_id: '1472721'
title: IDOR at https://demo.sftool.gov/TwsHome/ScorecardManage/ via scorecard name
weakness: Improper Access Control - Generic
team_handle: gsa_vdp
created_at: '2022-02-06T18:56:17.559Z'
disclosed_at: '2022-03-17T16:23:22.721Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: demo.sftool.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# IDOR at https://demo.sftool.gov/TwsHome/ScorecardManage/ via scorecard name

## Metadata

- HackerOne Report ID: 1472721
- Weakness: Improper Access Control - Generic
- Program: gsa_vdp
- Disclosed At: 2022-03-17T16:23:22.721Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

I have found a broken access control vulnerability on https://demo.sftool.gov/ under your /tws directory. 
I made two accounts.
One account i browsed to /tws and created a new scorecard. Here i can submit all information I need. The scorecard name is in the end of the URL https://demo.sftool.gov/TwsHome/ScorecardManage/testdsfdfsf
I logged out this account
I logged into attacker account. I browse to https://demo.sftool.gov/TwsHome/ScorecardManage/testdsfdfsf (the last part is the name of the other accounts score card). I can now view the scorecard and even edit the score card from the attackers account. I can add accounts to read only and edit permissions on the score card and change information as-well as download the score card.

Log back into the victim account and the scorecard information has been changed, downloaded and attacker has assigned permissions.

We can brute force scorecard names but i am not doing this as the above on my accounts already shows the issue.

Many thanks
Holla

## Impact

An attacker can read, edit and download and assign permissions to another users scorecard.

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
