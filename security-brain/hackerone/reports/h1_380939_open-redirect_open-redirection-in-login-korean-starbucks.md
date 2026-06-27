---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '380939'
original_report_id: '380939'
title: Open Redirection in Login - Korean Starbucks
weakness: Open Redirect
team_handle: starbucks
created_at: '2018-07-12T12:07:22.382Z'
disclosed_at: '2019-03-20T16:49:58.028Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 52
tags:
- hackerone
- open-redirect
---

# Open Redirection in Login - Korean Starbucks

## Metadata

- HackerOne Report ID: 380939
- Weakness: Open Redirect
- Program: starbucks
- Disclosed At: 2019-03-20T16:49:58.028Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Summary:
Open Redirection is performed in Korean Starbucks login page.
An attacker can redirect victim to other site such as fishing.

Description:
When victim visit https://www.istarbucks.co.kr/login/login.do?redirect_url=//www.bughunting.net this site, and login, he/she is redirected to www.bughunting.net page.

PoC 
https://www.istarbucks.co.kr/login/login.do?redirect_url=//www.bughunting.net

Etc
I attached a PoC video.

## Impact

Fishing

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
