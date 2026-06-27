---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2334420'
original_report_id: '2334420'
title: Improper Authentication (Login without Registration with any user) at ████
weakness: Improper Authentication - Generic
team_handle: deptofdefense
created_at: '2024-01-25T13:29:09.995Z'
disclosed_at: '2024-03-22T17:50:41.409Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 53
tags:
- hackerone
- improper-authentication-generic
---

# Improper Authentication (Login without Registration with any user) at ████

## Metadata

- HackerOne Report ID: 2334420
- Weakness: Improper Authentication - Generic
- Program: deptofdefense
- Disclosed At: 2024-03-22T17:50:41.409Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team!

I found a security issue in ███████. An attacker could login as a any user without registration in the page and above all it can change the session of a victim and authenticate him as any user. 

The problem is at the endpoint  ██████████ which, thanks to the **signin** parameter, allows to authenticate anyone with any user.

## Impact

Authentication bypass (Login as any user without authentication)
Force a victim to change session with other user

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to ██████████
2. To check the authentication bypass go to ████:

███

As the link corresponds to a GET request you can force any user to log out and authenticate to any other account.

Additional bonus: *clientid and clientsecret are stored in the page source*

███████

## Suggested Mitigation/Remediation Actions

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
