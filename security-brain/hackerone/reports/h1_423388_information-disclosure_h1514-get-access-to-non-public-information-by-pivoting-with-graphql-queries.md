---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '423388'
original_report_id: '423388'
title: H1514 Get access to non public information by pivoting with graphql queries
weakness: Information Disclosure
team_handle: shopify
created_at: '2018-10-13T15:40:09.333Z'
disclosed_at: '2019-11-03T23:20:11.797Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# H1514 Get access to non public information by pivoting with graphql queries

## Metadata

- HackerOne Report ID: 423388
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2019-11-03T23:20:11.797Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi security team,

**Summary:** It is possible to pivot with queries to get access to information you shouldn't have access to according to docs located at https://help.shopify.com/en/api/graphql-admin-api/reference/queryroot

**Description:** I will try to write up all the ones I can find related to information disclosure where a user with only access to Apps can get from other parts of the store using the graphiql app.

* Example 1:
User with no home access can use locations query to find out store locations and address
{F360024}
It is also possible to use inventoryLevel(inventoryItemId) to get access to inventory without access

* Example 2:
Marketing activities with no marketing access
{F360044}
even though it is possible to ask for more this is the basic query I used. Note it doesn't say access denied.
`query{marketingActivities(first:100){edges{node{id,title, createdAt, budget{total{amount}}}}}}`

* Example 3:
Publications and api keys(I suspect app access makes you see api keys but still)
{F360060}
Query I used:
`query{publications(first: 100){edges{node{name, id, supportsFuturePublishing, app{apiKey}}}}}`

## Impact

This means the graphql can be used to disclose information about other parts of the store that a low permissions user shouldn't have access to.

Best,
Eray

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
