---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2180521'
original_report_id: '2180521'
title: Google Docs link in JS files allows editing & reading survey information
weakness: Information Disclosure
team_handle: security
created_at: '2023-09-25T19:08:17.241Z'
disclosed_at: '2023-11-04T08:17:49.373Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 203
asset_identifier: www.hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Google Docs link in JS files allows editing & reading survey information

## Metadata

- HackerOne Report ID: 2180521
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2023-11-04T08:17:49.373Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello HackerOne security team,

I've been monitoring your JS files for a while now. I've just noticed that a new Google Docs link appeared.
https://docs.google.com/forms/d/1cwHTgNBd51ECJ3w-5Hy6LgioJWhJ2qFF_vdlmXb6zao/edit#responses
{F2725244}

This google docs link has been leaked in JS chunk file located at:
`https://hackerone.com/assets/static/js/5930.078b8e86.chunk.js`

It allows an attacker to edit anything & view some confidential data about users such as emails/survey responses.

Have a great day!

## Impact

The attacker is able to edit the survey & view some confidential data about some users.

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
