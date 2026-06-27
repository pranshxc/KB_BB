---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '186862'
original_report_id: '186862'
title: Order-phishing via Payment ID URL
weakness: Cross-Site Request Forgery (CSRF)
team_handle: portswigger
created_at: '2016-11-30T13:21:13.847Z'
disclosed_at: '2016-11-30T20:14:33.226Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Order-phishing via Payment ID URL

## Metadata

- HackerOne Report ID: 186862
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: portswigger
- Disclosed At: 2016-11-30T20:14:33.226Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello. I discovered the endpoint, which allows the attacker conduct the fishing attack to other users and they can pay for attacker's order.
Why this can happen? 
On the site, order id parameter sends to the https://portswigger.net/CCPayment.aspx as POST, but attacker can append it as GET and it will works:

Example:
https://portswigger.net/CCPayment.aspx?id=DD6BE85CDD50DC829C0354F83E5C67

Steps to reproduce:
1) Go to the https://portswigger.net/buy/ and fill the form.
2) Click "Confirm details".
3) Click "Pay by credit card".
4) Catch the POST request from ССpayment.aspx with order id:

POST /CCPayment.aspx HTTP/1.1
[...Headers...]

id=05BC4BF36F9BB32E80F4B581BF4859

5) Now append the id as GET parameter. You will have link like https://portswigger.net/CCPayment.aspx?id=05BC4BF36F9BB32E80F4B581BF4859
6) Now you can conduct phishing attack with this link, and users can pay for your order.

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
