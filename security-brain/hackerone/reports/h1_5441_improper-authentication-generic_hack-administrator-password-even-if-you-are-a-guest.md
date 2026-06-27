---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '5441'
original_report_id: '5441'
title: Hack administrator password even if you are a guest
weakness: Improper Authentication - Generic
team_handle: msdos
created_at: '2014-04-01T06:55:46.582Z'
disclosed_at: '2014-04-01T17:17:55.722Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- improper-authentication-generic
---

# Hack administrator password even if you are a guest

## Metadata

- HackerOne Report ID: 5441
- Weakness: Improper Authentication - Generic
- Program: msdos
- Disclosed At: 2014-04-01T17:17:55.722Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Step1:Go to command prompt
Step2:Type "net user"
Step3:Find the administrator name which you would like to change the password
Step4:Type " net user" space "administrator name" space  *
Step5:It will ask you to change the password
Step6:Type the password and confirm it..

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
