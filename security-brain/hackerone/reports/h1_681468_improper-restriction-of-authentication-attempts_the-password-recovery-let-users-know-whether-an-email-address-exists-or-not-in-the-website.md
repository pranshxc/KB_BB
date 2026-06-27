---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '681468'
original_report_id: '681468'
title: The password recovery let users know whether an email address exists or not
  in the website
weakness: Improper Restriction of Authentication Attempts
team_handle: nextcloud
created_at: '2019-08-25T00:03:13.241Z'
disclosed_at: '2019-11-22T17:51:03.959Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: apps.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# The password recovery let users know whether an email address exists or not in the website

## Metadata

- HackerOne Report ID: 681468
- Weakness: Improper Restriction of Authentication Attempts
- Program: nextcloud
- Disclosed At: 2019-11-22T17:51:03.959Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

URL: https://apps.nextcloud.com/password/reset/

I have tried to recover the password for some emails:

test@test.com (exists)
teste@teste.com.br (does not exists)

After I clicked the "reset my password"'s button, the website informed that the email did not exist.

## Impact

This is a bad practice, and it is an invitation to brute force emails that possibly exist in the domain @nextcloud.com.

By using a wordlist of common passwords, it is possible to guess a combination of email/password of an administrator account.

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
