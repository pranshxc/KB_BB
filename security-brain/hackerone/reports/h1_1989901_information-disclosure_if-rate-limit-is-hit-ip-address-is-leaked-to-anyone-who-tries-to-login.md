---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1989901'
original_report_id: '1989901'
title: If rate limit is hit, IP address is leaked to anyone who tries to login
weakness: Information Disclosure
team_handle: mozilla
created_at: '2023-05-16T20:20:32.434Z'
disclosed_at: '2023-09-20T12:21:58.777Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: bugzilla.mozilla.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# If rate limit is hit, IP address is leaked to anyone who tries to login

## Metadata

- HackerOne Report ID: 1989901
- Weakness: Information Disclosure
- Program: mozilla
- Disclosed At: 2023-09-20T12:21:58.777Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
After the rate limit on https://bugzilla.mozilla.org/home on the login page is hit, bugzilla blocks the ip address. The next time someone logs in from any ip address, mozilla will say that the account has been locked and will list the ip address which broke the rate limit (which could be the user's).
This is the message that shows up: █████

## Steps To Reproduce:

  1. Activate the rate limit by getting 30+ wrong passwords. You can do an intruder attack with around 50 wrong passwords and when the attack stops without all the payloads going through, you know that the rate limit has been hit.
  2. Now, go to another tab from another ip address (using a vpn) and try to login (it doesn' t matter if it is the correct password or not). You will see the previous address you tried to login from as shown in the screenshot above.

## Supporting Material/References:
██████████

**Remediation**
Just say that the account has been locked due to excessive attempts. If you want to inform the user that this is happeneng, just email the ip address to them saying that there were too many requests coming in from that address.

## Impact

If a user logs in too many times and the rate limit is hit, an attacker who may try to attack the account will see the ip address of the user.

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
