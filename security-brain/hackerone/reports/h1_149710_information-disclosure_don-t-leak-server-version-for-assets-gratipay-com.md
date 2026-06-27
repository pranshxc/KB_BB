---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '149710'
original_report_id: '149710'
title: don't leak Server version for assets.gratipay.com
weakness: Information Disclosure
team_handle: gratipay
created_at: '2016-07-07T06:54:47.612Z'
disclosed_at: '2016-07-11T10:13:39.008Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 12
tags:
- hackerone
- information-disclosure
---

# don't leak Server version for assets.gratipay.com

## Metadata

- HackerOne Report ID: 149710
- Weakness: Information Disclosure
- Program: gratipay
- Disclosed At: 2016-07-11T10:13:39.008Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi i found that server version are being disclosed on the response header on this URL: __https://assets.gratipay.com__ , this is a low risk but you can consider this as best practice because it is important to keep secret of server versions.

See similar reports here: #141125

Feel free to close this as __Informative__ if don't see any security risk by the given information disclosure.

Regards
Japz

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
