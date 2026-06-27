---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '123380'
original_report_id: '123380'
title: Creating multiple user with the same link which is sent to email after registeration
weakness: Violation of Secure Design Principles
team_handle: veris
created_at: '2016-03-15T17:01:47.785Z'
disclosed_at: '2016-06-12T16:08:06.698Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Creating multiple user with the same link which is sent to email after registeration

## Metadata

- HackerOne Report ID: 123380
- Weakness: Violation of Secure Design Principles
- Program: veris
- Disclosed At: 2016-06-12T16:08:06.698Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1. Go to the Link for register
2.Email will be sent to the user - Email id 
3.Access the same Link in 2 different browser ( Google Chrome , Firefox)
4.Change the username in each browser !!!!
5. Still it works !!!

I guess you got to know what the problem is !!!!
the Link sent to the Email id for registration ( Activation Link) can be miss used !!!

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
