---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7968'
original_report_id: '7968'
title: Sensitive file
weakness: Violation of Secure Design Principles
team_handle: localize
created_at: '2014-04-18T06:40:34.994Z'
disclosed_at: '2014-04-18T22:47:58.481Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Sensitive file

## Metadata

- HackerOne Report ID: 7968
- Weakness: Violation of Secure Design Principles
- Program: localize
- Disclosed At: 2014-04-18T22:47:58.481Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

A possible sensitive file has been found. This file is not directly linked from the website. This check looks for common sensitive resources like password files, configuration files, log files, include files, statistics data, database dumps. Each one of these files could help an attacker to learn more about his target.
This vulnerability affects /.gitignore.
HTML
.idea/* temp/*/* uploads/*.xml img/contact.php config.php

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
