---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '250837'
original_report_id: '250837'
title: Stored xss via template injection
weakness: Cross-site Scripting (XSS) - Stored
team_handle: wordpress
created_at: '2017-07-18T14:56:15.741Z'
disclosed_at: '2017-12-11T13:36:15.053Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored xss via template injection

## Metadata

- HackerOne Report ID: 250837
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: wordpress
- Disclosed At: 2017-12-11T13:36:15.053Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Sir , I found Stored XSS in https://mercantile.wordpress.org/
POC is attached .
Steps to reproduce:
1.Login to your account.
2. Go to https://mercantile.wordpress.org/my-account/edit-address/ & fill details , press save & intercept this request in burp suit.
3.change name to {{constructor.constructor('alert(1)')()}} & forward request. as shown in screenshot.
Xss will popup when you visit your account page.
 
    Although its self XSS. but  following attack  scenario makes it useful.
Anyone can make account on https://mercantile.wordpress.org/ using someone else email id, Its not verifying whether its your email id or not. Lets consider "A" makes account with "B" persons email & by using this technique store XSS payload in its account. After that "B" wants account on mercantile.wordpress.org with same email. so rather creating account with new email, "B" person just do forget password & recover & recover his account. but xss payload is still there in his account so attacker "A" can access victim "B" account anytime.
        One more thing, even after changing name with https://mercantile.wordpress.org/my-account/edit-account/ setting payload is not removed its still there. so its make attack more sophisticated. 
     
Thanks & Regards,
Akshay

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
