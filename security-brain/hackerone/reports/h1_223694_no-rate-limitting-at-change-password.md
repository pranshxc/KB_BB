---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223694'
original_report_id: '223694'
title: No Rate Limitting at Change Password
team_handle: weblate
created_at: '2017-04-25T08:44:02.739Z'
disclosed_at: '2017-05-17T14:07:51.183Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
---

# No Rate Limitting at Change Password

## Metadata

- HackerOne Report ID: 223694
- Weakness: 
- Program: weblate
- Disclosed At: 2017-05-17T14:07:51.183Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

I found out that you didnt implement a Rate Limitting on Change Password.

**Scenario**
This Scenario is Limited. But some of Programs here consider this. Victim Forgot to logout his/her account in Cafe/Internet Computer Shops. Attacker saw the Account that it is not Logged out having a knowledge with this vulnerability. Attacker dont have any idea about  Victim's Password and allowing him to bruteforce the Victim's Password via Change Password.

**Proof Of Concept**
{F179198}

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
