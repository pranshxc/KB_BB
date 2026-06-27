---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1606961'
original_report_id: '1606961'
title: Generated passwords are not fully validated by HIBPValidator
weakness: Weak Cryptography for Passwords
team_handle: nextcloud
created_at: '2022-06-20T09:28:43.777Z'
disclosed_at: '2022-10-01T04:50:13.612Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- weak-cryptography-for-passwords
---

# Generated passwords are not fully validated by HIBPValidator

## Metadata

- HackerOne Report ID: 1606961
- Weakness: Weak Cryptography for Passwords
- Program: nextcloud
- Disclosed At: 2022-10-01T04:50:13.612Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
If the Nextcloud server generates a secure random password (e.g. for sharing files), the validation is checked before the shuffle function str_shuffle() is called. In very rare cases it could happen, that a password is validated by HIBPValidator before str_shuffle(), but would not validate after shuffle.

## Steps To Reproduce:
Since the password generation is usung random chars, the source code must be manipulated to see the problem.

For instance take the password "Password123". Shuffle the Password to "o3rw1sasd2P". 

In Generator::generate()
- delete: $password .= $chars = $this->random->generate($length, $chars);
- insert: $password = "o3rw1sasd2P"

Let the validator check the password

- delete: $password = str_shuffle($password);
- insert: $password = "Password123";

See the insecure password "Password123" in UI.

## Supporting Material/References:
https://github.com/nextcloud/password_policy/blob/master/lib/Generator.php

## Impact

In very rare cases the password generator may generate weak passwords.

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
