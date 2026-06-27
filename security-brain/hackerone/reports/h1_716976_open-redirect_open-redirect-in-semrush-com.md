---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '716976'
original_report_id: '716976'
title: Open redirect in semrush.com
weakness: Open Redirect
team_handle: semrush
created_at: '2019-10-18T00:33:49.162Z'
disclosed_at: '2019-10-25T14:54:22.105Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: '*.semrush.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open redirect in semrush.com

## Metadata

- HackerOne Report ID: 716976
- Weakness: Open Redirect
- Program: semrush
- Disclosed At: 2019-10-25T14:54:22.105Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
There is an open redirect on https://www.semrush.com/login/?redirect_to=.
By using /\ at the start of the link, you can bypass the open redirect filter.

**Description:** 
An attacker can control the value of the "redirect_to" parameter and make it redirect to a malicious endpoint.

## Steps To Reproduce:
Visit: `www.semrush.com/login/?redirect_to=/\google.com`
Once you login, you will be redirected to google.com

## Impact

This vulnerability can be used for phishing attacks

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
