---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '92353'
original_report_id: '92353'
title: CSV Injection in polldaddy.com
team_handle: automattic
created_at: '2015-10-04T23:17:40.723Z'
disclosed_at: '2015-11-20T14:27:08.783Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
---

# CSV Injection in polldaddy.com

## Metadata

- HackerOne Report ID: 92353
- Weakness: 
- Program: automattic
- Disclosed At: 2015-11-20T14:27:08.783Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

We can inject commands in any fields of a member in an email group (=2*10 for example), and when it's exported to CSV it will be evaluated to 20 in the corresponding cell, this enables an attacker to spread malware and execute system level commands on a victim's machine if the victim downloaded the CSV file.

Steps to reproduce:
1-  Create an email group and name it anything.
2- Add a member with =2*10 in their firstname, lastname, and custom data.
3- Export as CSV and open in Excel or any similar program, the evaluated value will replace the =2*10 expression.

References: Report #90415 was about the same issue.

Thanks,

strukt

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
