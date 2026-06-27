---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1167817'
original_report_id: '1167817'
title: Federated shares are not password protected
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2021-04-18T14:46:50.441Z'
disclosed_at: '2021-06-16T08:56:05.539Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Federated shares are not password protected

## Metadata

- HackerOne Report ID: 1167817
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2021-06-16T08:56:05.539Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi again,

So more from me.
Bare with me because this is a highly theoretical issue. But I never the less thing it should be mitigated. Or at least disclosed.

Premissie:
1. user1 on serverA has a federated share established with user2 on serverB
2. the database (not the full system) of serverB is compromised

Now since federated shares are not created with a password which is stored encrypted in the database this means that an attacker to serverB obtains access to data on serverA directly.

Now I am aware that if serverB is fully compromised the password could also be decrypted using the server secret

## Impact

Using federated sharing exposes the servers to a much larger attack service currently. Since an attacker on a different system can obtain access to data on your system as well. In some cases easier than to the target system.

I'd recommend to make sure that there is a password set that is stored encrypted. And that there is a way for admins to obtain a list of federated servers they need to notify in case they had a breach of their own system.

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
