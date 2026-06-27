---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1172933'
original_report_id: '1172933'
title: No Password Length Restriction leads to Denial of Service
weakness: Uncontrolled Resource Consumption
team_handle: reddit
created_at: '2021-06-24T12:42:31.738Z'
disclosed_at: '2021-10-21T19:51:35.598Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
asset_identifier: www.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# No Password Length Restriction leads to Denial of Service

## Metadata

- HackerOne Report ID: 1172933
- Weakness: Uncontrolled Resource Consumption
- Program: reddit
- Disclosed At: 2021-10-21T19:51:35.598Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hey when I try to set the password while creating account I noticed that you haven't kept any password limit.
You need to decrease password length :There are two reasons for limiting the password size. For one, hashing a large amount of data can cause significant resource consumption on behalf of the server and would be an easy target for Denial Of Service attack.
Normally all sites have a password minimum to maximum length like 72 characters limit or 48 limit to prevent Denial Of Service attack. But in your  registration page there are no limitation. Let me know if you need any more details.

This is typically not DoS, but a vulnerability which may lead to DoS attack.

The password I tried is:

Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40Crissrock3%40

## Impact

As the response is seen, the server might not be able to handle such lengthy passwords coming from different machines simultaneously. The attacker can perform a DDOS attack by using this vulnerability.

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
