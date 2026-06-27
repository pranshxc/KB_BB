---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '341372'
original_report_id: '341372'
title: The session token in the URL
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2018-04-20T18:56:18.265Z'
disclosed_at: '2018-06-19T18:29:37.399Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 11
asset_identifier: auth.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# The session token in the URL

## Metadata

- HackerOne Report ID: 341372
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2018-06-19T18:29:37.399Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello team 
I found that tat the URL transport the Session token and it's a sentive information so Placing session tokens into the URL increases the risk that they will be captured by an attacker.
###fix
Applications should use an alternative mechanism for transmitting session tokens, such as HTTP cookies or hidden fields in forms that are submitted using the POST method.

## Impact

an attacker can capture these tokens

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
