---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '227880'
original_report_id: '227880'
title: XXE in DoD website that may lead to RCE
weakness: XML External Entities (XXE)
team_handle: deptofdefense
created_at: '2017-05-12T10:41:43.936Z'
disclosed_at: '2019-10-04T15:22:27.419Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 90
tags:
- hackerone
- xml-external-entities-xxe
---

# XXE in DoD website that may lead to RCE

## Metadata

- HackerOne Report ID: 227880
- Weakness: XML External Entities (XXE)
- Program: deptofdefense
- Disclosed At: 2019-10-04T15:22:27.419Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
XXE in https://█████

**Description:**
A malicious user can modify an XML-based request to include XML content that is then parsed locally.

## Impact
An attacker can use an XML external entity vulnerability to send specially crafted unauthorized XML requests, which will be processed by the XML parser. The attacker can use an XML external entity vulnerability for getting unauthorised access to the OS file system.

## PoC

```
POST /PSIGW/PeopleSoftServiceListeningConnector HTTP/1.1
Host: https://███
Content-type: text/xml
Content-Length: 50

<!DOCTYPE a PUBLIC "-//B/A/EN" "HELLO_XXE"><a></a>
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
