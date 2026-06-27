---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145409'
original_report_id: '145409'
title: 'help.nextcloud.com: Known DoS condition (null pointer deref) in Nginx running'
weakness: Uncontrolled Resource Consumption
team_handle: nextcloud
created_at: '2016-06-17T14:10:20.459Z'
disclosed_at: '2016-07-27T20:51:19.652Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- uncontrolled-resource-consumption
---

# help.nextcloud.com: Known DoS condition (null pointer deref) in Nginx running

## Metadata

- HackerOne Report ID: 145409
- Weakness: Uncontrolled Resource Consumption
- Program: nextcloud
- Disclosed At: 2016-07-27T20:51:19.652Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The https://help.nextcloud.com sub-site is running Nginx/1.10.0 which is vuln to a known issue (CVE-2016-4450) which allows a remote malformed HTTP request to cause the Nginx process to crash.

DoS testing is mentioned as not requested, but if you know of an issue give it a go .. 

You can determine the version running by requesting the IP of the site and getting the HTTP 301, eg: https://88.198.160.135

https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2016-4450

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
