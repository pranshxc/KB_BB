---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17514'
original_report_id: '17514'
title: Information Disclosure (phpinfo())
weakness: Information Disclosure
team_handle: uzbey
created_at: '2014-06-25T13:43:46.001Z'
disclosed_at: '2014-06-28T09:32:32.029Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Information Disclosure (phpinfo())

## Metadata

- HackerOne Report ID: 17514
- Weakness: Information Disclosure
- Program: uzbey
- Disclosed At: 2014-06-28T09:32:32.029Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

URL :- https://staging.uzbey.com/phpinfo.php

Description :-
phpinfo() is a debug functionality that prints out detailed information on both the system and the PHP configuration.

An attacker can obtain information such as: 
•Exact PHP version.
•Exact OS and its version.
•Details of the PHP configuration.
•Internal IP addresses.
•Server environment variables.
•Loaded PHP extensions and their configurations.
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
