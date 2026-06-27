---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1050912'
original_report_id: '1050912'
title: PHP info page disclosure
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2020-12-04T22:56:49.475Z'
disclosed_at: '2021-01-12T21:36:14.453Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- information-disclosure
---

# PHP info page disclosure

## Metadata

- HackerOne Report ID: 1050912
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2021-01-12T21:36:14.453Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Summary:

phpinfo() is a debug functionality that prints out detailed information on both the system and the PHP configuration.

##Step-by-step Reproduction Instructions

1.Go to

 https://███████phpinfo

## Impact

An attacker can obtain information such as:
•Exact PHP version.
•Exact OS and its version.
•Details of the PHP configuration.
•Loaded PHP extensions and their configurations.
This information can help an attacker gain more information on the system. After gaining detailed information, the attacker can research known vulnerabilities for that system under review. The attacker can also use this information during the exploitation of other vulnerabilities

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
