---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '22858'
original_report_id: '22858'
title: Password Reset Links Not Expiring
weakness: Improper Authentication - Generic
team_handle: phabricator
created_at: '2014-08-07T10:06:56.686Z'
disclosed_at: '2014-09-06T10:37:00.297Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Password Reset Links Not Expiring

## Metadata

- HackerOne Report ID: 22858
- Weakness: Improper Authentication - Generic
- Program: phabricator
- Disclosed At: 2014-09-06T10:37:00.297Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Old unused Password reset tokens are not expiring on phabricator after the issuance of a new reset link.
Explaination
Suppose at 09:00 o'clock I used password forgot password option and got a reset link on my email. Lets call it reset_1. But i didnot use it.
And at 09:04 o'clock  I used again the forgot password option and got a new reset_link,which is reset_2.
Now generally after the issuance of reset_2,the previous unused reset link should expire.But in case of phabricator its not happening.Both the reset links are remaining usable at the same time.

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
