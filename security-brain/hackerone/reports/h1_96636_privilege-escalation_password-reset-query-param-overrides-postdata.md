---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '96636'
original_report_id: '96636'
title: Password Reset - query param overrides postdata
weakness: Privilege Escalation
team_handle: snapchat
created_at: '2015-10-29T20:31:00.808Z'
disclosed_at: '2015-12-24T18:49:30.262Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: accounts.snapchat.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Password Reset - query param overrides postdata

## Metadata

- HackerOne Report ID: 96636
- Weakness: Privilege Escalation
- Program: snapchat
- Disclosed At: 2015-12-24T18:49:30.262Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Suppose a user were to reset their password at the following url (with the given query parameters):
```
https://accounts.snapchat.com/accounts/change_password?
newpassword={someNewPass}&newpassword2={someNewPass}
```
Then regardless of the new password entered into the form, `{someNewPass}` becomes the user's new password.  This becomes malicious when an attacker refers a users to this url which contains these query parameters to change the user's password.

Even though this requires some level of social engineering -- convincing a user (whose username is known) not only to change his/her password, but do so via a given url -- I don't see a good reason to allow this behavior. Bottom line, _don't read username/passwords from query string_.

I look forward to your response.

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
