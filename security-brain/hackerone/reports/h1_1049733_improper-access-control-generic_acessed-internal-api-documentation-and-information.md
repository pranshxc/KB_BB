---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1049733'
original_report_id: '1049733'
title: Acessed internal api documentation and information
weakness: Improper Access Control - Generic
team_handle: mailru
created_at: '2020-12-03T12:41:29.985Z'
disclosed_at: '2021-06-06T09:17:16.230Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: Foodplex
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Acessed internal api documentation and information

## Metadata

- HackerOne Report ID: 1049733
- Weakness: Improper Access Control - Generic
- Program: mailru
- Disclosed At: 2021-06-06T09:17:16.230Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

hello team, Anyone can be able to access api documents and files . Actually this domain have proper authentication mechanism. https://apidocs.ucs.ru/
when i browse the above domain , it goes to login page . not possible to create accounts . means can access authenticated people .

but when we browse this end point, Anyone can access the internal api documentation and can be able to see files

url :   https://apidocs.ucs.ru/doku.php/whiteserver:start?do=index  . 

So through bypassed authentication mechanisim and can be able to access api contents files
i have attached screenshots

And also following few end points leaking informations

1. https://apidocs.ucs.ru/feed.php?mode=list&ns=whiteserver:configuration
this above url leaking whiteserver configuration file information

2. https://apidocs.ucs.ru/feed.php?mode=list&ns=whiteserver:configuration:wsa:scenarios
This url leaks some configuration information

kindly take a look at this

thank you :)
have a great day

## Impact

The following files are in the server
 egaisforpos_external_api
 playground
 rk7_lite
 rk7crm_api
 ru
 ucs
 whiteserver
 api
 apiv2
 configuration
 dcintegrations
 scenario
 api
 apiv2
 faq
 howtostart
 license_using
 licenseerror
 start
 whiteserver_v2
 wiki
 egaisforpos_external_api
 ru

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
