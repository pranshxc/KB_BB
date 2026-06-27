---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1130235'
original_report_id: '1130235'
title: Hackers can reveal the names of private programs that have an external link
  and Enterprise Product Edition
weakness: Information Disclosure
team_handle: security
created_at: '2021-03-18T19:29:28.866Z'
disclosed_at: '2021-08-24T04:13:36.994Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 32
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Hackers can reveal the names of private programs that have an external link and Enterprise Product Edition

## Metadata

- HackerOne Report ID: 1130235
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2021-08-24T04:13:36.994Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Hi team,

A few days ago, your engineers revealed a field in the report- `Custom fields`. The team removed it after a while, but did not remove the design line

`Custom fields` Available only for `Enterprise Product Edition` , Therefore, the sandbox program cannot independently accept this version of the product, which means that only a program with an administrator can do this, which means that the program has a private part 

## Steps To Reproduce:

1. https://hackerone.com/hacktivity/publish
1.1 Input ██████ and create report.

█████

As we can see, there are two dividing lines, between them and there should be (was some time ago) a Custom Fields field.

This means that this program have `Enterprise Product Edition` , And hence the private part

## Impact

Hackers can reveal the names of private programs that have an external link and Enterprise Product Edition

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
