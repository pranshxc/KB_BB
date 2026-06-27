---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '118582'
original_report_id: '118582'
title: CSV Injection at the CSV export feature
weakness: Command Injection - Generic
team_handle: security
created_at: '2016-02-24T20:06:33.317Z'
disclosed_at: '2019-04-08T19:03:12.316Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# CSV Injection at the CSV export feature

## Metadata

- HackerOne Report ID: 118582
- Weakness: Command Injection - Generic
- Program: security
- Disclosed At: 2019-04-08T19:03:12.316Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi there, I have find a way to bypass the mitigation done in [#72785](https://hackerone.com/reports/72785) and [#111192](https://hackerone.com/reports/111192).


What happens if an attacker creates a Ticket with the Tittle `":";-3+3+cmd|' /C calc'!D2`. The ; will break the field making excel think that there are two fields. Although, you are using "" to encapsulate a field and , to separate them, its possible to break one field in two.

Normal case:
`118470,333333,open,new,Denial of Service,2016-02-24 17:43:52 UTC,,,,,,perra,,no,,`

Case where the field is splitted:
`118555,"'"":"";-3+3+cmd|' /C calc'!D2",open,new,"Design Issue,Missing Best Practice",2016-02-24 19:31:14 UTC,,,,,,perra,,no,,`

Once the CSV is create excel will ignore the " and split the field into two by taking into account the ;.

I have tried in:

* Excel Office 2013 on W8.1
* Excel Office 2016 on windows 10
In all cases the code got executed. 


I attach one picture with the executed code.

To Reproduce the issue:

1- Create a Ticket with the following name `":";-3+3+cmd|' /C calc'!D2`. 
2- Export it to CSV
3- Open the CSV. Check attached picture to see the executed code.


If you have further question do not hesitate to ask me.

Best,
███████

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
