---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2233'
original_report_id: '2233'
title: Bypass auth.email-domains (2)
weakness: Improper Authentication - Generic
team_handle: phabricator
created_at: '2014-02-23T18:44:37.166Z'
disclosed_at: '2014-03-26T01:04:47.585Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- improper-authentication-generic
---

# Bypass auth.email-domains (2)

## Metadata

- HackerOne Report ID: 2233
- Weakness: Improper Authentication - Generic
- Program: phabricator
- Disclosed At: 2014-03-26T01:04:47.585Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

This vulnerability has the same effect as my previously reported bug [#2224 Bypass `auth.email`-domains](https://hackerone.com/reports/2224), but uses a very different approach, bypassing the current fix.

Instead of truncating through length, this vulnerability uses truncation via MySQL’s (weird) behaviour on inserting Unicode characters with code points greater than `0xFFFF` into columns that have a `utf8` charset. MySQL then truncates a string as soon as it reaches such a character. For more info, see [How to support full Unicode in MySQL databases](http://mathiasbynens.be/notes/mysql-utf8mb4) by @mathias.

To replicate, register an account with following address: `attacker@gmail.com𝌆@allowed-domain.com`.

I would suggest to reconsider not verifying email addresses as was mentioned [here](https://secure.phabricator.com/D8308#5).

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
