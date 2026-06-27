---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1959219'
original_report_id: '1959219'
title: Banned user still able to invited to reports as a collabrator and reset the
  password
weakness: Improper Access Control - Generic
team_handle: security
created_at: '2023-04-23T15:22:31.706Z'
disclosed_at: '2023-07-06T07:37:04.971Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 87
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Banned user still able to invited to reports as a collabrator and reset the password

## Metadata

- HackerOne Report ID: 1959219
- Weakness: Improper Access Control - Generic
- Program: security
- Disclosed At: 2023-07-06T07:37:04.971Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

#Description:

* The permanently banned user account can't access any account features or reports and when accessing his profile he receives 404 not found so the account seems to be not signed or not found so the permanently banned user account must be can not access any HackerOne/account features anymore or access reports, but I was able to add the permanently banned user as a collaborator In the report and reset the password without any restrictions

##Steps to reproduce:

* I created an account and send a message to the support team to permanently ban the user account 

* After the account was banned I created a new test account and sandbox program 

* I send a collaborator request to the banned account so he must be can't receive the collaborator email

* But he invited to the report as shown below:

{F2309760}

* Also I can send and reset the password

{F2309761}

{F2309769}

* Here I reset the password

{F2309773}

* Now the banned user is able to join reports as a collaborator and reset his password and this restricted to banned user

## Impact

The banned user able to join reports as a collaborator and reset his password this Is restricted due to be permanently banned from the platform and must be can't access any data or use any feature from the HackerOne platform because his account Is seems to be deleted from the platform and must be can't access anything from his account or access any data

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
