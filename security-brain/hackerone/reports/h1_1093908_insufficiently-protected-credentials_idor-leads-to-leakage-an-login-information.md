---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1093908'
original_report_id: '1093908'
title: IDOR leads to Leakage an ██████████ Login Information
weakness: Insufficiently Protected Credentials
team_handle: deptofdefense
created_at: '2021-02-03T15:03:52.868Z'
disclosed_at: '2021-03-11T20:48:29.360Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- insufficiently-protected-credentials
---

# IDOR leads to Leakage an ██████████ Login Information

## Metadata

- HackerOne Report ID: 1093908
- Weakness: Insufficiently Protected Credentials
- Program: deptofdefense
- Disclosed At: 2021-03-11T20:48:29.360Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi security team,
According to my report #1092618, The VDP team agreed that ***█████████*** and it's subdomains is in the scope of the DoD program
I continue testing that domain
.
.

##Issue Description:
There is an IDOR in██████.███████ that connected with ████████.███████ 
(highly protected encryption chat app)
.
This IDOR leaks only the usernames 
When I used this IDOR in my account it leaks my username which is required for the login authentication
So I tried to  get the █████████ username in order to use this credential to access to the ██████████ panel in██████.██████
And It Worked I get the ███ username which is required for the login authentication
```displayname	"█████"```
.
.
With the correct ██████████ username an attacker can easily make a successful Bruteforce attack by using simple bruteforce tools to get access the █████████ panel as there is no rate limit in the login page
.
.
.

##Expected Behavior
403 forbidden

## Impact

With the correct █████████ username an attacker can easily make a successful Bruteforce attack by using simple bruteforce tools to get access the ███████ panel as there is no rate limit in the login page

## System Host(s)
██████.██████████.████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1 - Visit██████████.██████ 
2 - Sign in ( You can my test account ***username:███*** and  ***password: ███████████████*** )
3 - Now you logged in████.████████ 
4 - Visit█████.████/████.█████████
5 - After that try replace the username ***█████████*** with ***████*** /█████@***██████***:█████.████████
6 - Final link███.███████/████@████████:███████.██████
7 - Notice the █████████ username

## Suggested Mitigation/Remediation Actions
***██████████.███████.███████*** Should use HTTP Authorization header or 
The directory ***/████████/*** should not be accessed by any one

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
