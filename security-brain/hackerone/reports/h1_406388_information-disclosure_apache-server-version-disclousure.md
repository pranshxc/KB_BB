---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '406388'
original_report_id: '406388'
title: Apache Server Version Disclousure
weakness: Information Disclosure
team_handle: bohemia
created_at: '2018-09-06T08:43:46.114Z'
disclosed_at: '2020-03-30T17:20:39.600Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: Domain listed in the policy scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Apache Server Version Disclousure

## Metadata

- HackerOne Report ID: 406388
- Weakness: Information Disclosure
- Program: bohemia
- Disclosed At: 2020-03-30T17:20:39.600Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,
I would like to report a bug for https://forums.bohemia.net/
Banner Grabbing is a technique used to get information about remote servers. In addition, this directory is used to find information about remote servers.

Proof of concept :
1. Go to https://forums.bohemia.net/applications/

This information might help an attacker gain a greater understanding of the systems in use and potentially develop further attacks targeted at the specific version of Apache.

Remediation
Configure your web server to prevent information leakage from the SERVER header of its HTTP response.

I hope my report can help you to fix it and impress you. Looking forward from you soon.

Kind Regards,

## Impact

Impact
An attacker might use information aimed at harvesting specifically for an exploit version.

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
