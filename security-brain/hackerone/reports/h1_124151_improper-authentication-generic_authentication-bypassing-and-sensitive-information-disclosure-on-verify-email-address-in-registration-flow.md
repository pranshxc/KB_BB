---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '124151'
original_report_id: '124151'
title: Authentication Bypassing and Sensitive Information Disclosure on Verify Email
  Address in Registration Flow
weakness: Improper Authentication - Generic
team_handle: zomato
created_at: '2016-03-18T05:11:36.331Z'
disclosed_at: '2016-05-28T04:27:55.833Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# Authentication Bypassing and Sensitive Information Disclosure on Verify Email Address in Registration Flow

## Metadata

- HackerOne Report ID: 124151
- Weakness: Improper Authentication - Generic
- Program: zomato
- Disclosed At: 2016-05-28T04:27:55.833Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The zomato.com web application is vulnerable to authentication bypassing and sensitive information disclosure.

The flaw exist in “Verify Email Address” link which is received in a mail after registration. Once the user enters Full Name, Email Address and Password during registration, he/she is either asked to enter a 4 digit code or directly verify email address by clicking the red button for successful account activation/creation.
The verify email address link doesn’t expire even after successful user registration/account activation which allows a malicious user to authenticate into the victim’s session without password. When an user clicks on verify email address link, he/she is directly authenticated without a need of password, thereby bypassing authentication. Also, the verify email address link consist of ‘fbcid’ parameter which is just Base64 encoded. It leaks sensitive data like unique user id, 4 digit code and email address of the user. All these three parameter are being passed in URL itself (GET request).The application is authenticating a user using these three parameter without a need of a password. 

The verify email address GET URL consisting of sensitive data like unique user id, 4 digit code and email address gets stored in cache, browser history, web server logs. If the victim has accessed this link or activated his account from a public computer/cyber cafe, any user with malicious intent can access and misuse this url in order to authenticate into the victim session without a need of a password.

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
