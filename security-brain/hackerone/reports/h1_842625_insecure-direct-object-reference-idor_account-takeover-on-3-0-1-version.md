---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '842625'
original_report_id: '842625'
title: account takeover on 3.0.1 version
weakness: Insecure Direct Object Reference (IDOR)
team_handle: rocket_chat
created_at: '2020-04-07T15:36:39.138Z'
disclosed_at: '2020-06-14T15:22:44.184Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 57
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# account takeover on 3.0.1 version

## Metadata

- HackerOne Report ID: 842625
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: rocket_chat
- Disclosed At: 2020-06-14T15:22:44.184Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I find user reset password hash info and other security info on "/api/v1/[users.info](http://users.info)"  
note : I login on rocketchat with ldap account (my role : user)  
note: in request "[https://target/api/v1/users.info?username=[x]](https://target/api/v1/users.info?username=%5Bx%5D)" you should change usrname to userId

1- please login with user ldap account (role user)  
2- send a request to&nbsp;[https://target/api/v1/users.list](https://target/api/v1/users.list)&nbsp;and copy \_id value  
3- send a request to&nbsp;[https://target/api/v1/users.info?userId=[userId]](https://target/api/v1/users.info?userId=%5BuserId%5D)&nbsp;and copy email value (in response you can see important security information )  
4- logout and click "forget your password" link on&nbsp;[https://target/home](https://target/home)&nbsp;and send an email to above email address that you copied  
4- login with Your account and send a request to&nbsp;[https://target/api/v1/users.list](https://target/api/v1/users.list)&nbsp;and search the same email in response and copy \_id value  
5- send a request to&nbsp;[https://target/api/v1/users.info?userId=[userId]](https://target/api/v1/users.info?userId=%5BuserId%5D)&nbsp;and copy reset hash value  
6- logout your account and send a request to&nbsp;[https://target/reset-password/[reset\_hash]](https://target/reset-password/%5Breset_hash%5D)  
7- set new password  
8- login and enjoy

## Impact

account takeover

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
