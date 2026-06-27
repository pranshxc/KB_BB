---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '307670'
original_report_id: '307670'
title: Difference in query string parameter processing between Hacker News and Keybase
  Chrome extension spawns chat to incorrect user
weakness: Violation of Secure Design Principles
team_handle: keybase
created_at: '2018-01-21T16:07:59.791Z'
disclosed_at: '2018-03-02T16:57:16.920Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
tags:
- hackerone
- violation-of-secure-design-principles
---

# Difference in query string parameter processing between Hacker News and Keybase Chrome extension spawns chat to incorrect user

## Metadata

- HackerOne Report ID: 307670
- Weakness: Violation of Secure Design Principles
- Program: keybase
- Disclosed At: 2018-03-02T16:57:16.920Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello!

When using the Keybase Chrome extension and viewing a Hacker News profile page with an additional `id` parameter in the query string, Hacker News uses the username from the first `id` parameter, whereas the Keybase extension uses the username from the second `id` parameter.

Example URL: https://news.ycombinator.com/user?id=TomNomNom&id=edoverflow

{F256097}

Note that this is the profile page for the Hacker News user `TomNomNom`, whereas the Keybase Chat modal is for the (in this case non-existent) Keybase user `TornNomNom` (i.e. with the first `m` replaced with an `r` and an `n`). In a real attack the attacker would register the Keybase account, use the same Avatar as the target, and probably choose a more convincing homograph than `m` -> `rn`

## Impact

Users attempting to send a secure, sensitive message to a Keybase user can be tricked into sending that message to a malicious user instead.

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
