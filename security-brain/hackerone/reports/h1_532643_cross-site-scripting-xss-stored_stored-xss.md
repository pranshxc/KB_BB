---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '532643'
original_report_id: '532643'
title: Stored - XSS
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2019-04-09T13:53:42.265Z'
disclosed_at: '2019-05-28T16:07:58.818Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 26
asset_identifier: oberlo.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored - XSS

## Metadata

- HackerOne Report ID: 532643
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2019-05-28T16:07:58.818Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Security Team,
I have Found Stored XSS Vulnerability 

POC : 
Step1: Go to https://app.oberlo.com/suppliers
Step2: Click on any product you will be redirected to URL as i have given for example https://app.oberlo.com/suppliers/8/products/488813?referralUrl=https%3A%2F%2Fapp.oberlo.com%2Fsuppliers%2F8%2Fproducts
Step3: You will get message icon in front of supplier name 
Step4: Click on that message 
Step5: Add Reason-->Subject-->and in message add my payload 
Payload: "><img src=x onerror=prompt(document.cookie)>
Step6: Click on send message 
Step7: Go to Inbox and you will see XSS is triggered and your payload was executed successfully

I have attached POC Video, Please go through it 

Thank you!
Ashish Dhone

## Impact

An attacker who exploits a cross-site scripting vulnerability is typically able to:

1) Impersonate or masquerade as the victim user.
2) Carry out any action that the user is able to perform.
3) Read any data that the user is able to access.
4) Capture the user's login credentials.
5) Perform virtual defacement of the web site.
6) Inject trojan functionality into the web site.

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
