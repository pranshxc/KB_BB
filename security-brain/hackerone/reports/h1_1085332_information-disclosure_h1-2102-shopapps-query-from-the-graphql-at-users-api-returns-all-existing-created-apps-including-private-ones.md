---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1085332'
original_report_id: '1085332'
title: '[h1-2102] shopApps query from the graphql at /users/api returns all existing
  created apps, including private ones'
weakness: Information Disclosure
team_handle: shopify
created_at: '2021-01-23T14:10:22.981Z'
disclosed_at: '2022-07-15T08:23:26.500Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 32
asset_identifier: Plus Web Admin with Single Domain Feature
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# [h1-2102] shopApps query from the graphql at /users/api returns all existing created apps, including private ones

## Metadata

- HackerOne Report ID: 1085332
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2022-07-15T08:23:26.500Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I have seen that there is query called shopApps executable on the `/[ID]/users/api` graphql that returns a huge amount of apps (it timeouts with a limiting). In the response I have noticed the returned apps also include the private apps, so I do not think that this is intented like this. Using this method, one can grab all the apps, including private ones from shopify.

## Steps To Reproduce:
1. Login to shopify.plus as the admin
2. Go to users, monitor the request and send the POST made to `/[ID]/users/api` to repeater
3. Change the body with this one :

```
{"query":"query xxx { shopApps(first:10000) { edges { node { id isPrivate handle name title shopifyApiClientId } } } }"}
```

In the response, if you search for `"isPrivate":true` you will see also private apps.

## Supporting Material/References:
Screenshots attached

## Impact

One can grab all the shopify apps, including the private ones that I assume are not meant to be accessible.

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
