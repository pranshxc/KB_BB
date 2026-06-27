---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1169335'
original_report_id: '1169335'
title: Password policy changes not enforced for existing passwords
weakness: Weak Cryptography for Passwords
team_handle: nextcloud
created_at: '2021-04-20T07:30:49.057Z'
disclosed_at: '2021-04-26T14:07:13.486Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 7
asset_identifier: nextcloud/password_policy
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- weak-cryptography-for-passwords
---

# Password policy changes not enforced for existing passwords

## Metadata

- HackerOne Report ID: 1169335
- Weakness: Weak Cryptography for Passwords
- Program: nextcloud
- Disclosed At: 2021-04-26T14:07:13.486Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

So this is two reports in one. Sort of. But they are the same issue, or at least related.

1. When you setup your nextcloud there is no password policy at all. There is the strength indicator.

I get the password policy app is not yet active at that point. But a minimum length would not be that insane or hard to enforce.
I noticed this when setting up my test setup with admin/admin


2. Now afterwards the password policy app was active. And I enabled the HaveIBeenPwned check. So now I have an admin password that doesn't pass any of the my criteria

* min password length (defaults to 8)
* no common passwords (admin is in there)
* not in HIBP (admin is also in there)


I would expect that if I set a stronger password policy all passwords have to follow that. Now since the passwords are stored hashed you can't do this at policy change time. However at login time you do have the password. And checking against the criteria is possible.

There should at the very least be a warning to the user that their password is not meeting the password criteria. And possibly even a warning to the administrators that a user is using a password that is not meeting the requirements.
But one could even argue that a mandatory password change is in order.

## Impact

Administrators of the system can feel like they have everything pretty well in check when they update the password policy to the latest standards. But in reality all the users that setup their accounts before could use very weak and insecure passwords.

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
