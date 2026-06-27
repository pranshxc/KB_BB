---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '299552'
original_report_id: '299552'
title: Information disclosure on https://paycard.rapida.ru
weakness: Information Disclosure
team_handle: qiwi
created_at: '2017-12-20T09:58:14.959Z'
disclosed_at: '2018-01-20T12:20:14.887Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- information-disclosure
---

# Information disclosure on https://paycard.rapida.ru

## Metadata

- HackerOne Report ID: 299552
- Weakness: Information Disclosure
- Program: qiwi
- Disclosed At: 2018-01-20T12:20:14.887Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I would like to report information disclosure on one of your sub-domains due to some files that might contain some useful information.

Basically i have found 3 files that might giveaway some information about the infrastructure :
1 composer.json
2 composer.lock
3 package.json

I found all the 3 files using dirsearch tool and location where these files can be found are :-
https://paycard.rapida.ru/composer.json , https://paycard.rapida.ru/composer.lock , https://paycard.rapida.ru/package.json 

If the subdomain is no longer in use then these files must be removed.

regards
sahil tikoo

## Impact

Some juicy information that might help an attacker in information gathering about organization and might also contain some sensitive data.

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
