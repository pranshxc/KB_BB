---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1627961'
original_report_id: '1627961'
title: Account takeover on ███████ [HtUS]
weakness: Improper Authentication - Generic
team_handle: deptofdefense
created_at: '2022-07-06T14:00:54.287Z'
disclosed_at: '2022-10-14T13:05:24.465Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- improper-authentication-generic
---

# Account takeover on ███████ [HtUS]

## Metadata

- HackerOne Report ID: 1627961
- Weakness: Improper Authentication - Generic
- Program: deptofdefense
- Disclosed At: 2022-10-14T13:05:24.465Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,
I have found an endpoint in ████████ is vulnerable to Account takeover

Steps to reproduce:
1. Create 2 accounts ( Attacker ( A ) and vicitm ( B ) )
2. Log in to all of them and go to https://███████/███████/EditUserProfile with attacker's account
3. Now fill out the password with your password 
4. Change the attacker's attacker@gmail.com email with victim's email victim@gmail.com
5. Click Submit button and forward the request to repeater
6. Now if the vicim tried to log into his account, he will facing an error
7. Back to the request go to repeater and change the User id of the attacker with the vicim's user ID ( You probley need to brute-force it )
8. Forward the request and you will see 302 code response
9. Stay in the request and change back all changes ( EMAIL and USER ID of Attacker ) and send the request again
9. Now try to log into the victim's victim@gmail.com account with your password
10. You will be logged in



POC:
	████

## Impact

An attacker can takeover accounts

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
