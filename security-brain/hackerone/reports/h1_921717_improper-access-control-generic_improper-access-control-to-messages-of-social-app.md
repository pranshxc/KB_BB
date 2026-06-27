---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '921717'
original_report_id: '921717'
title: Improper access control to messages of Social app
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2020-07-12T22:16:43.535Z'
disclosed_at: '2020-11-17T16:36:32.453Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-access-control-generic
---

# Improper access control to messages of Social app

## Metadata

- HackerOne Report ID: 921717
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2020-11-17T16:36:32.453Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The Social App (https://apps.nextcloud.com/apps/social) lacks access controls in the `displayPost` function (`/@{username}/{token}`) allowing an unauthenticated user to view any message content by knowing or guessing the message ID.

The vulnerable code is at https://github.com/nextcloud/social/blob/97fb063479d4c0ad6fccdea3774601a619f8a886/lib/Controller/ActivityPubController.php#L367.
Note the TODO comment and the lack of authentication and authorization checks.

The following is a sample curl request to access a direct (private) message (replace the host, username, and the token value):

```
curl -X 'GET' -H 'Accept: application/activity+json' 'http://{nextcloudHost}/apps/social/@{username}/{token}'|jq
```

The `token` value consists of digits only and is based on the unix time.
An attacker would have to know or guess (e.g. brute force) this message ID.

## Impact

An unauthenticated attacker can view any social message, including private (direct) messages from one user to another.
The attacker would have to know or guess the token value.

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
