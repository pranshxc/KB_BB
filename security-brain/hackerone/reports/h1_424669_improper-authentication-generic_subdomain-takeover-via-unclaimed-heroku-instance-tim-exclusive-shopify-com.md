---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '424669'
original_report_id: '424669'
title: Subdomain Takeover Via unclaimed Heroku Instance tim-exclusive.shopify.com
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2018-10-16T15:32:20.195Z'
disclosed_at: '2021-02-24T01:59:51.189Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 60
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- improper-authentication-generic
---

# Subdomain Takeover Via unclaimed Heroku Instance tim-exclusive.shopify.com

## Metadata

- HackerOne Report ID: 424669
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2021-02-24T01:59:51.189Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Good day, I truly hope it treats you great on your side of the screen :)

I have found that your website tim-exclusive.shopify.com is pointed via a cname to an unclaimed Heroku Instance

This was not registered on Heroku.

I was able to take over the domain:

See my POC (Pug of Concept)
http://tim-exclusive.shopify.com/

POC Video:
https://www.dropbox.com/s/0p6dqz3rwbx2wxn/Screenshot%202018-10-16%2011.30.52.png?dl=0

Options How to fix:

1) Remove the Cname record on tim-exclusive.shopify.com to not point to Heroku

2) Ask me to remove my registered tim-exclusive.shopify.com on Heroku, and you can re register yours :)

May you be well on your side of the screen :)

-Eric

## Impact

control over domain :)

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
