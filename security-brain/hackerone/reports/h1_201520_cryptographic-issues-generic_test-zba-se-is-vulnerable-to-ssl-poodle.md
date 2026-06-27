---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '201520'
original_report_id: '201520'
title: test.zba.se is vulnerable to SSL POODLE
weakness: Cryptographic Issues - Generic
team_handle: zomato
created_at: '2017-01-27T10:49:07.396Z'
disclosed_at: '2017-02-27T10:50:34.423Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- cryptographic-issues-generic
---

# test.zba.se is vulnerable to SSL POODLE

## Metadata

- HackerOne Report ID: 201520
- Weakness: Cryptographic Issues - Generic
- Program: zomato
- Disclosed At: 2017-02-27T10:50:34.423Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

test.zba.se is vulnerable to ssl poodle
 Steps to reproduce:
 1.nmap -sV --version-light --script ssl-poodle -p 443 example.com

 2.curl -v3 -X HEAD https://www.example.com<br> 
  3.or script given at https://access.redhat.com/node/1232123/40/0<br> 
  command: ./poodle.sh example.com 
  Result from these all 3 commands proves that test.zba.se is vulnerable to ssl poodle issue. 


Attack scenario:
It was discovered by researchers at Google itself and announced on Google’s online security blog.<br> read here for more information and attack scenario:<br> https://security.googleblog.com/2014/10/this-poodle-bites-exploiting-ssl-30.html.

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
