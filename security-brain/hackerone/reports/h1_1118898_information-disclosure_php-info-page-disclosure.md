---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1118898'
original_report_id: '1118898'
title: PHP info page disclosure
weakness: Information Disclosure
team_handle: gsa_vdp
created_at: '2021-03-06T17:33:17.304Z'
disclosed_at: '2021-04-14T15:23:52.164Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
asset_identifier: mysmartplans.gsa.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# PHP info page disclosure

## Metadata

- HackerOne Report ID: 1118898
- Weakness: Information Disclosure
- Program: gsa_vdp
- Disclosed At: 2021-04-14T15:23:52.164Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

phpinfo() is a debug functionality that prints out detailed information on both the system and the PHP configuration.

Step to reproduce:
Go here: https://mysmartplans.gsa.gov/phpinfo.php


An attacker can obtain information such as:
Exact PHP version.
Exact OS and its version.
Details of the PHP configuration.
Internal IP addresses.
Server environment variables.
Loaded PHP extensions and their configurations and etc.

## Impact

This information can help an attacker gain more information on the system. After gaining detailed information, the attacker can research known vulnerabilities for that system under review. The attacker can also use this information during the exploitation of other vulnerabilities.

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
