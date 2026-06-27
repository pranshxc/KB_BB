---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1609004'
original_report_id: '1609004'
title: Rate limit is implemented in Reddit , but its not working .
weakness: Improper Authentication - Generic
team_handle: reddit
created_at: '2022-06-22T13:19:32.749Z'
disclosed_at: '2023-05-18T14:43:25.013Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 5
asset_identifier: www.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Rate limit is implemented in Reddit , but its not working .

## Metadata

- HackerOne Report ID: 1609004
- Weakness: Improper Authentication - Generic
- Program: reddit
- Disclosed At: 2023-05-18T14:43:25.013Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

## Summary:
It is a vulnerability which can prove to be critical when misused by attackers ,rate limit is a flaw that doesn't limit the no. of attempts one makes on a website server. this vulnerability makes the website more susceptible to brute force the username while keeping the password constant that is ,, <same password>:<diff. username>,
 secondly it also make susceptible to brute force the <diff. username>:<diff. password>. Please refer to my Conclusion below:

## Impact:
No rate limit means their is no mechanism to protect against the requests you made in a short frame of time . Hence the hacker can brute force the Login page of Reddit , he may also gain easy access to user accounts , it has a lot of chances to flood the server with lot of requests

## Steps To Reproduce:

  1. NOTE : as we know we are not allowed to brute force , therefore i generated 20 random accounts and did manual login as well as few automated logins. 
 
I CAME TO CONCLUSION :

MECHANISM OF RATE LIMIT ON REDDIT##

1.SAME USERNAME DIFF PASS: RATE LIMIT IS WORKING

2.DIFF USERNAME , SAME PASS : RATE LIMIT IS  NOT WORKING
3.REDDIT IS NOT RESTRICTING THE IP ADDRESS , NEITHER THERE IS TIME DELAY IN MAKING REQUEST
4.DIFFERENT USERNAME , DIFF PASS AREN'T RESTTRICTED , CAN DEFINATELY LEAD TO DDOS OR BRUTEFORCE ATTACK

## Impact

this vulnerability making the website more susceptible to brute force which may also lead to gaining unauthorized access to users account.

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
