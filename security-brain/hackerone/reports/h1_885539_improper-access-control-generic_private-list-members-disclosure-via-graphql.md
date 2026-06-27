---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '885539'
original_report_id: '885539'
title: Private list members disclosure via GraphQL
weakness: Improper Access Control - Generic
team_handle: x
created_at: '2020-05-29T07:23:13.570Z'
disclosed_at: '2020-08-04T01:25:19.220Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 327
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Private list members disclosure via GraphQL

## Metadata

- HackerOne Report ID: 885539
- Weakness: Improper Access Control - Generic
- Program: x
- Disclosed At: 2020-08-04T01:25:19.220Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Due to improper queries of GraphQL, the attacker can steal members of the private list.

**Description:**
Twitter implements a unique GraphQL endpoint, which can use only the queries that Twitter specified. However, there is a flaw in the backend (https://api.████████.com/graphql/iUmNRKLdkKVH4WyBNw9x2A/ListMembers).
This vulnerability requires snowflake brute-force, but it's not impossible. Snowflake is built from the timestamp, sequence id, and worker id. Sequence id is basically 0 because it'll reset automatically at the start of every millisecond. Worker id can have 2 ^ 10 = 1024 different values in principle.
So you need to send 1024 * 1000 = 1024000 requests to perform brute-force snowflake which created in a sec.
1024000 * 60 = 61440000 requests will be enough to brute-force a list created in a minute.
It takes a few hours to perform, but it's not impossible.

## Steps To Reproduce:

To reproduce this:
1. Create a private list in account A and add some people.
1. Login to account B, and trigger `ListMembers` request.
1. Intercept the request and replace ID to the list's one which you created in step 1.
1. Now, you know the members of account A's private list from account B.

In real attack: 
  1. Send requests to `https://api.█████████.com/graphql/iUmNRKLdkKVH4WyBNw9x2A/ListMembers?variables=%7B%22listId%22%3A%22[Valid Snowflake Here]%22%2C%22count%22%3A20%2C%22includePromotedContent%22%3Atrue%2C%22withHighlightedLabel%22%3Atrue%2C%22withTweetQuoteCount%22%3Atrue%2C%22withTweetResult%22%3Atrue%7D` until you got valid response.
  1. If you found a valid snowflake, open `https://████████.com/i/lists/[ID Here]`.
  1. If the list is private, you know members of the list now.

## Supporting Material/References:

██████

## Impact

Leakage of private list members.

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
