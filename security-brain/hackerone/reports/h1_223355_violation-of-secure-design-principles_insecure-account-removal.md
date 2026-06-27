---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223355'
original_report_id: '223355'
title: Insecure Account Removal
weakness: Violation of Secure Design Principles
team_handle: weblate
created_at: '2017-04-24T10:09:41.069Z'
disclosed_at: '2017-05-17T14:15:35.554Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- violation-of-secure-design-principles
---

# Insecure Account Removal

## Metadata

- HackerOne Report ID: 223355
- Weakness: Violation of Secure Design Principles
- Program: weblate
- Disclosed At: 2017-05-17T14:15:35.554Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

The removal of account is one of the sensitive part of a web application that needs to protect, therefor removing an account should validate the authenticity of the legitimate user, however i have found that when removing an account, the system did not require the user to input the account password.

### Scenario

  1. The user logins to a shared computer (office, library, cafe) 
  2. Left the account open.
  3. Intruder came and try to delete the users account
  4. Intruder can easily delete the account because the system did not protect it by asking the password to validate that the person deleting the account is the legitimate user.

### Mitigation:

Put reauthentication when anyone/user is deleting an account, ask the user to input password before the completion of the account deletion.

Let me know if you need more information.

Regards
Japz

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
