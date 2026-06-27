---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1193321'
original_report_id: '1193321'
title: Scoped apptokens can be changed by that very apptoken
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2021-05-12T11:09:51.926Z'
disclosed_at: '2021-07-15T19:10:01.824Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Scoped apptokens can be changed by that very apptoken

## Metadata

- HackerOne Report ID: 1193321
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2021-07-15T19:10:01.824Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I noticed that there is the possibility to limit apptokens to not be able to access the filesystem.

1. Create a new apptoken in `https://server/settings/user/security`
2. Click the .. of your new apptoken and make it not allowed to access the filesystem
3. Log out
4. Navigate to `https://server/remote.php/dav` and login with your username + apptoken
5. Navigate again to `https://server/settings/user/security`
6. You won't be able to access the apptoken data
7. Obtain the CSRF token
8. Send a PUT request to `https://server/settings/personal/authtokens/ID` chaging the scope

Now the ID you do not know. However even on a decent sized system it is not hard to iterate this as there is no rate limiting or throttling at all.
And voila. You have filesystem access.

You could also remove other apptokens of the same user (if you'd want).

## Impact

Leaked scoped tokens could be used to gain full access to all your data. Defeating the whole purpose of scoped tokens.

I recommend.

1. Only allow tokens that result from a real login (so user+pass+2fa) to modify/delete tokens
2. Do not allow the current token in use to edit itself

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
