---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2213251'
original_report_id: '2213251'
title: 'New Search Feature: Search for non-public words in limited disclosure reports'
weakness: Information Disclosure
team_handle: security
created_at: '2023-10-17T15:26:45.868Z'
disclosed_at: '2023-10-25T14:51:19.199Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 50
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# New Search Feature: Search for non-public words in limited disclosure reports

## Metadata

- HackerOne Report ID: 2213251
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2023-10-25T14:51:19.199Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Similar to https://hackerone.com/reports/685909
An attacker can search for words in limited disclosure reports, and see if it exists in the full report. HackerOne will return whether the word exists in the full report, rather than in the limited part (e.g. summary/title ...) of the report

### Steps to reproduce:
Have the new beta search feature enabled:
1. Search for 
`addProjectV2ItemById AND reporter:("ahacker1")`
Note that there is a hit for the phrase in the limited disclosure report (https://hackerone.com/reports/1711938) even though the word cannot be publicly found in the limited disclosure report.

(This phrase is only the full report, not in the limited disclosure report)
## Impact

For example, if there is a secret inside the full report (but not inside the limited portion), the attacker could leak it with a lot of tries.
Suppose secret starts with PREFIX_

then attacker could search for:
PREFIX_a
PREFIX_b
...
until it matches in the report
PREFIX_k

then the attacker could continue
searching for
PREFIX_ka
PREFIX_kb
PREFIX_kc
...
until a match
PREFIX_ko
This could be continued on until the attacker hits the end of the secret, therefore leaking the secrets.

The number of tries would take around:
around 30 chars to try in each iteration * 40 (average length of a secret) 
= 1200 tries

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
