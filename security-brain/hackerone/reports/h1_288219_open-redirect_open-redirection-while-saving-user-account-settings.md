---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '288219'
original_report_id: '288219'
title: Open Redirection while saving User account Settings
weakness: Open Redirect
team_handle: moneybird
created_at: '2017-11-07T18:15:35.477Z'
disclosed_at: '2017-11-15T09:05:40.611Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
tags:
- hackerone
- open-redirect
---

# Open Redirection while saving User account Settings

## Metadata

- HackerOne Report ID: 288219
- Weakness: Open Redirect
- Program: moneybird
- Disclosed At: 2017-11-15T09:05:40.611Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team ,
I got a Open redirection while saving account setting . This could lead to serious issues .

**Endpoint :-** https://moneybird.com/user/edit?return_to=//evil.com

##Reproduce :-
* Visit https://moneybird.com/user/edit?return_to=//evil.com and click on `Save` .
* You will be take to evil.com .

##Impact :-
Attacker can redirect a user to a fake login page easily to get his login and other sensitive infos .

Thanks .

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
