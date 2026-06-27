---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159395'
original_report_id: '159395'
title: Unauthorized access to all the actions of invoices by PM (Access control Issues)
weakness: Improper Authentication - Generic
team_handle: harvest
created_at: '2016-08-15T02:20:47.960Z'
disclosed_at: '2016-09-29T23:03:39.070Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- improper-authentication-generic
---

# Unauthorized access to all the actions of invoices by PM (Access control Issues)

## Metadata

- HackerOne Report ID: 159395
- Weakness: Improper Authentication - Generic
- Program: harvest
- Disclosed At: 2016-09-29T23:03:39.070Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Description : Project Manager(Full access) Can't access the projects and invoices which are not assigned to him.But this can be bypassed and following action Can be done by Any project manager : 
1. Mark as send 
2.Mark as draft
3.Mark as closed
4.Mark as open 
Any manager Can change above mentioned settings of any Invoices of the company.

Steps to reproduce : 
1. Create a Account with Admin and Add a project manager with Full access. Assign him Some project. Add some more projects and invoices but don't assign these to the project manager.
2.Now login from Project manager's account you will see that you won't have access to all the invoices . You can only create the invoices based on your assigned projects.
3.Open a Invoice and you will see more action section in the invoice. Here you will have multiple options like Mark as sent,Mark as closed,Mark as draft etc. All these requests will have different HTTP requests .
5.Just clicking on the actions you can intercept these requests by any proxy tool.
4.I am Giving an example of mark as draft Request here : 

POST /invoices/[Invoice_ID]/messages/mark_as_draft HTTP/1.1
Host: vijaygangani.harvestapp.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://vijaygangani.harvestapp.com/invoices/10392603
Cookie: [Cookie_Values]
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 119

authenticity_token=[Oauth_Token]

5.Change the Invoice_ID to Any private Invoice ID of the company.And the Invoice will be drafted.
6.All the above mentioned Actions can be done on the private projects by limited access Project manager.

Let me know if you need Detailed steps or Video POC to understand the issue.


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
