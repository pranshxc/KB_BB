---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159399'
original_report_id: '159399'
title: Unauthorized read access to Invoices by PM (Access control Issues)
weakness: Improper Authentication - Generic
team_handle: harvest
created_at: '2016-08-15T02:45:15.238Z'
disclosed_at: '2016-09-29T23:03:56.508Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- improper-authentication-generic
---

# Unauthorized read access to Invoices by PM (Access control Issues)

## Metadata

- HackerOne Report ID: 159399
- Weakness: Improper Authentication - Generic
- Program: harvest
- Disclosed At: 2016-09-29T23:03:56.508Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Description : Project Manager have access to limited projects and corresponding Invoices. But he can view any private Invoices of the company which he doesn't have access to. Sending Invoice Request is Vulnerable to Indirect Object Reference Attack. Any Unprivileged Project manager can send this request to get Invoices over mail and view all the attachments and details to the Invoice.

Steps to reproduce : 
1.Create a Account with Admin and Add a project manager with Full access. Assign him Some project. Add some more projects and invoices but don't assign these to the project manager. 
2.Now login from Project manager's account you will see that you won't have access to all the invoices . You can only create the invoices based on your assigned projects. 
3.Open a Invoice and you will see Send/Resend Invoice Option by which you can send this Invoice to Any user . Also you can Click on the option of send a copy to my mail option here which will send you the copy of that invoice. 
4.Now Intercept the Send request and it will look something like : 

POST /invoices/[Invoice_ID]/messages HTTP/1.1
Host: vijaygangani.harvestapp.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://vijaygangani.harvestapp.com/invoices/10392603
Cookie: [Cookie_Values]
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 772

Post_paramenters 

5.Now change the Invoice ID to any invoice ID of your company And the Invoice Copy will be sent your email with Attachments and PDF of it. 



Let me know if you need any video Poc or Detailed steps to reproduce.


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
