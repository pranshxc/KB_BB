---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '117159'
original_report_id: '117159'
title: SPF/DKIM/DMARC for aspen.io
weakness: Improper Authentication - Generic
team_handle: gratipay
created_at: '2016-02-18T15:07:59.485Z'
disclosed_at: '2016-03-19T21:43:20.574Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# SPF/DKIM/DMARC for aspen.io

## Metadata

- HackerOne Report ID: 117159
- Weakness: Improper Authentication - Generic
- Program: gratipay
- Disclosed At: 2016-03-19T21:43:20.574Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1.aspen.io
2.grtp.co


`SPF record lookup and validation for: grtp.co
SPF records are published in DNS as TXT records.
The TXT records found for your domain are:
Checking to see if there is a valid SPF record.
No valid SPF record found of either type TXT or type SPF.`


`SPF record lookup and validation for: aspen.io
SPF records are published in DNS as TXT records.
The TXT records found for your domain are:
ALIAS for aspen-io.herokuapp.com
Checking to see if there is a valid SPF record.`

No valid SPF record found of either type TXT or type SPF.



Check here-->`http://www.kitterman.com/spf/validate.html`

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
