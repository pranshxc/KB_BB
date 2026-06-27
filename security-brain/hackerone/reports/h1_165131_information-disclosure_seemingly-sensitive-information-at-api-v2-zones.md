---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '165131'
original_report_id: '165131'
title: Seemingly sensitive information at /api/v2/zones
weakness: Information Disclosure
team_handle: instacart
created_at: '2016-09-01T22:16:06.226Z'
disclosed_at: '2016-11-16T19:59:26.593Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Seemingly sensitive information at /api/v2/zones

## Metadata

- HackerOne Report ID: 165131
- Weakness: Information Disclosure
- Program: instacart
- Disclosed At: 2016-11-16T19:59:26.593Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Overview
==
https://www.instacart.com/api/v2/zones is accessible by a regular Instacart user and seems to return sensitive information such as names, emails, phone numbers, money amounts and dates.

```
GET /api/v2/zones

{
  "meta": {
    "code": 200
  },
  "data": {
    "zones": [
      ...
      {
        "id": 73,
        "name": "████",
        "created_at": "2014-10-01T01:36:07.302Z",
        "updated_at": "2016-06-14T23:32:39.147Z",
        ...
        "active": true,
        "supervisor_phone": "███████",
        ...
        "hourly_guarantee_amount_cents": █████████,
        "hourly_guarantee_amount_currency": "USD",
        "guarantee_ends_at": "2015-12-31T00:00:00.000Z",
        ...
        "applicant_supervisor_name": "█████",
        "applicant_supervisor_phone": "████",
        ...
        "applicant_supervisor_email": "██████",
        "use_phone_screening": false,
        ...
        "strict_shopper_probation": true,
        "picking_only_hourly_guarantee_amount_cents": █████████,
        ...
```

Security Implications
==

It's hard for me to evaluate how sensitive the information is, but it definitely doesn't look like something you would put up on the website for everyone to see. I guess a competitor company could make good use of it. Also an attacker could use the information to plan social engineering attacks.

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
