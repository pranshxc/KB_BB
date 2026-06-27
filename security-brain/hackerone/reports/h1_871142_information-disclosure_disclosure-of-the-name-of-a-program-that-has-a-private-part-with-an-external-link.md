---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '871142'
original_report_id: '871142'
title: Disclosure of the name of a program that has a private part with an external
  link
weakness: Information Disclosure
team_handle: security
created_at: '2020-05-11T22:12:09.285Z'
disclosed_at: '2020-05-22T17:10:18.073Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 43
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Disclosure of the name of a program that has a private part with an external link

## Metadata

- HackerOne Report ID: 871142
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2020-05-22T17:10:18.073Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hi team , @jobert , @bencode . Not so long ago, you made an output to the program panel of information about whether the program has the function- `retest`. Also, this is reflected in the report by the attribute `active_retest_subscription`. It seems that it is reflected in publish reports that are created in programs that have external links. The function itself cannot be enabled in the sandbox, which means that it can only be found in real programs. It turns out that if we see this attribute in the report, it means that the program is real, which means it is private

### Steps To Reproduce

1. Go to https://hackerone.com/hacktivity/publish
2. Input program , create reports
3. Check .json report - https://hackerone.com/reports/ID.json

If we see this attribute, it means that the program is private. And it has the `retest` function enabled

Thanks!
@haxta4ok00

## Impact

Disclosure of the name of a program that has a private part with an external link

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
