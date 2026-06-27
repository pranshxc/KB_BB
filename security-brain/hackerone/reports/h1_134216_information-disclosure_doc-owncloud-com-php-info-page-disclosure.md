---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '134216'
original_report_id: '134216'
title: 'doc.owncloud.com: PHP info page disclosure'
weakness: Information Disclosure
team_handle: owncloud
created_at: '2016-04-24T15:29:12.060Z'
disclosed_at: '2016-05-24T19:26:38.995Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# doc.owncloud.com: PHP info page disclosure

## Metadata

- HackerOne Report ID: 134216
- Weakness: Information Disclosure
- Program: owncloud
- Disclosed At: 2016-05-24T19:26:38.995Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

URL :- http://doc.owncloud.com/t/

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
