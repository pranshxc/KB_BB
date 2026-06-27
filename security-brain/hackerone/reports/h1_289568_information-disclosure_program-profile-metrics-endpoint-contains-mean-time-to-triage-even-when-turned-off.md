---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '289568'
original_report_id: '289568'
title: Program profile metrics endpoint contains mean time to triage, even when turned
  off
weakness: Information Disclosure
team_handle: security
created_at: '2017-11-12T08:51:01.968Z'
disclosed_at: '2017-11-14T17:46:59.226Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Program profile metrics endpoint contains mean time to triage, even when turned off

## Metadata

- HackerOne Report ID: 289568
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2017-11-14T17:46:59.226Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Description (Include Impact):**

when a bug bounty program disables its profile metrics which shows the Response Efficiency, there still 
some data leaked in the response of the the following endpoint:
`` hackerone.com/PROGRAM_HANDLE/profile_metrics.json`` 
this endpoint leaks the **mean_time_to_triage** although the program disabled the Response Efficiency in the profile page.

### Steps To Reproduce

1. go to a program that doesn't show the profile metrics such as *wordpress*

2. send the following HTTP get request: 
```
GET /wordpress/profile_metrics.json HTTP/1.1
Host: hackerone.com
Connection: close
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8
Cookie: your_cookies!
```
and the response will be:
```
{"mean_time_to_first_response":null,"mean_time_to_triage":███████,"mean_time_to_resolution":null,"mean_time_to_bounty":null,"total_bounties_paid_prefix":"\u003e","total_bounties_paid":null,"average_bounty_lower_range":null,"average_bounty_upper_range":null,"top_bounty_lower_range":null,"top_bounty_upper_range":null}
```

as you can see here the **mean_time_to_triage** is leaked in the response instead of being NULL.

I am totally sure that this should not be leaked in this response and should be hidden!

hope this is clear, thanks.

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
