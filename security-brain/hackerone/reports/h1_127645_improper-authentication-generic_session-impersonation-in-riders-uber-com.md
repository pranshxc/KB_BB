---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '127645'
original_report_id: '127645'
title: Session Impersonation in riders.uber.com
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2016-04-01T19:57:11.651Z'
disclosed_at: '2016-06-13T22:35:03.743Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# Session Impersonation in riders.uber.com

## Metadata

- HackerOne Report ID: 127645
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2016-06-13T22:35:03.743Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Steps:**
* First log in as attacker in riders.uber.com.
* Victim now opens  https://login.uber.com/login in same browser (eg: net cafe).
* It asks you to enter login credentials even though another session is alive.
* If victim enters his account credentials, he will be taken to riders site.
* Even though riders domain is logged in with attacker account, it still takes him to that attacker logged in session.

**Should be:**
* Shouldn't show login when session is alive.
* Should have cleared old account and let new user login.

**Problems:**
* Serious consequences could be, user might assuming he is updating his account and may enter his credit card details in attacker account.

**POC**
https://drive.google.com/file/d/0B9ftrLQ2j3woVktxY181U1pSMk0/view?usp=sharing
(sending link as attachment is 11.X mb)

Thanks

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
