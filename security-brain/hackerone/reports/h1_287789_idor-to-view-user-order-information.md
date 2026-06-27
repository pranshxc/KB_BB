---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '287789'
original_report_id: '287789'
title: IDOR to view User Order Information
team_handle: bohemia
created_at: '2017-11-06T17:42:59.907Z'
disclosed_at: '2018-09-17T15:33:04.833Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
tags:
- hackerone
---

# IDOR to view User Order Information

## Metadata

- HackerOne Report ID: 287789
- Weakness: 
- Program: bohemia
- Disclosed At: 2018-09-17T15:33:04.833Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!


**Description:** There is an idor to view other user's order information and determine their IP addresses and other order infromation

## Application & Version:

https://store.bistudio.com/order/1003793?confirmed=true

## Steps To Reproduce:
1. Login to your account
2. Visit the above endpoint
3. You can iterate through the order ID to view other users details.

## Supporting Material/References:

{F237085}
{F237086}

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
