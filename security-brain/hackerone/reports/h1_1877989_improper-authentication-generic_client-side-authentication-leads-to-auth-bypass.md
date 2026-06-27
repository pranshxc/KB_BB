---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1877989'
original_report_id: '1877989'
title: Client side authentication leads to Auth Bypass
weakness: Improper Authentication - Generic
team_handle: deptofdefense
created_at: '2023-02-17T19:46:50.452Z'
disclosed_at: '2023-03-24T17:28:11.268Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- improper-authentication-generic
---

# Client side authentication leads to Auth Bypass

## Metadata

- HackerOne Report ID: 1877989
- Weakness: Improper Authentication - Generic
- Program: deptofdefense
- Disclosed At: 2023-03-24T17:28:11.268Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team

I have found  that to access the data of endpoint ```https://████████/███/?#/``` as user has to submit a password/passphrase.
When we provide wrong password then we get and error message asked to get pass assistance message  ```Contact ████ for password assistance.``` 
After analyzing the JS file I found that when correct password is provide a parameter is set in the localstorage "███████:true"

## Impact

Auth bypass lead to sensitive data exposer like phone number, email id etc.

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Visit https://███/█████/?#/
2. Set a new parameter in local storage name ```█████``` and value ```true```
3. Reload the page

█████

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
