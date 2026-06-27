---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '347693'
original_report_id: '347693'
title: Program metrics disclosed response_efficiency_percentage via /program_name
  json response despite the team decided not to show on their profile
weakness: Information Disclosure
team_handle: security
created_at: '2018-05-05T04:17:33.205Z'
disclosed_at: '2018-05-08T03:30:02.965Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 64
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Program metrics disclosed response_efficiency_percentage via /program_name json response despite the team decided not to show on their profile

## Metadata

- HackerOne Report ID: 347693
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2018-05-08T03:30:02.965Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

**Summary:**

First of all, i am not sure if a private program or any program have the capability to not show their response efficiency, __but i assume they have because i saw some private programs that do not show response efficiency percentage on their public page__.

**Description:**

Below list of private program was not showing their `response efficiency percentage` on their public profile, but using `profile_metrics.json` response, the percentage can be view resulting an information disclosure about the program.

█████████ = 100%
███████ = 100%
████ = 66%
████ = 68%
██████ = 52%

### Steps To Reproduce

  1. Go to ██████████
  2. Observed that response efficiency was not visible
  3. Now go to █████████/profile_metrics.json
  4. I can confirm that `66%` is the percentage of ██████████ because of this `"response_efficiency_percentage":66`


## PoC screenshot below:

███████

## Impact

Information disclosure despite the private program is not showing the response efficiency percentage.

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
