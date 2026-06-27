---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1066790'
original_report_id: '1066790'
title: Internal API endpoint is accesible for everyone
weakness: Improper Access Control - Generic
team_handle: who-covid-19-mobile-app
created_at: '2020-12-26T21:55:14.561Z'
disclosed_at: '2020-12-28T08:48:55.752Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 35
asset_identifier: hack.whocoronavirus.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Internal API endpoint is accesible for everyone

## Metadata

- HackerOne Report ID: 1066790
- Weakness: Improper Access Control - Generic
- Program: who-covid-19-mobile-app
- Disclosed At: 2020-12-28T08:48:55.752Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
It looks like the endpoint **/internal/cron/refreshCaseStats** as configured in [cron.yaml]  (https://github.com/WorldHealthOrganization/app/blob/master/server/appengine/src/main/webapp/WEB-INF/cron.yaml#L3) is accesible for everyone. Since it is configured as a cronjob to run every 5 minutes and starts with internal, this should not be the case, and could worst case lead to DoS if it's a costly operation.

## Steps To Reproduce:

  1. Go to https://hack.whocoronavirus.org/internal/cron/refreshCaseStats
```time curl -v https://hack.whocoronavirus.org/internal/cron/refreshCaseStats```

{F1130894}
Show that it takes about 20 seconds, before a 200 OK response returns (with a single request).

## Supporting Material/References:
https://github.com/WorldHealthOrganization/app/blob/master/server/appengine/src/main/webapp/WEB-INF/cron.yaml#L3

## Impact

Depending on the impact / performance of the action 'refresh case stats'  this could lead to unnecesarry load on the backend (and charges) or even DoS.

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
