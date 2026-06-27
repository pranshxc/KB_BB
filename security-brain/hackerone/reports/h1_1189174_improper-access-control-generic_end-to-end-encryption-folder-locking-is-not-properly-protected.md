---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1189174'
original_report_id: '1189174'
title: End to end encryption folder locking is not properly protected
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2021-05-08T19:53:39.481Z'
disclosed_at: '2021-06-10T11:45:03.623Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: nextcloud/end_to_end_encryption
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# End to end encryption folder locking is not properly protected

## Metadata

- HackerOne Report ID: 1189174
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2021-06-10T11:45:03.623Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I do not see the end_to_end_encryption app listed here. But since you advertise it big on your website and in communication. And the clients (that also support it are covered) I assume this is part of the program as well.

1. userA has end to end encryption setup
2. userB wants to annoy userA
3. userB starts to send curl request like

```bash
curl -u user1:user -X POST https://SERVER/ocs/v2.php/apps/end_to_end_encryption/api/v1/lock/332 -X POST  -H 'OCS-APIREQUEST: true' -H 'user-agent: Mozilla/5.0 (Android) Nextcloud-android/3.13.1'
```

Here 332 is a fileid. But it can be any fileid.

4. If userB just keeps looping they can just lock all fileids. Limiting any other user from interacting with their encrypted folders.

## Impact

userB in this case can avoid userA from interacting with their encrypted data. Effectively locking them out of adding new data.

Now admitted they do not know which file id the encrypted folder of userA is. But a small script can lock a lot of ids very quickly. And the job to fix this only runs once an hour and clears max 25. So I'm relatively sure that userB has a big advantage here.

Recommendations:

1. While locking there should also be checks (like with unlocking) if the user has access
2. There should be throttling on those endpoints esp if users try to lock things they have no access to

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
