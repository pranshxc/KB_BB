---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1306942'
original_report_id: '1306942'
title: Use of a Broken or Risky Cryptographic Algorithm
weakness: Use of a Broken or Risky Cryptographic Algorithm
team_handle: revive_adserver
created_at: '2021-08-16T15:14:50.331Z'
disclosed_at: '2021-09-15T12:51:43.134Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: https://github.com/revive-adserver/revive-adserver
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- use-of-a-broken-or-risky-cryptographic-algorithm
---

# Use of a Broken or Risky Cryptographic Algorithm

## Metadata

- HackerOne Report ID: 1306942
- Weakness: Use of a Broken or Risky Cryptographic Algorithm
- Program: revive_adserver
- Disclosed At: 2021-09-15T12:51:43.134Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

revive-adserver utilizes a PRNG for session-token generation, this means that an attacker could theoretically be able to generate session tokens at random and take over accounts at random.

[This function does not generate cryptographically secure values, and should not be used for cryptographic purposes.](https://www.php.net/manual/en/function.uniqid.php)

Location: https://github.com/revive-adserver/revive-adserver/blob/6e665eac9b20ff21c167eae420b73a976f3bb52a/www/admin/lib-sessions.inc.php#L228

References: https://www.php.net/manual/en/function.uniqid.php

## Impact

This vulnerability is capable of allowing mass account takeover by having attackers generate other users' session tokens.

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
