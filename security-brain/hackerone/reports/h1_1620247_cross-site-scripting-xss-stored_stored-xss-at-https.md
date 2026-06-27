---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1620247'
original_report_id: '1620247'
title: Stored XSS at https://█████
weakness: Cross-site Scripting (XSS) - Stored
team_handle: deptofdefense
created_at: '2022-06-30T11:47:10.053Z'
disclosed_at: '2022-09-06T19:04:09.997Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS at https://█████

## Metadata

- HackerOne Report ID: 1620247
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: deptofdefense
- Disclosed At: 2022-09-06T19:04:09.997Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
In registeration page ( https://████ ) , first name and last name field are vulnerable to Stored Cross Site Scripting.

## Proof of concept
For the fastly test, use this credentials to login (my test account)
> email: █████████
password: ██████

After login , alert document.cookie will triggered

## Impact

Stored Cross Site Scripting which attacker can execute malicious javascript payload.

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to registration page ( https://████ ), insert `<svg/onload=confirm(document.cookie)>` payload in firstname and lastname fields and create account.
2. Verified your account.
3. Go to login page and login your account.
4. And XSS will triggered ( XSS also triggered in `My Profile` page) .

## Suggested Mitigation/Remediation Actions
1. Filter input on arrival.
2. Encode data on output.
3. Content Security Policy

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
