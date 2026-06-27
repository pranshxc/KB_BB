---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '674757'
original_report_id: '674757'
title: Total Paid Bounty Paid can be disclose
weakness: Information Disclosure
team_handle: security
created_at: '2019-08-15T23:29:33.343Z'
disclosed_at: '2020-02-28T17:36:38.163Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 160
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Total Paid Bounty Paid can be disclose

## Metadata

- HackerOne Report ID: 674757
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2020-02-28T17:36:38.163Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

Hello HackerOne Bug Bounty Team,

I noticed that HackerOne recently updated their interface. Indeed, when a hacker hover his mouse over a program, it now disclose some new information :
{F556858}
The one that interested us is "Bounties sent in the last 90 days" value

**Description:**

This new feature could potentially disclose some program information that the team isn't willing to share. Indeed, this can happen in some scenario :

1- The program is 90 days or younger and has choose to not disclose the total paid amount.
2- The program is not 90 days or younger, but an automated script is continually tracking "Bounties sent in the last 90 days" value (note that this would give an exact number since the tracking has started or a very approximate number) (inspired from report #148050)

## Impact

Total Paid Bounty Paid can be disclose

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
