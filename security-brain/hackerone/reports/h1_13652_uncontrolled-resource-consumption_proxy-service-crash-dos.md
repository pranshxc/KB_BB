---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13652'
original_report_id: '13652'
title: Proxy service crash DoS
weakness: Uncontrolled Resource Consumption
team_handle: factlink
created_at: '2014-05-27T15:54:52.896Z'
disclosed_at: '2014-06-04T11:19:15.608Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Proxy service crash DoS

## Metadata

- HackerOne Report ID: 13652
- Weakness: Uncontrolled Resource Consumption
- Program: factlink
- Disclosed At: 2014-06-04T11:19:15.608Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Sending certain URLs to the proxy appears to crash the service, leading to a _502 Bad Gateway_ from nginx, presumably until the service is restarted. The following sequence sent in a short period appears to cause the crash (it could just be the _javascript:confirm()_ request, as the last request receives the 502, but I can't re-test to be sure):

http://staging.fct.li/?url=data:text/html,Hello
http://staging.fct.li/?url=data://text/html,Hello
http://staging.fct.li/?url=data://staging.fct.li/
http://staging.fct.li/?url=javascript:confirm()
http://staging.fct.li/?url=javascript:confirm("staging.fct.li")

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
