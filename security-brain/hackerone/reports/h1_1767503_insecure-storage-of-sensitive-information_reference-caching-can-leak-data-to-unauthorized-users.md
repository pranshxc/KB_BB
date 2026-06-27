---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1767503'
original_report_id: '1767503'
title: Reference caching can leak data to unauthorized users
weakness: Insecure Storage of Sensitive Information
team_handle: nextcloud
created_at: '2022-11-08T22:00:44.155Z'
disclosed_at: '2023-01-13T08:39:06.107Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: nextcloud/deck
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# Reference caching can leak data to unauthorized users

## Metadata

- HackerOne Report ID: 1767503
- Weakness: Insecure Storage of Sensitive Information
- Program: nextcloud
- Disclosed At: 2023-01-13T08:39:06.107Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
The [ReferenceManager](https://github.com/nextcloud/server/blob/master/lib/private/Collaboration/Reference/ReferenceManager.php) uses a cache to store information about previously accessed references. The used `cachePrefix` in deck ([see here](https://github.com/nextcloud/deck/blob/e55b3a0a26a65a01fae8cfdf83b1066616bfa6ee/lib/Reference/CardReferenceProvider.php#L154-L166)) is independent of the user. If User1 has access to a deck card and the reference data is stored in the cache, any user with knowledge of the boardId/cardId can access the information of that deck card.

## Steps To Reproduce:
  1. User1 has a deck card and shares the link in a talk conversation
  2. Any user of that conversation (or with knowledge of the link) is able to see the deck card, if the call to the reference provider was done for user1 before


## Supporting Material/References:
User "Admin":
{F2025386}

User "Test":
{F2025389}

## Impact

I think the impact should be minimal, because multiple things need to happen to leak information (the reference needs to be cached, another user needs to know the url, etc.).
The GitHub-Integration uses the `userId` as a cachePrefix, this so this shouldn't be a issue in that case, [see here](https://github.com/nextcloud/integration_github/blob/bb443c47fc8a9b0ba090456461040136a93c9214/lib/Reference/GithubReferenceProvider.php#L175-L182).
I haven't looked at other reference providers.

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
