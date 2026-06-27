---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '342978'
original_report_id: '342978'
title: Team object in GraphQL disclosed total number of whitelisted hackers
weakness: Information Disclosure
team_handle: security
created_at: '2018-04-25T03:16:55.808Z'
disclosed_at: '2018-05-12T02:05:47.341Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 86
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Team object in GraphQL disclosed total number of whitelisted hackers

## Metadata

- HackerOne Report ID: 342978
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2018-05-12T02:05:47.341Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hi team. Whitelisted_hackers i think your setup - `Two-factor authentication and IP whitelisting are available to further restrict access to accounts.`
**Description:**
Again, because of the link error, I can see the number, but I can't see these links. Analogue #310946
### Steps To Reproduce

1. {"query": "query {team(handle:\\\"security\\\"){id,name,handle,whitelisted_hackers{total_count}}}"}

Result:

`{"data":{"team":{"id":"Z2lkOi8vaGFja2Vyb25lL1RlYW0vMTM=","name":"HackerOne","handle":"security",
"whitelisted_hackers":{"total_count":30}}}}`

* whitelisted_hackers":{"total_count":30} - You have 30 members for 2FA and white IP

Sorry i bad speak english
I hope you understand me
Thank you,haxta4ok00

PS. I'm glad you accept reports in other languages, but I'm used to this format

## Impact

Disclosure count "whitelisted_hackers"

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
