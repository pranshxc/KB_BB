---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '244092'
original_report_id: '244092'
title: Password of failed (2FA) login attempt is stored in log
weakness: Plaintext Storage of a Password
team_handle: nextcloud
created_at: '2017-06-28T19:13:38.872Z'
disclosed_at: '2020-03-01T14:10:53.113Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: nextcloud/logreader
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- plaintext-storage-of-a-password
---

# Password of failed (2FA) login attempt is stored in log

## Metadata

- HackerOne Report ID: 244092
- Weakness: Plaintext Storage of a Password
- Program: nextcloud
- Disclosed At: 2020-03-01T14:10:53.113Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

If I try to log in on Webdav with my usual Nextcloud password, it doesn't work due to 2FA. I need an application password.

The password of a failed login attempt by any user is stored plain text in the log:
`[...]OCA\\\\DAV\\\\Connector\\\\Sabre\\\\Auth->validateUserPass('matthes', '***THE_PASSWORD***')[...]`

Even though the login attempt failed, the password is the right password. I am using two factor, but still, the password may not be leaked to anyone. It may also be used for other websites or services, like LDAP. And you can disable 2FA and still use the same password. The log is in some cases visible to multiple people, may it be admins (but who shouldn't have access to the user data) or if the file is just sent to someone else for debugging.

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
